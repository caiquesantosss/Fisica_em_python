import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Função que calcula a trajetória do lançamento oblíquo
def calcular_trajectoria(v0, angulo, g):
    angulo_rad = np.radians(angulo)  # Converter para radianos
    t_voo = (2 * v0 * np.sin(angulo_rad)) / g  # Tempo total de voo
    x = np.linspace(0, v0 * np.cos(angulo_rad) * t_voo, 1000)  # Intervalo de x
    y = x * np.tan(angulo_rad) - (g / (2 * v0 ** 2 * np.cos(angulo_rad) ** 2)) * x ** 2  # Equação da parábola
    return x, y, t_voo

# Função que calcula a área sob a curva (integral da parábola)
def calcular_area(v0, angulo, g):
    angulo_rad = np.radians(angulo)
    x_final = (v0 ** 2 * np.sin(2 * angulo_rad)) / g  # Distância final (alcance)
    area = (v0 ** 2 * np.sin(angulo_rad) * x_final) / g - (g / (2 * v0 ** 2 * np.cos(angulo_rad) ** 2)) * (x_final ** 3) / 3
    return area

# Função que será chamada quando o botão for pressionado
def mostrar_grafico():
    try:
        v0 = float(entry_v0.get())  # Velocidade inicial
        angulo = float(entry_angulo.get())  # Ângulo de lançamento
        g = float(entry_g.get())  # Gravidade

        # Verifica se os valores são válidos
        if v0 <= 0 or angulo < 0 or angulo > 90 or g <= 0:
            messagebox.showerror("Erro", "Insira valores válidos!")
            return

        # Calcular a trajetória
        x, y, t_voo = calcular_trajectoria(v0, angulo, g)

        # Calcular a área
        area = calcular_area(v0, angulo, g)

        # Criar o gráfico
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x, y, label="Trajetória do projétil")
        ax.set_xlabel("Distância (m)")
        ax.set_ylabel("Altura (m)")
        ax.set_title("Lançamento Oblíquo")
        ax.legend()

        # Exibir a área calculada
        area_label.config(text=f"Área sob a curva: {area:.2f} m²")

        # Exibir o gráfico no Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

root = tk.Tk()
root.title("Simulação de Lançamento Oblíquo")

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Velocidade Inicial (m/s):").grid(row=0, column=0, padx=10)
entry_v0 = tk.Entry(frame_inputs)
entry_v0.grid(row=0, column=1)

tk.Label(frame_inputs, text="Ângulo (°):").grid(row=1, column=0, padx=10)
entry_angulo = tk.Entry(frame_inputs)
entry_angulo.grid(row=1, column=1)

tk.Label(frame_inputs, text="Gravidade (m/s²):").grid(row=2, column=0, padx=10)
entry_g = tk.Entry(frame_inputs)
entry_g.grid(row=2, column=1)

btn_grafico = tk.Button(root, text="Mostrar Trajetória", command=mostrar_grafico)
btn_grafico.pack(pady=10)

frame_grafico = tk.Frame(root)
frame_grafico.pack()

area_label = tk.Label(root, text="Área sob a curva: ")
area_label.pack(pady=10)

root.mainloop()
