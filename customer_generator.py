import random
from atm import Customer
from customer_subscriber import _handlers, new_customer


def generate_customer():

    print(f"Customer generator start with handlers {_handlers}")
    
    num_transac = random.randint(1, 10)
    num_id = random.randint(1, 1000)
    
    return Customer(id_number=str(num_id), num_transac=num_transac)
