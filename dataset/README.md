# Dataset description

## Dataset.tsv
This dataset contains all of the data measured and collected for all the phenotypes.

It is composed of 3 dimensions, the generations diets of the parents *Generation*, the phenotype measured *Phenotype*, and the value of this phenotypes *Values*. The units are described below.

The generations represent the different food the adult laying eggs ate:

**P**: Poor; **R**: Rich; **S**: Standard

XY: F0 was subjected to diet X and F1 diet Y (example: PR: F0 poor and F1 rich)

XYZ: F0 was subjected to diet X, F1 diet Y and F2 diet Z (example: SRP: F0 standard, F1 rich and F2 poor)

The different phenotypes are:

**mass**: The mass of the fly in mg

**eggsize**: The volume of the egg in mm<sup>3</sup>

**winglength**: The length of the wing in mm<sup>3</sup>

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

**eggsize**: The volume of the egg in mm<sup>3</sup>

**winglength**: The length of the wing in mm<sup>3</sup>

**devL1A**: The developmental time from 1st instar larva to adult in days

**devL1LP**: The developmental time from 1st instar larva to pupae in days

**devLPA**: The developmental time from pupae to adult in days

## RawData.csv

**no_id**: individual id
**gen_id**: generation (F0, F1, and F2)
**vial_id**: number id
**genvial_id**: meta variable composed of gen_id and vial_id numbers, so use genvial_id if you wish to include the effects of a vial
**diet_group**: diet treatment group, categorized by an individual's diet (R, S, or P, representing rich, standard, or poor diet, respectively) and diet of previous generations (e.g., F0=R, F1=RP, F2=RPP; F0 had rich food, F1 had poor food, F2 had poor food. The rightmost letter always represents the diet of that generation, and each preceding letter represents the diet of the previous generation.
**lineage**: indicates which grandparent they had (R, S, or P)
**F2_diet**: diet of F2
**F1_diet**: diet of F1
**F0_diet**: diet of F0    
**sex**: sex of the fly
**mass_mg**: mass (in mg)
**dev_L1-LP**: larval development period = development period (in days) from L1 to LP
**dev_LP-A**: pupal development period = development period (in days) from LP to adult
**dev_L1-A**: larval and pupal development period = development time (in days) from L1 to adult
**ovar_no**: ovariole number
**wing_length**: length of the fly wing in mm<sup>3</sup>

## StatisticalTests.zip

Complete results of the statistical tests performed on the raw data. They are the results of a Dunn test for multiple comparisons
done after a Kruskal-Wallis test (Bonferroni-adjusted p-value). The suffix indicates the phenotype. Note- devL1-A = development time, in days L1-Adult; devLP-A = development time in days, LP-adult; mass is in mg; egg size is estimated egg volume in mm<sup>3</sup>; ovarno is ovariole number; wing length is in mm<sup>3</sup>.
