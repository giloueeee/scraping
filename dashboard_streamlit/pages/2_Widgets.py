import streamlit as st

# Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or hiding Widget")

# Radio dans la barre latérale
status = st.sidebar.radio("What is your status", ["Activate", "Inactivate"])
if status == "Activate":
    st.sidebar.success("You're activated")
else:
    st.sidebar.warning("Inactivate")

# Selectbox
occupation = st.selectbox("Your occupation", ["Data scientist", "Data engineer", "Programmer"])
st.write("You selected this option", occupation)

# Multiselect
location = st.multiselect("Where do you work", ["London", "New York", "Paris"])
st.write(f"You have selected {len(location)} location/s")

# Slider
level = st.slider("What is your level", 1, 5)
st.write("Level :", level)
