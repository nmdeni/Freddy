import datetime
class Freddy:
    """Основной класс помощника Freddy"""

    def __init__(self,status):
        self.name = 'Freddy'
        self.age = int(datetime.date.today().year) - 2024
        self.status = status
        self.menu = [
            'q - выключить Freddy',
            'name - узнать имя',
            'age - узнать возраст'
        ]

        self.startFreddy()
    def startFreddy(self):
        while(self.status):
            for i in self.menu:
                print(i)
            user_com = input("Введите команду > ")

if __name__ == '__main__':
    user_com = input("включить Freddy (y/n)? > ")
    freddy = Freddy(True if user_com == "y" else False)