import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Streamlit app of vgu")
st.text("Welcome to our dashboard")
st.header("I am a student ")
st.write("You can write",10+5)

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:")
st.write("Your name is:",name,"Your age is:", age)
st.selectbox("Enter your course :",["BCA","BTECH","MCA"])

if st.button("Click ME"):
    st.success("Clicked Button ")
file = st.file_uploader("Upload your file ")

if file:
    content = file.read()
    st.write("File uploaded Successfully !!!!")

data = {"Name": ["TOM","Jack","POP","Hurry"],"Marks": [20,15,18,19]}
df = pd.DataFrame(data)

st.dataframe(df)

data = pd.DataFrame({
"Marks": [20,15,18,19]
})

st.line_chart(data)
st.bar_chart(data)

subject = ["Python",["C++"],["Java"]]
marks=[20,15,10]

fig , ax = plt.subplots(1,1)
ax.pie(marks, labels=subject, autopct="%1.1f%%")
st.pyplot(fig)
plt.show()
