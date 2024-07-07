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
            print(f"Привет, я {self.name}! Вот что я умею")

            for i in self.menu:
                print(i)
            user_com = input("Введите команду > ")

            if user_com == 'q':
                self.status = False
            elif user_com == 'name':
                print(self.name)
            elif user_com == 'age':
                print(self.age)
            else:
                print("Я еще этого не умею")

if __name__ == '__main__':
    user_com = input("включить Freddy (y/n)? > ")
    freddy = Freddy(True if user_com == "y" else False)