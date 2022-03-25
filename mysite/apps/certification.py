from PIL import Image
import sys
import itaizi
import pyocr
import pyocr.builders

# 氏名と画像データを引数として受け取る
def certification(file,first,last):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        sys.exit(1)
    tool = tools[0]

# pyocrの言語を日本語に設定する
    lang = "jpn"
    txt = tool.image_to_string(
        file,
        lang=lang,
        builder=pyocr.builders.TextBuilder())

# 取得したテキスト内に氏名が含まれているか確認する
# この時、itaiziを用いて異体字、正字それぞれでのチェックを行う
    if ((itaizi.to_seizi(first) in txt) or (itaizi.to_itaizi(first) in txt)) and ((itaizi.to_seizi(last) in txt) or (itaizi.to_itaizi(last) in txt)):
        txt = ""
        return True
    else:
        txt = ""
        return False
