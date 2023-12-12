from tkinter import *
import ctypes
from window_class import Window

class AddItemWindow(Window):

    def __init__(self, json_data = {}):
        super().__init__(200,350)

        self.json_data = json_data

        self.number_of_buttons = 1
        self.buttons_paths = [r"\add_item_window_images\img0.png"]
        self.buttons_places = [(79, 127)]
        self.buttons_sizes = [(192, 62)]        
        self.buttons_functions = [lambda: self.add_item_to_database_button_click(self.entries[0].get(),self.entries[1].get())]

        

        self.number_of_entries = 2
        self.entries_paths = [r"\add_item_window_images\img_textBox0.png",
                              r"\add_item_window_images\img_textBox1.png"]
        self.entries_background_sizes = [(196.0, 35.0),
                                         (215.0, 85.0)]
        self.entries_places = [(53, 23),
                               (91, 73)]
        self.entries_sizes = [(286, 22),
                              (248, 22)]

        self.background_image_path = r"\add_item_window_images\background.png"
        self.background_image_size = (175.0,100.0)

    def add_item_to_database_button_click(self, item_entry, amount_entry):

        if amount_entry.isdigit() and item_entry not in self.json_data.keys():
            self.json_data[item_entry] = int(amount_entry)
            text  = 'Item successfully added! Item: {}, Amount: {}'.format(item_entry, self.json_data[item_entry])
            title = 'Item registered!'
            
        elif item_entry in self.json_data.keys():
            text  = 'Item already registered! Do you wish to increment the value ({}) to the item {}? Current amount: {}'.format(amount_entry,item_entry, self.json_data[item_entry])
            title = 'Item already registered!'
            if 1 == ctypes.windll.user32.MessageBoxW(0, text, title, 1):
                self.json_data[item_entry] += int(amount_entry)
                text  = 'Item {} successfully incremented! Current amount: {}'.format(item_entry, self.json_data[item_entry])
                title = 'Item incremented!'

        else:
            text  = 'The amount must be an intenger!'
            title = 'User typing error'

        ctypes.windll.user32.MessageBoxW(0, text, title, 0)

    def create_add_item_window(self):
            
        self.create_window('Adding item to the list...')
        self.add_window_background()
        self.add_buttons_to_window()
        self.add_entries_to_window()

def execute_add_item_window(json_data = {}):

    add_item_window = AddItemWindow(json_data)
    add_item_window.create_add_item_window()
    add_item_window.window.resizable(False, False)
    add_item_window.window.mainloop()

if __name__ == '__main__':

    execute_add_item_window()