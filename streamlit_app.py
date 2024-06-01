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
corr_min = st.number_input('相関値の最小値', placeholder=df_name['corr'].min())
corr_max = st.number_input('相関値の最大値', placeholder=df_name['corr'].max())

df_name = df_name[df_name['corr'] >= corr_min]
df_name = df_name[df_name['corr'] <= corr_max]
df_name = df_name.sort_values('corr')
df_name = df_name[::-1]

res11 = []
res00 = []
res10 = []
res01 = []
for i in range(len(df_name['var1'])):
    id_1 = data[0].index(df_name['var1'].iat[i])

    id_2 = data[0].index(df_name['var2'].iat[i])

    c_11= 0
    c_10 =0
    c_01= 0
    c_00 = 0

    for d in data[1:]:
        if d[id_1] == '1' and d[id_2] == '1':
            c_11 += 1
        elif d[id_1] == '1' and d[id_2] == '0':
            c_10 += 1
        elif d[id_1] == '0' and d[id_2] == '1':
            c_01 += 1
        elif d[id_1] == '0' and d[id_2] == '0':
            c_00 += 1

    prob = np.array([[c_00, c_01], [c_10, c_11]])

    s = np.sum(prob)
    prob = prob / s #同時確率の完成

    prob_1 = np.sum(prob, axis=1)
    prob_2 = np.sum(prob, axis=0)
    
    res11.append((prob[1,1]/prob_1[1]/prob_2[1] - 1.0)*100)
    res00.append( (prob[0,0]/prob_1[0]/prob_2[0] - 1.0)*100)
    res10.append(( prob[1,0]/prob_1[1]/prob_2[0] - 1.0)*100)
    res01.append((prob[0,1]/prob_1[0]/prob_2[1] - 1.0)*100)
    
df_name['p11/p1p1(%)'] = res11
df_name['p00/p0p0(%)'] = res00
df_name['p10/p1p0(%)'] = res10
df_name['p01/p0p1(%)'] = res01
#st.write()
st.dataframe(
	df_name,
	width=1200,
	use_container_width=True,
	
)
