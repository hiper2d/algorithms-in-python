import unittest

from imagecache.image_cache import ImageCache


class ImageCacheTest(unittest.TestCase):

    def init(self):
        self.im = ImageCache('input.txt')

    def test_input_content(self):
        ...