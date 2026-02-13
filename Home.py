# Home.py
import streamlit as st
import pandas as pd
import io
import zipfile
import os
import plotly.express as px
import plotly.graph_objects as go

# ────────────────────────────────────────────────
# Page Configuration
# ────────────────────────────────────────────────
st.set_page_config(
    page_title="Credit Card Fraud Detection Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ────────────────────────────────────────────────
# Custom CSS (Professional Look)
# ────────────────────────────────────────────────
st.markdown("""
    <style>
    .main .block-container {padding-top: 1.5rem; padding-bottom: 2rem;}
    h1, h2, h3 {color: #1E3A8A;}
    .stExpander > div > div > div {background-color: #f8fafc;}
    hr {border-color: #e2e8f0;}
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Sidebar – Navigation & Filters
# ────────────────────────────────────────────────
with st.sidebar:
    st.title("🛡️ Fraud Dashboard")
    st.markdown("---")
    
    page = st.radio("Main Sections", [
        "🏠 Overview",
        "📊 Key Insights",
        "🔍 Detailed Analysis",
        "🗺️ Geographic Patterns",
        "⏰ Temporal Patterns",
        "📈 Feature Importance"
    ], index=0)
    
    st.markdown("---")
    st.caption("Dataset: 1,296,675 credit card transactions")
    st.caption("Fraud rate: ~0.58%")
    st.caption(f"Last updated: February 2026")

# ────────────────────────────────────────────────
# Data Loading (cached)
# ────────────────────────────────────────────────
@st.cache_data(show_spinner="Loading cleaned dataset...")
def load_data():
    encodings = ["utf-8", "cp1252", "latin1"]
    df = pd.DataFrame()
    # Prefer a parquet file if present, otherwise fall back to CSV in workspace
    preferred = 'cleaned_df.parquet'
    fallback_csv = 'credit_card_transactions.csv'

    path = preferred if os.path.exists(preferred) else (fallback_csv if os.path.exists(fallback_csv) else preferred)

    # Handle parquet quickly
    if path.lower().endswith('.parquet') and os.path.exists(path):
        try:
            df = pd.read_parquet(path)
        except Exception as e:
            st.error(f"Failed to read parquet file '{path}': {e}")
            return pd.DataFrame()
        # coerce datetimes if present
        if 'trans_date_trans_time' in df.columns:
            df['trans_date_trans_time'] = pd.to_datetime(df.get('trans_date_trans_time'), errors='coerce')
        if 'dob' in df.columns:
            df['dob'] = pd.to_datetime(df.get('dob'), errors='coerce')
        return df

    # Otherwise attempt CSV (or zip containing CSV)
    zipped = zipfile.is_zipfile(path) if os.path.exists(path) else False
    inner_name = None
    zf = None

    try:
        if zipped:
            zf = zipfile.ZipFile(path)
            csv_names = [n for n in zf.namelist() if n.lower().endswith('.csv')]
            inner_name = csv_names[0] if csv_names else zf.namelist()[0]

        for enc in encodings:
            try:
                if zipped:
                    with zf.open(inner_name, 'r') as binf:
                        text_stream = io.TextIOWrapper(binf, encoding=enc)
                        df = pd.read_csv(text_stream, engine='c', on_bad_lines='skip')
                else:
                    df = pd.read_csv(path, encoding=enc, on_bad_lines='skip')
                break
            except UnicodeDecodeError:
                continue
            except pd.errors.ParserError:
                try:
                    if zipped:
                        with zf.open(inner_name, 'r') as binf:
                            text_stream = io.TextIOWrapper(binf, encoding=enc)
                            df = pd.read_csv(text_stream, engine='python', sep=None, on_bad_lines='skip')
                    else:
                        df = pd.read_csv(path, encoding=enc, engine='python', sep=None, on_bad_lines='skip')
                    break
                except Exception:
                    continue

        if df.empty:
            # Final fallback: try reading raw bytes and decoding
            try:
                if zipped:
                    with zf.open(inner_name, 'r') as binf:
                        raw = binf.read().decode('utf-8', errors='replace')
                else:
                    with open(path, 'rb') as f:
                        raw = f.read().decode('utf-8', errors='replace')
                try:
                    df = pd.read_csv(io.StringIO(raw))
                except pd.errors.ParserError:
                    df = pd.read_csv(io.StringIO(raw), engine='python', sep=None, on_bad_lines='skip')
            except Exception as e:
                st.error(f"Failed to load '{path}': {e}")
                return pd.DataFrame()

    finally:
        if zf is not None:
            zf.close()

    # Ensure these date columns exist before coercing
    if not df.empty:
        if 'trans_date_trans_time' in df.columns:
            df['trans_date_trans_time'] = pd.to_datetime(df.get('trans_date_trans_time'), errors='coerce')
        if 'dob' in df.columns:
            df['dob'] = pd.to_datetime(df.get('dob'), errors='coerce')

    return df

df = load_data()

# ────────────────────────────────────────────────
# Helper Functions
# ────────────────────────────────────────────────
def fraud_percentage():
    if df is None or df.empty or 'is_fraud' not in df.columns:
        return pd.Series({0: 0.0, 1: 0.0})
    pct = df['is_fraud'].value_counts(normalize=True) * 100
    return pct.round(3)

def metric_card(title, value, delta=None, color="#1E3A8A"):
    with st.container():
        st.markdown(f"<h4 style='color:{color}; margin-bottom:0;'>{title}</h4>", unsafe_allow_html=True)
        st.metric(label=title, value=value, delta=delta)

# ────────────────────────────────────────────────
# PAGE: OVERVIEW
# ────────────────────────────────────────────────
if page == "🏠 Overview":

    st.title("Credit Card Fraud Detection Dashboard")
    st.markdown("### Real-world transaction fraud pattern analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        fraud_pct = fraud_percentage().get(1, 0.0)
        metric_card("Fraud Rate", f"{fraud_pct:.3f}%", color="#dc2626")

    with col2:
        total_tx = len(df) if df is not None else 0
        metric_card("Total Transactions", f"{total_tx:,}")

    with col3:
        fraud_count = int(df['is_fraud'].sum()) if ('is_fraud' in df.columns) else 0
        metric_card("Fraud Cases", f"{fraud_count:,}", color="#dc2626")

    st.markdown("---")

    colA, colB = st.columns([3, 2])

    with colA:
        fig_pie = px.pie(
            names=['Legitimate', 'Fraud'],
            values=fraud_percentage(),
            color_discrete_sequence=['#60a5fa', '#dc2626'],
            title="Transaction Class Distribution",
            hole=0.4
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie, use_container_width=True)

    with colB:
        st.subheader("Key Observations")
        st.markdown("""
        - **Severe class imbalance** → only ~0.58% fraudulent
        - High-value transactions more suspicious
        - Distance from home → strong fraud signal
        - Night hours (especially 22:00–04:00) show elevated risk
        - Certain **categories** and **merchants** are riskier
        """)

# ────────────────────────────────────────────────
# PAGE: KEY INSIGHTS
# ────────────────────────────────────────────────
elif page == "📊 Key Insights":

    st.title("Most Important Fraud Patterns")

    tabs = st.tabs([
        "Amount",
        "Distance",
        "Hour of Day",
        "Category Risk",
        "Merchant Risk"
    ])

    with tabs[0]:
        st.subheader("Transaction Amount – Fraud vs Legitimate")
        fig_amt = px.box(
            df,
            x='is_fraud',
            y='amt',
            color='is_fraud',
            color_discrete_map={0: '#60a5fa', 1: '#dc2626'},
            title="Transaction Amount Distribution",
            labels={'is_fraud': 'Type', 'amt': 'Amount (USD)'}
        )
        fig_amt.update_layout(showlegend=False)
        st.plotly_chart(fig_amt, use_container_width=True)

    with tabs[1]:
        st.subheader("Customer–Merchant Distance")
        fig_dist = px.box(
            df,
            x='is_fraud',
            y='distance',
            color='is_fraud',
            color_discrete_map={0: '#60a5fa', 1: '#dc2626'},
            title="Geographic Distance (approximate Euclidean)"
        )
        fig_dist.update_layout(showlegend=False)
        st.plotly_chart(fig_dist, use_container_width=True)

    with tabs[2]:
        st.subheader("Fraud Rate by Hour of Day")
        hour_fraud = df.groupby('hour')['is_fraud'].mean() * 100
        fig_hour = px.line(
            hour_fraud,
            title="Fraud Probability by Hour (%)",
            markers=True,
            color_discrete_sequence=['#1e40af']
        )
        fig_hour.update_layout(yaxis_title="Fraud Rate (%)")
        st.plotly_chart(fig_hour, use_container_width=True)

    with tabs[3]:
        cat_fraud = df.groupby('category')['is_fraud'].mean().sort_values(ascending=False) * 100
        fig_cat = px.bar(
            cat_fraud,
            title="Fraud Rate by Merchant Category (%)",
            color=cat_fraud.values,
            color_continuous_scale='Reds'
        )
        st.plotly_chart(fig_cat, use_container_width=True)

    with tabs[4]:
        top_merch = df.groupby('merchant')['is_fraud'].mean().nlargest(12) * 100
        fig_merch = px.bar(
            top_merch,
            title="Top 12 Merchants by Fraud Rate (%)",
            color=top_merch.values,
            color_continuous_scale='Reds'
        )
        st.plotly_chart(fig_merch, use_container_width=True)

# ────────────────────────────────────────────────
# PAGE: DETAILED ANALYSIS
# ────────────────────────────────────────────────
elif page == "🔍 Detailed Analysis":

    st.title("Detailed Exploratory Analysis")

    with st.expander("Age & Gender", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            fig_age = px.histogram(
                df,
                x='age',
                color='is_fraud',
                barmode='overlay',
                title="Customer Age Distribution by Fraud Status",
                color_discrete_map={0: '#60a5fa', 1: '#dc2626'}
            )
            st.plotly_chart(fig_age, use_container_width=True)

        with col2:
            gender_rate = df.groupby('gender')['is_fraud'].mean() * 100
            fig_gender = px.bar(
                gender_rate,
                title="Fraud Rate by Gender (%)",
                color=gender_rate.index,
                color_discrete_sequence=['#ec4899', '#64748b']
            )
            st.plotly_chart(fig_gender, use_container_width=True)

    with st.expander("Job Titles – Top Riskiest", expanded=False):
        job_risk = df.groupby('job')['is_fraud'].mean().nlargest(10) * 100
        fig_job = px.bar(job_risk, title="Top 10 Riskiest Occupations (%)")
        st.plotly_chart(fig_job, use_container_width=True)

# ────────────────────────────────────────────────
# PAGE: GEOGRAPHIC PATTERNS
# ────────────────────────────────────────────────
elif page == "🗺️ Geographic Patterns":

    st.title("Geographic Fraud Hotspots")

    tab1, tab2 = st.tabs(["By State", "Top Cities"])

    with tab1:
        state_fraud = df.groupby('state')['is_fraud'].sum().sort_values(ascending=False).head(15)
        fig_state = px.bar(
            state_fraud,
            title="Number of Fraud Cases by State (Top 15)",
            color=state_fraud.values,
            color_continuous_scale='OrRd'
        )
        st.plotly_chart(fig_state, use_container_width=True)

    with tab2:
        city_fraud = df.groupby('city')['is_fraud'].sum().nlargest(12)
        fig_city = px.bar(city_fraud, title="Top 12 Cities by Fraud Count")
        st.plotly_chart(fig_city, use_container_width=True)

# ────────────────────────────────────────────────
# PAGE: TEMPORAL PATTERNS
# ────────────────────────────────────────────────
elif page == "⏰ Temporal Patterns":

    st.title("Time-based Fraud Patterns")

    col1, col2 = st.columns(2)

    with col1:
        hour_line = df.groupby('hour')['is_fraud'].mean() * 100
        fig_h = px.line(hour_line, title="Fraud Rate by Hour of Day (%)", markers=True)
        st.plotly_chart(fig_h, use_container_width=True)

    with col2:
        dow_fraud = df.groupby('day')['is_fraud'].mean() * 100
        fig_dow = px.bar(
            dow_fraud,
            title="Fraud Rate by Day of Week (%)",
            labels={'day': 'Day (0=Mon … 6=Sun)'}
        )
        st.plotly_chart(fig_dow, use_container_width=True)

# ────────────────────────────────────────────────
# PAGE: FEATURE IMPORTANCE
# ────────────────────────────────────────────────
elif page == "📈 Feature Importance":

    st.title("Numerical Features – Correlation with Fraud")

    num_cols = df.select_dtypes(include='number').columns
    corr = df[num_cols].corr()['is_fraud'].sort_values(ascending=False)[1:]

    fig_corr = px.bar(
        corr,
        title="Pearson Correlation with is_fraud",
        color=corr.values,
        color_continuous_scale='RdBu_r'
    )
    fig_corr.update_layout(yaxis_title="Correlation", xaxis_title="Feature")
    st.plotly_chart(fig_corr, use_container_width=True)

    st.info("""
    **Strongest signals (in descending order):**
    • amt (transaction amount)
    • distance (customer–merchant distance)
    • hour (time of day)
    """)

# ────────────────────────────────────────────────
# Footer
# ────────────────────────────────────────────────
st.markdown("---")
st.caption("Credit Card Fraud Exploratory Analysis • Streamlit Dashboard • 2026")