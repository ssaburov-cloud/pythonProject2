from tkinter import *


class CateringView:
    def __init__(self, root):
        self.root = root
        self.root.title("Catering App")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")

        self.food_var = StringVar(self.root)
        self.food_var.set("Pizza")
        self.quantity_var = IntVar(self.root)

        self.name_label = Label(self.root, text="Enter your name:", bg="#f0f0f0")
        self.name_label.pack(pady=10)

        self.name_entry = Entry(self.root)
        self.name_entry.pack(pady=5)

        self.food_label = Label(self.root, text="Select food type:", bg="#f0f0f0")
        self.food_label.pack(pady=10)

        self.food_dropdown = OptionMenu(self.root, self.food_var, "Pizza", "Pasta", "Salad", "Burger")
        self.food_dropdown.pack(pady=5)

        self.quantity_label = Label(self.root, text="Quantity (1-4):", bg="#f0f0f0")
        self.quantity_label.pack(pady=10)

        self.quantity_entry = Entry(self.root, textvariable=self.quantity_var)
        self.quantity_entry.pack(pady=5)

        self.flavor_frame = Frame(self.root)
        self.flavor_frame.pack(pady=10)

        self.result_label = Label(self.root, text="", bg="#f0f0f0", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.submit_button = Button(self.root, text="Submit Order", command=self.submit_order)
        self.submit_button.pack(side=BOTTOM, pady=20)

    def submit_order(self):
        name = self.name_entry.get()
        quantity = self.quantity_var.get()

        if not self.validate_order(name, quantity):
            self.show_error("Invalid input. Please make sure all fields are filled correctly.")
            return

        flavors = [entry.get() for entry in self.flavor_entries]
        if "" in flavors:
            self.show_error("Please fill in all flavor fields.")
            return

        return self.food_var.get(), quantity, flavors

    def create_flavor_inputs(self, quantity):
        for widget in self.flavor_frame.winfo_children():
            widget.destroy()

        self.flavor_entries = []

        for i in range(quantity):
            label = Label(self.flavor_frame, text=f"Flavor for meal {i + 1}:")
            label.pack(pady=5)

            entry = Entry(self.flavor_frame)
            entry.pack(pady=5)
            self.flavor_entries.append(entry)

    def validate_order(self, name, quantity):
        if not name or quantity < 1 or quantity > 4:
            return False
        return True

    def show_error(self, message):
        self.result_label.config(text=message, fg="red")

    def show_success(self, message):
        self.result_label.config(text=message, fg="green")

    def display_total_cost(self, total_cost):
        self.result_label.config(text=f"Total cost: ${total_cost:.2f}", fg="blue")

