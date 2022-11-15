# Инкапсуляция

# private protected public

# class Product:
#
#     def __init__(self, name: str, price: int):
#         self.name = name
#         self.price = price
#
#     def get_info(self):
#         print(f"{self.name} - {self.price}")
#
#
# potato = Product("potato", 25)
# potato.get_info()
import uuid


# class Bank:
#     def __init__(self, name: str):
#         self.name = name
#         self.__generate_account()
#
#     @property
#     def account(self):
#         print(f"Ваш аккаунт {self.account}")
#
#     def __generate_account(self):
#         self.account = str(uuid.uuid4())
#
#     @account.setter
#     def account(self, key_word: str):
#         self.account = str(uuid.uuid4()) + self.name
#
#
# """_ - before methods signature means protected"""
# """_- - before methods signature means private"""
#
# nazgul = Bank("Nazgul")
# nazgul.account
# nazgul.account = "no_name"


# getter, setter

# Задача 2
username_list = ["Nazgul", "Bekbolsun", "Syimyk"]


class Registration:

    """ def __init__ validates the created user if it is already had been created, had it had wrong password
        standart, if the e-mail correct. For that purposes there are following methods:

        __username_validate()
        __password_validate()
        __email_validate()

        After that all mentioned methods were successfully passed, then Registration object will be
        added to the username_list by method .append()
    """

    def __init__(self, user_name: str, password: str, email: str):
        self.user_name = user_name
        self.__username_validate()
        self.password = password
        self.__password_validate()
        self.email = email
        self.__email_validate()
        username_list.append(self.user_name)
        print(f"Пользователь {self.user_name} был успешно добавлен в систему")

    def __password_validate(self):
        if len(self.password) < 8 or self.password.isalpha() or self.password.isdigit() or self.password[0].islower():
            raise Exception("Пароль должен содержать не менее 8 символов включая символы и числа")

    def __username_validate(self):
        if self.user_name in username_list:
            raise Exception("Данный пользователь уже существует")

    def __email_validate(self):
        if self.email.endswith("@gmail.com") or self.email.endswith("@outlook.com") or self.email.endswith("@mail.ru"):
            pass
        else:
            raise Exception("Введите корректный e-mail")

    def get_info(self):
        print(f"Пользователь: {self.user_name}, пароль: {self.password}, e-mail пользователя: {self.email}")


while True:
    input_user_name = input("Введите username: ")
    input_user_password = input("Введите password: ")
    input_user_email = input("Введите email: ")
    if input_user_email == "выйти".lower() \
            or input_user_password == "выйти".lower() \
            or input_user_email == "выйти".lower():
        break
    created_user = Registration(input_user_name, input_user_password, input_user_email)
    created_user.get_info()




