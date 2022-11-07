from atm import ATM, Customer
from customer_generator import generate_customer
from customer_subscriber import add_handler
from ui import ATMUi
from asyncio import get_event_loop, ensure_future, create_task

from tkinter import *
from tkinter import ttk






# atm.start()
# atm.join()

# customer_generator.start()
# customer_generator.join()


if __name__ == "__main__":
    
    root = Tk()

    root.title("ATM")

    root.geometry("400x400")

    customer_list = Frame(root, width=200,)
    customer_list.pack(expand=True, fill=BOTH, side=LEFT)

    customers = Listbox(master=customer_list)
    customers.insert(1, "123123 -> cusadasdaosda")

    customers.pack()


    customer_transaction = Frame(root, width=400)
    customer_transaction.pack(expand=True, fill=BOTH, side=RIGHT)
    

    title_container = Frame(master=customer_transaction, height=40)
    title = Label(master=title_container, text="Customer")
    title.pack(side=LEFT)

    customer_name = Label(master=title_container, text="Customer id")
    customer_name.pack(side=RIGHT)

    title_container.pack()


    root.mainloop()
