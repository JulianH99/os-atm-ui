from __future__ import annotations

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


class ATM():
    
    head = Node()
    kill = False

    def put_customer_inline(self, customer: Customer):
        customer.next = self.head
        if self.head.next is None:
            self.head.next = customer
        else:
            prev_customer = self.head.next
            while prev_customer.next != self.head:
                prev_customer = prev_customer.next
            prev_customer.next = customer
