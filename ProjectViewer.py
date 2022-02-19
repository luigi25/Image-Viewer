from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QSize, QFileInfo
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTableWidgetItem, QDialog, QMessageBox, QLabel
from Model import Model
from ExifWindowUI import Ui_Dialog
from ImageWindowUI import Ui_MainWindow
from gps_utils import gps_map


# ExifViewer class.
class ExifViewer(QDialog):
    def __init__(self, info, exif, parent=None):
        super(ExifViewer, self).__init__(parent)
        # get the Ui_Dialog.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # general info extracted from the current image.
        self.info = info
        # exif data extracted from the current image.
        self.exif = exif
        self.fill_table()

    # fill the tables widgets with the available infos.
    def fill_table(self):
        gps = self.exif.pop('GPSInfo') if ('GPSInfo' in self.exif) else None
        # fill this tab if general infos are available, else show a message in the window.
        if self.info:
            self.ui.tableWidget.setRowCount(len(self.info))
            for r, tag in enumerate(self.info):
                self.ui.tableWidget.setItem(r, 0, QTableWidgetItem(tag))
                self.ui.tableWidget.setItem(r, 1, QTableWidgetItem(str(self.info[tag])))
        else:
            self.ui.tableWidget.hide()
            no_info = QLabel()
            no_info.setAlignment(Qt.AlignCenter)
            no_info.setText(f"<h1>No Infos available for this image</h1>")
            self.ui.gridLayout.addWidget(no_info, 0, 0, 1, 1)

        # fill this tab if exif data are available, else show a message in the window.
        if self.exif:
            if gps:
                self.ui.tableWidget1.setRowCount(len(self.exif) + len(gps))
                for r, tag in enumerate(self.exif):
                    self.ui.tableWidget1.setItem(r, 0, QTableWidgetItem(tag))
                    self.ui.tableWidget1.setItem(r, 1, QTableWidgetItem(str(self.exif[tag])))

                for r, tag in enumerate(gps):
                    self.ui.tableWidget1.setItem(len(self.exif) + r, 0, QTableWidgetItem(tag))
                    self.ui.tableWidget1.setItem(len(self.exif) + r, 1, QTableWidgetItem(str(gps[tag])))

                # visualize the map present in gps tag of exif data.
                gps_location = gps_map(gps)
                self.ui.gridLayout2.addWidget(gps_location, 0, 0, 1, 1)
            else:
                self.ui.tableWidget1.setRowCount(len(self.exif))
                for r, tag in enumerate(self.exif):
                    self.ui.tableWidget1.setItem(r, 0, QTableWidgetItem(tag))
                    self.ui.tableWidget1.setItem(r, 1, QTableWidgetItem(str(self.exif[tag])))
                # show a message in the window.
                no_gps = QLabel()
                no_gps.setAlignment(Qt.AlignCenter)
                no_gps.setText(f"<h1>No GPS map available for this image</h1>")
                self.ui.gridLayout2.addWidget(no_gps, 0, 0, 1, 1)

        else:
            self.ui.tableWidget1.hide()
            no_exif = QLabel()
            no_exif.setAlignment(Qt.AlignCenter)
            no_exif.setText(f"<h1>No Exif data available for this image</h1>")
            no_gps = QLabel()
            no_gps.setAlignment(Qt.AlignCenter)
            no_gps.setText(f"<h1>No GPS map available for this image</h1>")
            self.ui.gridLayout1.addWidget(no_exif, 0, 0, 1, 1)
            self.ui.gridLayout2.addWidget(no_gps, 0, 0, 1, 1)


# ImgViewer class.
class ImageViewer(QMainWindow):
    def __init__(self, model: Model):
        super(ImageViewer, self).__init__()
        # get the Ui_MainWindow.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # get the model.
        self.model = model
        # current item from the loaded images list in list_widget.
        self.current_item = -1
        # initially hide list_widget.
        self.ui.list_widget.hide()

        self.show()
        self.interaction()

    # override resizeEvent to keep the image aspect ratio if any images is loaded.
    def resizeEvent(self, ev):
        if self.model.images:
            self.set_aspect_ratio()
        super().resizeEvent(ev)

    # update the current image to visualize when Enter key is pressed in list_widget section.
    def keyPressEvent(self, key_event):
        if key_event.key() == Qt.Key_Return:
            self.view_img()
        else:
            super().keyPressEvent(key_event)

    # drag and drop event is implement to drop one or more images.
    def dragEnterEvent(self, e):
        if len(e.mimeData().urls()) > 0 and e.mimeData().urls()[0].isLocalFile():
            qi = QFileInfo(e.mimeData().urls()[0].toLocalFile())
            ext = qi.suffix()
            if ext == 'jpg' or ext == 'jpeg' or ext == 'png' or ext == 'JPG' or ext == 'PNG':
                e.accept()
            else:
                e.ignore()
        else:
            e.ignore()

    def dropEvent(self, e):
        if e.mimeData().hasUrls:
            e.setDropAction(Qt.CopyAction)
            e.accept()
            for url in e.mimeData().urls():
                f_name = str(url.toLocalFile())
                self.load_img(f_name)
        else:
            e.ignore()

    # right click to open the context menu and have all tools at hand.
    def contextMenuEvent(self, event):
        action = self.ui.context_menu.exec_(self.mapToGlobal(event.pos()))
        if action == self.ui.open_context:
            self.load_img()
        elif action == self.ui.close_context:
            self.close_img()
        elif action == self.ui.close_all_context:
            self.close_all_images()
        elif action == self.ui.cw_rotate_context:
            self.right_rotate()
        elif action == self.ui.ccw_rotate_context:
            self.left_rotate()
        elif action == self.ui.info_context:
            self.show_img_info()
        elif action == self.ui.list_context:
            self.toggle_img_list()

    # allow to do every interaction in the window.
    def interaction(self):
        self.ui.action_open.triggered.connect(self.load_img)
        self.ui.ccw_rotate.triggered.connect(self.left_rotate)
        self.ui.cw_rotate.triggered.connect(self.right_rotate)
        self.ui.close_img.triggered.connect(self.close_img)
        self.ui.close_all_img.triggered.connect(self.close_all_images)
        self.ui.get_info.triggered.connect(self.show_img_info)
        self.ui.side_list.triggered.connect(self.toggle_img_list)
        self.ui.list_widget.itemClicked.connect(self.view_img)

    # load an image from file_dialog if is not drag and drop in the window.
    def load_img(self, f_name=None):
        # choose f_name from file_dialog if is None.
        if not f_name:
            file_dialog = QFileDialog()
            options = file_dialog.Options()
            options |= file_dialog.DontUseNativeDialog
            file_dialog.setGeometry(560, 290, 800, 480)
            file_dialog.setWindowIcon(QtGui.QIcon("icons/application-dialog.png"))
            f_name, _ = file_dialog.getOpenFileName(file_dialog, "Open File", '/home',
                                                    "Images (*.jpg *.jpeg *.png *.JPG *.PNG)", options=options)

        # check if f_name is selected, else a warning message is shown.
        if f_name:
            if f_name not in self.model.file_names:
                # load the f_name and the image in the model and display the image.
                self.model.file_names.append(f_name)
                self.model.images.append(QtGui.QPixmap(f_name))
                item = QtWidgets.QListWidgetItem(f_name.split('/')[-1])
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(f_name), QtGui.QIcon.Normal)
                item.setIcon(icon)
                self.ui.list_widget.addItem(item)
                self.ui.list_widget.setCurrentRow(len(self.ui.list_widget) - 1)
                self.ui.list_widget.show()
                self.view_img()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle('Warning')
            msg_box.setWindowIcon(QtGui.QIcon('icons/exclamation.png'))
            msg_box.setText("No image selected")
            msg_box.exec_()

    # update the image to display by selecting from list_widget and activate all tools;
    # check if the current model image has already been chosen.
    def view_img(self):
        self.current_item = self.ui.list_widget.currentRow()
        if self.model.images[self.current_item] != self.model.current_image:
            self.model.set_current_img(self.current_item)
            self.set_aspect_ratio()
            self.set_tools_enabled()

    # keep aspect ratio with a maximum size of 512 for width/height.
    def set_aspect_ratio(self):
        max_size = 512
        self.ui.image_label.setPixmap(
            self.model.current_image.scaled(
                QSize(min(self.ui.image_label.width(), max_size), min(self.ui.image_label.height(), max_size)),
                Qt.KeepAspectRatio, Qt.FastTransformation))

    # rotate the current image to the left.
    def left_rotate(self):
        if self.model.current_image:
            rotation = QtGui.QTransform().rotate(-90.0)
            self.model.current_image = self.model.current_image.transformed(rotation, Qt.FastTransformation)
            self.set_aspect_ratio()

    # rotate the current image to the right.
    def right_rotate(self):
        if self.model.current_image:
            rotation = QtGui.QTransform().rotate(90.0)
            self.model.current_image = self.model.current_image.transformed(rotation, Qt.FastTransformation)
            self.set_aspect_ratio()

    # close and delete the current image (if any);
    # the tools are disabled and the default image is set in the window if all loaded images are deleted.
    def close_img(self):
        if self.model.current_image:
            self.model.delete_img(self.current_item)
            self.ui.list_widget.takeItem(self.current_item)
            # set default image if all images are deleted.
            if self.model.images:
                self.view_img()
            else:
                self.ui.image_label.setPixmap(QtGui.QPixmap("icons/default_img.PNG"))
                self.set_tools_disabled()
                self.ui.list_widget.hide()

    # close all images (if any) and empty the images list;
    # all tools are disabled and the default image is set in the window.
    def close_all_images(self):
        if self.model.current_image:
            self.model.empty_images_list()
            self.ui.list_widget.clear()
            self.ui.image_label.setPixmap(QtGui.QPixmap("icons/default_img.PNG"))
            self.set_tools_disabled()
            self.ui.list_widget.hide()

    # show the ExifViewer of the current image.
    def show_img_info(self):
        if self.model.current_image:
            info = self.model.extract_general_info(self.model.file_names[self.current_item])
            exif = self.model.extract_exif(self.model.file_names[self.current_item])
            exif_viewer = ExifViewer(info, exif, self)
            exif_viewer.show()

    # toggle the images list.
    def toggle_img_list(self):
        if self.ui.list_widget.isHidden():
            self.ui.list_widget.show()
        else:
            self.ui.list_widget.hide()

    # set tools enabled.
    def set_tools_enabled(self):
        self.ui.ccw_rotate.setEnabled(True)
        self.ui.cw_rotate.setEnabled(True)
        self.ui.close_option.setEnabled(True)
        self.ui.get_info.setEnabled(True)
        self.ui.ccw_rotate_context.setEnabled(True)
        self.ui.cw_rotate_context.setEnabled(True)
        self.ui.close_context.setEnabled(True)
        self.ui.close_all_context.setEnabled(True)
        self.ui.info_context.setEnabled(True)

    # set tools disabled.
    def set_tools_disabled(self):
        self.ui.ccw_rotate.setDisabled(True)
        self.ui.cw_rotate.setDisabled(True)
        self.ui.close_option.setDisabled(True)
        self.ui.get_info.setDisabled(True)
        self.ui.ccw_rotate_context.setDisabled(True)
        self.ui.cw_rotate_context.setDisabled(True)
        self.ui.close_context.setDisabled(True)
        self.ui.close_all_context.setDisabled(True)
        self.ui.info_context.setDisabled(True)