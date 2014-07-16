#
# The Python Imaging Library.
# $Id$
#
# Windows Cursor support for PIL
#
# notes:
#       uses BmpImagePlugin.py to read the bitmap data.
#
# history:
#       96-05-27 fl     Created
#
# Copyright (c) Secret Labs AB 1997.
# Copyright (c) Fredrik Lundh 1996.
#
# See the README file for information on usage and redistribution.
#


__version__ = "0.1"

from PIL import Image, BmpImagePlugin, _binary


#
# --------------------------------------------------------------------

i8 = _binary.i8
i16 = _binary.i16le
i32 = _binary.i32le


def _accept(prefix):
    return prefix[:4] == b"\0\0\2\0"


##
# Image plugin for Windows Cursor files.

class CurImageFile(BmpImagePlugin.BmpImageFile):

    format = "CUR"
    format_description = "Windows Cursor"

    def _open(self):

        offset = self.fp.tell()

        # check magic
        s = self.fp.read(6)
        if not _accept(s):
            raise SyntaxError("not a CUR file")

        # pick the largest cursor in the file
        m = b""
        for i in range(i16(s[4:])):
            s = self.fp.read(16)
            if not m:
                m = s
            elif i8(s[0]) > i8(m[0]) and i8(s[1]) > i8(m[1]):
                m = s
            # print "width", i8(s[0])
            # print "height", i8(s[1])
            # print "colors", i8(s[2])
            # print "reserved", i8(s[3])
            # print "hotspot x", i16(s[4:])
            # print "hotspot y", i16(s[6:])
            # print "bytes", i32(s[8:])
            # print "offset", i32(s[12:])

        # load as bitmap
        self._bitmap(i32(m[12:]) + offset)

        # patch up the bitmap height
        self.size = self.size[0], self.size[1]//2
        d, e, o, a = self.tile[0]
        self.tile[0] = d, (0, 0)+self.size, o, a

        return


#
# --------------------------------------------------------------------

Image.register_open("CUR", CurImageFile, _accept)

Image.register_extension("CUR", ".cur")
