
import streamlit as st
from datetime import date, timedelta

# Lista de filmes/jogos disponíveis
produtos_disponiveis = [
    "Filme: O Senhor dos Anéis",
    "Filme: Matrix",
    "Jogo: The Witcher 3",
    "Jogo: Cyberpunk 2077",
    "Filme: Interestelar"
]

st.title("Sistema de Gerenciamento de Aluguel")

# Seleção do produto
produto_selecionado = st.selectbox(
    "Selecione um filme ou jogo:",
    produtos_disponiveis
)

# Seleção da data de retirada
data_retirada = st.date_input(
    "Data de Retirada:",
    value=date.today()
)

# Seleção da data de devolução
data_devolucao = st.date_input(
    "Data de Devolução:",
    value=date.today() + timedelta(days=7) # Sugere 7 dias para devolução
)

# Botão para registrar o aluguel
if st.button("Registrar Aluguel"):
    st.subheader("Detalhes do Aluguel:")
    st.write(f"**Produto:** {produto_selecionado}")
    st.write(f"**Data de Retirada:** {data_retirada.strftime('%d/%m/%Y')}")
    st.write(f"**Data de Devolução:** {data_devolucao.strftime('%d/%m/%Y')}")

    hoje = date.today()
    dias_restantes = (data_devolucao - hoje).days

    if dias_restantes > 0:
        st.success(f"Faltam {dias_restantes} dias para a devolução.")
    elif dias_restantes == 0:
        st.warning("A devolução é hoje!")
    else:
        st.error(f"O prazo já passou! A devolução deveria ter sido há {-dias_restantes} dias.")

