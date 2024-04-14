from faker import Faker

fake = Faker('ru_RU')

for i in range(30):
    print(fake.name())