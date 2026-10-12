import streamlit as st
import pandas as pd

st.set_page_config(page_title="Govana Dashboard", layout="wide", page_icon="📊")
st.title("Govana Dashboard - Zeejay's Agency")
st.write("Live sales tracking for free")

data = {
    "Client": ["Safaricom", "Naivas", "Equity", "KQ", "Twiga"],
    "Revenue (KSH)": [150000, 80000, 120000, 45000, 95000],
    "Deal Status": ["Closed Won", "In Progress", "In Progress", "Recent Lead", "Closed Won"],
    "Date": ["2026-10-10", "2026-10-11", "2026-10-12", "2026-10-11","2026-10-12"]
}
df = pd.DataFrame(data)

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"KSH {df['Revenue (KSH)'].sum():,}")
col2.metric("Deals In Progress", len(df[df['Deal Status']=="In Progress"]))
col3.metric("Recent Leads", len(df[df['Deal Status']=="Recent Lead"]))

st.subheader("Revenue by Client")
st.bar_chart(df.set_index("Client")["Revenue (KSH)"])

st.subheader("All Deals")
st.dataframe(df, use_container_width=True)
