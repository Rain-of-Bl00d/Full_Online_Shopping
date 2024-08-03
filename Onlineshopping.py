class Product:
    #initialization of instance attributes
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_saved = price - deal_price
    
    #instance method printing 
    def display_products_details(self):
        print("product :{}".format(self.name))
        print("price of the product :{}".format(self.price))
        print("deal price of the product :{}".format(self.deal_price))
        print("ratings of the product :{}".format(self.ratings))
        print("you saved on the product :{}".format(self.you_saved))
        
    def get_deal_price(self):
        return(self.deal_price)

class ElectronicItems(Product):
    def __init__(self, name, price, deal_price, ratings, warrenty_in_months):
        super().__init__(name, price, deal_price, ratings)
        self.warrenty_in_months = warrenty_in_months
    
    def display_products_details(self):
        super().display_products_details()
        print("warrenty :{}".format(self.warrenty_in_months))
        print("-------------------")

class GroceryItems(Product):
    def __init__(self, name, price, deal_price, ratings, expiry_date):
        super().__init__(name, price, deal_price, ratings)
        self.expiry_date = expiry_date
    
    def display_products_details(self):
        super().display_products_details()
        print("expiry date :{}".format(self.expiry_date))
        print("-------------------")

class Order:
    delivery_charges ={
        'Normal' : 10,
        'Prime delivery' : 100 
    }
    
    def __init__(self, delivery_method, delivery_address):
        self.items_in_cart = []
        self.delivery_method = delivery_method
        self.delivery_address = delivery_address
    
    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))
        
    def display_order_details(self):
        print("Delivery Method :{}".format(self.delivery_method))
        print("Delivery Address :{}".format(self.delivery_address))
        print("Products :")
        print("=============")
        for product, quantity in self.items_in_cart:
            product.display_products_details()
            print("Quantity :{}".format(quantity))
        total_bill = self.get_total_bill()
        print("Ttoal Bill :",total_bill)
        print("-------------------")
    
    def get_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            total_bill += product.get_deal_price() * quantity
        order_delivery_charges = Order.delivery_charges[self.delivery_method]
        total_bill += order_delivery_charges
        return(total_bill)
    
    @classmethod
    def update_delivery_charges(cls, delivery_method, charges):
        cls.delivery_charges[delivery_method] = charges
        
Tv = ElectronicItems("Sony", 50000, 40000, 4.5, 12)
Milk = GroceryItems("Amul", 45, 35, 5.0, "Aug_12/24")

my_order = Order("Normal", "Kolkata")
my_order.add_item(Tv, 1)
my_order.add_item(Milk, 4)

my_order.display_order_details()
my_order.get_total_bill()

Order.update_delivery_charges("Normal", 30)
my_order.get_total_bill()