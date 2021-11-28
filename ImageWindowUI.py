from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # MainWindow and its properties.
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 550)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setMinimumSize(QtCore.QSize(820, 550))
        MainWindow.setWindowIcon(QtGui.QIcon('icons/application-image.png'))
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # label that contains the default image and all images that are subsequently loaded.
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setAutoFillBackground(False)
        self.image_label.setText("")
        self.image_label.setPixmap(QtGui.QPixmap("icons/default_img.png"))
        self.image_label.setScaledContents(False)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setWordWrap(False)
        self.image_label.setObjectName("image_label")
        self.gridLayout.addWidget(self.image_label, 0, 2, 1, 1)

        # list_widget that contains all images that are loaded.
        self.list_widget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_widget.sizePolicy().hasHeightForWidth())
        self.list_widget.setSizePolicy(sizePolicy)
        self.list_widget.setMinimumSize(QtCore.QSize(200, 16777215))
        self.list_widget.setMaximumSize(QtCore.QSize(350, 16777215))
        self.list_widget.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.list_widget.setProperty("isWrapping", False)
        self.list_widget.setWordWrap(False)
        self.list_widget.setObjectName("list_widget")
        self.list_widget.setAlternatingRowColors(True)
        self.list_widget.setTabKeyNavigation(True)
        self.list_widget.setSpacing(5)
        self.list_widget.setIconSize(QtCore.QSize(75, 75))
        self.gridLayout.addWidget(self.list_widget, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)

        # menubar creation, addition of all tools and relative icons.
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 26))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.close_option = QtWidgets.QMenu(self.menu_file)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icons/cross-script.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_option.setIcon(icon)
        self.close_option.setObjectName("close_option")
        self.tools = QtWidgets.QMenu(self.menubar)
        self.tools.setObjectName("tools")
        self.view = QtWidgets.QMenu(self.menubar)
        self.view.setObjectName("view")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        icon_open = QtGui.QIcon()
        icon_open.addPixmap(QtGui.QPixmap("icons/open_image.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open.setIcon(icon_open)
        self.action_open.setObjectName("action_open")
        self.action_current = QtWidgets.QAction(MainWindow)
        self.action_current.setObjectName("action_current")
        self.close_img = QtWidgets.QAction(MainWindow)
        self.close_img.setObjectName("close_img")
        icon_close = QtGui.QIcon()
        icon_close.addPixmap(QtGui.QPixmap("icons/del_img.png"),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_img.setIcon(icon_close)

        self.close_all_img = QtWidgets.QAction(MainWindow)
        self.close_all_img.setObjectName("close_all_img")
        icon_close_all = QtGui.QIcon()
        icon_close_all.addPixmap(QtGui.QPixmap("icons/del_images.png"),
                                 QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_all_img.setIcon(icon_close_all)
        self.cw_rotate = QtWidgets.QAction(MainWindow)
        icon_cw = QtGui.QIcon()
        icon_cw.addPixmap(QtGui.QPixmap("icons/arrow-circle-315.png"),
                          QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cw_rotate.setIcon(icon_cw)
        self.cw_rotate.setObjectName("cw_rotate")
        self.ccw_rotate = QtWidgets.QAction(MainWindow)
        icon_ccw = QtGui.QIcon()
        icon_ccw.addPixmap(QtGui.QPixmap("icons/arrow-circle-225-left.png"),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ccw_rotate.setIcon(icon_ccw)
        self.ccw_rotate.setObjectName("ccw_rotate")
        self.get_info = QtWidgets.QAction(MainWindow)
        icon_info = QtGui.QIcon()
        icon_info.addPixmap(
            QtGui.QPixmap("icons/information.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.get_info.setIcon(icon_info)
        self.get_info.setObjectName("action_exif")
        self.side_list = QtWidgets.QAction(MainWindow)
        icon_list = QtGui.QIcon()
        icon_list.addPixmap(
            QtGui.QPixmap("icons/application-sidebar-list.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.side_list.setIcon(icon_list)
        self.side_list.setObjectName("side_list")
        self.close_option.addAction(self.close_img)
        self.close_option.addSeparator()
        self.close_option.addAction(self.close_all_img)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.close_option.menuAction())
        self.tools.addAction(self.cw_rotate)
        self.tools.addSeparator()
        self.tools.addAction(self.ccw_rotate)
        self.view.addAction(self.side_list)
        self.view.addAction(self.get_info)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.tools.menuAction())
        self.menubar.addAction(self.view.menuAction())

        # set disabled initially with default image.
        self.close_option.setDisabled(True)
        self.cw_rotate.setDisabled(True)
        self.ccw_rotate.setDisabled(True)
        self.get_info.setDisabled(True)

        # context_menu creation, addition of all tools (same as before) and relative icons;
        # set disabled initially with default image.
        self.context_menu = QtWidgets.QMenu(MainWindow)
        self.open_context = self.context_menu.addAction("Open an image")
        self.open_context.setIcon(icon_open)
        self.cw_rotate_context = self.context_menu.addAction("90° clockwise")
        self.cw_rotate_context.setIcon(icon_cw)
        self.cw_rotate_context.setDisabled(True)
        self.ccw_rotate_context = self.context_menu.addAction("90° counterclockwise")
        self.ccw_rotate_context.setIcon(icon_ccw)
        self.ccw_rotate_context.setDisabled(True)
        self.info_context = self.context_menu.addAction("Get image info")
        self.info_context.setIcon(icon_info)
        self.info_context.setDisabled(True)
        self.list_context = self.context_menu.addAction("Toggle images list")
        self.list_context.setIcon(icon_list)
        self.close_context = self.context_menu.addAction("Close current image")
        self.close_context.setIcon(icon_close)
        self.close_context.setDisabled(True)
        self.close_all_context = self.context_menu.addAction("Close all images")
        self.close_all_context.setIcon(icon_close_all)
        self.close_all_context.setDisabled(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Viewer"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.close_option.setTitle(_translate("MainWindow", "Close image(s)"))
        self.tools.setTitle(_translate("MainWindow", "Tools"))
        self.view.setTitle(_translate("MainWindow", "View"))
        self.action_open.setText(_translate("MainWindow", "Open"))
        self.action_open.setIconText(_translate("MainWindow", "Open"))
        self.action_open.setToolTip(_translate("MainWindow", "Open"))
        self.action_open.setStatusTip(_translate("MainWindow", "Select the image to open"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.open_context.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_current.setText(_translate("MainWindow", "Selected"))
        self.close_img.setText(_translate("MainWindow", "Current"))
        self.close_img.setStatusTip(_translate("MainWindow", "Close the displayed image"))
        self.close_img.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.close_context.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.close_all_img.setText(_translate("MainWindow", "All"))
        self.close_all_img.setStatusTip(_translate("MainWindow", "Close all images"))
        self.close_all_img.setShortcut(_translate("MainWindow", "Ctrl+Shift+W"))
        self.close_all_context.setShortcut(_translate("MainWindow", "Ctrl+Shift+W"))
        self.cw_rotate.setText(_translate("MainWindow", "90° clockwise"))
        self.cw_rotate.setStatusTip(_translate("MainWindow", "Rotate the image to the right"))
        self.cw_rotate.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.cw_rotate_context.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.ccw_rotate.setText(_translate("MainWindow", "90° counterclockwise"))
        self.ccw_rotate.setStatusTip(_translate("MainWindow", "Rotate the image to the left"))
        self.ccw_rotate.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.ccw_rotate_context.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.get_info.setText(_translate("MainWindow", "Get info"))
        self.get_info.setStatusTip(_translate("MainWindow", "Get general info and exif data of the current image"))
        self.get_info.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.info_context.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.side_list.setText(_translate("MainWindow", "Images list"))
        self.side_list.setStatusTip(_translate("MainWindow", "Toggle the list of open images"))
        self.side_list.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.list_widget.setStatusTip(_translate("MainWindow", "The list of open images"))
        self.list_context.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.image_label.setStatusTip(
            _translate("MainWindow", 'Press "Ctrl+O" to open an image or drop some here'))


if __name__ == "__main__":
    import sys
    import qdarkstyle
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
