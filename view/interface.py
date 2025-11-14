import streamlit as st

def mostrar_interface(formula, calcular_callback):
    """
    Exibe o formulário correspondente à fórmula escolhida.
    Chama a função 'calcular_callback' passando os valores inseridos.
    """
    if formula == "Equação de 1º Grau":
        st.header("Equação de 1º Grau — ax + b = 0")
        a = st.number_input("Valor de a:", step=1)
        b = st.number_input("Valor de b:", step=1)
        if st.button("Calcular"):
            st.success(calcular_callback("eq1", a, b))

    elif formula == "Equação de 2º Grau":
        st.header("Equação de 2º Grau — ax² + bx + c = 0")
        a = st.number_input("Valor de a:", step=1)
        b = st.number_input("Valor de b:", step=1)
        c = st.number_input("Valor de c:", step=1)
        if st.button("Calcular"):
            st.success(calcular_callback("eq2", a, b, c))

    elif formula == "Área do Quadrado":
        st.header("Área do Quadrado — A = lado²")
        lado = st.number_input("Lado:", step=1)
        if st.button("Calcular"):
            st.success(calcular_callback("area_quadrado", lado))

    elif formula == "Área do Triângulo":
        st.header("Área do Triângulo — A = (base × altura) / 2")
        base = st.number_input("Base:", step=1)
        altura = st.number_input("Altura:", step=1)
        if st.button("Calcular"):
            st.success(calcular_callback("area_triangulo", base, altura))

    elif formula == "Logaritmo":
        st.header("Logaritmo — log₍b₎(x)")
        base = st.number_input("Base (b):", step=1)
        valor = st.number_input("Valor (x):", step=1)
        if st.button("Calcular"):
            st.success(calcular_callback("log", base, valor))
