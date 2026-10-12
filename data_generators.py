import random
from faker import Faker

fake = Faker('ru_RU')

def generate_unique_name():
    return fake.first_name()

def generate_unique_last_name():
    return fake.last_name()

def generate_unique_phone_number():
    digits = ''.join(random.choices('0123456789', k=10))
    return '8' + digits

def generate_address():
    return f"ул. {fake.street_name()}, д. {fake.building_number()}"