from __future__ import annotations
from time import sleep
from event import EventEmitter, EVENT_NEW_CUSTOMER, EVENT_UPDATE_LIST

MAX_TRANSAC = 5

class Node:
    next: Node

    def __init__(self) -> None:
        self.next = None

class Customer(Node):
    id_number: str
    num_transac: int

    def __init__(self, id_number: str, num_transac: int) -> None:
        super().__init__()
        self.id_number = id_number
        self.num_transac = num_transac

    def __str__(self) -> str:
        return f"{self.id_number} - {self.num_transac}"


class ATM():
    
    head = Node()
    running = False

    def __init__(self) -> None:
        self.head.next = self.head

        EventEmitter.subscribe(EVENT_NEW_CUSTOMER, self.run)

    
    def run(self, customer):
        self.put_customer_inline(customer)

        if not self.running:
            self.running = True
            self.process_line()
            self.running = False
            
    
    def remove_customer_from_line(self, customer):
        
        head = self.head.next
        print(f"Remove item {customer} with head {head}")
        if head == customer and customer.next == head:
            self.head.next = self.head
            return

        last = head
        d = None

        if head == customer:
            while last.next != head:
                last = last.next

            last.next = head.next
            head = last.next

        while last.next != head and last.next != customer:
            last = last.next

        if last.next != customer:
            d = last.next
            last.next = d.next

    def put_customer_inline(self, customer: Customer):
        customer.next = self.head
        if self.head.next is None:
            self.head.next = customer
        else:
            prev_customer = self.head.next
            while prev_customer.next != self.head:
                prev_customer = prev_customer.next
            prev_customer.next = customer

    def customers_to_list(self, current = None, num_transac = 0):
        customer_list = []

        head = self.head.next

        while head != self.head:

            if current:
                if head.id_number == current.id_number:
                    customer_list.append(
                        Customer(id_number=head.id_number, num_transac=num_transac)
                    )
                else:
                    customer_list.append(head)

            head = head.next

        return customer_list


    def process_line(self):
        print("Running line with customers")
        current = self.head.next
        self.customers_to_list()

        while current != self.head:
            
            print(f"Process customer {current.id_number}")
            remaining_transac = current.num_transac - MAX_TRANSAC
            transac_to_proc = MAX_TRANSAC if remaining_transac > 0 else current.num_transac

            for i in range(0, transac_to_proc):
                print(f"Procesing transac #{i}")
                EventEmitter.emit(EVENT_UPDATE_LIST, self.customers_to_list(current, transac_to_proc - i))
                sleep(2)
            EventEmitter.emit(EVENT_UPDATE_LIST, self.customers_to_list())

            self.remove_customer_from_line(current)
            if remaining_transac > 0:
                print(f"Putting customer {current.id_number} back in line")    
                self.put_customer_inline(Customer(id_number=current.id_number, num_transac=remaining_transac))
            EventEmitter.emit(EVENT_UPDATE_LIST, self.customers_to_list())
            
            current = current.next
            
        EventEmitter.emit(EVENT_UPDATE_LIST, self.customers_to_list())
        print("Line is empty")
        