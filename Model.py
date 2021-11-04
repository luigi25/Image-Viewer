from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os
import os.path
import time


class Model:
    def __init__(self, current_image=None):
        # list of images
        self.images = list()
        self.current_image = current_image

    def get_exif(self, image):
        try:
            img = Image.open(image)
            if img._getexif() is not None:
                exif_info = img._getexif().items()
                exif_data = {TAGS[tag]: value for tag, value in exif_info if tag in TAGS}
                if 'GPSInfo' in exif_data:
                    gps_data = dict()
                    for k in exif_data['GPSInfo'].keys():
                        gps_info = GPSTAGS.get(k, k)
                        gps_data[gps_info] = exif_data['GPSInfo'][k]
                    exif_data['GPSInfo'] = gps_data
                return exif_data
        except AttributeError:
            print('Select an image!')
            return None

    def update(self, image):
        self.current_image = image

    def get_element(self, index):
        current_element = self.images[index]
        self.update(current_element)

    def empty_list(self):
        del self.images[:]
