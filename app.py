import streamlit as st

st.set_page_config(layout="wide")

st.title("India EV Market Dashboard 🚗⚡")

# Replace this with your Power BI publish-to-web link
powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=1334753b-0570-4b95-9f43-f4e493227906&autoAuth=true&ctid=f372731b-ab11-4425-ae60-7130988374fd" \
""

# Show Power BI dashboard inside Streamlit
st.components.v1.iframe(powerbi_url, width=1200, height=700)
