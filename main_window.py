from tkinter import *
from tkinter import filedialog
from window_gerenciando import window_gerenciando
import json
import os

def btn_nova_lista(window):
    dicio = {}
    window.destroy()
    window_gerenciando(dicio)
    main_window()

def btn_open_file(window):
    file_str = filedialog.askopenfilename(initialdir=os.path.dirname(__file__),
                                  title='Abrir arquivo JSON',
                                  filetypes=[('json files','*.json')])
    if not file_str:
        return
    with open(file_str) as file:

        window.destroy()
        window_gerenciando(json.load(file))
    main_window()

def btn_sair(window):
    window.destroy()

def main_window():

    window = Tk()
    window.title('App Lista de Compras do Non')
    caminho = os.path.dirname(__file__)

    window.geometry("700x400")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 400,
        width = 700,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = caminho + r"\main_window_images\background.png")
    background = canvas.create_image(
        335.0, 200.0,
        image=background_img)

    img0 = PhotoImage(file = caminho + r"\main_window_images\img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: btn_nova_lista(window),
        relief = "flat")

    b0.place(
        x = 439, y = 114,
        width = 192,
        height = 62)

    img1 = PhotoImage(file = caminho + r"\main_window_images\img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: btn_open_file(window),
        relief = "flat")

    b1.place(
        x = 439, y = 200,
        width = 192,
        height = 62)

    img2 = PhotoImage(file = caminho + r"\main_window_images\img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: btn_sair(window),
        relief = "flat")

    b2.place(
        x = 439, y = 286,
        width = 192,
        height = 62)

    canvas.create_text(
        561.0, 5.0,
        text = "",
        fill = "#ffffff",
        font = ("InriaSerif-Bold", int(13.0)))

    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    main_window()