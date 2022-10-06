import pytest

from PIL.GimpPaletteFile import GimpPaletteFile


def test_sanity():
    with open("Tests/images/test.gpl", "rb") as fp:
        GimpPaletteFile(fp)

    with open("Tests/images/hopper.jpg", "rb") as fp:
        with pytest.raises(SyntaxError):
            GimpPaletteFile(fp)

    with open("Tests/images/bad_palette_file.gpl", "rb") as fp:
        with pytest.raises(SyntaxError):
            GimpPaletteFile(fp)

    with open("Tests/images/bad_palette_entry.gpl", "rb") as fp:
        with pytest.raises(ValueError):
            GimpPaletteFile(fp)


def test_large_file_is_truncated():
    import warnings
    from unittest.mock import patch

    try:
        original_value = GimpPaletteFile._max_file_size
        GimpPaletteFile._max_file_size = 100
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            with pytest.raises(UserWarning):
                with open("Tests/images/custom_gimp_palette.gpl", "rb") as fp:
                    palette_file = GimpPaletteFile(fp)

    finally:
        GimpPaletteFile._max_file_size = original_value


def test_get_palette():
    # Arrange
    with open("Tests/images/custom_gimp_palette.gpl", "rb") as fp:
        palette_file = GimpPaletteFile(fp)

    # Act
    palette, mode = palette_file.getpalette()

    # Assert
    expected_palette = b""
    for color in (
        (0, 0, 0),
        (65, 38, 30),
        (103, 62, 49),
        (79, 73, 72),
        (114, 101, 97),
        (208, 127, 100),
        (151, 144, 142),
        (221, 207, 199),
    ):
        expected_palette += bytes(color)
    assert palette == expected_palette
    assert mode == "RGB"


def test_n_colors():
    # Arrange
    with open("Tests/images/custom_gimp_palette.gpl", "rb") as fp:
        palette_file = GimpPaletteFile(fp)

    palette, _ = palette_file.getpalette()
    assert len(palette) == 24
    assert palette_file.n_colors == 8
