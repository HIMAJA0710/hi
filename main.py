
import streamlit as st
import matplotlib.pyplot as plt

st.title('Matplotlib Test')

# Create a simple plot
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
ax.set_ylabel('Some numbers')

st.pyplot(fig)

