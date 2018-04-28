# Dataset description

## dataset.tsv
This dataset contains all of the data measured and collected for all the phenotypes.

It is composed of 3 dimensions, the generations diets of the parents *Generation*, the phenotype measured *Phenotype*, and the value of this phenotypes *Values*. The units are described below.

The generations represent the different food the adult laying eggs ate:

**P**: Poor; **R**: Rich; **S**: Standard
XY: F0 was subjected to diet X and F1 diet Y (example: PR: F0 poor and F1 rich)
XYZ: F0 was subjected to diet X, F1 diet Y and F2 diet Z (example: SRP: F0 standard, F1 rich and F2 poor)

The different phenotypes are:
**mass**: The mass of the fly in mg
**eggsize**: The length of the egg in um
**winglength**: The length of the wing in mm
**devL1A**: The developmental time from 1st instar larva to adult in days
**devL1LP**: The developmental time from 1st instar larva to pupae in days
**devLPA**: The developmental time from pupae to adult in days

## StatisticalTests.tsv
This dataset contains all the corrected multiple comparison testing between generations and phenotypes.
It is composed of 4 dimensions, the two generation tested against *Generation1* and	*Generation2*, the phenotype assessed by the test *Phenotype*, and the corresponding p-value of the test *pvalue*.

The generations represent the different food the adult laying eggs ate:

**P**: Poor; **R**: Rich; **S**: Standard
XY: F0 was subjected to diet X and F1 diet Y (example: PR: F0 poor and F1 rich)
XYZ: F0 was subjected to diet X, F1 diet Y and F2 diet Z (example: SRP: F0 standard, F1 rich and F2 poor)

The different phenotypes are:
**mass**: The mass of the fly in mg
**eggsize**: The length of the egg in um
**winglength**: The length of the wing in mm
**devL1A**: The developmental time from 1st instar larva to adult in days
**devL1LP**: The developmental time from 1st instar larva to pupae in days
**devLPA**: The developmental time from pupae to adult in days
