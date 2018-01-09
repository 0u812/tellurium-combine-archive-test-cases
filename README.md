# COMBINE Archive Test Cases

As part of implementing support for interoperability via COMBINE archives in Tellurium, we used a number of archives from different sources, including published papers, existing models, other software, and our own examples. This repository contains an extensive set of COMBINE archives to help developers implement support for COMBINE archives, and test existing software for compliance.

Internally, [Tellurium](http://tellurium.analogmachine.org/) uses [libCombine](https://github.com/sbmlteam/libCombine) to read and write COMBINE archives.

* Examples in the `demos` directory are designed to help developers bootstrap COMBINE archive support. They use progressively more advanced features of SED-ML.
* Examples in the `swt` directory are taken from the [SED-ML Web Tools](http://sysbioapps.dyndns.org/SED-ML_Web_Tools), and showcase advanced usage of SED-ML for performing repeated stochastic simulations, steady state scans as a function of a parameter, and nested simulations.
* The `real-models` directory contains demos of Tellurium's COMBINE archive editing functionality: A study varying Hill coefficient values for a (yeast respiratory model)[https://www.ebi.ac.uk/biomodels-main/BIOMD0000000090] and an expanded version of the [COMBINE archive by Scharm et al.](https://github.com/SemsProject/CombineArchiveShowCase).
* The `published` directory contains COMBINE archives published in the literature.
* The [jws](https://github.com/0u812/tellurium-combine-archive-test-cases/tree/master/jws) directory contains misc. archives from JWS used as examplars in testing compliance of other tools (Tellurium) with JWS. [Tellurium version 2.0.13](https://github.com/sys-bio/tellurium/releases/tag/2.0.13) or later required.
* The `sbml-test-suite` directory contains the entire SBML test suite converted into COMBINE archives.
