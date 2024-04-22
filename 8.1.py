from PIL import Image
left=int(input("Сколько обрезать слева? "))
right=int(input("Сколько обрезать справа? "))
upper=int(input("Сколько обрезать сверху? "))
lower=int(input("Сколько обрезать снизу? "))
pic=Image.open("Масленица.jpg")
width, height = pic.size
res=pic.crop((left, upper, width-right, height-lower))
#crop(left,upper,right, lower).Координаты, соответствующие картинке изначально (0,0, ширина, высота)
pic.show()
res.show()
res.save("результат 8.1.jpg")