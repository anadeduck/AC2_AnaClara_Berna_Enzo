import streamlit as st

st.title("Calcular IMC")
altura = st.number_input("Digite sua altura(em metros):", min_value=0.0,format="%.2f")
peso = st.number_input("Digite seu peso (em kg):", min_value=0.0, format="%.2f")
if altura>0:
    imc=peso/(altura**2)
else:
    imc=0
if imc>0:
    if imc <18.5:
        classificacao="abaixo do peso"
    elif 18.5<= imc< 24.9:
        classificacao="Peso normal"
    elif 25<= imc< 29.9:
        classificacao="sobrepeso"
    else:
        classificacao ="obsedidade"
else:
    classificacao="Informe altura e peso validos"
if st.button("Calcular IMC"):
    st.write(f"Seu IMC é:{imc:.2f}")
    st.write(f"Classificacao: {classificacao}")
