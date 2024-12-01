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
            'turing-simulate=turing_pattern_simulator.simulation:main',
            'turing-visualize=turing_pattern_simulator.visualization:main',
            'turing-sweep=turing_pattern_simulator.parameter_sweep:main',
        ],
    },
)
