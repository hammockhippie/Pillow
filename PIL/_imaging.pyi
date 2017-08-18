if False:
    from PIL.aliases import *

    from typing import Any  # temporarily, hopefully ;)
    from typing import Optional, List

PILLOW_VERSION = ...
DEFAULT_STRATEGY = ...
FILTERED = ...
HUFFMAN_ONLY = ...
RLE = ...
FIXED = ...

# List of functions is incomplete

def alpha_composite(core1: ImagingCore, core2: ImagingCore) -> ImagingCore: ...
def blend(core1: ImagingCore, core2: ImagingCore, alpha: float) -> ImagingCore: ...
def fill(mode: Mode, size: Size, color: Any) -> Any: ...
def new(mode: Mode, size: Size) -> ImagingCore: ...

def map_buffer(data, size, decoder_name, isNone, isint, args): ...

def crc32(): ... ###

def effect_mandelbrot(size, extent, quality): ...
def effect_noise(size, sigma): ...
def linear_gradient(mode): ...
def radial_gradient(mode): ...
def wedge(something): ...

class ImagingCore:
    mode = ...  # type: str
    size = ...  # type: Size  ## close enough?
    bands = ...  # type: int
    id = ... ### use? size_t? int?
    ptr = ... ###

    def getpixel(self, xy: XY) -> Optional[Any]: ...
    def putpixel(self, xy: XY, value: Any) -> None: ...
    def pixel_access(self, readonly: bool) -> Any: ...

    def convert(self, mode, dither, paletteimage): ...
    def convert2(self): ... ###
    def convert_matrix(self, a): ...
    def convert_transparent(self, a, b): ...
    def copy(self) -> ImagingCore: ...
    def crop(self, bbox: LURD) -> ImagingCore: ...
    def expand(self, xmargin: int, ymargin: int, mode: Mode) -> Any: ...
    def filter(self, xy, divisor, offset, kernel): ...
    def histogram(self, tuple2: Optional[Any], coremask: Optional[Any]) -> List[int]: ...

    def modefilter(self, i: int) -> Any: ...

#    def offset(self): ... ### Function removed?

    def paste(self, core: ImagingCore, box: LURD, coremask: ImagingCore) -> None: ...
    def point(self, lut, mode): ...
    def point_transform(self, scale, offset): ...
    def putdata(self, data, scale, offset): ...

    def quantize(self, colors, method, kmeans): ...

    def rankfilter(self): ... ###

    def resize(self, size, resample): ...
    def transpose(self, method): ...
    def transform2(self, box, core, method, data, resample, fill): ...

    def isblock(self): ... ###

    def getbbox(self) -> Optional[LURD]: ...
    def getcolors(self, maxcolors): ...
    def getextrema(self): ... ###
    def getprojection(self): ... # returns tuple x, y

    def getband(self, band): ...
    # each band has: getextrema() which may return a 2tuple?
    def putband(self, alphacore, band): ...
    def split(self): ...
    def fillband(self, band, alpha): ...

    def setmode(self, mode): ...

    def getpalette(self, mode): ...
    def getpalettemode(self): ... ###
    def putpalette(self, a): ...
    def putpalettealpha(self, a, b): ...
    def putpalettealphas(self, a): ...

### chop_* here

### gaussian_blur and unsharp_mask here

### box_blur here

    def effect_spread(self, distance): ...

    def new_block(self): ... ###

    def save_ppm(self, file): ... ###
