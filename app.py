import streamlit as st
import pandas as pd
import plotly.express as px
import json

# Page config
st.set_page_config(page_title="Web Attack Timeline", layout="wide")
st.title("🛡️ Web App Attack Timeline Dashboard")
st.markdown("Visualizing a simulated web attack from phishing to root access.")

# Load attack data
with open("attack_events.json") as f:
    events = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(events)
df["Start"] = pd.to_datetime(df["start"])
df["End"] = pd.to_datetime(df["end"])

# Plot timeline
fig = px.timeline(
    df,
    x_start="Start",
    x_end="End",
    y="task",
    color="task",
    hover_data=["detail"],
    title="Web Attack Progression"
)
fig.update_yaxes(autorange="reversed")
st.plotly_chart(fig, use_container_width=True)

# Event Table
st.subheader("📋 Event Breakdown")
st.dataframe(df[["task", "detail", "start", "end"]])
