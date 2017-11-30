#!/usr/bin/env python

####Step 2 - Clean, Join & Save New Files####

#%matplotlib inline
import pandas as pd
import statsmodels.api as sm
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import seaborn as sns

##ELEMENTARY SCHOOLS##

#Clean "acct.xls" for elementary
acctelem = pd.read_excel("acct.xls", index_col = "School ID", sheetname = 1, header = 1, skiprows = [2],
usecols = ["School ID", "School Name", "SQRP Total Points Earned", "National School Growth Percentile - Reading", "National School Growth Percentile - Math", "Percent of Students Meeting/Exceeding National Average Growth Norms", "Average Daily Attendance Rate (Grades K-8)"]).dropna()
#Clean "demo.xls" for elementary
demoelem = pd.read_excel("demo.xls", index_col = "School ID", sheetname = 1, header = 1, skiprows = [2],
usecols = ["School ID", "Bilingual %", "SpED %", "FRL %"]).fillna(0)
#Join Elem Data from "acct.xls" and "demo.xls"
joinedelem = acctelem.join(demoelem)
#Save joined data as new excel file
joinedelem.to_excel("joinedelem.xls")

##HIGH SCHOOLS##

#Clean "acct.xls" for high school
accthigh = pd.read_excel("acct.xls", index_col = "School ID", sheetname = 2, header = 1, skiprows = [2],
usecols = ["School ID", "School Name", "SQRP Total Points Earned", "School Growth Percentile PSAT10", "School Growth Percentile SAT11", "Percent Meeting College Readiness Benchmarks", "Freshmen On-Track Rate", "4-Year Cohort Graduation Rate", "Average Daily Attendance Rate"]).dropna()
#Clean "demo.xls" for high school
demohigh = pd.read_excel("demo.xls", index_col = "School ID", sheetname = 1, header = 1, skiprows = [2],
usecols = ["School ID", "Bilingual %", "SpED %", "FRL %"]).fillna(0)
#Join high school data from "acct.xls" and "demo.xls"
joinedhigh = accthigh.join(demohigh)
#Save joined data as new excel file
joinedhigh.to_excel("joinedhigh.xls")

####Step 3 - The Fun Part!!####

# 1) Run Regressions for Elementary Schools and High Schools

##Elementary School - Regression on SQRP##
df = pd.read_excel("joinedelem.xls")
X = df[["SpED %", "Bilingual %", "FRL %"]] 
X = sm.add_constant(X)
est = sm.OLS(y, X).fit()
est.summary()

##High Schools - Regression on SQRP##
df = pd.read_excel("joinedhigh.xls")
X = df[["SpED %", "Bilingual %", "FRL %"]]
y = df["SQRP Total Points Earned"]
X = sm.add_constant(X)
hest = sm.OLS(y, X).fit()
hest.summary()

# 2) Plot & Graph Results

sns.set_style("whitegrid", rc={'axes.linewidth': 2.5})
sns.set_context('notebook', font_scale=1.45, rc={"lines.linewidth": 3, "figure.figsize" : (7, 3)})

##ELEMENTARY SCHOOLS##
#SpED
ax = sns.regplot(y = "SQRP Total Points Earned", x = "SpED %", data = joinedelem)
plt.title("SQRP Points and Special Education Percentage in CPS Elementary Schools")
plt.plot()

#Bilingual
ax = sns.regplot(y = "SQRP Total Points Earned", x = "Bilingual %", data = joinedelem)
plt.title("SQRP Points and Bilingual Percentage in CPS Elementary Schools")
plt.plot()

#FRL
ax = sns.regplot(y = "SQRP Total Points Earned", x = "FRL %", data = joinedelem)
plt.title("SQRP Points and Free/Reduced Lunch Percentage in CPS Elementary Schools")
plt.plot()

##HIGH SCHOOLS##

#SpED
ax = sns.regplot(y = "SQRP Total Points Earned", x = "SpED %", data = joinedhigh)
plt.title("SQRP Points and Special Education Percentage in CPS High Schools")
plt.plot()

#Bilingual
ax = sns.regplot(y = "SQRP Total Points Earned", x = "Bilingual %", data = joinedhigh)
plt.title("SQRP Points and Bilingual Percentage in CPS High Schools")
plt.plot()

#FRL
ax = sns.regplot(y = "SQRP Total Points Earned", x = "FRL %", data = joinedhigh)
plt.title("SQRP Points and Free/Reduced Lunch Percentage in CPS High Schools")
plt.plot()
