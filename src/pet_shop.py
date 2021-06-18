# WRITE YOUR FUNCTIONS HERE
import pdb

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash_amount):
    #need to update the dictionary with the change in cash value
        #in the function that calls this one it then simply calls the new cash value using the previously established get_total_cash()
    pet_shop["admin"]["total_cash"] = (pet_shop["admin"]["total_cash"] + cash_amount)

def get_pets_sold(pet_shop):
    #need to return the pets sold value from admin dictionary
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pet_sales):
    #need to update the dictionary with the change pets sold
    pet_shop["admin"]["pets_sold"] = (pet_shop["admin"]["pets_sold"] + pet_sales)

def get_stock_count(pet_shop):
    #need to take a count of the keys in the pets list, as each pet is one stock
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    # pdb.set_trace()
    #need to create a list of dog names that have a breed matching the breed type specified
    pets_matching_breed = []
    for pet in pet_shop["pets"]:
        #pets is a list not a dictionary, so breed is not a key of pets
        if breed == pet['breed']:
            pets_matching_breed.append(pet['name'])
    return pets_matching_breed

