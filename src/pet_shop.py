# WRITE YOUR FUNCTIONS HERE
import pdb

#function searching the pet_shop dictionary and returns the value assigned to the name key
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

#function searching the admin dictionary within the petshop dictionary and returns the value assigned to the total_cash key
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

#function locates the value assigned to the total_cash key within the nested admin dictionary and adjusts it by the cash amount value provided (+/-)
def add_or_remove_cash(pet_shop, cash_amount):
    pet_shop["admin"]["total_cash"] = (pet_shop["admin"]["total_cash"] + cash_amount)

#function searching the admin dictionary within the petshop dictionary and returns the value assigned to the pets_sold key
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

#function searching the admin dictionary within the petshop dictionary and adjusts the value assigned to the pets_sold key using the pet_sales argument
def increase_pets_sold(pet_shop, pet_sales):
    pet_shop["admin"]["pets_sold"] += pet_sales

#function checks the length of the pets list within the pet shop dictionary as each item in the list is a pet (stock item)
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    #function creates a blank list of pets matching the specified breed
    pets_matching_breed = []
    #funciton loops through the items in the pet shop list
    for pet in pet_shop["pets"]:
        #if the list item (which is a dictionary) has a value in it's "breed" key matching the breed argument then this pets name is added to the pets_matching_breed list
        if breed == pet["breed"]:
            pets_matching_breed.append(pet["name"])
    return pets_matching_breed

#function takes the pet name argument and loops through the pet_shop list
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        #if the pet name argument matches the pet['name'] value of the list item, the entire list item (dictionary) for this pet is returned
         if pet_name == pet["name"]:
            return pet
            break

#function takes the pet name argument and loops through the pet_shop list
def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        #if the pet name argument matches the pet['name'] value of the list item, the entire list item (dictionary) for this pet is removed from the pet_shop list
         if pet_name == pet["name"]:
            pet_shop["pets"].remove(pet)
            break

#function adds on the new_pet dictionary item to the pet_shop["pets"] list
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

