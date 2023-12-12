from tkinter import *
import os
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









# def execute_view_list_window(dicio):
#     window = Tk()

#     window.title('Visualizando Lista de Compras')

#     caminho = os.path.dirname(__file__)

#     window.geometry("350x400")
#     window.configure(bg = "#ffffff")
#     canvas = Canvas(
#         window,
#         bg = "#ffffff",
#         height = 400,
#         width = 350,
#         bd = 0,
#         highlightthickness = 0,
#         relief = "ridge")
#     canvas.place(x = 0, y = 0)

#     background_img = PhotoImage(file = caminho + r"\window_view_list_images\background.png")
#     background = canvas.create_image(
#         175.0, 200.0,
#         image=background_img)

#     lista_main_frame = Frame(window, borderwidth=0)
#     lista_main_frame.place(
#         x = 75, y = 61,
#         width = 200,
#         height = 316)

#     lista_main_frame.grid_rowconfigure(0, weight=5)
#     lista_main_frame.grid_columnconfigure(0, weight=5)
#     #lista_main_frame.grid_propagate(False)

#     img0 = PhotoImage(file = caminho + r"\window_view_list_images\img0.png")

#     topo_tabela = Label(lista_main_frame,
#         image = img0,
#         borderwidth = 0,
#         highlightthickness = 0,
#         relief = "flat")

#     topo_tabela.place(
#         x = 0, y = 0,
#         width = 184,
#         height = 24)

#     lista_canvas = Canvas(lista_main_frame, borderwidth=0, highlightthickness=0)
#     lista_canvas.place(
#         x = 0, y = 24,
#         width = 184,
#         height = 292)

#     lista_scroll_bar = Scrollbar(lista_main_frame, 
#         orient=VERTICAL,
#         command = lista_canvas.yview)
#     lista_scroll_bar.place(
#         x = 184, y = 0,
#         width = 16,
#         height = 314)
    
#     lista_canvas.config(yscrollcommand = lista_scroll_bar.set)

#     lista_internal_frame = Frame(lista_canvas)
#     lista_canvas.create_window((0, 0) ,window=lista_internal_frame, anchor='nw')
#     lista_internal_frame.config(width=184, height = 292)

#     tamanho = len(dicio)

#     img_tabela = PhotoImage(file = caminho + r"\window_view_list_images\img_tabela.png")

#     for i,chave in enumerate(dicio.keys()):

#         if len(chave) > 16:
#             fonte = 7
#             quebra_linha = 80
#         else:
#             fonte = 8
#             quebra_linha = 0

#         e = Label(lista_internal_frame, image = img_tabela,
#             borderwidth = 0, highlightthickness = 0, bd=0,
#             anchor='center', text=chave, font=('Inria Serif', fonte), compound='center',
#             relief = "flat", padx=0, pady=0, fg='#FFFFFF',wraplength=quebra_linha)
#         e.grid(row=i, column=0, sticky=NSEW)
#         e = Label(lista_internal_frame, image = img_tabela,
#                 borderwidth = 0, highlightthickness = 0, bd=0,
#                 anchor='center', text=dicio[chave], font=('Inria Serif', fonte), compound='center',
#                 relief = "flat", padx=0, pady=0, fg='#FFFFFF',wraplength=quebra_linha)
#         e.grid(row=i, column=1, sticky=NSEW)

#         if tamanho < 13:
#             for i in range(tamanho, 13):
#                 e = Label(lista_internal_frame, image = img_tabela,
#                     borderwidth = 0, highlightthickness = 0, bd=0,
#                     anchor='center', relief = "flat", padx=0, pady=0)
#                 e.grid(row=i, column=0, sticky=NSEW)
#                 e = Label(lista_internal_frame, image = img_tabela,
#                     borderwidth = 0, highlightthickness = 0, bd=0,
#                     anchor='center', relief = "flat", padx=0, pady=0)
#                 e.grid(row=i, column=1, sticky=NSEW)

#     lista_internal_frame.update_idletasks()
#     lista_canvas.config(scrollregion=lista_canvas.bbox("all"))

#     window.resizable(False, False)
#     window.mainloop()