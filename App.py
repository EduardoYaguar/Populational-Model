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

        def prey(n):
            prey_model = prey_population[n-1]
            predator_model = predator_population[n-1]
            return prey_model + a * prey_model * (1 - prey_model / K) - b * prey_model * predator_model
        def predator(n):
            prey_model = prey_population[n-1]
            predator_model = predator_population[n-1]
            return predator_model + f * b * prey_model * predator_model - c * predator_model
        
        def model(): 
            for i in range(1,cycles):
                prey_population.append(prey(i))
                predator_population.append(predator(i))
        prey_e = c / (b * f)
        predator_e = (a / b) * (1 - prey_e / K)

        def plot_population_time():

            plt.figure(1)

            plt.axhline(y=predator_e, color='red', linestyle='--')

            plt.axhline(y=prey_e, color='red', linestyle='--')

            plt.plot(np.arange(cycles), prey_population, label='Prey Population', markersize=marker_size)

            plt.plot(np.arange(cycles), predator_population, label='Predator Population', markersize=marker_size)

            plt.ylabel('Population')

            plt.xlabel('Time')

            plt.title('Predator and Prey Populations over Time')

            plt.legend()
            return plt.gcf()
        model()
        figure = plot_population_time()

        canvas = FigureCanvasTkAgg(figure, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Predator And Prey Population model")
        self.geometry('1080x990')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.MyFrame = MyFrame(self)
        self.MyFrame.grid(row=0, column=0, sticky='nsew')



app = App()
app.mainloop()