from setuptools import setup, find_packages

setup(
    name='Turing_pattern_simulator',
    version='1',
    description='A Python-based tool for constructing, verifying, and visualizing Turing Pattern based on reaction-diffusion models.',
    author='Zihao Song',
    author_email='zhsong@uw.edu',
    url='https://github.com/songzi123songzi/Turing-Pattern-Simulator',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'Turing_pattern_simulator-simulate=Turing_pattern_simulator.simulation:main',
            'Turing_pattern_simulator-visualize=Turing_pattern_simulator.visualization:main',
            'Turing_pattern_simulator-sweep=Turing_pattern_simulator.parameter_sweep:main',
        ],
    },
)
