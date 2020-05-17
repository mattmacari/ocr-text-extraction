
import pathlib

from google.cloud.vision import types

from ocr_text_extraction import utils

def generate_image(path: pathlib.Path) -> types.Image:
    """
    Takes a path and returns an image to be processed.
    """
    content = utils.read_file(path=path)
    return types.Image(content=content)
