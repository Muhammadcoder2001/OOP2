'''U14:

Car deb nomlangan class yarating. Unda name, price, capacity:int, color, model deb nomlangan atributlar bo'lsin. Cardan olingan obyekt print qilinsa avtomobil haqida to'liq ma'lumot ekranga chiqsin.

Carda:
setPrice(),setName(), getPrice(),getName(), setCapacity(),getCapacity(),setColor(),getColor(), setModel(),getModel() deb nomlangan metodlar bo'lsin.

Address nomnli class yarating. Unda country,city, street nomli  atributlar bo'lsin. Addressdan olingan obyekt print qilinsa adressdagi barcha atributlar ekranga chiqsin.

Adressda:
getCountry(),setCountry(),getCity(),setCity(),getStreet().setStreet() nomli metodlar bo'lsin.


CarShowroom nomli class yarating. Unda Adress typida adress, List<Car> typida cars, name, rating:List<int>  kabi atributlar bo'lsin.

ushbu classda addCar, removeCar, getCarsInfo, getAdress, changeAdress, changeName, getName, rate,getAvarageRating degan metodlar bo'lsin.

- addCar(car:Car)=> car qo'shadi.
- removeCar(car:Car)=>carni o'chiradi
- getCarsInfo()=>Barcha carlarni print qiladi
- getAdress(): Adresni print qiladi
- changeName(newName): Avtasalon nomini almashtiradi
- getName(): Avtasalon nomini print qiladi.
- rate(rate:int): rating qo'shadi(0<n<=5)
- getAvarageRating():o'ratacha ratingni chiqaradi.

Carshowroom obekti print qilinsa, ekranga avtasalon nomi, adresi, nechta avto borligi va o'rtacha ratingi ekranga chiqishi kerak.'''


class Car:
    def __init__(self, name:str , price:int , capacity:int, color:str, model:str):
        self.name = name
        self.price = price
        self.capacity = capacity
        self.color = color
        self.model = model
        # print("Methods: ", dir(Car))


    def set_name(self, new_name):
        self.name = new_name
    
    def set_price(self, new_Price):
        self.price = new_Price

    def set_capacity(self, new_capacity):
        self.capacity = new_capacity

    def set_color(self, new_color):
        self.color = new_color

    def set_model(self, new_model):
        self.model = new_model

    def get_name(self):
        return f"Name: {self.name}"
    
    def get_price(self):
        return f"Price: {self.price}"

    def get_capacity(self):
        return f"Capacity: {self.capacity}"
    
    def get_color(self):
        return f"Color: {self.color}"
    
    def get_model(self):
        return f"Color: {self.model}"
    
    def __str__(self) -> str:
        return f"""Car:
        Name: {self.name} 
        Price: {self.price} 
        Capacity: {self.capacity} 
        Color: {self.color} 
        Model: {self.model}"""
    

class Adress:
    def __init__(self, country, city, street):
        self.country = country
        self.city =city
        self.street = street
        dir(Adress)
        # print("Methods: ", dir(Adress))


    def get_street(self):
        return f"Street: {self.street}"
    
    def get_city(self):
        return f"City: {self.city}"
    
    def get_country(self):
        return f"Country: {self.country}"

    def set_street(self, new_street):
        self.street = new_street

    def set_city(self, new_city):
        self.city = new_city

    def set_country(self, new_country):
        self.country = new_country

    def __str__(self) -> str:
        return f"""
        Country: {self.country}
        City: {self.city}
        Street: {self.street}
        """

class CarShowRoom(Car, Adress):
    def __init__(self, address:Adress, name):
        self.address = address
        self.name = name
        self.cars = []
        self.rating = []
    def __str__(self) -> str:
        pass

    def add_car(self, car:Car):
        self.cars.append(car)
        
    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
        else:
            print("Bajarilmadi.")

    def get_car_info(self):
        for car in self.cars:
            print(car)

    def change_addres(self, new_address):
        self.address = new_address

    def change_name(self, new_name):
        self.name = new_name
    
    def get_name(self):
        print(self.name)

    def rate(self, rate):
        if 0 < rate <= 5:
            self.rating.append(rate)
        
    def get_average_rating(self):
        if self.rating:
            return sum(self.rating) / len(self.rating)

        return 0
    
    def get_address(self):
        print(self.address)

    def __str__(self):
        return (f"Car Showroom(name: {self.name}, address: {self.address}, "
                f"number of cars: {len(self.cars)}, average rating: {self.get_average_rating():.2f})")
    

car1 = Car("Toyota", 20000, 5, "Red", "Corolla")
car2 = Car("Honda", 22000, 5, "Blue", "Civic")

address = Adress("USA", "New York", "5th Avenue")
showroom = CarShowRoom("Best Cars", address)

showroom.add_car(car1)
showroom.add_car(car2)
showroom.rate(4)
showroom.rate(5)

print(showroom)
showroom.get_car_info()
showroom.get_address()






