import random
from PIL import Image, ImageFont, ImageDraw
slovar={"день рождения" : "др.jpg",
        "новый год" : "новый год.jpg",
        "пасха" : "пасха.jpg",
        "масленица" : "Масленица.jpg"}
pr=input("К каком празднику вам нужна открытка? ")
name=input("Введите имя того, кого вы хотите поздравить ")
txt=name+", поздравляю!"
pic=Image.open(slovar[pr])
pic_draw=ImageDraw.Draw(pic)
watermark = Image.new("RGBA", pic.size , (0, 0, 0, 0))
watermark_draw=ImageDraw.Draw(watermark)
width, height = pic.size
position_text=[height-40, (height/2),70] #массив с положениями шрифта: сверху, посередине, снизу
fnt=ImageFont.truetype("arial.ttf", random.randint(35,50)) #шрифт рандомного размера
dl_text = pic_draw.textlength(txt, font=fnt)
width_text=(width-(dl_text))/(2)     #задаем координаты для расположения текста
height_text=height-(random.choice(position_text))
clr=[] #color
for i in range(3):
        clr.append(random.randint(0,255))
watermark_draw.text((width_text, height_text), txt, font=fnt, fill=(clr[0],clr[1],clr[2], 255))
#смещаем тот же текст, чтобы сделать жирный шрифт
watermark_draw.text((width_text+1, height_text+1), txt, font=fnt, fill=(clr[0],clr[1],clr[2], 255))
watermark_draw.text((width_text-1, height_text-1), txt, font=fnt, fill=(clr[0],clr[1],clr[2], 255))
res=Image.alpha_composite(pic.convert("RGBA"), watermark)
res.show()
res.save("Результат 8.3.png")
