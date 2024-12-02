# Turing-Pattern-Simulator
This model is used for simulating Turing pattern by reaction diffusion model.

A Turing pattern is a spatially organized, stable pattern that emerges from the interaction between two or more chemical species undergoing reaction and diffusion. It was first described by Alan Turing in his 1952 paper on morphogenesis. The system typically involves an activator and an inhibitor, where:
1. Activator promotes both its own production and that of the inhibitor.
2. Inhibitor suppresses the activator's production.
3. Diffusion plays a key role: the inhibitor diffuses faster than the activator, leading to localized concentrations of the activator.
Mathematically, Turing patterns emerge when specific parameter conditions cause the homogeneous steady state of the reaction-diffusion system to become unstable, giving rise to periodic spatial patterns.

The Turing pattern appears in chemical reactions, in the formation and development of biological forms. Understanding the Turing pattern is important for understanding biomolecular interactions, biological development, the construction of self-forming systems, and systems biology. 

There are many reaction-diffusion models that describe the generation of Turing patterns. A classic example is the Gray-Scott (GS) model, which is widely used to study Turing patterns due to its simplicity and ability to produce complex, self-organizing structures. Details about the function can be seen

```John E. Pearson ,Complex Patterns in a Simple System.Science261,189-192(1993).DOI:10.1126/science.261.5118.189```


# Setup
```pip install Turing_Pattern_Simulator```

# Turing-pattern-simulation
This part is for users to generate their own Turing pattern by indicating parameters

How to use:
```from Turing_Pattern_Simulator import simulator```
```simulator(
#model part:
k = # removal rate of V, better give from 0.01 to 0.1
F = # feed rate of U into the system, better from 0 to 0.1
D_u = # diffusion coefficients for U, default = 0.16
D_v = # diffusion coefficients for V, default = 0.08 ```



