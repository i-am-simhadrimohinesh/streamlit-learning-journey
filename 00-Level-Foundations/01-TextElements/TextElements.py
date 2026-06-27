import streamlit as st

# 1. Logo (optional local image or URL)
st.logo("https://docs.streamlit.io/logo.svg")

# 2. Title
st.title("AI Learning Notes Dashboard")

# 5. Badge
st.badge("Beginner Friendly", color="green")

# 3. Header
st.header("Python Basics for AI")

# 4. Subheader
st.subheader("Variables & Data Types")

# 6. Write
st.write("This section explains how Python variables work in AI workflows.")

# 7. Markdown
st.markdown("""
### Key Points:
- Variables store data
- Python is dynamically typed
- Useful in ML preprocessing
""")

# 8. Text
st.text("Simple plain text explanation: No formatting here.")

# 9. Code
st.code("""
x = 10
y = 20
print(x + y)
""", language="python")

# 10. LaTeX
st.latex(r"x + y = z")

# 11. HTML
st.html("""
<div style="padding:10px; background-color:#f0f2f6; border-radius:10px">
    <h4 style="color:#1f77b4;">Tip Box</h4>
    <p>Always initialize variables before use in Python.</p>
</div>
""")

# 12. Divider
st.divider()

# 13. Caption
st.caption("End of lesson • Created using Streamlit")

# Extra (optional info display)
st.write("Next topic: Functions in Python 🚀")
