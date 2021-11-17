from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap, QIcon
import os
import os.path
import time


class Model:
    def __init__(self):
        # list of images
        self.images = list()
        self.pixmap = None
        self.current_image = None

    def get_exif(self, image):
        img = Image.open(image)
        if img._getexif():
            exif_info = img._getexif().items()
            exif_data = {TAGS[tag]: value for tag, value in exif_info if tag in TAGS}
            if 'GPSInfo' in exif_data:
                gps_data = dict()
                for k in exif_data['GPSInfo'].keys():
                    gps_info = GPSTAGS.get(k, k)
                    gps_data[gps_info] = exif_data['GPSInfo'][k]
                exif_data['GPSInfo'] = gps_data
            return exif_data
        else:
            return dict().items()

    def set_current_img(self, image):
        self.current_image = image

    def get_current_img(self, index):
        current_element = self.images[index]
        self.set_current_img(current_element)

    def get_list(self):
        return self.images

    def delete_current_img(self, position):
        if self.images[position] == self.current_image:
            self.set_current_img("")
        self.images = [v for i, v in enumerate(self.images) if i != position]

    def empty_list(self):
        del self.images[:]
