from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setAcceptDrops(True)
        self.rotation = 0
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setMinimumSize(QtCore.QSize(640, 480))
        # self.image_label.setMaximumSize(QtCore.QSize(700, 615))
        self.image_label.setAcceptDrops(True)
        self.image_label.setAutoFillBackground(False)
        self.image_label.setText("")
        self.image_label.setScaledContents(True)
        self.image_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.image_label.setWordWrap(False)
        self.image_label.setObjectName("image_label")
        self.gridLayout.addWidget(self.image_label, 2, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.add_photo = QtWidgets.QPushButton(self.centralwidget)
        self.add_photo.setMaximumSize(QtCore.QSize(100, 30))
        self.add_photo.setObjectName("add_photo")
        self.gridLayout.addWidget(self.add_photo, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.close_images = QtWidgets.QMenu(self.menuFile)
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
        # self.action_open.setShortcutVisibleInContextMenu(False)
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
        self.cw_rotate.setObjectName("action45_clockwise")
        self.ccw_rotate = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(
            "E:/UNIFI/Human Computer Interaction/Project Assignment/Image Viewer/icons/arrow-circle-225-left.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ccw_rotate.setIcon(icon3)
        self.ccw_rotate.setObjectName("action45_counterclockwise")
        self.actionExif = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap("E:/UNIFI/Human Computer Interaction/Project Assignment/Image Viewer/icons/information.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExif.setIcon(icon4)
        self.actionExif.setObjectName("actionExif")
        self.close_images.addAction(self.current_img)
        self.close_images.addSeparator()
        self.close_images.addAction(self.all_img)
        self.menuFile.addAction(self.action_open)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.close_images.menuAction())
        self.tools.addAction(self.cw_rotate)
        self.tools.addSeparator()
        self.tools.addAction(self.ccw_rotate)
        self.view.addAction(self.actionExif)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.tools.menuAction())
        self.menubar.addAction(self.view.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.action_open.triggered.connect(self.clicker)
        self.ccw_rotate.triggered.connect(self.left_rotate)
        self.cw_rotate.triggered.connect(self.right_rotate)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_photo.setText(_translate("MainWindow", "Add Photo"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
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
        self.cw_rotate.setText(_translate("MainWindow", "90° clockwise"))
        self.cw_rotate.setStatusTip(_translate("MainWindow", "Rotate the image to the right"))
        self.cw_rotate.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.ccw_rotate.setText(_translate("MainWindow", "90° counterclockwise"))
        self.ccw_rotate.setStatusTip(_translate("MainWindow", "Rotate the image to the left"))
        self.ccw_rotate.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionExif.setText(_translate("MainWindow", "Exif info"))
        self.actionExif.setStatusTip(_translate("MainWindow", "Get exif info"))
        self.actionExif.setShortcut(_translate("MainWindow", "Ctrl+E"))

    def clicker(self):
        fname = QFileDialog.getOpenFileName(None, "Open File", '/home',
                                            "jpeg images (*.jpg *.jpeg *.JPG);;All files (*.*)")
        # open the image
        self.pixmap = QPixmap(fname[0])
        # add pic to label
        self.image_label.setPixmap(self.pixmap)

    def left_rotate(self):
        if self.image_label.pixmap():
            self.rotate = True
            self.rotation = QTransform().rotate(-90.0)

            # transform = QTransform().rotate(self.rotation)
            self.pixmap = self.pixmap.transformed(self.rotation, Qt.SmoothTransformation)

            # add pic to label
            self.image_label.setPixmap(self.pixmap)
            self.rotation = 0

    def right_rotate(self):
        if self.image_label.pixmap():
            self.rotate = True
            self.rotation = QTransform().rotate(90.0)

            # transform = QTransform().rotate(self.rotation)
            self.pixmap = self.pixmap.transformed(self.rotation, Qt.SmoothTransformation)

            # add pic to label
            self.image_label.setPixmap(self.pixmap)
            self.rotation = 0


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
