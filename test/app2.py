from PIL import Image,ImageFilter

code = Image.open("../douban/codeImg/code.png")
newCode = code.filter(ImageFilter.GaussianBlur)
newCode.save("newCode.png")
newCode.show()