import datetime
import psycopg2
class Freddy:
    """Основной класс помощника Freddy"""

    def __init__(self,status):
        self.status = status
        self.name = 'Freddy'
        self.age = f"{int(datetime.date.today().year) - 2024} лет"
        self.name_dev = "Мой создатель NMD"
        # self.friends_list =
        self.menu = [
            'q - выключить Freddy',
            'name - узнать имя',
            'age - узнать возраст'
        ]

        if self.status:
            self.startFreddy()
    def startFreddy(self):
        self.connect_db()
        print(f"Привет, я {self.name}! Вот что я умею\n")

        while(self.status):

            for i in self.menu:
                print(i)
            user_com = input("\nВведите команду > ")

            if user_com == 'q':
                print('Отключение...')
                self.status = False
            elif user_com == 'name':
                print("Меня зовут " + self.name + '\n')
            elif user_com == 'age':
                print("Мне " + self.age + '\n')
            else:
                print("Я еще этого не умею")

    def connect_db(self):
        print('Подключение к базе данных')
        user_info_db = {
            'user': '',
            'dbname': '',
            'password': ''
        }

        for k in user_info_db.keys():
            print(k)
            user_info_db[k] = input('> ')
        try:
            self.conn_db = psycopg2.connect(
                dbname=user_info_db['dbname'],
                user=user_info_db['user'],
                password=user_info_db['password'])
            print('Подключение прошло успешно!!!')
        except:
            print('Не удалось подключиться к базе данных!!!')

if __name__ == '__main__':
    user_com = input("включить Freddy (y = Да)? > ")
    freddy = Freddy(True if user_com == "y" else False)