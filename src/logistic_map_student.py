import numpy as np
import matplotlib.pyplot as plt

def iterate_logistic(r, x0, n):
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, n):
        x[i] = r * x[i-1] * (1 - x[i-1])
    return x

def plot_time_series(r_list, x0, n_iterations):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.flatten()
    for i, r in enumerate(r_list):
        x = iterate_logistic(r, x0, n_iterations)
        t = np.arange(n_iterations)    
        axes[i].plot(t, x, 'b-', lw=1)
        axes[i].set_title(f'r = {r:.3f}')
        axes[i].set_xlabel('迭代次数')
        axes[i].set_ylabel('x')
        axes[i].grid(True)
    plt.tight_layout()
    return fig

def plot_bifurcation(r_min, r_max, n_r, n_iterations, n_discard):
    r = np.linspace(r_min, r_max, n_r)
    x = np.zeros(n_iterations)
    x_plot = []
    r_plot = [] 
    for r_val in r:
        x[0] = 0.5
        for i in range(1, n_iterations):
            x[i] = r_val * x[i-1] * (1 - x[i-1])   
        x_plot.extend(x[n_discard:])
        r_plot.extend([r_val] * (n_iterations - n_discard))
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(r_plot, x_plot, ',k', alpha=0.1, markersize=0.1)
    ax.set_xlabel('r')
    ax.set_ylabel('x')
    ax.set_title('Logistic映射分岔图')   
    return fig

if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    r_values = [2, 3.2, 3.45, 3.6]
    fig1 = plot_time_series(r_values, 0.5, 60)
    fig1.canvas.manager.set_window_title('figure1')    
    fig2 = plot_bifurcation(2.6, 4, 1400, 250, 100)
    fig2.canvas.manager.set_window_title('figure2')
    plt.show()
