from operator import truediv
from PIL import Image
import sys

import pyocr
import pyocr.builders

# TODO　ファイルのパスを受け取れるようにする
def certification():
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)

    tool = tools[0]


    langs = tool.get_available_languages()
    lang = "jpn"

    txt = tool.image_to_string(
        Image.open('../images/test4.webp'),
        lang=lang,
        builder=pyocr.builders.TextBuilder())

    name = "#TODO"
    if name in txt:
        return True
    else:
        return False

