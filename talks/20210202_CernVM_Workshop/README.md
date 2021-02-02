*(Tue February 2nd 2021)*

talk by Bob Dröge (@bedroge) at CernVM Virtual Workshop 2021.

https://indico.cern.ch/event/885212/overview

* [slides](EESSI-CernVM-Workshop-20210202.pdf)

## Q&A

* Q: Are some of the HPC centers in EuroHPC or PRACE?
  * A: Jülich and CSCS are examples for large centers which are part of EESSI (not sure if they are part of PRACE or EuroHPC).
  * A: LUMI has shown signs of interest.

* Q (Valentin Volkl): Key4HEP is already using Gitlab CI for publising to CVMFS and would be interested in a GitHub PR based workflow as envisaged by EESSI, interested in collaboration; perhaps the Github action runner can help.
  * A: We would be very interested to discuss this more. We also expect that the CVMFS ephemeral publish container would help.

* Q (Dave Dykstra): Rocky Linux already uses building based on github PRs.
  * A: Thanks for the comment, we will definitely look at how they are doing this.

* Q: Does your tool support multiple versions/compilers of a package in the same build tree?
  * A: We don’t do that at the moment for compilers, but modules are perfectly suitable for doing this.
  * A: We already have multiple versions of OpenFOAM in the EESSI pilot repository.

* Q (Graeme A. Stewart): Interested in continuing the discussion to learn in HSF from EESSI packaging experience.
  * A: Happy to get in touch and discuss this in more detail.
