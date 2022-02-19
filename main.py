import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication
from Model import Model
from ProjectViewer import ImageViewer


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # the singleton model instance.
    model = Model()
    img_viewer = ImageViewer(model)
    img_viewer.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
