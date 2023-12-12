from tkinter import *

import traceback
import ctypes
import os


class Window:

    def __init__(self, height, width):

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

        self.tables_main_frame = []
        self.tables_main_frame_places = None
        self.tables_main_frame_sizes = None

        self.tables_head = []
        self.tables_head_images = []
        self.tables_head_paths = None
        self.tables_head_places = None
        self.tables_head_sizes = None

        self.tables_canvas = []
        self.tables_canvas_places = None
        self.tables_canvas_sizes = None

        self.tables_scrollbar = []
        self.tables_scrollbar_places = None
        self.tables_scrollbar_sizes = None

        self.tables_internal_frame = []
        self.tables_internal_frame_sizes = None

        self.tables_border_images = None
        self.tables_border_image_path = None

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

    def create_table_main_frame(self, table_number):

        self.tables_main_frame.append(Frame(self.window, borderwidth=0))

        table_main_frame_x, table_main_frame_y = self.tables_main_frame_places[table_number]
        table_main_frame_width, table_main_frame_height = self.tables_main_frame_sizes[table_number]

        self.tables_main_frame[self.LAST_ADDED].place(x = table_main_frame_x, y = table_main_frame_y,
                                                      width = table_main_frame_width,height = table_main_frame_height)

        self.tables_main_frame[self.LAST_ADDED].grid_rowconfigure(0, weight=5)
        self.tables_main_frame[self.LAST_ADDED].grid_columnconfigure(0, weight=5)

    def create_table_head(self, table_number):

        self.tables_head_images.append(PhotoImage(file = self.path + self.tables_head_paths[table_number]))
        self.tables_head.append(Label(self.tables_main_frame[table_number],
                                      image = self.tables_head_images[self.LAST_ADDED],
                                      borderwidth = 0,highlightthickness = 0,relief = "flat"))
                
        table_head_x, table_head_y = self.tables_head_places[table_number]
        table_head_width, table_head_height = self.tables_head_sizes[table_number]

        self.tables_head[self.LAST_ADDED].place(x = table_head_x, y = table_head_y,
                               width = table_head_width, height = table_head_height)
        
    def create_table_canvas(self, table_number):

        self.tables_canvas.append(Canvas(self.tables_main_frame[table_number],
                                          borderwidth=0, highlightthickness=0))
        
        tables_canvas_x, tables_canvas_y = self.tables_canvas_places[table_number]
        tables_canvas_width, tables_canvas_height = self.tables_canvas_sizes[table_number]
        
        self.tables_canvas[self.LAST_ADDED].place(x = tables_canvas_x, y = tables_canvas_y,
                                                  width = tables_canvas_width,height = tables_canvas_height)
        
    def create_table_scrollbar(self, table_number):

        self.tables_scrollbar.append(Scrollbar(self.tables_main_frame[table_number], 
                                              orient=VERTICAL,command = self.tables_canvas[table_number].yview))

        tables_scrollbar_x, tables_scrollbar_y = self.tables_scrollbar_places[table_number]
        tables_scrollbar_width, tables_scrollbar_height = self.tables_scrollbar_sizes[table_number]

        self.tables_scrollbar[self.LAST_ADDED].place(x = tables_scrollbar_x, y = tables_scrollbar_y,
                                                     width = tables_scrollbar_width,height = tables_scrollbar_height)

    def add_scrollbar_to_table(self, table_number):
        self.tables_canvas[table_number].config(yscrollcommand = self.tables_scrollbar[table_number].set)

    def create_table_internal_frame(self,table_number):

        self.tables_internal_frame.append(Frame(self.tables_canvas[table_number]))
        self.tables_canvas[table_number].create_window((0, 0) ,window=self.tables_internal_frame[self.LAST_ADDED], anchor='nw')

        tables_internal_frame_width, tables_internal_frame_height = self.tables_internal_frame_sizes[table_number]

        self.tables_internal_frame[self.LAST_ADDED].config(width=tables_internal_frame_width, height = tables_internal_frame_height)

    def build_table(self, table_number):

        for item_index,item in enumerate(self.json_data.keys()):

            self.place_table_values(table_number, item_index, item)
            self.fill_table_empty_cells(table_number)

    def update_table_internal_frame(self, table_number):

        self.tables_internal_frame[table_number].update_idletasks()
    
    def place_table_values(self, table_number, item_index, item):

        cell_font, cell_wraplength = self.define_text_format(item)

        item_cell = Label(self.tables_internal_frame[table_number], image = self.tables_border_image,
                          borderwidth = 0, highlightthickness = 0, bd=0, anchor='center',
                          text=item, font=('Inria Serif', cell_font), compound='center',
                          relief = "flat", padx=0, pady=0, fg='#FFFFFF', wraplength=cell_wraplength)
        item_cell.grid(row=item_index, column=0, sticky=NSEW)

        amount_cell = Label(self.tables_internal_frame[table_number], image = self.tables_border_image,
                            borderwidth = 0, highlightthickness = 0, bd=0, anchor='center',
                            text=self.json_data[item], font=('Inria Serif', cell_font), compound='center',
                            relief = "flat", padx=0, pady=0, fg='#FFFFFF', wraplength=cell_wraplength)
        amount_cell.grid(row=item_index, column=1, sticky=NSEW)

    def define_text_format(self, item):

        if len(item) > 16:
            cell_font = 7
            cell_wraplength = 80
        else:
            cell_font = 8
            cell_wraplength = 0

        return cell_font, cell_wraplength
    
    def fill_table_empty_cells(self, table_number):
        if self.tables_sizes[table_number] < 13:
            for empty_index in range(self.tables_sizes[table_number], 13):
                empty_text_cell = Label(self.tables_internal_frame[table_number], image = self.tables_border_image,
                                        borderwidth = 0, highlightthickness = 0, bd=0, anchor='center',
                                        relief = "flat", padx=0, pady=0)
                empty_text_cell.grid(row=empty_index, column=0, sticky=NSEW)
                empty_amount_cell = Label(self.tables_internal_frame[table_number], image = self.tables_border_image,
                                          borderwidth = 0, highlightthickness = 0, bd=0, anchor='center',
                                          relief = "flat", padx=0, pady=0)
                empty_amount_cell.grid(row=empty_index, column=1, sticky=NSEW)

    def define_table_canvas_scrollregion(self, table_number):

        self.tables_canvas[table_number].config(scrollregion=self.tables_canvas[table_number].bbox("all"))

    def exit_button_click(self):
        self.window.destroy()

    def action_window(self, text, title):
        return ctypes.windll.user32.MessageBoxW(0, text, title, 0)

    def amount_not_intenger_texts(self):
        return ('The amount must be an intenger!', 'Error!')
    
    def set_window_final_parameters(self):
        self.window.resizable(False, False)
        self.window.mainloop()


if __name__ == '__main__':
     
    print('Executed as main')
    print('-------------------------------------------------------------')