import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def simulator(D_u, D_v, k, f, t, output_type='gif', filename='turing_pattern'):
    """
    Simulate Turing pattern and output as an image or GIF.

    Parameters:
        D_u (float): Diffusion coefficient for species U.
        D_v (float): Diffusion coefficient for species V.
        k (float): Reaction rate constant.
        f (float): Feed rate.
        t (int): Number of time steps.
        output_type (str): 'gif' or 'png' for output format.
        filename (str): Name of the output file without extension.
    """
    # Initialize grid
    size = 100
    U = np.random.rand(size, size)
    V = np.random.rand(size, size)
    delta = 1.0
    dt = 1.0

    def laplacian(Z):
        return (
            -4 * Z +
            np.roll(Z, 1, axis=0) + np.roll(Z, -1, axis=0) +
            np.roll(Z, 1, axis=1) + np.roll(Z, -1, axis=1)
        ) / (delta ** 2)

    history = []

    for _ in range(t):
        # Reaction-diffusion equations
        dU = D_u * laplacian(U) - U * V ** 2 + f * (1 - U)
        dV = D_v * laplacian(V) + U * V ** 2 - (f + k) * V

        U += dt * dU
        V += dt * dV

        if output_type == 'gif':
            history.append(U.copy())

    if output_type == 'png':
        plt.imshow(U, cmap='viridis')
        plt.colorbar(label='Concentration')
        plt.title('Final Turing Pattern')
        plt.axis('off')
        plt.savefig(f'{filename}.png')
        plt.close()
    elif output_type == 'gif':
        fig, ax = plt.subplots()
        cax = ax.imshow(history[0], cmap='viridis')
        plt.axis('off')

        def update(frame):
            cax.set_array(history[frame])
            return cax,

        anim = FuncAnimation(fig, update, frames=len(history), blit=True)
        anim.save(f'{filename}.gif', writer=PillowWriter(fps=30))
        plt.close(fig)
    else:
        raise ValueError("Unsupported output_type. Use 'gif' or 'png'.")

    print(f"Simulation saved to {filename}.{output_type}")

