# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 18:24:05 2024

@author: vitau
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from pandas_profiling import ProfileReport
import seaborn as sns
from sklearn.feature_selection import f_classif
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PowerTransformer
df = pd.read_excel('dataset_fraude.xlsx')

df_teste = df[["NUM_CPF_CNPJ","DSC_STATUS_EMPRESA_LARANJA","VLR_CAPITAL_SOCIAL","VLR_TOTAL_NFCE",
                    "VLR_ENTRADAS_TOTAL","VLR_SAIDAS_TOTAL","VLR_BRUTO_PRODUTO_I",
                    "VLR_BRUTO_PRODUTO_IE","QTD_LARANJA_TODOS_CONTADORES","QTD_EMPRESAS_LARANJA_CONTADOR",
                    "QTD_LARANJAS_SOCIO","QTD_LARANJA_ANTIGO_SOCIO", "NUM_DDD_01","ENQUADRAMENTO_AUX", 
                    "SGL_UF_AUX", "UF_AUX_CONTADOR", "DIV_SAIDA_ENTRADA"]]



df_teste.isna().sum()

df_teste[["QTD_LARANJAS_SOCIO"]].boxplot()
plt.show()




df_teste["DDD"] = df_teste["NUM_DDD_01"].apply(lambda x: 0 if x == 27 else 1)  
df_teste["FLAG_AUX"] = df_teste["ENQUADRAMENTO_AUX"].fillna(value=0)
df_teste["FLAG_AUX"] = df_teste["FLAG_AUX"].apply(lambda x: 1 if x != 0 else 0)
df_teste["FLAG_UF_AUX"] = df_teste["SGL_UF_AUX"].fillna(value=0)
df_teste["FLAG_UF_AUX"] = df_teste["SGL_UF_AUX"].apply(lambda x:0 if x !="ES" else 1)
df_teste["UF_CONTADOR"] = df_teste["UF_AUX_CONTADOR"].apply(lambda x:0 if x=="ES" else 1)
df_teste["NUM_CPF_CNPJ"] = df_teste["NUM_CPF_CNPJ"].astype(str)
df_teste["MATRIZ"] = df_teste["NUM_CPF_CNPJ"].str.get(11)
df_teste["FLAG_MATRIZ"] = df_teste["MATRIZ"].apply(lambda x:0 if x=="1" else 1)
df_teste["STATUS_LARANJA"] = df_teste["DSC_STATUS_EMPRESA_LARANJA"].apply(lambda x: 0 if x == "REGULAR" else 1)


df_teste["DIV_SAIDA_ENTRADA"].fillna(0)
df_teste["NUM_DDD_01"].value_counts(dropna=False)


sns.histplot(data=df_teste,x="QTD_LARANJAS_SOCIO",hue="STATUS_LARANJA",kde=True)
plt.show()
sns.kdeplot(data=df_teste,x="QTD_LARANJAS_SOCIO",hue="STATUS_LARANJA")
plt.show()
sns.boxplot(data=df_teste,x="STATUS_LARANJA", y="QTD_LARANJAS_SOCIO")
plt.show()

df_teste["QTD_LARANJAS_SOCIO"].describe(include=df_teste["STATUS_LARANJA"])

sns.histplot(data=df_teste,x="QTD_EMPRESAS_LARANJA_CONTADOR",hue="STATUS_LARANJA",kde=True)
plt.show()
sns.kdeplot(data=df_teste,x="QTD_EMPRESAS_LARANJA_CONTADOR",hue="STATUS_LARANJA")
plt.show()
sns.boxplot(data=df_teste,x="STATUS_LARANJA", y="QTD_EMPRESAS_LARANJA_CONTADOR")
plt.show()


df_teste["QTD_EMPRESAS_LARANJA_CONTADOR"][df_teste["STATUS_LARANJA"]==1].describe()
df_teste["QTD_EMPRESAS_LARANJA_CONTADOR"][df_teste["STATUS_LARANJA"]==0].describe()



sns.histplot(data=df_teste,x="VLR_BRUTO_PRODUTO_I",hue="STATUS_LARANJA",kde=True)
plt.show()
sns.kdeplot(data=df_teste,x="VLR_BRUTO_PRODUTO_I",hue="STATUS_LARANJA")
plt.show()
sns.boxplot(data=df_teste,x="STATUS_LARANJA", y="VLR_BRUTO_PRODUTO_I")
plt.show()


df_teste["VLR_BRUTO_PRODUTO_I"][df_teste["STATUS_LARANJA"]==1].describe()
df_teste["VLR_BRUTO_PRODUTO_I"][df_teste["STATUS_LARANJA"]==0].describe()




