import streamlit as st

def ma_fonction(texte):
    return f"Vous avez entré : {texte.upper()}"

# Interface Streamlit
st.title("Application Streamlit Simple")

# Centrer le contenu
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

# Boîte de sortie
resultat_placeholder = st.empty()

# Disposition en colonne centrée
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    user_input = st.text_input("Entrez du texte :", key="input_text")
    if st.button("Soumettre"):
        resultat = ma_fonction(user_input)
        resultat_placeholder.markdown(f"<h3 style='text-align: center;'>{resultat}</h3>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
