# COMBINE Archive Test Cases

As part of implementing support for interoperability via COMBINE archives in Tellurium, we used a number of archives from different sources, including published papers, existing models, other software, and our own examples. This repository contains an extensive set of COMBINE archives to help developers implement support for COMBINE archives, and test existing software for compliance.

Internally, [Tellurium](http://tellurium.analogmachine.org/) uses [libCombine](https://github.com/sbmlteam/libCombine) to read and write COMBINE archives.

* Examples in the `basic` directory are designed to help developers bootstrap COMBINE archive support. They use progressively more advanced features of SED-ML.
* Examples in the `swt` directory are taken from the [SED-ML Web Tools](http://sysbioapps.dyndns.org/SED-ML_Web_Tools), and showcase advanced usage of SED-ML for performing repeated stochastic simulations, steady state scans as a function of a parameter, and nested simulations.
* The `models` directory contains a selection of BioModels converted into COMBINE archives.
* The `published` directory contains COMBINE archives published in the literature.
* The `sbml-test-suite` directory contains the entire SBML test suite converted into COMBINE archives.
