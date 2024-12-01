import numpy as np

class ReactionDiffusionModel:
    def __init__(self, reaction_rates, diffusion_coefficients, grid_size=100, dt=1.0, dx=1.0):
        self.reaction_rates = reaction_rates
        self.diffusion_coefficients = diffusion_coefficients
        self.grid_size = grid_size
        self.dt = dt
        self.dx = dx

        # Initialize concentration grids for activator (A) and inhibitor (B)
        self.A = np.random.rand(grid_size, grid_size)
        self.B = np.random.rand(grid_size, grid_size)

    def laplacian(self, matrix):
        return (
            -4 * matrix +
            np.roll(matrix, 1, axis=0) +
            np.roll(matrix, -1, axis=0) +
            np.roll(matrix, 1, axis=1) +
            np.roll(matrix, -1, axis=1)
        ) / (self.dx ** 2)

    def step(self):
        # Calculate changes due to reactions
        dA = self.reaction_rates['k1'] * self.A - self.A * self.B ** 2 + self.reaction_rates['f']
        dB = -self.B + self.A * self.B ** 2

        # Add diffusion
        dA += self.diffusion_coefficients['D_A'] * self.laplacian(self.A)
        dB += self.diffusion_coefficients['D_B'] * self.laplacian(self.B)

        # Update concentrations
        self.A += dA * self.dt
        self.B += dB * self.dt

    def simulate(self, time_steps):
        for _ in range(time_steps):
            self.step()
        return self.A, self.B

