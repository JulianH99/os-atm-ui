from threading import Thread

from atm import ATM
from customer_generator import generate_customer
from ui import ATMUI

if __name__ == "__main__":
    
    print("Initialize everything")

    atm = ATM()

    ui = ATMUI()

    print("New customer process")
    generate_customer_thread = Thread(target=generate_customer, daemon=True)
    ui_thread = Thread(target=ui.start)


    generate_customer_thread.start()
    ui_thread.start()

    generate_customer_thread.join()
    ui_thread.join()
