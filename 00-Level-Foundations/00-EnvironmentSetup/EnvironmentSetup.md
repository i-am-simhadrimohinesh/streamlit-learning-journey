# 🚀 Recommended Streamlit Environment Setup

🧱 1. Create Virtual Environment
```bash
py -m venv .venv
```
▶️ 2. Activate Environment

Windows (PowerShell / CMD):
```bash
.venv\Scripts\activate
```
🧪 3. Check Python Version
```bash
py --version
```
📦 4. Install Streamlit (Important: upgrade pip first)
```bash
py -m pip install --upgrade pip
pip install streamlit
```
📌 5. Verify Installation
```bash
streamlit --version
```
🚀 6. Run First Streamlit App

Create a file:
app.py

Add:
```python
import streamlit as st

st.title("Hello Streamlit 🚀")
st.write("My first app is running!")
```
Run:
```bash
streamlit run app.py
```