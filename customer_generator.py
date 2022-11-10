import random
from atm import Customer
from event import EventEmitter, EVENT_NEW_CUSTOMER
from time import sleep

def generate_customer():
    while True:
        sleep(2)
        num_transac = random.randint(1, 10)
        num_id = random.randint(1, 1000)
        
        customer = Customer(id_number=str(num_id), num_transac=num_transac)

        print(f"New customer {customer}")

        EventEmitter.emit(EVENT_NEW_CUSTOMER, customer)
