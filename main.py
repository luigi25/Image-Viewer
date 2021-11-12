import sys
from PyQt5.QtWidgets import QApplication
from Model import Model
from ProjectViewer import ImgViewer
import qdarkstyle


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    model = Model()
    img_viewer = ImgViewer(model)
    img_viewer.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
