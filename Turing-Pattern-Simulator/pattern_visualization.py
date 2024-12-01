import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def plot_pattern(concentration, title, color_map='viridis'):
    """
    Visualize a static Turing pattern as a 2D heatmap.
    """
    plt.imshow(concentration, cmap=color_map)
    plt.colorbar(label='Concentration')
    plt.title(title)
    plt.axis('off')
    plt.show()

def save_pattern_gif(history, filename='pattern.gif', color_map='viridis', fps=30):
    """
    Visualize and save a GIF of the evolving Turing pattern.
    
    Parameters:
        history (list of numpy arrays): Each array represents the concentration grid at a time step.
        filename (str): Name of the output GIF file (e.g., 'pattern.gif').
        color_map (str): Color map for visualization.
        fps (int): Frames per second for the GIF.
    """
    fig, ax = plt.subplots()
    cax = ax.imshow(history[0], cmap=color_map)
    plt.axis('off')

    def update(frame):
        cax.set_array(history[frame])
        return cax,

    # Create animation
    anim = FuncAnimation(fig, update, frames=len(history), blit=True)

    # Save animation as GIF
    anim.save(filename, writer=PillowWriter(fps=fps))
    plt.close(fig)

