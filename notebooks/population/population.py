# -*- coding: utf-8 -*-
"""Population.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TWDLZMwmAfUUUfJfVRf19aJSJGQAeqjn
"""

import pandas as pd
import pandas as pd

pop = pd.read_csv('Population_new.csv', encoding = 'unicode_escape', index_col=None)

pop.head(10)

pop.tail()

pop.columns

pop.info()

pop['Ten_Year_Population_Growth'] = pop.Ten_Year_Population_Growth.str.replace('%', '').astype(float)

pop.columns = pop.columns.str.replace(' ', '_')

pop.rename(columns = {'2019 Population': '2019_Population', 'Ten_Year_Population_Growth': 'Ten_Year_Population_Growth(%)'}, inplace=True)

pop['2019_Population'] = pop['2019_Population'].str.replace(',', '').astype(int)

pop.describe()

pop["State"] = pop["State"].apply(lambda x: x.replace("?ashington", "Washington"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?labama", "Alabama"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?alifornia", "California"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?daho", "Idaho"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?ennessee", "Tennessee"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?irginia", "Virginia"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?exas", "Texas"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?regon", "Oregon"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?lorida", "Florida"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?ississippi", "Mississippi"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?ouisian", "Louisiana"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?ennsylvania", "Pennsylvania"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?ontana", "Montana"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?klahoma", "Oklahoma"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?aryland", "Maryland"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?eorgia", "Georgia"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?ichigan", "Michigan"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?hio", "Ohio"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?entucky", "Kentucky"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?onnecticut", "Connecticut"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?rkansas", "Arkansas"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?assachusetts", "Massachusetts"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?ebraska", "Nebraska"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?isconsin", "Wisconsin"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?laska", "Alaska"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?rizona", "Arizona"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?ansas", "Kansas"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?tah", "Utah"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?issouri", "Missouri"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?llinois", "Illinois"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?innesota", "Minnesota"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?ndiana", "Indiana"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?olorado", "Colorado"))
pop["State"] = pop["State"].apply(lambda x: x.replace("?owa", "Iowa"))
pop["State"] = pop["State"].apply(lambda x: x.replace("Louisianaa", "Louisiana"))
pop["State"] = pop["State"].apply(lambda x: x.replace("C0lorado", "Colorado"))

pop = pop.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

pop['State'] = pop['State'].replace(['?est Virginia','?ew York','?outh Dakota','?orth Carolina','?hode Island','?ew Jersey','?ew Mexico','?ew Hampshire','?orth Dakota','?outh Carolina','COlorado']
                                    ,['West Virginia','New York','South Dakota','North Carolina','Rhode Island','New Jersey','New Mexico','New Hampshire','North Dakota','South Carolina','Colorado'])

pop['State'].nunique()

! pip install pandas==0.25

from pandas_profiling import ProfileReport

profile = ProfileReport(pop)
profile

pop.describe()

# Summarize data by City and sum of ten Year Population Growth
pop.groupby('City').sum()

# Summarize data by City and median of Ten year Population Growth
pop.groupby('State').median()

# Group data by state and summarize 2019_Population
grp_state = pop.groupby(["State"])[["2019_Population"]].describe()
grp_state

grp_state.columns = grp_state.columns.droplevel(0)
grp_state

# Group data by state and summarize Ten Year Population Growth
grp_growth = pop.groupby(["State"])[["Ten_Year_Population_Growth(%)"]].describe()
grp_growth

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(15,7))
pd.value_counts(pop['State']).plot.bar()

grp_growth.columns = grp_growth.columns.droplevel(0)
grp_growth

fig, ax = plt.subplots(figsize=(15,7))


ax.bar(grp_growth.index,
        grp_growth["50%"],
        color="purple")

plt.xticks(grp_growth.index,grp_growth.index, rotation='vertical')
ax.set(title="Bar Plot of Median State Growth")
plt.show()

top_cities = pop.head(11)

from google.colab import files

pop.to_csv('Population_final.csv')
files.download('Population_final.csv')

