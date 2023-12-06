from tkinter import *
import os
import ctypes

def btn_clicked(dicio, item, quantidade):

    if quantidade.isdigit() and item in dicio.keys():
        if int(quantidade) <= dicio[item]:
            dicio[item] = dicio[item] - int(quantidade)
            if dicio[item] == 0:
                del dicio[item]
            text  = '{} removido com sucesso! Quantidade atualizada: {}'.format(item, dicio[item])
            title = 'Item removido!'
        else:
            text  = 'Item {} com quantidade atual ({}) menor que quantidade a ser removida ({})! Remoção deve ser de valor menor ou igual ao atual!'.format(item, dicio[item], quantidade)
            title = 'Item removido!'
            
    elif item not in dicio.keys():
        text  = 'Item não encontrado!'
        title = 'Erro!'

    else:
        text  = 'A quantidade precisa ser um inteiro!'
        title = 'Erro de digitação do usuário'

    ctypes.windll.user32.MessageBoxW(0, text, title, 0)

def window_remove_item(dicio):
    window = Tk()

    window.title('Adicionando item a lista...')

    caminho = os.path.dirname(__file__)

    window.geometry("350x200")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 200,
        width = 350,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = caminho + r"\window_remove_item_images\background.png")
    background = canvas.create_image(
        175.0, 100.0,
        image=background_img)

    img0 = PhotoImage(file = caminho + r"\window_remove_item_images\img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: btn_clicked(dicio,entry0.get(),entry1.get()),
        relief = "flat")

    b0.place(
        x = 79, y = 127,
        width = 192,
        height = 62)

    entry0_img = PhotoImage(file = caminho + r"\window_remove_item_images\img_textBox0.png")
    entry0_bg = canvas.create_image(
        196.0, 35.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)

    entry0.place(
        x = 53, y = 23,
        width = 286,
        height = 22)

    entry1_img = PhotoImage(file = caminho + r"\window_remove_item_images\img_textBox1.png")
    entry1_bg = canvas.create_image(
        215.0, 85.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)

    entry1.place(
        x = 91, y = 73,
        width = 248,
        height = 22)

    window.resizable(False, False)
    window.mainloop()