import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título da aplicação
st.title("📊 Gráfico da Função de Quarto Grau")

st.write("Função: f(x) = ax⁴ + bx³ + cx² + dx + e")

# Entradas dos coeficientes
a = st.number_input("Coeficiente a (x⁴)", value=1.0)
b = st.number_input("Coeficiente b (x³)", value=0.0)
c = st.number_input("Coeficiente c (x²)", value=0.0)
d = st.number_input("Coeficiente d (x)", value=0.0)
e = st.number_input("Coeficiente e (termo constante)", value=0.0)

# Intervalo do gráfico
intervalo = st.slider(
    "Intervalo de x",
    min_value=5,
    max_value=50,
    value=10
)

# Verificação
if a == 0:
    st.error("O coeficiente 'a' deve ser diferente de zero para ser uma função de 4º grau.")
else:
    # Define a função de quarto grau
    def funcao_quarto_grau(x, a, b, c, d, e):
        return a*x**4 + b*x**3 + c*x**2 + d*x + e

    # Valores de x e y
    x_values = np.linspace(-intervalo, intervalo, 600)
    y_values = funcao_quarto_grau(x_values, a, b, c, d, e)

    # Criação do gráfico
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.plot(
        x_values,
        y_values,
        label=f"f(x) = {a}x⁴ + {b}x³ + {c}x² + {d}x + {e}"
    )

    # Configurações do gráfico
    ax.set_title("Gráfico da Função de Quarto Grau")
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.grid(True, linestyle="--", alpha=0.7)

    # Eixos cartesianos
    ax.axhline(0)
    ax.axvline(0)

    ax.legend()

    # Exibição no Streamlit
    st.pyplot(fig)
