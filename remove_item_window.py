from tkinter import *
from window_class import Window

class RemoveItemWindow(Window):

    def __init__(self, json_data = {}):
        super().__init__(200,350)

        self.json_data = json_data

        self.number_of_buttons = 1
        self.buttons_paths = [r"\remove_item_window_images\img0.png"]
        self.buttons_places = [(79, 127)]
        self.buttons_sizes = [(192, 62)]        
        self.buttons_functions = [lambda: self.remove_item_from_database_button_click(self.entries[0].get(),self.entries[1].get())]

        self.number_of_entries = 2
        self.entries_paths = [r"\remove_item_window_images\img_textBox0.png",
                              r"\remove_item_window_images\img_textBox1.png"]
        self.entries_background_sizes = [(196.0, 35.0),
                                         (215.0, 85.0)]
        self.entries_places = [(53, 23),
                               (91, 73)]
        self.entries_sizes = [(286, 22),
                              (248, 22)]

        self.background_image_path = r"\remove_item_window_images\background.png"
        self.background_image_size = (175.0,100.0)

    def remove_item_from_database_button_click(self, item_entry, amount_entry):
        action_window_text, action_window_title = self.decide_action_to_take(item_entry, amount_entry)
        self.action_window(action_window_text,action_window_title)

    def decide_action_to_take(self, item_entry, amount_entry):
        if self.amount_correctly_digited(amount_entry):
            if self.item_in_database(item_entry):
                if self.amount_to_remove_too_big(item_entry, amount_entry):
                    action_window_text, action_window_title = self.wrong_amount_texts(item_entry, amount_entry)
                else:
                    action_window_text, action_window_title = self.remove_item_from_database_texts(item_entry, amount_entry) 
            else:
                action_window_text, action_window_title = self.item_not_found_texts()
        else:
            action_window_text, action_window_title = self.amount_not_intenger_texts()

        return action_window_text, action_window_title

    def amount_correctly_digited(self, amount_entry):
        return amount_entry.isdigit()
    
    def item_in_database(self, item_entry):
        return item_entry in self.json_data.keys()
    
    def amount_to_remove_too_big(self, item_entry, amount_entry):
        return int(amount_entry) > self.json_data[item_entry]
    
    def wrong_amount_texts(self, item_entry, amount_entry):
        action_window_text  = 'Item {} with current amount ({}) smaller than the amount to be removed ({})! Removal must be of value smaller or equal to the current amount!'.format(item_entry, self.json_data[item_entry], amount_entry)
        action_window_title = 'Item not removed!'
        return action_window_text, action_window_title
    
    def remove_item_from_database_texts(self,item_entry, amount_entry):
        self.json_data[item_entry] = self.json_data[item_entry] - int(amount_entry)
        if self.json_data[item_entry] == 0:
            del self.json_data[item_entry]
            return ('{} successfully removed! Current amount: {}'.format(item_entry, 0), 'Item removed!')
        return ('{} successfully removed! Current amount: {}'.format(item_entry, self.json_data[item_entry]), 'Item removed!')

    def item_not_found_texts(self):
        return ('Item not found!', 'Error!')

    def create_remove_item_window(self):
            
        self.create_window('Removing item from the list...')
        self.add_window_background()
        self.add_buttons_to_window()
        self.add_entries_to_window()


def execute_remove_item_window(json_data = {}):

    remove_item_window = RemoveItemWindow(json_data)
    remove_item_window.create_remove_item_window()
    remove_item_window.window.resizable(False, False)
    remove_item_window.window.mainloop()


if __name__ == '__main__':

    execute_remove_item_window()