from tkinter import *
from gui import CateringView
from model import CateringModel


class CateringController:
    def __init__(self, root):
        self.model = CateringModel()
        self.view = CateringView(root)
        self.setup_event_handlers()

    def setup_event_handlers(self):
        self.view.quantity_entry.bind("<Return>", self.handle_quantity_change)
        self.view.submit_button.config(command=self.handle_submit_order)

    def handle_quantity_change(self, event):
        quantity = self.view.quantity_var.get()
        if 1 <= quantity <= 4:
            self.view.create_flavor_inputs(quantity)
        else:
            self.view.show_error("Invalid quantity. Please enter a number between 1 and 4.")

    def handle_submit_order(self):
        food_type, quantity, flavors = self.view.submit_order()

        if food_type is None:
            return

        total_cost = self.model.add_order(food_type, quantity, flavors)

        self.view.display_total_cost(total_cost)


if __name__ == "__main__":
    root = Tk()
    controller = CateringController(root)
    root.mainloop()


