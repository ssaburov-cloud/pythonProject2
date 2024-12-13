class CateringModel:
    food_prices = {
        "Pizza": 10,
        "Pasta": 8,
        "Salad": 5,
        "Burger": 7,
    }

    def __init__(self):
        self.orders = []

    def add_order(self, food_type, quantity, flavors):
        total_cost = self.food_prices[food_type] * quantity
        self.orders.append({"food_type": food_type, "quantity": quantity, "flavors": flavors, "total_cost": total_cost})
        return total_cost

    def validate_order(self, name, quantity):
        if not name or quantity < 1 or quantity > 4:
            return False
        return True

    def calculate_total_cost(self):
        total = sum(order["total_cost"] for order in self.orders)
        return total
