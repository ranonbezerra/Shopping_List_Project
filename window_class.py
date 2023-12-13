from tkinter import *
import traceback
import ctypes
import os
from table_creator import TableObject


class Window(TableObject):

    def __init__(self, height, width):

        super().__init__()

        self.height = height
        self.width = width

        self.LAST_ADDED = -1

        self.window = Tk()
        self.path = os.path.dirname(__file__)
        self.canvas = None

        self.background_image_path = None
        self.background_image_size = None
        
        self.number_of_buttons = None
        self.buttons_paths = None
        self.buttons_places = None
        self.buttons_sizes = None
        self.butons_functions = None
        self.buttons = []
        self.buttons_images = []
        
        self.number_of_entries = None
        self.entries_paths = None
        self.entries_background_sizes = None
        self.entries_places = None
        self.entries_sizes = None
        self.entries = []
        self.entries_images = []
        self.entries_background = []

        self.number_of_tables = None
        self.tables_sizes = None

    def create_window(self, title):

        self.window.title(title)
        self.window.geometry("{}x{}".format(self.width,self.height))
        self.window.configure(bg = "#ffffff")
        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = self.height,
            width = self.width,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.canvas.background = PhotoImage(file = self.path + self.background_image_path)
        background_x, background_y = self.background_image_size
        background = self.canvas.create_image(
            background_x, background_y,
            image=self.canvas.background)

    def add_window_background(self):

        try:
            self.canvas.background = PhotoImage(file = self.path + self.background_image_path)
            background_x, background_y = self.background_image_size

            self.background = self.canvas.create_image(
                background_x, background_y,
                image=self.canvas.background)
            
        except Exception:
            print(traceback.print_exc())
            print('Attributes regarding background image size and path might not be defined.')

    def add_buttons_to_window(self):
            
        try:

            for button_number in range(self.number_of_buttons):
        
                button_x, button_y = self.buttons_places[button_number]
                button_width, button_height = self.buttons_sizes[button_number]

                self.buttons_images.append(PhotoImage(file = self.path + self.buttons_paths[button_number]))
                self.buttons.append(Button(image = self.buttons_images[self.LAST_ADDED],borderwidth = 0,highlightthickness = 0,
                                            command = self.buttons_functions[button_number],relief = "flat"))

                self.buttons[self.LAST_ADDED].place(x = button_x, y = button_y,width = button_width,height = button_height)

        except Exception:
            print(traceback.print_exc())
            print('Attributes regarding number of buttons, size, place and images path might not be defined.')

    def add_entries_to_window(self):

        try:

            for entry_number in range(self.number_of_entries):

                self.entries_images.append(PhotoImage(file = self.path + self.entries_paths[entry_number]))
                entry_background_x, entry_background_y = self.entries_background_sizes[entry_number]
                self.entries_background.append(self.canvas.create_image(entry_background_x, entry_background_y,image = self.entries_images[self.LAST_ADDED]))

                self.entries.append(Entry(bd = 0,bg = "#d9d9d9",highlightthickness = 0))

                entry_x, entry_y = self.entries_places[entry_number]
                entry_width, entry_height = self.entries_sizes[entry_number]
                self.entries[self.LAST_ADDED].place(x = entry_x, y = entry_y,
                                        width = entry_width, height = entry_height)

        except Exception:
            print(traceback.print_exc())
            print('Attributes regarding the entries might not be defined.')

    def add_table_to_window(self):

        try:

            for table_number in range(self.number_of_tables):
                self.create_table_main_frame(table_number)
                self.create_table_head(table_number)
                self.create_table_canvas(table_number)
                self.create_table_scrollbar(table_number)
                self.add_scrollbar_to_table(table_number)
                self.create_table_internal_frame(table_number)
                self.build_table(table_number)
                self.update_table_internal_frame(table_number)
                self.define_table_canvas_scrollregion(table_number)

        except Exception:
            print(traceback.print_exc())
            print('Attributes regarding the tables might not be defined.')

    def close_window(self):
        self.window.destroy()

    def action_window(self, text, title, return_value=0):
        return ctypes.windll.user32.MessageBoxW(0, text, title, return_value)

    def amount_not_intenger_texts(self):
        return ('The amount must be an intenger!', 'Error!')
    
    def set_window_final_parameters(self):
        self.window.resizable(False, False)
        self.window.mainloop()


if __name__ == '__main__':
     
    print('Executed as main')
    print('-------------------------------------------------------------')