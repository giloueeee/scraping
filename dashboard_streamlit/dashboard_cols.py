import streamlit as st
import plotly.express as px

# Importer les datasets
df_stocks = px.data.stocks()
df_tips = px.data.tips()

st.set_page_config(layout="wide")

# Deux colonnes
col1, col2 = st.columns(2)

# --- Colonne 1 ---
with col1:
    st.subheader("Evolution of stock prices")

    companies_options = df_stocks.columns[1:]
    companies = st.multiselect(
        "Companies selected:",
        companies_options,
        default=list(companies_options)
    )

    if companies:
        fig_lines = px.line(df_stocks, x="date", y=companies, title="Companies stocks")
        st.plotly_chart(fig_lines)
    else:
        st.info("Select at least one company.")

# --- Colonne 2 ---
with col2:
    st.subheader("Tips amount per day")

    size = st.slider("Size of clients", 1, int(df_tips["size"].max()))

    df_filtered = df_tips[df_tips["size"] == size]

    fig_bars = px.bar(
        df_filtered,
        x="day",
        y="tip",
        color="sex",
        title="Tips by Sex on Each Day",
        labels={"tip": "Tip Amount", "day": "Day of the Week"}
    )

    st.plotly_chart(fig_bars)
