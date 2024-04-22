from PIL import Image, ImageFilter
for i in range(1,6):
    nazvan=str(i)+".jpg"
    pic=Image.open(nazvan)
    pic=pic.filter(ImageFilter.CONTOUR)
    nazvan ="D:\Pycharm\Сохраненные изображения лабы 7 8"+"\\"+ str(i) + " результат" + ".jpg"
    pic.save(nazvan)


