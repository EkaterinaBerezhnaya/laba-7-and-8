from PIL import Image
i = Image.open("Кот.jpg")
i2 = i.reduce(3)
i2otzerk = i.transpose(Image.FLIP_LEFT_RIGHT)
i2vertik = i2otzerk.rotate(90)
# i2.show()
# i2otzerk.show()
# i2vertik.show()
i2.save("Уменьшенный.jpg")
i2otzerk.save("Гориз+отзерк.jpg")
i2vertik.save("Вертик+отзерк.jpg")
