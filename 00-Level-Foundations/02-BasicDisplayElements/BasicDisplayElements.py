import streamlit as st
import pandas as pd

st.title("🔍 API Debugging Dashboard")

# Simulated API response
api_response = {
    "user_id": 101,
    "name": "Kiran",
    "active": True,
    "login_count": 45,
    "session_times": [12, 15, 10, 20]
}

# -----------------------------
# 1. st.metric() → Key API KPIs
# -----------------------------
st.subheader("📊 User Activity Metrics")

avg_session = sum(api_response["session_times"]) / len(api_response["session_times"])

col1, col2 = st.columns(2)

col1.metric("Login Count", api_response["login_count"], "+5 this week")
col2.metric("Avg Session (min)", round(avg_session, 2), "+2 min")


# -----------------------------
# 2. st.json() → Raw API Response
# -----------------------------
st.subheader("📦 Raw API Response")
st.json(api_response)


# -----------------------------
# 3. st.help() → Understanding Tools Used
# -----------------------------
st.subheader("📚 Help: Understanding Data Structures")

st.help(dict)   # shows dictionary documentation


# -----------------------------
# 4. st.echo() → Explain Processing Logic
# -----------------------------
st.subheader("🧠 Data Processing Logic")

with st.echo():
    sessions = api_response["session_times"]
    total = sum(sessions)
    avg = total / len(sessions)

    st.write("Total session time:", total)
    st.write("Average session time:", avg)


# -----------------------------
# 5. st.exception() → Error Handling
# -----------------------------
st.subheader("⚠️ Error Monitoring")

try:
    # Simulating a missing field error
    error_test = api_response["logout_time"] / 10
    st.write(error_test)

except Exception as e:
    st.exception(e)
    st.warning("logout_time field is missing in API response")