import os
import time
import os.path
from PIL import Image
from hurry.filesize import size
from PIL.ExifTags import TAGS, GPSTAGS


class Model:
    def __init__(self):
        # list of the loaded images.
        self.images = list()
        # list of all file_names of the loaded images.
        self.file_names = list()
        # keep track of the current image.
        self.current_image = None
        # general info of the displayed image.
        self.info = dict()
        # exif data of the displayed image.
        self.exif = dict()

    # extract exif data from the displayed image.
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

    # extract general info from the displayed image.
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

    # update the current image.
    def update_img(self, image):
        self.current_image = image

    # set the current image.
    def set_current_img(self, index):
        current_element = self.images[index]
        self.update_img(current_element)

    # delete the displayed image (and its file_name) and set self.current_image None if necessary.
    def delete_img(self, position):
        if self.images[position] == self.current_image:
            self.update_img(None)
        self.images.pop(position)
        self.file_names.pop(position)

    # set self.current_image None, empty the images and file_names list.
    def empty_images_list(self):
        del self.images[:]
        del self.file_names[:]
        self.update_img(None)