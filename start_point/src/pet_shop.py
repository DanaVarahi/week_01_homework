import pdb


def get_pet_shop_name(pet_shop):
    return pet_shop['name']


def get_total_cash(pet_shop):
    return pet_shop['admin']['total_cash']


def add_or_remove_cash(pet_shop, amount):
    pet_shop['admin']['total_cash'] += amount
    return pet_shop['admin']['total_cash']


def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']


def increase_pets_sold(pet_shop, amount):
    pet_shop['admin']['pets_sold'] += amount
    return pet_shop['admin']['pets_sold']


def get_stock_count(pet_shop):
    return len(pet_shop['pets'])


def get_pets_by_breed(pet_shop, breed):

    pets_of_breed = []

    for pet in pet_shop['pets']:
        if pet['breed'] == breed:
            pets_of_breed.append(pet)

    return pets_of_breed


def find_pet_by_name(pet_shop, name):
    # pdb.set_trace()
    named_pet = []

    for pet in pet_shop['pets']:
        if pet['name'] == name:
            named_pet = pet

    return named_pet
