import streamlit as st
from model import formulas
from view.interface import mostrar_interface

# -------------------------------
# CONFIGURAÇÕES GERAIS
# -------------------------------
st.set_page_config(page_title="Calculadora de Fórmulas (MVC)", page_icon="🧮", layout="centered")
st.title("🧮 Calculadora de Fórmulas Matemáticas — Alunos Ifam")
st.markdown("### Estrutura MVC com Streamlit: Model (lógica), View (interface), Controller (controle)")

# -------------------------------
# CONTROLLER - Função de controle
# -------------------------------

def calcular(formula, *args):
    """Controlador que decide qual função chamar do Model."""
    if formula == "eq1":
        return formulas.equacao_1_grau(*args)
    elif formula == "eq2":
        return formulas.equacao_2_grau(*args)
    elif formula == "area_quadrado":
        return formulas.area_quadrado(*args)
    elif formula == "area_triangulo":
        return formulas.area_triangulo(*args)
    elif formula == "log":
        return formulas.logaritmo(*args)
    else:
        return "❌ Fórmula não reconhecida."

# -------------------------------
# VIEW - Interface principal
# -------------------------------

opcao = st.sidebar.selectbox(
    "Escolha uma fórmula:",
    [
        "Equação de 1º Grau",
        "Equação de 2º Grau",
        "Área do Quadrado",
        "Área do Triângulo",
        "Logaritmo"
    ]
)

mostrar_interface(opcao, calcular)

st.markdown("---")
st.caption("📘 Projeto Educacional - Streamlit + MVC | Computação e Matemática 💡")
