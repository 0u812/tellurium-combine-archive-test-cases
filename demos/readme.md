# Demos

This directory contains SED-ML demos of increasing difficulty. The demos are also accessible as a Tellurium notebook by choosing `File->Example Notebooks->COMBINE Archive Basics`.

* `demo-trivial.omex`: Minimal Combine archive containing an SBML model (myModel) representing conversion of species S1 to S2, a single timecourse simulation, and a plot.

* `demo-dual-simulations.omex`: Plots a deterministic simulation and a stochastic simulation of the same system.

* `demo-stochastic-ensemble.omex`: Uses a repeated task to run multiple copies of a stochastic simulation, then plots the ensemble

* `demo-phase-plot.omex`: Shows how to plot the value of one variable of a system vs. another variable.

* `demo-dynamics.omex`: Another dynamical simulation, but for a larger model (10 reactions).

* `demo-repeated-task.omex`: Using the model from `demo-dynamics.omex`, scans through a set of predefined values for a kinetic parameter (**J1_KK2**).

* `demo-2-sedml-files.omex`: An example of a COMBINE archive containing multiple SED-ML files.
