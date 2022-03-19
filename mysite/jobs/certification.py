from operator import truediv
from PIL import Image
import sys

import pyocr
import pyocr.builders

# TODO　ファイルのパスを受け取れるようにする
def certification(file,first,last):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)

    tool = tools[0]


    langs = tool.get_available_languages()
    lang = "jpn"

    txt = tool.image_to_string(
        # imageを受け取る
        Image.open(file),
        lang=lang,
        builder=pyocr.builders.TextBuilder())
    print(txt)

    if first in txt and last in txt:
        print(1)
        return True
    else:
        print(2)
        return False
