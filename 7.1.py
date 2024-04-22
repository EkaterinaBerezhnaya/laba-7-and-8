from PIL import Image
i=Image.open("Кот.jpg")
i.show()
print(i.size, i.format, i.mode)