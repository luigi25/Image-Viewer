import os
import time
import os.path
from PIL import Image
from hurry.filesize import size
from PIL.ExifTags import TAGS, GPSTAGS


class Model:
    def __init__(self):
        # list of images
        self.images = list()
        self.current_image = None
        self.info = dict()
        self.exif = dict()

    def extract_exif(self, image):
        img = Image.open(image)
        if img._getexif():
            exif_info = img._getexif().items()
            self.exif = {TAGS[tag]: value for tag, value in exif_info if tag in TAGS}
            if 'GPSInfo' in self.exif:
                gps_data = dict()
                for k in self.exif['GPSInfo'].keys():
                    gps_info = GPSTAGS.get(k, k)
                    gps_data[gps_info] = self.exif['GPSInfo'][k]
                self.exif['GPSInfo'] = gps_data
        else:
            self.exif = dict()
        return self.exif

    def extract_general_info(self, image):
        img = Image.open(image)
        if img:
            self.info['FileName'] = os.path.basename(img.filename)
            self.info['Format'] = img.format
            self.info['FileSize'] = size(os.stat(img.filename).st_size) + " (%5d bytes)" % os.stat(
                img.filename).st_size
            self.info['CreationDate'] = time.ctime(os.path.getctime(img.filename))
            self.info['ModificationDate'] = time.ctime(os.path.getmtime(img.filename))
            self.info['ImageSize'] = img.size
            self.info['ColorMode'] = img.mode
        else:
            self.info = dict()
        return self.info

    def update_img(self, image):
        self.current_image = image

    def set_current_img(self, index):
        current_element = self.images[index]
        self.update_img(current_element)

    def delete_current_img(self, position):
        if self.images[position] == self.current_image:
            self.update_img("")
        self.images = [v for i, v in enumerate(self.images) if i != position]

    def empty_list(self):
        del self.images[:]
