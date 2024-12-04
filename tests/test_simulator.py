import unittest
import os
import numpy as np
from Turing_Pattern_Simulator.main import simulator

class TestSimulator(unittest.TestCase):

    def test_parameter_effects(self):
        """Test the effects of different parameters on the result."""
        result_high_F = simulator(
            grid_size=50,
            time_steps=100,
            F=0.1,  # High feed rate
            k=0.06,
            D_u=0.16,
            D_v=0.08,
            add_noise=False,
            output_type="none"
        )

        result_low_F = simulator(
            grid_size=50,
            time_steps=100,
            F=0.01,  # Low feed rate
            k=0.06,
            D_u=0.16,
            D_v=0.08,
            add_noise=False,
            output_type="none"
        )

        # Validate that higher F produces more spread of V
        U_high, V_high = result_high_F
        U_low, V_low = result_low_F
        self.assertGreater(np.mean(V_high), np.mean(V_low))

    
    def test_simulator_creates_png(self):
        """Test if simulator creates a PNG file correctly."""
        output_file = "test_simulation_output"
        simulator(
            grid_size=50,
            time_steps=100,
            F=0.04,
            k=0.06,
            D_u=0.16,
            D_v=0.08,
            output_type="png",
            filename=output_file
        )
        
        # Check if output file exists
        self.assertTrue(os.path.exists(f"{output_file}.png"))

        # Cleanup
        os.remove(f"{output_file}.png")

    def test_simulator_with_noise(self):
        """Test simulator with noise enabled."""
        output_file = "test_simulation_with_noise"
        result = simulator(
            grid_size=50,
            time_steps=100,
            F=0.04,
            k=0.06,
            D_u=0.16,
            D_v=0.08,
            add_noise=True,
            noise_U_to_V=0.05,
            noise_V_to_U=0.05,
            output_type="png",
            filename=output_file
        )

        # Check if output file exists
        self.assertTrue(os.path.exists(f"{output_file}.png"))

        # Validate result array dimensions
        U, V = result
        self.assertEqual(U.shape, (50, 50))
        self.assertEqual(V.shape, (50, 50))

        # Validate noise was applied
        self.assertTrue(np.any(U != 1.0))  # Ensure some perturbation
        self.assertTrue(np.any(V != 0.0))

        # Cleanup
        os.remove(f"{output_file}.png")

    def test_simulator_with_gif(self):
        """Test simulator with GIF output."""
        output_file = "test_simulation_with_gif"
        simulator(
            grid_size=50,
            time_steps=100,
            F=0.04,
            k=0.06,
            D_u=0.16,
            D_v=0.08,
            add_noise=False,
            output_type="gif",
            filename=output_file
        )

        # Check if output file exists
        self.assertTrue(os.path.exists(f"{output_file}.gif"))

        # Cleanup
        os.remove(f"{output_file}.gif")

    def test_invalid_parameters(self):
        """Test simulator with invalid parameters."""
        with self.assertRaises(ValueError):
            simulator(
                grid_size=-10,  # Invalid grid size
                time_steps=100,
                F=0.04,
                k=0.06,
                D_u=0.16,
                D_v=0.08,
                output_type="png",
                filename="invalid_test"
            )

        with self.assertRaises(ValueError):
            simulator(
                grid_size=50,
                time_steps=-100,  # Invalid time steps
                F=0.04,
                k=0.06,
                D_u=0.16,
                D_v=0.08,
                output_type="png",
                filename="invalid_test"
            )


if __name__ == '__main__':
    unittest.main()
