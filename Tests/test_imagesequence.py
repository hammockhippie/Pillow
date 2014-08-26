from helper import unittest, PillowTestCase, lena

from PIL import Image, ImageSequence, TiffImagePlugin


class TestImageSequence(PillowTestCase):

    def test_sanity(self):

        file = self.tempfile("temp.im")

        im = lena("RGB")
        im.save(file)

        seq = ImageSequence.Iterator(im)

        index = 0
        for frame in seq:
            self.assert_image_equal(im, frame)
            self.assertEqual(im.tell(), index)
            index += 1

        self.assertEqual(index, 1)

    def _test_multipage_tiff(self):
        im = Image.open('Tests/images/multipage.tiff')
        for index, frame in enumerate(ImageSequence.Iterator(im)):
            frame.load()
            self.assertEqual(index, im.tell())
            frame.convert('RGB')
            
    def test_tiff(self):
        return self._test_multipage_tiff()

    def test_libtiff(self):
        codecs = dir(Image.core)
        
        if "libtiff_encoder" not in codecs or "libtiff_decoder" not in codecs:
            self.skipTest("tiff support not available")

        TiffImagePlugin.READ_LIBTIFF = True
        self._test_multipage_tiff()
        TiffImagePlugin.READ_LIBTIFF = False
        
if __name__ == '__main__':
    unittest.main()

# End of file
