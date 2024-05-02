from faker import Faker

fake = Faker('ru_RU')

for i in range(13):
    print(fake.city_name())