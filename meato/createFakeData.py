import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meato.settings")

import django

django.setup()

import faker.providers
from faker import Faker
from MainContainer.models import Meat, MeatType, Staff, Store
from model_bakery.recipe import Recipe, foreign_key

MEAT_CATEGORIES = ['beef', 'pork', 'chicken', 'lamb', 'fish', 'other']
STORE_CATEGORIES = ['meat', 'dairy', 'bakery', 'produce', 'other']
MEAT_TYPES = ['ground', 'steak', 'roast', 'sausage', 'other']
class Provider(faker.providers.BaseProvider):
    def meat_categories(self):
        return self.random_element(MEAT_CATEGORIES)

    def store_categories(self):
        return self.random_element(STORE_CATEGORIES)

    def meat_types(self):
        return self.random_element(MEAT_TYPES)

fake = Faker()
fake.add_provider(Provider)

for k in range(100):

    meattype = Recipe(
    MeatType,
    name = fake.meat_types(),
    )
    meattype.make()

    store = Recipe(
    Store,
    name = fake.name(),
    address = fake.address(),
    phone = fake.phone_number(),
    email = fake.email(),
    website = fake.text(),
    image=fake.image_url(),
    meat_category=fake.meat_categories(),
    state = fake.state(),
    country = fake.country(),
    total_meat = fake.random_int(),
    total_price = fake.random_int(),
    description = fake.text(),
    store_date=fake.date_time(),
    )

    store.make()

    meat = Recipe(
    Meat,
    name=fake.name(),
    price=fake.random_int(1000, 100000, 1000),
    image=fake.image_url(),
    description=fake.text(),
    meat_type=foreign_key(meattype),
    meat_size=fake.random_int(1, 50),
    meat_price=fake.random_int(1000, 100000),
    meat_category=foreign_key(store),
    date_added=fake.date_time(),
    slaughtered_date=fake.date_time(),
    )
    meat.make()

    staff = Recipe(
    Staff,
    image = fake.image_url(),
    firstname = fake.name(),
    lastname = fake.name(),
    stipend = fake.random_int(1000, 100000, 1000),
    phone_no = fake.phone_number(),
    store = foreign_key(store),
    country = fake.country(),
    )

    staff.make()
