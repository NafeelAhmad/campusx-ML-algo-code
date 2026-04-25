# class PaymentGateway:
#     def process_payment(self,amount):
#         print('making payment on stripe')
#         pass

# class Item:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price

# class Order:
#     def __init__(self,order_id,items,payment_gateway):
#         self.order_id = order_id
#         self.items = items
#         self.payment_gateway = payment_gateway

#     def calculate_total(self):
#         total = sum(item.price for item in self.items)
#         return total

#     def place_order(self):
#         total = self.calculate_total()
#         self.payment_gateway.process_payment(total)

# class OrderManager:
#     def __init__(self,order):
#         self.order = order


#     def place_order(self):
#         self.order.place_order()

# payment_gateway = PaymentGateway()
# order_items = [
#     Item('Product 1',10),
#     Item('Product 2',20),
#     Item('Product 3',15)
# ]

# order = Order(123,order_items,payment_gateway)
# order_manager = OrderManager(order)
# order_manager.place_order()


from abc import ABC, abstractmethod

# Abstraction
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


# Concrete implementations
class StripePayment(PaymentGateway):
    def process_payment(self, amount):
        print("Payment via Stripe:", amount)


class RazorpayPayment(PaymentGateway):
    def process_payment(self, amount):
        print("Payment via Razorpay:", amount)


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self, order_id, items, payment_gateway: PaymentGateway):
        self.order_id = order_id
        self.items = items
        self.payment_gateway = payment_gateway

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def place_order(self):
        total = self.calculate_total()
        self.payment_gateway.process_payment(total)


class OrderManager:
    def __init__(self, order):
        self.order = order

    def place_order(self):
        self.order.place_order()


# Usage
payment = RazorpayPayment()  # Change here only
items = [Item("A", 10), Item("B", 20)]

order = Order(1, items, payment)
OrderManager(order).place_order()