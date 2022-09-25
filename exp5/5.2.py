# -*- codeing = UTF-8 -*-
# @Time : 2021/1/17 14:52
# @Author : 马增龙 15634099385
# @File : 5.2.py
# @Software : PyCharm
class car:
    def __init__(self, year, model, make):
        self.speed = 0
        self.model = model
        self.year = year

    def getspeed(self):
        return self.speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def info(self):
        print("当前速度为", self.speed, "公里/时")


def main():
    user = car(2021, "supercar", "Lamborghini")
    for i in range(5):
        user.accelerate()
        user.info()
    for j in range(5):
        user.brake()
        user.info()

    main()

