class Bird:
    def __init__(self):
        print('Bird init')
        self.age = 10

    def eat(self):
        print('Bird eat')


class SongBird(Bird):
    def __init__(self):
        print('SongBird init')
        super().__init__()

    def sing(self):
        super().eat()
        print(self.age)

    def eat(self):
        print('SongBird eat')


bird = SongBird()
bird.sing()


