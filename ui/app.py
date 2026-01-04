import sys
import os
# This line tells the Cloud to look at the main project folder for your code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import plotly.express as px
from engine.scraper import fetch_market_news
from engine.analyzer import analyze_headlines

# ... rest of your code ...

st.set_page_config(page_title="AI-Market Pulse", page_icon="📈", layout="wide")

st.title("🛡️ AI-Market Pulse: Intelligence Dashboard")
st.markdown("Automated Sentiment Analysis driven by **Cloud & Networking Probes**.")

if st.button("🚀 Run Live Analysis"):
    with st.spinner("Networking Probe active... Analyzing headlines with AI..."):
        # 1. Fetch
        news = fetch_market_news()
        # 2. Analyze
        results = analyze_headlines(news)
        df = pd.DataFrame(results)
        
        # 3. Visualize
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Sentiment Distribution")
            fig = px.pie(df, names='sentiment', color='sentiment',
                         color_discrete_map={'POSITIVE':'green', 'NEGATIVE':'red'})
            st.plotly_chart(fig)
            
        with col2:
            st.subheader("📝 Latest Intelligence Report")
            st.dataframe(df[['sentiment', 'confidence', 'text']], use_container_width=True)

        # Cloud Status Indicator
        st.success("Analysis Complete! Powered by GitHub Cloud Automation.")
