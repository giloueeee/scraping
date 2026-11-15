import streamlit as st

# Texte pur, monospace (style "code")
st.text("Hello this is a text")

# Interprète la syntaxe Markdown : **gras**, *italique*, HTML simple
st.markdown("Hello **this is a markdown**")

st.success("Hello this is a success message")

st.info("Hello this is an info message")

st.warning("Hello this is a warning message")

st.error("Hello this is an error message")

# Afficher proprement une exception Python dans l'interface
try:
    1 / 0
except Exception as e:
    st.exception(e)
