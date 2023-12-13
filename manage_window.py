from tkinter import *
from tkinter import filedialog
import json
from add_item_window import execute_add_item_window
from remove_item_window import execute_remove_item_window
from view_list_window import execute_view_list_window
from window_class import Window
import traceback

class ManageListWindow(Window):

    def __init__(self, json_data = {}):
        super().__init__(400,700)

        self.json_data = json_data
        self.number_of_buttons = 5
        self.buttons_paths = [r"\manage_window_images\img0.png",
                              r"\manage_window_images\img1.png",
                              r"\manage_window_images\img2.png",
                              r"\manage_window_images\img3.png",
                              r"\manage_window_images\img4.png"]
        self.buttons_places = [(437, 47),
                               (437, 114),
                               (437, 181),
                               (437, 248),
                               (437, 315)]
        self.buttons_sizes = [(192, 62),
                              (192, 62),
                              (192, 62),
                              (192, 62),
                              (192, 62)]
        self.buttons_functions = [lambda: self.add_item_button_click(),
                                  lambda: self.remove_item_button_click(), #self.remove_item_button_click(json_data),
                                  lambda: self.view_list_button_click(), #self.view_list_button_click(json_data),
                                  lambda: self.save_and_exit_button_click(),
                                  lambda: self.close_window()]

        self.background_image_path = r"\manage_window_images\background.png"
        self.background_image_size = (366.5,200.0)

    def create_manage_list_window(self):
            
        self.create_window('Managing list...')
        self.add_window_background()
        self.add_buttons_to_window()
        self.set_window_final_parameters()

    def add_item_button_click(self):

        self.close_window()
        execute_add_item_window(self.json_data)
        print(self.json_data)
        execute_manage_list_window(self.json_data)

    def remove_item_button_click(self):

        if self.list_have_itens():
            self.close_window()
            execute_remove_item_window(self.json_data)
            print(self.json_data)
            execute_manage_list_window(self.json_data)
        else:
            text  = 'Your shopping list is empty!'
            title = 'Error!'
            self.action_window(text, title)

    def list_have_itens(self):
        return len(self.json_data.keys())
            
    def view_list_button_click(self):

        self.close_window()
        execute_view_list_window(self.json_data)
        execute_manage_list_window(self.json_data)

    def save_and_exit_button_click(self):

        self.execute_save()

    def execute_save(self):

        try:
            json_file_name = self.get_json_file_name()
            self.save_json_file(json_file_name)

        except Exception:
            print(traceback.print_exc())
            print('Something went wrong when trying to save the json file.')

        self.close_window()

    def get_json_file_name(self):
        return filedialog.asksaveasfilename(initialdir=self.path,
                                            defaultextension='.json',
                                            filetypes=[('json files', '*.json')])
    
    def save_json_file(self, json_file_name):
        if not json_file_name:
            return
        with open (json_file_name, 'w') as file:
            json.dump(self.json_data, file)


def execute_manage_list_window(json_data = {}):

    manage_window = ManageListWindow(json_data)
    manage_window.create_manage_list_window()


if __name__ == '__main__':

    execute_manage_list_window()