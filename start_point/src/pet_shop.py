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

    for pet in pet_shop['pets']:
        if pet['name'] == name:
            return pet

# this example is not working
# def remove_pet_by_name(list, name_to_remove):
#     for pet in list:
#         if pet['name'] == name_to_remove:
#             list.remove(pet)


# def add_pet_to_stock(list, newpet):
#     pdb.set_trace()
#     list['pets'].append(newpet)

# def get_customer_cash(customers, index):
#     return customers[index]['cash']

def get_customer_cash(customer):
    # pdb.set_trace()
    return customer['cash']


def remove_customer_cash(customer, amount):
    customer['cash'] -= amount
