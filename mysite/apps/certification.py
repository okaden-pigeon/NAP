from operator import truediv
from PIL import Image
import sys
import itaizi

import pyocr
import pyocr.builders

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
        file,
        lang=lang,
        builder=pyocr.builders.TextBuilder())
    print(itaizi.to_seizi("齋藤"))

    if (itaizi.to_seizi(first) in txt or itaizi.to_itaizi(first) in txt) and (itaizi.to_seizi(last) in txt or itaizi.to_itaizi(last) in txt) :
        txt = ""
        return True
    else:
        txt = ""
        return False
