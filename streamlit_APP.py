# 导入需要的库
import streamlit as st
import pandas as pd
import joblib

st.header('The interactive web page of the application for identifying pulmonary nodule based on Salivary microbiota')
# 输入框
st.sidebar.header('Variables', )

a = st.sidebar.number_input("g__Oribacterium", step=1, min_value=0)
b = st.sidebar.number_input("g__Defluviitaleaceae_UCG-011", step=1, min_value=0)
c = st.sidebar.number_input("g__Gemella", step=1, min_value=0)
d = st.sidebar.number_input("g__Aggregatibacter	", step=1, min_value=0)
e = st.sidebar.number_input("g__Streptococcus", step=1, min_value=0)
f = st.sidebar.number_input("g__Porphyromonas", step=1, min_value=0)
g = st.sidebar.number_input("g__Lautropia", step=1, min_value=0)
h = st.sidebar.number_input("g__Bacillus", step=1, min_value=0)
i = st.sidebar.number_input("g__Actinomyces	", step=1, min_value=0)
j = st.sidebar.number_input("g__Prevotella", step=1, min_value=0)

# 如果按下按钮
if st.button("Predict"):  # 显示按钮
    # 加载训练好的模型
    model_XGB = joblib.load("BSXGB.pkl")
    # 将输入存储DataFrame
    X = pd.DataFrame([[a, b, c, d, e, f, g, h, i, j]],
                     columns=['g__Oribacterium', 'g__Defluviitaleaceae_UCG-011', 'g__Gemella',
                               'g__Aggregatibacter', 'g__Streptococcus', 'g__Porphyromonas',
                               'g__Lautropia', 'g__Bacillus', 'g__Actinomyces', 'g__Prevotella'
                              ])
    # 进行预测
    prediction = model_XGB.predict(X)[0]
    Predict_proba = model_XGB.predict_proba(X)[:, 1][0]
    # 输出预测结果
    if prediction == 0:
        st.subheader(f"Risk grouping for pulmonary nodule:  HC")
    else:
        st.subheader(f"Risk grouping for pulmonary nodule:  PN")
    st.subheader(f"Probability of pulmonary nodule: :  {'%.2f' % float(Predict_proba * 100) + '%'}")
