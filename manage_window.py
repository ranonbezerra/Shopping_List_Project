from tkinter import *
from tkinter import filedialog
import json
from window_add_item import window_add_item
from window_remove_item import window_remove_item
from window_view_list import window_view_list
import ctypes
import os
from window_class import *


class ManageWindow(Window):

    def __init__(self):
        super().__init__(400,700)

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
        self.buttons_functions = [lambda: print('Button 1'),
                                  lambda: print('Button 2'),
                                  lambda: print('Button 3'),
                                  lambda: print('Button 4'),
                                  lambda: self.exit_button_click()]

        self.background_image_path = r"\manage_window_images\background.png"
        self.background_image_size = (366.5,200.0)

    def create_manage_window(self, json_data):

        self.create_window('Managing list...')
        self.add_window_background()
        self.add_buttons_to_window()

def execute_manage_window(json_data = {}):

    manage_window = ManageWindow()
    manage_window.create_manage_window(json_data)
    manage_window.window.resizable(False, False)
    manage_window.window.mainloop()

if __name__ == '__main__':

    execute_manage_window()


# def btn_clicked():
#     print("Button Clicked")

# def btn_add_item(window_ger, dicio):

#     window_ger.destroy()
#     window_add_item(dicio)
#     window_gerenciando(dicio)
    
# def btn_remove_item(window_ger, dicio):

#     if len(dicio.keys()):
#         window_ger.destroy()
#         window_remove_item(dicio)
#         window_gerenciando(dicio)
#     else:
#         text  = 'Sua lista está vazia!'
#         title = 'Erro!'
#         ctypes.windll.user32.MessageBoxW(0, text, title, 0)

# def btn_view_list(window_ger,dicio):

#     window_ger.destroy()
#     window_view_list(dicio)
#     window_gerenciando(dicio)

# def btn_save_and_exit(window,dicio):
#     file_str = filedialog.asksaveasfilename(initialdir=os.path.dirname(__file__),
#                                           defaultextension='.json',
#                                           filetypes=[('json files', '*.json')])
    
#     if not file_str:
#         return
#     with open (file_str, 'w') as file:
#         json.dump(dicio, file)
#     window.destroy()

# def btn_exit(window):
#     window.destroy()

# def window_gerenciando(dicio={}):

#     window_ger = Tk()

#     window_ger.title('Gerenciando lista...')

#     caminho = os.path.dirname(__file__)

#     window_ger.geometry("700x400")
#     window_ger.configure(bg = "#ffffff")
#     canvas = Canvas(
#         window_ger,
#         bg = "#ffffff",
#         height = 400,
#         width = 700,
#         bd = 0,
#         highlightthickness = 0,
#         relief = "ridge")
#     canvas.place(x = 0, y = 0)

#     background_img = PhotoImage(file = caminho + r"\window_gerenciando_images\background.png")
#     backgroung = canvas.create_image(
#         366.5, 200.0,
#         image=background_img)

#     img0 = PhotoImage(file = caminho + r"\window_gerenciando_images\img0.png")
#     b0 = Button(
#         image = img0,
#         borderwidth = 0,
#         highlightthickness = 0,
#         command = lambda: btn_add_item(window_ger,dicio),
#         relief = "flat")

#     b0.place(
#         x = 437, y = 47,
#         width = 192,
#         height = 62)

#     img1 = PhotoImage(file = caminho + r"\window_gerenciando_images\img1.png")
#     b1 = Button(
#         image = img1,
#         borderwidth = 0,
#         highlightthickness = 0,
#         command = lambda: btn_remove_item(window_ger,dicio),
#         relief = "flat")

#     b1.place(
#         x = 438, y = 114,
#         width = 192,
#         height = 62)

#     img2 = PhotoImage(file = caminho + r"\window_gerenciando_images\img2.png")
#     b2 = Button(
#         image = img2,
#         borderwidth = 0,
#         highlightthickness = 0,
#         command = lambda: btn_view_list(window_ger,dicio),
#         relief = "flat")

#     b2.place(
#         x = 439, y = 181,
#         width = 192,
#         height = 62)

#     img3 = PhotoImage(file = caminho + r"\window_gerenciando_images\img3.png")
#     b3 = Button(
#         image = img3,
#         borderwidth = 0,
#         highlightthickness = 0,
#         command = lambda: btn_save_and_exit(window_ger,dicio),
#         relief = "flat")

#     b3.place(
#         x = 437, y = 248,
#         width = 192,
#         height = 62)

#     img4 = PhotoImage(file = caminho + r"\window_gerenciando_images\img4.png")
#     b4 = Button(
#         image = img4,
#         borderwidth = 0,
#         highlightthickness = 0,
#         command = lambda: btn_exit(window_ger),
#         relief = "flat")

#     b4.place(
#         x = 437, y = 315,
#         width = 192,
#         height = 62)

#     window_ger.resizable(False, False)
#     window_ger.mainloop()