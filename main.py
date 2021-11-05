import sys
from PyQt5.QtWidgets import QApplication
from Model import Model
from Viewer import ImgViewer

model = Model()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    im_viewer = ImgViewer(model)
    im_viewer.show()
    sys.exit(app.exec_())
