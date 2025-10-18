from customer import Customer

class CustomerQueue:
    def __init__(self):
        self.queue = []
        self.id_counter = 1

    def add_customer(self, name):
        customer = Customer(self.id_counter, name)
        self.queue.append(customer)
        print(f"Has agregado a {name} como cliente.")
        self.id_counter += 1

    def serve_customer(self):
        if not self.queue:
            print("No hay clientes en espera.")
        else:
            customer = self.queue.pop(0)
            print(f"Has atendido al cliente {customer.Name}.")

    def show_queue(self):
        if not self.queue:
            print("No hay clientes en la cola.")
        else:
            print("\nLista de clientes en espera:")
            for customer in self.queue:
                print(f"ID: {customer.ID_Customer} | Nombre: {customer.Name}")

    def remove_customer(self, customer_id):
        for customer in self.queue:
            if customer.ID_Customer == customer_id:
                self.queue.remove(customer)
                print(f"Has eliminado al cliente {customer.Name}.")
                return
        print("No se encontró un cliente con ese ID.")