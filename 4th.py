import streamlit as st
import time

age = st.slider("Select your age", 0, 100, 25)
st.write("Your age is:", age)

bio = st.text_area("Write about yourself:", height=150)
st.write("Your Bio:")
st.write(bio)

st.markdown("Welcome VGU Jaipur")

st.markdown("<h3 style='color:blue;'>Blue Text Example</h3>", unsafe_allow_html=True)



progress = st.progress(0)

for i in range(100):
    time.sleep(0.05)
    progress.progress(i+1)

st.success("Loading Complete!")

st.markdown("My first webpage ")
st.markdown("""Thank you for the python""")