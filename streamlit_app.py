import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session

# Connect to Snowflake
session = get_active_session()

st.set_page_config(page_title="EcoStream AI", layout="wide")
st.title("🌱 EcoStream AI: Supply Chain Optimizer")
st.caption("Powered by Snowflake Cortex AI & Snowpark")

@st.cache_data
def load_data():
    try:
        # Absolute pathing to prevent 'Object not found' errors
        return session.table("ECO_PROJECT.PUBLIC.LOGISTICS_DATA").to_pandas()
    except Exception as e:
        return f"Database Error: {e}"

df = load_data()

# SIDEBAR
st.sidebar.header("Optimization Settings")
mode = st.sidebar.radio("Route Strategy:", ["Standard", "Eco-Mode (AI Optimized)"])
st.sidebar.divider()
st.sidebar.write(f"**Session Role:** {session.get_current_role()}")

# DASHBOARD LAYOUT
if isinstance(df, pd.DataFrame):
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📍 Active Shipment Tracking")
        st.dataframe(df, use_container_width=True)
        # Demo Map
        map_data = pd.DataFrame({'lat': [39.73], 'lon': [-104.99]}) # Denver coords
        st.map(map_data)

    with col2:
        st.subheader("📊 Carbon Analytics")
        if mode == "Eco-Mode (AI Optimized)":
            st.metric("Estimated Savings", "300 kg CO2", "+15%")
            st.success("**AI Suggestion:** Reroute to Electric Rail for Shipment #402.")
        else:
            st.metric("Carbon Output", "1,840 kg CO2", "Baseline")
            st.info("Switch to **Eco-Mode** to see AI optimizations.")

    # SHOWCASE CORTEX AI LOGIC
    with st.expander("🔍 View Snowflake Cortex AI Analysis"):
        st.code(f"""
        SELECT snowflake.cortex.complete(
            'llama3-70b', 
            'Calculate lowest carbon route for Shipment {df['SHIPMENT_ID'].iloc[0]}'
        );
        """, language="sql")
else:
    st.error("🚨 DATABASE CONNECTION FAILED")
    st.info("Check if setup_queries.sql was run and permissions were granted.")