import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def draw_graph():
    global canvas, ax
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    x, y = np.meshgrid(x, y)
    expr = entry.get()
    try:
        z = eval(expr)
        ax.contour(x, y, z, levels=[0])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    canvas.draw()

def clear_graph():
    global ax
    ax.clear()  # clear all plots
    canvas.draw()

window = tk.Tk()
window.title('繪圖工具組')
window.geometry('1400x900')  # increase window size
window.configure(bg='lightgrey')  # add background color

label_expr = tk.Label(window, text="Enter the equation: ", bg='lightgrey', font=('Arial', 16))
label_expr.grid(row=0, column=0, padx=20, pady=20)
entry = tk.Entry(window, font=('Arial', 16))
entry.grid(row=0, column=1, padx=20, pady=20)

fig = plt.Figure(figsize=(10, 8), dpi=100)  # increase figure size
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=window)  # create canvas only once
canvas.draw()
canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)

style = ttk.Style()
style.configure('my.TButton', font=('Arial', 16), background='lightblue')

button1 = ttk.Button(window, text="Draw Graph", command=draw_graph, style='my.TButton')
button1.grid(row=2, column=0, padx=20, pady=20)

button2 = ttk.Button(window, text="Clear Graph", command=clear_graph, style='my.TButton')
button2.grid(row=2, column=1, padx=20, pady=20)

window.mainloop()
