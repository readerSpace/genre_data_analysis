import pandas as pd
import numpy as np
import csv
import streamlit as st
df = pd.read_csv('./genre_corr.csv')

with open("genre_dataset_for_pandas.csv", encoding="utf-8") as f:
    data = list(csv.reader(f))

options = data[0]

selected_var1 = st.selectbox("タグを選択してください：", options)
#selected_var2 = st.selectbox("タグを選択してください：", options)

#df_1 = df.query('var1 == ' + selected_var1)
df_1 = df[df['var1'] == selected_var1]
# df_1
#df_2 = df.query('var2 == ' + + selected_var1)
df_2 = df[df['var2'] == selected_var1]
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
st.write(df_name[:20])
