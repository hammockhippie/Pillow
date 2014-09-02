from helper import unittest, PillowTestCase

from PIL import Image, ImageSequence, TiffImagePlugin

TiffImagePlugin.READ_LIBTIFF = True

class TestFileTiff(PillowTestCase):

    def setUp(self):
        codecs = dir(Image.core)

        if "libtiff_encoder" not in codecs or "libtiff_decoder" not in codecs:
            self.skipTest("tiff support not available")

    def testSequence(self):
        try:
            im = Image.open('Tests/images/multi.tif')
            index = 0
            for frame in ImageSequence.Iterator(im):
                frame.load()
                self.assertEqual(index, im.tell())
                index = index+1
        except Exception as e:
            self.assertTrue(False, str(e))
            
if __name__ == '__main__':
    unittest.main()

# End of file

