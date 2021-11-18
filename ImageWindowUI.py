from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 550)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setMinimumSize(QtCore.QSize(820, 550))
        MainWindow.setWindowIcon(QtGui.QIcon('icons/application-image.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setAutoFillBackground(False)
        self.image_label.setText("")
        self.image_label.setPixmap(QtGui.QPixmap("icons/add_img.png"))
        self.image_label.setScaledContents(False)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setWordWrap(False)
        self.image_label.setObjectName("image_label")
        self.gridLayout.addWidget(self.image_label, 0, 2, 1, 1)

        self.list_widget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_widget.sizePolicy().hasHeightForWidth())
        self.list_widget.setSizePolicy(sizePolicy)
        self.list_widget.setMinimumSize(QtCore.QSize(200, 16777215))
        self.list_widget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.list_widget.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.list_widget.setProperty("isWrapping", False)
        self.list_widget.setWordWrap(False)
        self.list_widget.setObjectName("list_view")
        self.list_widget.setAlternatingRowColors(True)
        self.list_widget.setTabKeyNavigation(True)
        self.list_widget.setSpacing(5)
        self.list_widget.setIconSize(QtCore.QSize(75, 75))
        self.gridLayout.addWidget(self.list_widget, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)

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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/image.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open.setIcon(icon1)
        self.action_open.setObjectName("action_open")
        self.actionCurrent = QtWidgets.QAction(MainWindow)
        self.actionCurrent.setObjectName("actionCurrent")
        self.close_img = QtWidgets.QAction(MainWindow)
        self.close_img.setObjectName("close_img")
        icon_close = QtGui.QIcon()
        icon_close.addPixmap(QtGui.QPixmap("icons/slide.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_img.setIcon(icon_close)
        self.close_all_img = QtWidgets.QAction(MainWindow)
        self.close_all_img.setObjectName("close_all_img")
        icon_close_all = QtGui.QIcon()
        icon_close_all.addPixmap(QtGui.QPixmap("icons/slides-stack.png"),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_all_img.setIcon(icon_close_all)
        self.cw_rotate = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/arrow-circle-315.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cw_rotate.setIcon(icon2)
        self.cw_rotate.setObjectName("cw_rotate")
        self.ccw_rotate = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/arrow-circle-225-left.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ccw_rotate.setIcon(icon3)
        self.ccw_rotate.setObjectName("ccw_rotate")
        self.action_exif = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap("icons/information.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_exif.setIcon(icon4)
        self.action_exif.setObjectName("action_exif")

        self.side_list = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap("icons/application-sidebar-list.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.side_list.setIcon(icon5)
        self.side_list.setObjectName("side_list")
        self.side_list.setCheckable(True)
        self.side_list.setChecked(False)

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
        self.view.addAction(self.action_exif)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.tools.menuAction())
        self.menubar.addAction(self.view.menuAction())
        self.close_option.setDisabled(True)
        self.cw_rotate.setDisabled(True)
        self.ccw_rotate.setDisabled(True)
        self.action_exif.setDisabled(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Viewer"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.close_option.setTitle(_translate("MainWindow", "Close Image(s)"))
        self.tools.setTitle(_translate("MainWindow", "Tools"))
        self.view.setTitle(_translate("MainWindow", "View"))
        self.action_open.setText(_translate("MainWindow", "Open"))
        self.action_open.setIconText(_translate("MainWindow", "Open"))
        self.action_open.setToolTip(_translate("MainWindow", "Open"))
        self.action_open.setStatusTip(_translate("MainWindow", "Select the image to open"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionCurrent.setText(_translate("MainWindow", "Current"))
        self.close_img.setText(_translate("MainWindow", "Current"))
        self.close_img.setStatusTip(_translate("MainWindow", "Close the current image"))
        self.close_img.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.close_all_img.setText(_translate("MainWindow", "All"))
        self.close_all_img.setStatusTip(_translate("MainWindow", "Close all images"))
        self.close_all_img.setShortcut(_translate("MainWindow", "Ctrl+Shift+W"))
        self.cw_rotate.setText(_translate("MainWindow", "90° clockwise"))
        self.cw_rotate.setStatusTip(_translate("MainWindow", "Rotate the image to the right"))
        self.cw_rotate.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.ccw_rotate.setText(_translate("MainWindow", "90° counterclockwise"))
        self.ccw_rotate.setStatusTip(_translate("MainWindow", "Rotate the image to the left"))
        self.ccw_rotate.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.action_exif.setText(_translate("MainWindow", "Get Info"))
        self.action_exif.setStatusTip(_translate("MainWindow", "Get general info and exif data of the current image"))
        self.action_exif.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.side_list.setText(_translate("MainWindow", "Images List"))
        self.side_list.setStatusTip(_translate("MainWindow", "Show the list of open images"))
        self.side_list.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.image_label.setStatusTip(
            _translate("MainWindow", 'Go to "File" and click "Open" or Press "Ctrl+O" to open an image'))
        self.list_widget.setStatusTip(_translate("MainWindow", "The list of open images"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
