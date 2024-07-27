import datetime
class Freddy:
    """Основной класс помощника Freddy"""

    def __init__(self,status):
        self.status = status
        self.name = 'Freddy'
        self.age = f"{int(datetime.date.today().year) - 2024} лет"
        self.name_dev = "Мой создатель NMD"
        self.friends_list =
        self.menu = [
            'q - выключить Freddy',
            'name - узнать имя',
            'age - узнать возраст'
        ]
        if self.status:
            self.startFreddy()
    def startFreddy(self):
        print(f"Привет, я {self.name}! Вот что я умею\n")

        while(self.status):

            for i in self.menu:
                print(i)
            user_com = input("\nВведите команду > ")

            if user_com == 'q':
                print('Отключение...')
                self.status = False
            elif user_com == 'name':
                print(self.name + '\n')
            elif user_com == 'age':
                print(self.age + '\n')
            else:
                print("Я еще этого не умею")

if __name__ == '__main__':
    user_com = input("включить Freddy (y/n)? > ")
    freddy = Freddy(True if user_com == "y" else False)