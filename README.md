# COMBINE Archive Test Cases

This repository contains COMBINE archive test cases to help developers implement support for COMBINE archives, and test the support of existing software for COMBINE archives. The archives in this repository were created with the [Tellurium notebook](http://tellurium.analogmachine.org/), which uses [libCombine](https://github.com/sbmlteam/libCombine) to read and write COMBINE archives.

* Examples in the `basic` directory are designed to help developers bootstrap COMBINE archive support. They use progressively more advanced features of SED-ML.
* Examples in the `advanced` directory are taken from the [SED-ML Web Tools](http://sysbioapps.dyndns.org/SED-ML_Web_Tools), and showcase advanced usage of SED-ML for performing repeated stochastic simulations, steady state scans as a function of a parameter, and nested simulations.
* The `models` directory contains a selection of BioModels converted into COMBINE archives.
* The `published` directory contains COMBINE archives published in the literature.
* The `sbml-test-suite` directory contains the entire SBML test suite converted into COMBINE archives.
