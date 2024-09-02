import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

"""The function to be plotted is 3*pi*e^(-5sin(2*pi*t))"""
"""Plot at a scale of 100 in the y-axis at 1 in the x-axis"""

class FuncVisualiser:
    def __init__(self, min=0, max=2, points=1000):
        """Initialise the minimum value of t, maximum value of t and the total number of points to be plotted."""
        self.min = min
        self.max = max
        self.points = points

        self.curve = np.linspace(min, max, points)

    def lambda_func(self, t):
        """Plot the lambda function 5sin(2*pi*t)"""
        return 5 * np.sin(2 * t * np.pi)
    
    def main_func(self):
        """Plot the main function h(t)"""
        lambda_value = self.lambda_func(self.curve)
        return 3 * np.pi * np.exp(-lambda_value)
    
    def slider_plot(self, value):
        """Update the plot based on the slider value."""
        new_max = self.slider.val 
        self.curve = np.linspace(self.min, new_max, self.points)
        h_t = self.main_func()
        self.plot_line.set_xdata(self.curve)
        self.plot_line.set_ydata(h_t)
        self.axis.relim()  
        self.axis.autoscale_view() 
        plt.draw()

    def plot(self):
        """Matplotlib code to plot the graph."""

        h_t = self.main_func()
        fig, self.axis = plt.subplots(figsize=(12, 10))
        plt.subplots_adjust(bottom=0.25)  
        self.plot_line, = plt.plot(self.curve, h_t)
        plt.title("Function h(t)")
        plt.xlabel('t')
        plt.ylabel('h(t)')
        plt.grid(True)

        axis_slider = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='#4DBEEE')
        self.slider = Slider(axis_slider, 't_max', self.min, 10 * self.max)
        self.slider.on_changed(self.slider_plot)

        plt.show()

# Example usage
graph = FuncVisualiser()
graph.plot()
