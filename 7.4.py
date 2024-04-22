from PIL import Image, ImageFont, ImageDraw
pic=Image.open("4num.jpg") #print(pic.mode) находится в режиме RGB (= без показателя прозрачности)
watermark = Image.new("RGBA", pic.size , (0, 0, 0, 0)) # четвертый (альфа) канал задает уровень прозрачности
watermark_draw=ImageDraw.Draw(watermark)
width, height = pic.size
width_text=width/(6)     #задаем координаты для расположения watermark
height_text=height/1.2
fnt=ImageFont.truetype("arial.ttf", 150)
watermark_draw.text((width_text, height_text), "Лабораторная 7", font=fnt, fill=(255,255,255, 120))
res=Image.alpha_composite(pic.convert("RGBA"), watermark) # функция Image.alpha_composite(p1, p2)
# накладывает изображения друг на друга. При этом p1 и p2 должны быть одинакового размера
# и в режиме RGBA
watermark.show()
res.show()



