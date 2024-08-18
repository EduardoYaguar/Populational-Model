import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)

        self.cycles = 3000
        #Se crean los sliders y sus labels

        self.prey_initial_slider = customtkinter.CTkSlider(self, from_=10, to=100, number_of_steps=90, command=self.update_plot)
        self.prey_initial_slider.set(50)
        self.prey_initial_slider.grid(row=1, column=0, sticky='ew', padx=10, pady=10)
        self.prey_initial_label = customtkinter.CTkLabel(self, text="Initial prey population")
        self.prey_initial_label.grid(row=1, column=1, padx=10, pady=10)
        self.prey_initial_value = customtkinter.CTkLabel(self, text=f"{self.prey_initial_slider.get():.0f}")
        self.prey_initial_value.grid(row=1, column=2, padx=10, pady=10)

        self.predator_initial_slider = customtkinter.CTkSlider(self, from_=5, to=50, number_of_steps=45, command=self.update_plot)
        self.predator_initial_slider.set(20)
        self.predator_initial_slider.grid(row=2, column=0, sticky='ew', padx=10, pady=10)
        self.predator_initial_label = customtkinter.CTkLabel(self, text="Initial predator population")
        self.predator_initial_label.grid(row=2, column=1, padx=10, pady=10)
        self.predator_initial_value = customtkinter.CTkLabel(self, text=f"{self.predator_initial_slider.get():.0f}")
        self.predator_initial_value.grid(row=2, column=2, padx=10, pady=10)

        self.K_slider = customtkinter.CTkSlider(self, from_=500, to=2000, number_of_steps=1500, command=self.update_plot)
        self.K_slider.set(1200)
        self.K_slider.grid(row=3, column=0, sticky='ew', padx=10, pady=10)
        self.K_label = customtkinter.CTkLabel(self, text="Carrying capacity (K)")
        self.K_label.grid(row=3, column=1, padx=10, pady=10)
        self.K_value = customtkinter.CTkLabel(self, text=f"{self.K_slider.get():.0f}")
        self.K_value.grid(row=3, column=2, padx=10, pady=10)

        self.a_slider = customtkinter.CTkSlider(self, from_=0.01, to=0.1, number_of_steps=100, command=self.update_plot)
        self.a_slider.set(0.04)
        self.a_slider.grid(row=4, column=0, sticky='ew', padx=10, pady=10)
        self.a_label = customtkinter.CTkLabel(self, text="Prey intrinsic growth rate (a)")
        self.a_label.grid(row=4, column=1, padx=10, pady=10)
        self.a_value = customtkinter.CTkLabel(self, text=f"{self.a_slider.get():.3f}")
        self.a_value.grid(row=4, column=2, padx=10, pady=10)

        self.b_slider = customtkinter.CTkSlider(self, from_=0.001, to=0.01, number_of_steps=100, command=self.update_plot)
        self.b_slider.set(0.003)
        self.b_slider.grid(row=5, column=0, sticky='ew', padx=10, pady=10)
        self.b_label = customtkinter.CTkLabel(self, text="per-capita attack rate of predators on prey (b)")
        self.b_label.grid(row=5, column=1, padx=10, pady=10)
        self.b_value = customtkinter.CTkLabel(self, text=f"{self.b_slider.get():.3f}")
        self.b_value.grid(row=5, column=2, padx=10, pady=10)


        self.c_slider = customtkinter.CTkSlider(self, from_=0.001, to=0.05, number_of_steps=100, command=self.update_plot)
        self.c_slider.set(0.01)
        self.c_slider.grid(row=6, column=0, sticky='ew', padx=10, pady=10)
        self.c_label = customtkinter.CTkLabel(self, text="Predators natural deathrate (c)")
        self.c_label.grid(row=6, column=1, padx=10, pady=10)
        self.c_value = customtkinter.CTkLabel(self, text=f"{self.c_slider.get():.3f}")
        self.c_value.grid(row=6, column=2, padx=10, pady=10)


        self.f_slider = customtkinter.CTkSlider(self, from_=0.01, to=0.1, number_of_steps=100, command=self.update_plot)
        self.f_slider.set(0.02)
        self.f_slider.grid(row=7, column=0, sticky='ew', padx=10, pady=10)
        self.f_label = customtkinter.CTkLabel(self, text="Conversion rate (f)")
        self.f_label.grid(row=7, column=1, padx=10, pady=10)
        self.f_value = customtkinter.CTkLabel(self, text=f"{self.c_slider.get():.3f}")
        self.f_value.grid(row=7, column=2, padx=10, pady=10)

        self.figure = None
        self.update_plot()


    def update_plot(self, event=None):
        #Obtiene los parametros de los sliders y actualiza el plot
        self.prey_initial_value.configure(text=f"{self.prey_initial_slider.get():.0f}")
        self.predator_initial_value.configure(text=f"{self.predator_initial_slider.get():.0f}")
        self.K_value.configure(text=f"{self.K_slider.get():.0f}")
        self.a_value.configure(text=f"{self.a_slider.get():.3f}")
        self.b_value.configure(text=f"{self.b_slider.get():.3f}")
        self.c_value.configure(text=f"{self.c_slider.get():.3f}")
        self.f_value.configure(text=f"{self.f_slider.get():.3f}")

        prey_initial = self.prey_initial_slider.get()
        predator_initial = self.predator_initial_slider.get()
        K = self.K_slider.get()
        a = self.a_slider.get()
        b = self.b_slider.get()
        c = self.c_slider.get()
        f = self.f_slider.get()

        prey_population = [prey_initial]
        predator_population = [predator_initial]
        marker_size = 2

        def prey(n): 
            #Calcula la población de presas en un ciclo n
            prey_model = prey_population[n-1]
            predator_model = predator_population[n-1]
            return prey_model + a * prey_model * (1 - prey_model / K) - b * prey_model * predator_model
        def predator(n):
            #Calcula la población de depredadores en un ciclo n
            prey_model = prey_population[n-1]
            predator_model = predator_population[n-1]
            return predator_model + f * b * prey_model * predator_model - c * predator_model
        
        def model(): 
            #La función itera sobre los ciclos, actualizando la poblacion de presas y depredadores
            for i in range(1,self.cycles):
                prey_population.append(prey(i))
                predator_population.append(predator(i))
        prey_e = c / (b * f) #punto de equilibrio presas
        predator_e = (a / b) * (1 - prey_e / K) #punto de equilibrio predadores

        #Si existe una figura se va a borrar para redibujar el gráfico
        if self.figure:
            self.figure.clear()

        model()
        self.figure = plt.figure()
        #Se dibujan los puntos de equilibrio de las poblaciones
        plt.axhline(y=predator_e, color='red', linestyle='--') 
        plt.axhline(y=prey_e, color='red', linestyle='--')
        #Se genera un array con los numeros de los ciclos y se trazan las curvas de las poblaciones a lo largo de los ciclos
        plt.plot(np.arange(self.cycles), prey_population, label='Prey Population', markersize=marker_size)
        plt.plot(np.arange(self.cycles), predator_population, label='Predator Population', markersize=marker_size)
        #Etiquetas y título del gráfico
        plt.ylabel('Population')
        plt.xlabel('Cycles')
        plt.title('Predator and Prey Populations over Time')
        plt.legend()
        #Se integra el gráfico a la UI
        canvas = FigureCanvasTkAgg(self.figure, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky='nsew')


class App(customtkinter.CTk):
    #Se configura la ventana principal de la app y se añade un objeto Myframe que es el widget que contiene las funcionalidades
    def __init__(self):
        super().__init__()
        self.title("Predator And Prey Population model")
        self.geometry('1080x650')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.MyFrame = MyFrame(self)
        self.MyFrame.grid(row=0, column=0, sticky='nsew')


#Se crea una instancia de la app y se inicia un bucle para mantener la ventana activa.
app = App()
app.mainloop()