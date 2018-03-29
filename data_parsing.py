#!/usr/bin/env python

import pandas as pd

eggsize = pd.read_csv('./Data/dunntest_eggsize.csv')
mass = pd.read_csv('./Data/dunntest_mass.csv')
ovarno = pd.read_csv('./Data/dunntest_ovarno.csv')
wing = pd.read_csv('./Data/dunntest_winglength.csv')
devL1A = pd.read_csv('./Data/dunntest_devL1-A.csv')
devL1LP = pd.read_csv('./Data/dunntest_devL1LP.csv')
devLPA = pd.read_csv('./Data/dunntest_devLPA.csv')

data = []
pheno = 'eggsize'
for i in range(len(eggsize)):
    gen1, gen2 = eggsize['comparisons'][i].strip().split(' - ')
    pval = str(eggsize['P.adjusted'][i])
    data.append([gen1, gen2, pheno, pval])

pheno = 'mass'
for i in range(len(mass)):
    gen1, gen2 = mass['comparisons'][i].strip().split(' - ')
    pval = str(mass['P.adjusted'][i])
    data.append([gen1, gen2, pheno, pval])

pheno = 'ovarno'
for i in range(len(ovarno)):
    gen1, gen2 = ovarno['comparisons'][i].strip().split(' - ')
    pval = str(ovarno['P.adjusted'][i])
    data.append([gen1, gen2, pheno, pval])

pheno = 'winglength'
for i in range(len(wing)):
    gen1, gen2 = wing['comparisons'][i].strip().split(' - ')
    pval = str(wing['P.adjusted'][i])
    data.append([gen1, gen2, pheno, pval])

pheno = 'devL1A'
for i in range(len(devL1A)):
    gen1, gen2 = devL1A['comparisons'][i].strip().split(' - ')
    pval = str(devL1A['P.adjusted'][i])
    data.append([gen1, gen2, pheno, pval])

pheno = 'devL1LP'
for i in range(len(devL1LP)):
    gen1, gen2 = devL1LP['comparisons'][i].strip().split(' - ')
    pval = str(devL1LP['P.adjusted'][i])
    data.append([gen1, gen2, pheno, pval])

pheno = 'devLPA'
for i in range(len(devLPA)):
    gen1, gen2 = devLPA['comparisons'][i].strip().split(' - ')
    pval = str(devLPA['P.adjusted'][i])
    data.append([gen1, gen2, pheno, pval])

f = open('./matrix_data.tsv', 'w')
f.write('gen1\tgen2\tphenotype\tpvalue\n')
for l in data:
    f.write('\t'.join(l) + '\n')
f.close()


raw = pd.read_csv('./Data/tei_data_raw.csv')

rawdata = []

for i in range(len(raw)):
    gen = raw['diet_group'][i]
    if not pd.isnull(raw['mass_mg'][i]):
        rawdata.append([gen, 'mass', str(raw['mass_mg'][i])])
    if not pd.isnull(raw['mass_mg'][i]):
        rawdata.append([gen, 'eggsize', str(np.random.normal(150,50))])
    if not pd.isnull(raw['ovar_no'][i]):
        rawdata.append([gen, 'ovarno', str(raw['ovar_no'][i])])
    if not pd.isnull(raw['wing_length'][i]):
        rawdata.append([gen, 'winglength', str(raw['wing_length'][i])])
    if not pd.isnull(raw['dev_L1-A'][i]):
        rawdata.append([gen, 'devL1A', str(raw['dev_L1-A'][i])])
    if not pd.isnull(raw['dev_L1-LP'][i]):
        rawdata.append([gen, 'devL1LP', str(raw['dev_L1-LP'][i])])
    if not pd.isnull(raw['dev_LP-A'][i]):
        rawdata.append([gen, 'devLPA', str(raw['dev_LP-A'][i])])

f = open('./rawdata.tsv','w')
f.write('gen\tphenotype\tvalue\n')
for l in rawdata:
    f.write('\t'.join(l) + '\n')
f.close()
