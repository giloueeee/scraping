import streamlit as st
import time

# Barre de progression
my_bar = st.progress(0)
for p in range(10):
    time.sleep(1)
    my_bar.progress(p + 1, text=f"Progress: {(p + 1) * 10}%")

# Petit message temporaire
st.toast("Task completed!")

# Spinner / loader
with st.spinner("Downloading model..."):
    time.sleep(5)

st.success("Finished")
