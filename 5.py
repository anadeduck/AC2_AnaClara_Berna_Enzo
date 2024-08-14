# 5.      ( 2 pontos) O cardápio de uma lanchonete é o seguinte:
 #LANCHE          CÓDIGO      VALOR
 #Cachorro Quente  101         8,50
 #Bauru Simples    102         4,50
 #Hambúrger        104         5,50
#Cheeseburger      105         6,60
#Refrigerante      106         6,00

 #Crie uma aplicação (online) que leia o código do item pedido e a quantidade. Calcule o valor a ser pago por cliente. Caso não seja informado algum código da lista, deve-se informar que o código do lanche é inválido.

 import streamlit as st

 st.title( "Cardapio Lanchonete:")
 st.write( "Escolha seu lanche:")
 st.write("Cachorro quente - 101")
 st.write( "Bauru simples - 102")
 st.write( "Hamburguer - 104" )
 st.write( "Cheeseburguer - 105" )
 st.write( "Refrigerante - 106")
 st.sidebar.header("Me informe algumas coisas:")
 while True:
  codigo = st.sidebar.number_input("Digite qual o código do seu pedido:")
  quant = st.sidebar.number_input("Quantos itens você deseja?")
  add = st.sidebar.number_input("deseja adicionar mais algum item? (1 - sim e 2 - não) ")
  if add == 1:
     continue
  else:
    st.write("Clique em calcular para ver o valor total do seu pedido")
    break
  calcular_bottom = st.sidebar.button("Calcular")
   if calcular_bottom:
     while True:
      compras = 0
      if codigo == 101:
        compras = quant * 8.50
      elif codigo == 102:
        compras = quant * 4.50
      elif codigo == 104:
        compras = quant * 5.50
      elif codigo == 105:
        compras = quant * 6.60
      elif codigo == 106:
        compras = quant * 6
    st.write(f"O valor da sua compra é: {compras}")

