import tkinter as tk
from tkinter import Scale
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random
import time

class SelectionSortVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Selection Sort Visualizer")

        self.array_length = 50
        self.array = [random.randint(1, 100) for _ in range(self.array_length)]
        self.delay = tk.DoubleVar(value=0.0)

        self.fig, self.ax = plt.subplots()
        self.ax.bar(range(len(self.array)), self.array, align='center')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.start_button = tk.Button(self.button_frame, text="Start Selection Sort", command=self.start_sort)
        self.start_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.generate_button = tk.Button(self.button_frame, text="Generate Data", command=self.generate_data)
        self.generate_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.delay_scale = Scale(self.button_frame, from_=0.0, to=0.5, orient=tk.HORIZONTAL, resolution=0.1, label="Delay", variable=self.delay)
        self.delay_scale.pack(side=tk.LEFT, padx=5, pady=5)

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def draw_bars(self, color_array):
        self.ax.clear()
        self.ax.bar(range(len(self.array)), self.array, color=color_array, align='center')
        self.canvas.draw()
        self.root.update_idletasks()

    def generate_data(self):
        self.array = [random.randint(1, 100) for _ in range(self.array_length)]
        self.draw_bars(['blue'] * len(self.array))

    def start_sort(self):
        self.selection_sort()

    def selection_sort(self):
        n = len(self.array)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                color_array = ['blue'] * len(self.array)
                color_array[i] = 'orange'
                color_array[j] = 'orange'
                self.draw_bars(color_array)
                time.sleep(self.delay.get())
                if self.array[j] < self.array[min_index]:
                    min_index = j
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            self.draw_bars(['green' if x == i or x == min_index else 'blue' for x in range(len(self.array))])
            time.sleep(self.delay.get())

    def on_closing(self):
        self.root.quit()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    visualizer = SelectionSortVisualizer(root)
    root.mainloop()
