import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
import networkx as nx
from pyvis.network import Network

import csv

df = pd.read_csv('./genre_corr.csv')

with open("genre_dataset_for_pandas.csv", encoding="utf-8") as f:
    data = list(csv.reader(f))

df_1 = df.query('var1 == "女装"')
# df_1
df_2 = df.query('var2 == "女装"')
# df_2
df_name = pd.concat(
    [df_1, df_2],
    axis=0,
    ignore_index=True
)
# df_3
df_name = df_name.query('-0.001 <= corr <= 0.001')
df_name = df_name.sort_values('corr')
df_name = df_name[::-1]
df_name[:30]
