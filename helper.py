from faker import Faker




faker = Faker()

class Generator:

    # статический метод генерирует пользователя со случайными данными
    @staticmethod
    def random_user_data():
        user_data = {
            "email": faker.email(domain='mail.com'),
            "password": faker.password(length=10, special_chars=False, upper_case=False),
            "name": faker.first_name()
        }
        return user_data


