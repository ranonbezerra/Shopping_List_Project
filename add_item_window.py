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

        action_window_text, action_window_title = self.decide_action_to_take(item_entry, amount_entry)
        self.action_window(action_window_text,action_window_title)

    def decide_action_to_take(self, item_entry, amount_entry):
        if self.amount_correctly_digited(amount_entry):
            if self.new_item_to_database(item_entry):
                self.add_item_to_database(item_entry, amount_entry)
                action_window_text, action_window_title = self.add_item_to_database_texts(item_entry, amount_entry)
            elif self.user_wants_to_increment(item_entry, amount_entry):
                self.increment_item_in_database(item_entry, amount_entry)
                action_window_text, action_window_title = self.increment_item_in_database_texts(item_entry, amount_entry)
            else:
                action_window_text, action_window_title = self.no_changes_texts()
        else:
            action_window_text, action_window_title = self.amount_not_intenger_texts()

        return action_window_text, action_window_title

    def amount_correctly_digited(self, amount_entry):
        return amount_entry.isdigit()
    
    def new_item_to_database(self, item_entry):
        return item_entry not in self.json_data.keys()
    
    def add_item_to_database(self, item_entry, amount_entry):
        self.json_data[item_entry] = int(amount_entry)
    
    def add_item_to_database_texts(self,item_entry, amount_entry):
        return ('Item successfully added! Item: {}, Amount: {}'.format(item_entry, self.json_data[item_entry]),'Item registered!')
    
    def increment_item_in_database(self, item_entry, amount_entry):
        self.json_data[item_entry] += int(amount_entry)
    
    def increment_item_in_database_texts(self, item_entry, amount_entry):
            return ('Item {} successfully incremented! Current amount: {}'.format(item_entry, self.json_data[item_entry]),'Item incremented!')
    
    def no_changes_texts(self):
        return ('No changes made to the list', 'No changes!')

    def user_wants_to_increment(self,item_entry, amount_entry):
        text  = 'Item already registered! Do you wish to increment the value ({}) to the item {}? Current amount: {}'.format(amount_entry,item_entry, self.json_data[item_entry])
        title = 'Item already registered!'
        return 1 == ctypes.windll.user32.MessageBoxW(0, text, title, 1)
    
    def create_add_item_window(self):
            
        self.create_window('Adding item to the list...')
        self.add_window_background()
        self.add_buttons_to_window()
        self.add_entries_to_window()
        self.set_window_final_parameters()


def execute_add_item_window(json_data = {}):

    add_item_window = AddItemWindow(json_data)
    add_item_window.create_add_item_window()

if __name__ == '__main__':

    execute_add_item_window()