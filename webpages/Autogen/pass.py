import pandas as pd
from PIL import Image, ImageDraw, ImageFont

data = pd.read_excel (r'E:\Django Projects\DjangoWeb\webpages\Autogen\list1.xlsx') 
name_list = data["Name"].tolist() 
for i in name_list:
    im = Image.open(r'E:\Django Projects\DjangoWeb\webpages\Autogen\pictures\certificate.jpg')
    d = ImageDraw.Draw(im)
    location = (100, 398)
    text_color = (0, 137, 209)
    font = ImageFont.truetype("arial.ttf", 120)
    d.text(location, i, fill = text_color, font = font)
    im.save("certificate_" + i + ".pdf")