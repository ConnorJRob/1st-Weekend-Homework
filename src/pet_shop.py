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

#funciton takes customer list and an index number as an argument, then return the value stored in the cash key of this customers dictionary
def get_customer_cash(customer):
    return customer['cash']
    
#function accesses specified customer and removes the cash_payment value provided from the cash key of their dictionary
def remove_customer_cash(customer, cash_payment):
    customer["cash"] -= cash_payment

#function returns the length of the pets list within the specified customers dictionary, i.e how many pets they have
def get_customer_pet_count(customer):
    return len(customer["pets"])

#function adds on the new_pet dictionary item to the specified customers ["pets"] list
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

#function compares the value in the cash key of the specified customer dictionary with the value in the price key of the new pet dictionary and returns true if the customer cash value is >=
def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

#function runs a series of logical checks before processing the sale of the pet, using a number of the already created functions to do so
def sell_pet_to_customer(pet_shop, pet, customer):
    #in order to account for the test where the pet name 'dave' is given, resulting in a null result from the find_pet_by_name functon, this if statment ends the sale function if no such pet is found in the pet store list
    if pet == None:
        print("I'm sorry, we have no pets by that name")
    else:
        afford = customer_can_afford_pet(customer, pet)
        if afford == True:
            remove_customer_cash(customer,pet["price"])
            add_or_remove_cash(pet_shop, pet["price"])
            increase_pets_sold(pet_shop, 1)
            add_pet_to_customer(customer, pet)
        else:
            print("Im sorry, you do not have sufficient funds for this purchase")


