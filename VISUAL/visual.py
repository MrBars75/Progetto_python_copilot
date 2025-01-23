import matplotlib.pyplot as plt
import numpy as np

def initial_plot():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    plt.show()

def plot_coseno_label():
    x = np.linspace(0, 10, 100)
    y = np.cos(x)
    plt.plot(x, y, label='coseno')
    plt.legend()
    plt.show()

def plot_seno_coseno_label():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    plt.plot(x, y1, 'r--', label='seno')
    plt.plot(x, y2, label='coseno')
    plt.legend()
    plt.show() 

def plot_incremento_popolazione_mondiale():
    years = list(range(1950, 2021, 10))  # Convert range to list, include 2020
    years = np.linspace(1950, 2025, 10, dtype=int).tolist()
    population = [2.5, 2.7, 3.0, 3.3, 3.6, 4.0, 4.4, 4.8, 5.3, 5.7]
    
    # Verify lengths match
    assert len(years) == len(population), "Arrays must have same length"
    
    plt.plot(years, population, 'ro')
    plt.xlabel('Years')
    plt.ylabel('Population (in billions)')
    plt.title('World Population Growth')
    plt.grid(True)  # Add grid for better readability
    plt.show()

plot_incremento_popolazione_mondiale()