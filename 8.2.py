from PIL import Image
slovar={"день рождения" : "др.jpg",
        "новый год" : "новый год.jpg",
        "пасха" : "пасха.jpg",
        "масленица" : "Масленица.jpg"}
pr=input("К каком празднику вам нужна открытка? ")
pic=Image.open(slovar[pr])
pic.show()