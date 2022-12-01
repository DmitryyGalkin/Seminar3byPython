""" Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой."""


# name = input("Введите Ваше имя: ")
# surname = input("Введите Вашу фамилию: ")
# year = int(input("Введите год Вашего рождения: "))
# user_city = input("Город Вашего проживания: ")
# email = input("Введите Ваш email: ")
# phone = int(input("Введите номер Вашего телефона: "))


def user_form(name, surname, year, user_city, email, phone):
    print(f"{name}, {surname}, {year}, {user_city}, {email}, {phone}")


user_form(name="Dmitry", surname="Galkin", year=1986,
                user_city="Orel", email="gdo@mail.ru",
                phone=89198888888)
