class FoodItem:
    food_id = 0
    
    def _init_(self, name, quantity, price, discount, stock):
        FoodItem.food_id += 1
        self.food_id = FoodItem.food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class FoodOrderingApp:
    def _init_(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        print(f"Food Item Added - ID: {food_item.food_id}")

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print(f"Food Item Updated - ID: {food_id}")
                break
        else:
            print(f"Food Item with ID {food_id} not found")

    def view_food_items(self):
        if len(self.food_items) == 0:
            print("No Food Items Available")
            return
        
        print("List of Food Items:")
        print(f"{'ID':<5}{'Name':<20}{'Quantity':<15}{'Price':<10}{'Discount':<10}{'Stock':<10}")
        for food_item in self.food_items:
            print(f"{food_item.food_id:<5}{food_item.name:<20}{food_item.quantity:<15}{food_item.price:<10}{food_item.discount:<10}{food_item.stock:<10}")

    def remove_food_item(self, food_id):
        for index, food_item in enumerate(self.food_items):
            if food_item.food_id == food_id:
                del self.food_items[index]
                print(f"Food Item Deleted - ID: {food_id}")
                break
        else:
            print(f"Food Item with ID {food_id} not found")

app = FoodOrderingApp()
app.add_food_item("Pizza", "Medium", 10.0, 0.2, 100)
app.add_food_item("Burger", "Single", 5.0, 0.1, 50)
app.view_food_items()
app.edit_food_item(1, "Pizza", "Large", 12.0, 0.2, 50)
app.view_food_items()
app.remove_food_item(2)
app.view_food_items()

import random

class FoodItem:
    def _init_(self, name, quantity, price, discount, stock):
        self.food_id = random.randint(1000, 9999)
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class FoodOrderingApplication:
    def _init_(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        print("Food item added successfully!")
        print("Food ID: ", food_item.food_id)

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("Food item edited successfully!")
                return
        print("Food item not found with Food ID: ", food_id)

    def view_food_items(self):
        print("List of all food items:")
        for food_item in self.food_items:
            print(f"Food ID: {food_item.food_id}, Name: {food_item.name}, Quantity: {food_item.quantity}, Price: {food_item.price}, Discount: {food_item.discount}, Stock: {food_item.stock}")

    def remove_food_item(self, food_id):
        for index, food_item in enumerate(self.food_items):
            if food_item.food_id == food_id:
                del self.food_items[index]
                print("Food item removed successfully!")
                return
        print("Food item not found with Food ID: ", food_id)

class User:
    def _init_(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

    def place_new_order(self, food_items):
        print("List of selected food items:")
        for food_item in food_items:
            print(f"Name: {food_item.name}, Quantity: {food_item.quantity}, Price: {food_item.price}")
        confirmation = input("Do you want to place this order? (y/n): ")
        if confirmation.lower() == "y":
            order_id = random.randint(100000, 999999)
            total_price = sum([food_item.price for food_item in food_items])
            order = {
                "order_id": order_id,
                "food_items": food_items,
                "total_price": total_price
            }
            self.orders.append(order)
            print("Order placed successfully!")
            print("Order ID: ", order_id)

    def view_order_history(self):
        print("List of all previous orders:")
        for order in self.orders:
            print(f"Order ID: {order['order_id']}, Total Price: {order['total_price']}")
            print("List of food items:")
            for food_item in order['food_items']:
                print(f"Name: {food_item.name}, Quantity: {food_item.quantity}, Price: {food_item.price}")

    def update_profile(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password