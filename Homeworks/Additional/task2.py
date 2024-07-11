class Product:
    def __init__(self, name:str, price:float, quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity
        

    def get_product(self):
        return f"""
        Product Name: {self.name} 
        Product Price: {self.price}$ 
        Product Quantity: {self.quantity}"""
    
    def update_quantity(self, new_quatity)->int:
        self.quantity = new_quatity
        return f"""Product Quantity: {self.quantity}"""
    
    def apply_discount(self, discount):
        self.price =(self.price / 100) * discount
        return f"{self.price}$"
    
    def total_value(self)->float:
        return f"Total value is {self.quantity * self.price}$"
    
class Phone(Product):
    def __init__(self, name: str, price: float, quantity: int, brand, model):
        super().__init__(name, price, quantity)
        self.__brand = brand
        self.__model = model


    def get_product_info(self):
        return f"""{super().get_product()}
        Brand: {self.__brand}
        Model: {self.__model}"""


    def update_quantity(self, new_quatity:int)->int:
        return super().update_quantity(new_quatity)
    
    def apply_discount(self, discount):
        return super().apply_discount(discount)
    
    def total_value(self) -> float:
        return f"{super().total_value()}"
    
class Laptop(Product):
    def __init__(self, name: str, price: float, quantity: int, author:str, prodsessor:str):
        super().__init__(name, price, quantity)
        self.author = author
        self.prodsessor = prodsessor

    def get_product(self):
        return super().get_product()
    
    def update_quantity(self, new_quatity) -> int:
        return super().update_quantity(new_quatity)
    
    def apply_discount(self, discount):
        return super().apply_discount(discount)
    
    def total_value(self) -> float:
        return super().total_value()
    

class Book(Product):
    def __init__(self, name: str, price: float, quantity: int, author:str, genre:str):
        super().__init__(name, price, quantity)
        self.author = author
        self.genre = genre

    def get_product(self):
        return super().get_product()
    
    def update_quantity(self, new_quatity) -> int:
        return super().update_quantity(new_quatity)
    
    def apply_discount(self, discount):
        return super().apply_discount(discount)
    
    def total_value(self) -> float:
        return super().total_value()
    

class User:
    def __init__(self, name, _id, cart):
        self.__name = name
        self.__id = _id
        self.__cart = cart

    def get_user_info(self):
        return f"""
        Name: {self.__name} 
        User ID: {self.__id} 
        User cart:{self.__cart}"""
    
    def add_to_cart(self, product:str):
        self.user_cart = list()
        self.user_cart.append(product)

    def view_cart(self):
        return f"View Cart: {self.user_cart}"
    
class OnlineShopingSystem:
    def __init__(self, products, users):
        self.__products = products
        self.__users = users

    def add_products(self, product:Product):
        pass

        
    
# phone1 = Phone(name="iPhone 12", price=999.99, quantity=10, brand="Apple", model="12")
# book1 = Book(name="Uluq Gatsby", price=15.99, quantity=5, author="F. Scott Fitzgerald", genre="Klassika")

# # Foydalanuvchi yaratish
# user1 = User(name="Alice", user_id="F001")

# # Onlayn do'kon tizimini yaratish
# shopping_system = OnlineShoppingSystem()

# # Mahsulotlarni tizimga qo'shish
# shopping_system.add_product(phone1)
# shopping_system.add_product(book1)

# # Foydalanuvchini tizimga qo'shish
# shopping_system.add_user(user1)

# # Foydalanuvchi mahsulotlarni savatchaga qo'shish
# user1.add_to_cart(phone1)
# user1.add_to_cart(book1)

# # Mahsulotlarga chegirma qo'shish
# phone1.apply_discount(10)
# book1.apply_discount(20)

# # Foydalanuvchi savatchasini chiqarish
# print(user1.view_cart())

# # Tizimdagi mavjud mahsulotlarni chiqarish
# print(shopping_system.view_products())
