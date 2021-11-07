from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt
from ExifWindow import Ui_Dialog
from Model import Model


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 707)
        # MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setMinimumSize(QtCore.QSize(1024, 600))
        # self.table_view = QtWidgets.QTableView(self.centralwidget)
        # self.table_view.setMinimumSize(QtCore.QSize(800, 150))
        # self.table_view.setMaximumSize(QtCore.QSize(16777215, 300))
        # self.table_view.setObjectName("table_view")
        # self.verticalLayout.addWidget(self.table_view)
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setMinimumSize(QtCore.QSize(150, 120))
        # self.image_label.setMaximumSize(QtCore.QSize(150, 120))
        self.image_label.setAcceptDrops(True)
        self.image_label.setAutoFillBackground(False)
        self.image_label.setText("")
        self.image_label.setPixmap(QtGui.QPixmap("icons8-add-image-96.png"))
        self.image_label.setScaledContents(False)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setWordWrap(False)
        self.image_label.setObjectName("image_label")
        self.gridLayout.addWidget(self.image_label, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.text_label = QtWidgets.QLabel(self.centralwidget)
        self.text_label.setScaledContents(False)
        self.text_label.setObjectName("text_label")
        self.gridLayout.addWidget(self.text_label, 0, 2, 1, 1)
        self.spacer_item = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(self.spacer_item, 0, 3, 1, 1)
        self.spacer_item1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(self.spacer_item1, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 26))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.close_images = QtWidgets.QMenu(self.menu_file)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("E:/UNIFI/Human Computer Interaction/Project Assignment/Image Viewer/icons/cross-script.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_images.setIcon(icon)
        self.close_images.setObjectName("close_images")
        self.tools = QtWidgets.QMenu(self.menubar)
        self.tools.setObjectName("tools")
        self.view = QtWidgets.QMenu(self.menubar)
        self.view.setObjectName("view")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("E:/UNIFI/Human Computer Interaction/Project Assignment/Image Viewer/icons/images.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open.setIcon(icon1)
        self.action_open.setObjectName("action_open")
        self.actionCurrent = QtWidgets.QAction(MainWindow)
        self.actionCurrent.setObjectName("actionCurrent")
        self.current_img = QtWidgets.QAction(MainWindow)
        self.current_img.setObjectName("current_img")
        self.all_img = QtWidgets.QAction(MainWindow)
        self.all_img.setObjectName("all_img")
        self.cw_rotate = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            "E:/UNIFI/Human Computer Interaction/Project Assignment/Image Viewer/icons/arrow-circle-315.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cw_rotate.setIcon(icon2)
        self.cw_rotate.setObjectName("cw_rotate")
        self.ccw_rotate = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(
            "E:/UNIFI/Human Computer Interaction/Project Assignment/Image Viewer/icons/arrow-circle-225-left.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ccw_rotate.setIcon(icon3)
        self.ccw_rotate.setObjectName("ccw_rotate")
        self.action_exif = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap("E:/UNIFI/Human Computer Interaction/Project Assignment/Image Viewer/icons/information.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_exif.setIcon(icon4)
        self.action_exif.setObjectName("action_exif")
        self.close_images.addAction(self.current_img)
        self.close_images.addSeparator()
        self.close_images.addAction(self.all_img)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.close_images.menuAction())
        self.tools.addAction(self.cw_rotate)
        self.tools.addSeparator()
        self.tools.addAction(self.ccw_rotate)
        self.view.addAction(self.action_exif)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.tools.menuAction())
        self.menubar.addAction(self.view.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.text_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Press Ctrl+O to open an image</span></p></body></html>"))
        self.close_images.setTitle(_translate("MainWindow", "Close Image(s)"))
        self.tools.setTitle(_translate("MainWindow", "Tools"))
        self.view.setTitle(_translate("MainWindow", "View"))
        self.action_open.setText(_translate("MainWindow", "Open"))
        self.action_open.setIconText(_translate("MainWindow", "Open"))
        self.action_open.setToolTip(_translate("MainWindow", "Open"))
        self.action_open.setStatusTip(_translate("MainWindow", "Select image(s) to open"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionCurrent.setText(_translate("MainWindow", "Current"))
        self.current_img.setText(_translate("MainWindow", "Current"))
        self.current_img.setStatusTip(_translate("MainWindow", "Close the current image"))
        self.current_img.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.all_img.setText(_translate("MainWindow", "All"))
        self.all_img.setStatusTip(_translate("MainWindow", "Close all images"))
        self.all_img.setShortcut(_translate("MainWindow", "Ctrl+Shift+W"))
        self.cw_rotate.setText(_translate("MainWindow", "45° clockwise"))
        self.cw_rotate.setStatusTip(_translate("MainWindow", "Rotate the image to the right"))
        self.cw_rotate.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.ccw_rotate.setText(_translate("MainWindow", "45° counterclockwise"))
        self.ccw_rotate.setStatusTip(_translate("MainWindow", "Rotate the image to the left"))
        self.ccw_rotate.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.action_exif.setText(_translate("MainWindow", "Exif Info"))
        self.action_exif.setStatusTip(_translate("MainWindow", "Get exif info"))
        self.action_exif.setShortcut(_translate("MainWindow", "Ctrl+E"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
