from window_class import Window
from manage_window import execute_manage_list_window
from tkinter import filedialog
from tkinter import *
import json

class MainWindow(Window):

    def __init__(self):

        super().__init__(400,700)

        self.number_of_buttons = 3
        self.buttons_paths = [r"\main_window_images\img0.png",
                              r"\main_window_images\img1.png",
                              r"\main_window_images\img2.png"]
        self.buttons_places = [(439, 114),
                               (439, 200),
                               (439, 286)]
        self.buttons_sizes = [(192, 62),
                              (192, 62),
                              (192, 62)]
        self.buttons_functions = [lambda: self.new_list_button_click(),
                                  lambda: self.open_file_button_click(),
                                  lambda: self.close_window()]

        self.background_image_path = r"\main_window_images\background.png"
        self.background_image_size = (335.0,200.0)

    def create_main_window(self):

        self.create_window('Shopping List App - by Ranon Bezerra')
        self.add_window_background()
        self.add_buttons_to_window()
        self.set_window_final_parameters()

    def new_list_button_click(self):

        self.close_window()
        execute_manage_list_window()
        execute_main_window()

    def open_file_button_click(self):
        file_str = filedialog.askopenfilename(initialdir=self.path,
                                              title='Open JSON file',
                                              filetypes=[('json files','*.json')])
        if file_str:
            with open(file_str) as file:
                self.close_window()
                execute_manage_list_window(json.load(file))


def execute_main_window():

    main_window = MainWindow()
    main_window.create_main_window()
    

if __name__ == '__main__':

    execute_main_window()