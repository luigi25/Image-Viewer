from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        # Dialog window and its properties.
        Dialog.setObjectName("Dialog")
        Dialog.resize(850, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(850, 650))
        Dialog.setWindowIcon(QtGui.QIcon('icons/database.png'))

        # set the grid layout and the tabWidget where the infos, exif data
        # and gps map of the selected image will be displayed.
        self.gridLayoutTabWidget = QtWidgets.QGridLayout(Dialog)
        self.gridLayoutTabWidget.setObjectName("gridLayoutTabWidget")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")

        # first tab where the infos of the selected image are displayed.
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(35)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")

        # second tab where exif data of the selected image are displayed.
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.gridLayout1 = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout1.setObjectName("gridLayout1")
        self.tableWidget1 = QtWidgets.QTableWidget(self.tab1)
        self.tableWidget1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget1.setAutoFillBackground(False)
        self.tableWidget1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget1.setAlternatingRowColors(True)
        self.tableWidget1.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget1.setRowCount(1)
        self.tableWidget1.setObjectName("tableWidget")
        self.tableWidget1.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, item)
        self.tableWidget1.horizontalHeader().setVisible(True)
        self.tableWidget1.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget1.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget1.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget1.verticalHeader().setVisible(False)
        self.tableWidget1.verticalHeader().setDefaultSectionSize(35)
        self.tableWidget1.verticalHeader().setHighlightSections(True)
        self.tableWidget1.verticalHeader().setMinimumSectionSize(25)
        self.gridLayout1.addWidget(self.tableWidget1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab1, "")

        # third tab where the gps map of the selected image is displayed.
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.gridLayout2 = QtWidgets.QGridLayout(self.tab2)
        self.gridLayout2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout2.setObjectName("gridLayout2")
        self.gps_map_label = QtWidgets.QLabel()
        self.gps_map_label.setEnabled(True)
        self.gps_map_label.setOpenExternalLinks(True)
        self.gps_map_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gps_map_label.setObjectName("gps_map_label")
        self.gridLayout2.addWidget(self.gps_map_label, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab2, "")
        self.gridLayoutTabWidget.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Dialog.setWindowTitle(_translate("Dialog", "Image Info"))
        item = self.tableWidget1.horizontalHeaderItem(0)
        item1 = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "TAGs"))
        item1.setText(_translate("Dialog", "TAGs"))
        item.setFont(font)
        item1.setFont(font)

        item = self.tableWidget1.horizontalHeaderItem(1)
        item1 = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Values"))
        item1.setText(_translate("Dialog", "Values"))
        item.setFont(font)
        item1.setFont(font)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "General info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Dialog", "Exif data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("Dialog", "GPS"))


if __name__ == "__main__":
    import sys
    import qdarkstyle
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
