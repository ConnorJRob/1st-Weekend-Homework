# WRITE YOUR FUNCTIONS HERE

import pdb

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash_amount):
    #need to update the dictionary with the change in cash value
        #in the function that calls this one it then simply calls the new cash value using the previously established get_total_cash()
