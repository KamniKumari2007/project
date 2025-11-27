import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown("<h1 style='color:black;'>Data Analysis of India vs England Test Match at Lord's (14 July 2025)</h1>", unsafe_allow_html=True)


st.markdown("<h3 style='color:violet;'>OVERVIEW:</h3>", unsafe_allow_html=True)
st.text("This project analyzes key performance statistics from the India vs England Test match using Python and Matplotlib. It includes batting, bowling, and team-wise performance visualizations.")


st.markdown("<h3 style='color:yellow;'>LEARNINGS:</h3>", unsafe_allow_html=True)
st.markdown("""
- *Real-world data wrangling using pandas*

- *Data visualization using matplotlib and optionally seaborn*

- *Drawing conclusions from match statistics*
""")

st.markdown("<h3 style='color:pink;'>FEATURES IN THIS CODE:</h3>", unsafe_allow_html=True)
st.markdown("""
(1)Bar charts for:

A.India batting performance

B.England batting performance

C.Bowling wickets for both teams

(2)Strike Rate comparison using a grouped bar chart.
""")

india_batting = pd.read_csv(r"C:\Users\pradi\Downloads\india_batting.csv")
england_batting = pd.read_csv(r"C:\Users\pradi\Downloads\england_batting.csv")
india_bowling = pd.read_csv(r"C:\Users\pradi\Downloads\india_bowling.csv")
england_bowling = pd.read_csv(r"C:\Users\pradi\Downloads\england_bowling.csv")


sns.set_style("whitegrid")

fig_1 = plt.figure(figsize=(10, 6))
sns.barplot(x='Runs', y='Batsman', data=india_batting, color='skyblue')
plt.title('India Batting Performance')
plt.xlabel('Runs Scored')
plt.ylabel('Batsman')
plt.tight_layout()
st.pyplot(fig_1)

fig_2 = plt.figure(figsize=(10, 6))
sns.barplot(x='Runs', y='Batsman', data=england_batting, color='pink')
plt.title('England Batting Performance')
plt.xlabel('Runs Scored')
plt.ylabel('Batsman')
plt.tight_layout()
st.pyplot(fig_2)

fig_3 = plt.figure(figsize=(8, 5))
sns.barplot(x='Wickets', y='Bowler', data=india_bowling, color='purple')
plt.title('India Bowling - Wickets Taken')
plt.xlabel('Wickets')
plt.ylabel('Bowler')
plt.tight_layout()
st.pyplot(fig_3)

fig_4 = plt.figure(figsize=(8, 5))
sns.barplot(x='Wickets', y='Bowler', data=england_bowling, color='lightgreen')
plt.title('England Bowling - Wickets Taken')
plt.xlabel('Wickets')
plt.ylabel('Bowler')
plt.tight_layout()
st.pyplot(fig_4)

india_batting['Strike Rate'] = (india_batting['Runs'] / india_batting['Balls']) * 100
england_batting['Strike Rate'] = (england_batting['Runs'] / england_batting['Balls']) * 100

combined_sr = pd.concat([
    india_batting[['Batsman', 'Strike Rate']].assign(Team='India'),
    england_batting[['Batsman', 'Strike Rate']].assign(Team='England')
])

fig_5 = plt.figure(figsize=(10, 6))
sns.barplot(x='Strike Rate', y='Batsman', hue='Team', data=combined_sr)
plt.title('Strike Rate Comparison')
plt.xlabel('Strike Rate')
plt.tight_layout()
st.pyplot(fig_5)