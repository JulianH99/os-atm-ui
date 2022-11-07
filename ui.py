from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, DataTable, TextLog
from textual.widget import Widget
from textual.containers import Container
from textual.reactive import reactive
from customer_generator import generate_customer
from atm import Customer, ATM

class CustomerName(Widget):

    name = reactive("")

    def render(self):
        return self.name

class CustomerTransactions(Widget):

    transactions_number = reactive(0)

    def render(self):
        return f"Transactions: {self.transactions_number}"

class ATMScreen(Widget):

    customer_id = reactive("")
    customer_transactions = reactive(0)
    


    def compose(self) -> ComposeResult:
        yield Container(
            Static("Current customer"),
            CustomerName(),
            id="customer-name-row"
        )

        yield Container(CustomerTransactions(), id="transactions-title")

        yield Container(
            *[TextLog("transaction 1") for i in range(0, self.customer_transactions)]
        )

    def update(self):
        self.query_one(CustomerName).name = self.customer_id
        self.query_one(CustomerTransactions).transactions_number = self.customer_transactions

class ATMUi(App):

    BINDINGS = [("c", "generate_customer", "Generate new customer")]

    CSS_PATH = "main.css"

    atm = None

    current_customer = None

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("Id num", "Transactions num")

        self.atm = ATM()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

        yield Container(
            DataTable(classes="data-table"),
            ATMScreen(classes="atm-screen"),
            classes="main-container"
        )


    def action_generate_customer(self):
        # self.add_new_customer(generate_customer(), "new")
        customer = generate_customer()
        self.add_new_customer(customer)
        self.atm.put_customer_inline(customer)

        if self.current_customer is None:
            atm_screen = self.query_one(ATMScreen)

            atm_screen.customer_id = customer.id_number
            atm_screen.customer_transactions = customer.num_transac

            atm_screen.update()

            # self.query_one(ATMScreen).update()



    def add_new_customer(self, customer: Customer):
        
        print("new customer added to ui")
        self.query_one(DataTable).add_row(customer.id_number, str(customer.num_transac))
