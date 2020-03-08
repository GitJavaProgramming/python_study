# python 类与对象
class Dog():
    # 形参self必不可少，且在第一位
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + "sit")

    def roll_over(self):
        print(self.name.title() + " rolled over!")
        return "next_line"


class Wolf(Dog):
    def __init__(self, transform, name, age):
        super().__init__(name, age)
        self.transform = transform
        self.dog = Dog("狗", 3)

    def tansform(self):
        print("变身狼人")
