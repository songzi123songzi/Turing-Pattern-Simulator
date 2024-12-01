import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter

def plot_pattern(concentration, title, color_map='viridis'):
    """
    Visualize a static Turing pattern as a 2D heatmap.
    """
    plt.imshow(concentration, cmap=color_map)
    plt.colorbar(label='Concentration')
    plt.title(title)
    plt.axis('off')
    plt.show()

def save_pattern_video(history, filename='pattern.mp4', color_map='viridis', fps=30, video_format='mp4'):
    """
    Visualize and save a video or GIF of the evolving Turing pattern.
    
    Parameters:
        history (list of numpy arrays): Each array represents the concentration grid at a time step.
        filename (str): Name of the output file (e.g., 'pattern.mp4' or 'pattern.gif').
        color_map (str): Color map for visualization.
        fps (int): Frames per second for the video.
        video_format (str): Either 'mp4' or 'gif'.
    """
    fig, ax = plt.subplots()
    cax = ax.imshow(history[0], cmap=color_map)
    plt.axis('off')

    def update(frame):
        cax.set_array(history[frame])
        return cax,

    # Create animation
    anim = FuncAnimation(fig, update, frames=len(history), blit=True)

    # Save animation
    if video_format == 'gif':
        anim.save(filename, writer=PillowWriter(fps=fps))
    elif video_format == 'mp4':
        anim.save(filename, writer=FFMpegWriter(fps=fps))
    else:
        raise ValueError("Unsupported format. Choose 'mp4' or 'gif'.")
    plt.close(fig)
