from tkinter import *
import traceback
import logging
import os


class Window:

    def __init__(self, height, width):

        self.height = height
        self.width = width

        self.window = Tk()
        self.path = os.path.dirname(__file__)

        self.background_image_path = None
        self.background_image_size = None
        
        self.number_of_buttons = None
        self.buttons_paths = None
        self.buttons_places = None
        self.buttons_sizes = None
        self.butons_functions = None
        self.buttons = []
        self.buttons_images = []
        

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
                self.buttons.append(Button(image = self.buttons_images[-1],borderwidth = 0,highlightthickness = 0,
                                            command = self.buttons_functions[button_number],relief = "flat"))

                self.buttons[-1].place(x = button_x, y = button_y,width = button_width,height = button_height)

        except Exception:
            print(traceback.print_exc())
            print('Attributes regarding number of buttons, size, place and images path might not be defined.')

    def exit_button_click(self):

        self.window.destroy()

if __name__ == '__main__':
     
    print('Executed as main')
    print('-------------------------------------------------------------')
    test = Window(400,700)
    test.add_window_background()

#COPY OF OLD VERSION FOR REFERENCE

    # def main_window_old():

    #     window = Tk()
    #     window.title('App Lista de Compras do Non')
    #     caminho = os.path.dirname(__file__)

    #     window.geometry("700x400")
    #     window.configure(bg = "#ffffff")
    #     canvas = Canvas(
    #         window,
    #         bg = "#ffffff",
    #         height = 400,
    #         width = 700,
    #         bd = 0,
    #         highlightthickness = 0,
    #         relief = "ridge")
    #     canvas.place(x = 0, y = 0)

    #     background_img = PhotoImage(file = caminho + r"\main_window_images\background.png")
    #     background = canvas.create_image(
    #         335.0, 200.0,
    #         image=background_img)

    #     img0 = PhotoImage(file = caminho + r"\main_window_images\img0.png")
    #     b0 = Button(
    #         image = img0,
    #         borderwidth = 0,
    #         highlightthickness = 0,
    #         command = lambda: btn_nova_lista(window),
    #         relief = "flat")

    #     b0.place(
    #         x = 439, y = 114,
    #         width = 192,
    #         height = 62)

    #     img1 = PhotoImage(file = caminho + r"\main_window_images\img1.png")
    #     b1 = Button(
    #         image = img1,
    #         borderwidth = 0,
    #         highlightthickness = 0,
    #         command = lambda: btn_open_file(window),
    #         relief = "flat")

    #     b1.place(
    #         x = 439, y = 200,
    #         width = 192,
    #         height = 62)

    #     img2 = PhotoImage(file = caminho + r"\main_window_images\img2.png")
    #     b2 = Button(
    #         image = img2,
    #         borderwidth = 0,
    #         highlightthickness = 0,
    #         command = lambda: btn_sair(window),
    #         relief = "flat")

    #     b2.place(
    #         x = 439, y = 286,
    #         width = 192,
    #         height = 62)

    #     canvas.create_text(
    #         561.0, 5.0,
    #         text = "",
    #         fill = "#ffffff",
    #         font = ("InriaSerif-Bold", int(13.0)))

    #     window.resizable(False, False)
    #     window.mainloop()