import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(page_title="My Portfolio", layout="wide")

# Read index.html file
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Render HTML with custom styling height
components.html(html_code, height=1000, scrolling=True)