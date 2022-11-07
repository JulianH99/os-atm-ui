from typing import Callable, List
from atm import Customer

_handlers: List[Callable] = []


def add_handler(handler: Callable) -> None:
    _handlers.append(handler)
    print(f"Handlers are {_handlers}")

def new_customer(customer: Customer) -> None:
    print(f"Taking new customer to {_handlers}")
    for handler in _handlers:
        handler(customer, "new")