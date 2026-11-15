import time
import streamlit as st
import plotly.express as px

t0 = time.perf_counter()
st.set_page_config(page_title="Mon dashboard", layout="wide")

# Compteur : le script est ré-exécuté à chaque interaction
if "runs" not in st.session_state:
    st.session_state.runs = 0
st.session_state.runs += 1

df_stocks = px.data.stocks()
df_tips = px.data.tips()

# ---- Étape 6 : plusieurs pages ----
def page_decouverte():
    st.title("Découverte de Streamlit")
    st.text("Hello this is a text")
    st.markdown("Hello **this is a markdown**")
    st.success("Hello this is a success message")
    if st.checkbox("Show/Hide"):
        st.text("Showing or hiding Widget")
    occupation = st.selectbox("Your occupation", ["Data scientist", "Data engineer", "Programmer"])
    st.write("You selected this option", occupation)


def page_dashboard():
    st.title("Le dashboard")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Evolution of stock prices")
        options = df_stocks.columns[1:]
        companies = st.multiselect("Companies selected:", options, default=list(options))
        if companies:
            st.plotly_chart(px.line(df_stocks, x="date", y=companies, title="Companies stocks"))
        else:
            st.info("Select at least one company.")
    with col2:
        st.subheader("Tips amount per day")
        size = st.slider("Size of clients", 1, int(df_tips["size"].max()))
        st.plotly_chart(px.bar(df_tips[df_tips["size"] == size], x="day", y="tip", color="sex",
                               title="Tips by Sex on Each Day"))


def page_stats():
    st.titl("Statistiques descriptives")
    st.subheader("Pour les stocks :")
    st.write(df_stocks.describe())
    st.subheader("Pour les tips :")
    st.write(df_tips.describe())


# Navigation dans la barre latérale
page = st.sidebar.radio("Select a page", ["Découverte", "Dashboard", "Statistiques"])
if page == "Découverte":
    page_decouverte()
elif page == "Dashboard":
    page_dashboard()
else:
    page_stats()

st.caption(f"Exécution n°{st.session_state.runs} du script · durée {(time.perf_counter() - t0) * 1000:.0f} ms")
