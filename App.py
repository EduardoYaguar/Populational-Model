import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        cycles = 3000


        #Datos Presas
        prey_initial = 50 #población inicial presas
        a = 0.04 # tasa de crecimiento intrínseca
        K = 1200 # capacidad de carga
        b = 0.003 # tasa de ataque per capita de los depredadores sobre las presas 

        #Datos Depredadores
        predator_initial = 20 # poblacion inicial predadores
        c = 0.01 #tasa de mortalidad de forma natural
        f = 0.02 #tasa de conversión de presas consumidas a nuevos depredadores

        prey_population = [prey_initial]
        predator_population = [predator_initial]
        marker_size = 2


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Predator And Prey Population model")
        self.geometry('1080x990')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)



app = App()
app.mainloop()