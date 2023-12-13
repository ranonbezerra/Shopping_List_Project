from tkinter import *
from window_class import Window

class ViewListWindow(Window):

    def __init__(self, json_data = {}):
        super().__init__(400,350)

        self.json_data = json_data

        self.number_of_tables = 1

        self.tables_sizes = [len(json_data)]

        self.tables_main_frame_places = [(75, 61)]
        self.tables_main_frame_sizes = [(200, 316)]

        self.tables_head_paths = [r"\view_list_window_images\img0.png"]
        self.tables_head_places = [(0,0)]
        self.tables_head_sizes = [(184,24)]

        self.tables_canvas_places = [(0,24)]
        self.tables_canvas_sizes = [(184,292)]

        self.tables_scrollbar_places = [(184,0)]
        self.tables_scrollbar_sizes = [(16,314)]
        
        self.tables_internal_frame_sizes = [(184,292)]

        self.tables_border_image_path = r"\view_list_window_images\img_tabela.png"
        self.tables_border_image = PhotoImage(file = self.path + self.tables_border_image_path)

        self.background_image_path = r"\view_list_window_images\background.png"
        self.background_image_size = (175.0,200.0)

    def create_view_list_window(self):
            
        self.create_window('Viewing Shopping list...')
        self.add_window_background()
        self.add_table_to_window()
        self.set_window_final_parameters()

def execute_view_list_window(json_data):

    view_list_window = ViewListWindow(json_data)
    view_list_window.create_view_list_window()