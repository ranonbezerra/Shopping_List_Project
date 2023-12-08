from window_class import Window
from tkinter import *

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
        self.background_image_path = r"\main_window_images\background.png"
        self.background_image_size = (335.0,200.0)
        
    def create_main_window(self):

        self.create_window('Shopping List App - by Ranon Bezerra')
        self.add_window_background()
        self.add_main_window_buttons()

    def add_main_window_buttons(self):

        for button_number in range(self.number_of_buttons):
            self.add_buttons_to_window(lambda: print('Botao {}'.format(button_number)),button_number)

# def btn_nova_lista(window):
#     dicio = {}
#     window.destroy()
#     window_gerenciando(dicio)
#     main_window()

# def btn_open_file(window):
#     file_str = filedialog.askopenfilename(initialdir=os.path.dirname(__file__),
#                                   title='Abrir arquivo JSON',
#                                   filetypes=[('json files','*.json')])
#     if not file_str:
#         return
#     with open(file_str) as file:

#         window.destroy()
#         window_gerenciando(json.load(file))
#     main_window()

# def btn_sair(window):
#     window.destroy()

# def main_window():

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

#     window.resizable(False, False)
#     window.mainloop()

if __name__ == '__main__':

    main_window = MainWindow()
    main_window.create_main_window()
    main_window.window.resizable(False, False)
    main_window.window.mainloop()