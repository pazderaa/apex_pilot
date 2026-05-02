import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime, timedelta

# --- 1. ABSOLUTNÍ PRIORITA: VYNUCONÝ LIGHT MODE A ČISTÝ DESIGN ---
st.set_page_config(page_title="APEX BI", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    /* Vynucení bílého pozadí a tmavého textu bez ohledu na systémové nastavení */
    :root { --primary-color: #0066FF; }
    .stApp { background-color: #FFFFFF !important; color: #1A1A1A !important; }
    
    /* Skrytí Streamlit prvků */
    header, footer, #MainMenu {visibility: hidden;}
    
    /* Fonty a texty */
    html, body, [class*="css"] { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important; }
    h1, h2, h3 { color: #1A1A1A !important; font-weight: 700 !important; letter-spacing: -0.02em !important; }
    
    /* Sidebar - čistě bílý s jemnou linkou */
    [data-testid="stSidebar"] { background-color: #FFFFFF !important; border-right: 1px solid #F0F0F0 !important; }
    
    /* Tlačítka - Moderní Apple Style */
    .stButton>button {
        background-color: #1A1A1A !important;
        color: #FFFFFF !important;
        border-radius: 6px !important;
        padding: 0.6rem 1.5rem !important;
        font-weight: 500 !important;
        border: none !important;
        width: 100%;
    }
    .stButton>button:hover { background-color: #333333 !important; }
    
    /* Karty a kontejnery */
    .stat-card {
        background: #FFFFFF;
        border: 1px solid #F0F0F0;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        margin-bottom: 20px;
    }
    
    /* Inputy */
    .stTextInput input { border-radius: 6px !important; border: 1px solid #E0E0E0 !important; background: #F9F9F9 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. LOGIKA NAVIGACE ---
if 'view' not in st.session_state:
    st.session_state.view = 'landing'

# --- 3. STRÁNKY ---

# A. LANDING PAGE
if st.session_state.view == 'landing':
    _, col, _ = st.columns([1, 2, 1])
    with col:
        st.write("")
        st.write("")
        st.write("")
        st.markdown("<h1 style='text-align: center; font-size: 3.5rem;'>Apex Engine</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #666; font-size: 1.2rem;'>Autonomní platforma pro růst e-commerce byznysu.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        
        # Grid vlastností
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### 🔍 Deep Audit")
            st.write("AI prohledá každou transakci, kliknutí i skladovou položku.")
        with c2:
            st.markdown("### 📈 Profit Optimization")
            st.write("Nalezení skrytých nákladů a automatické zvýšení marže.")
        
        st.write("")
        st.write("")
        if st.button("Vstoupit do aplikace"):
            st.session_state.view = 'login'
            st.rerun()

# B. LOGIN PAGE
elif st.session_state.view == 'login':
    _, col, _ = st.columns([1, 1, 1])
    with col:
        st.write("")
        st.write("")
        st.markdown("<h2 style='text-align: center;'>Vítejte zpět</h2>", unsafe_allow_html=True)
        st.write("")
        st.text_input("E-mail")
        st.text_input("Heslo", type="password")
        st.write("")
        if st.button("Přihlásit se"):
            st.session_state.view = 'dashboard'
            st.rerun()
        if st.button("Zpět", type="secondary"):
            st.session_state.view = 'landing'
            st.rerun()

# C. DASHBOARD
elif st.session_state.view == 'dashboard':
    # SIDEBAR
    with st.sidebar:
        st.markdown("## APEX 🦅")
        st.write("TechGear s.r.o.")
        st.write("---")
        menu = st.radio("Sekce", ["Přehled", "Marketing", "Sklad", "Nastavení API"])
        st.write("")
        if st.button("Odhlásit se"):
            st.session_state.view = 'landing'
            st.rerun()

    # CONTENT
    st.markdown(f"<h1>{menu}</h1>", unsafe_allow_html=True)
    st.write("Poslední synchronizace: Před 4 minutami")
    st.write("---")

    # KPI Metriky - Čistý design
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown("<div class='stat-card'><small>OBRAT (30D)</small><br><b style='font-size: 1.5rem;'>4.2M CZK</b><br><span style='color: green;'>↑ 12%</span></div>", unsafe_allow_html=True)
    with m2:
        st.markdown("<div class='stat-card'><small>ČISTÁ MARŽE</small><br><b style='font-size: 1.5rem;'>18.2%</b><br><span style='color: red;'>↓ 1.1%</span></div>", unsafe_allow_html=True)
    with m3:
        st.markdown("<div class='stat-card'><small>COST PER ACQ.</small><br><b style='font-size: 1.5rem;'>640 CZK</b><br><span style='color: green;'>↑ 45 CZK</span></div>", unsafe_allow_html=True)
    with m4:
        st.markdown("<div class='stat-card'><small>AI SCORE</small><br><b style='font-size: 1.5rem;'>92/100</b><br><span style='color: blue;'>Optimal</span></div>", unsafe_allow_html=True)

    # AI INSIGHTS
    st.markdown("### ✨ AI Prioritní Doporučení")
    
    with st.container():
        st.markdown("""
        <div style="background: #F8F9FA; border-left: 4px solid #1A1A1A; padding: 20px; border-radius: 4px;">
            <b style="font-size: 1.1rem;">🚨 Detekována ztráta marže v logistice</b><br>
            <p style="color: #444; margin-top: 10px;">Systém zjistil, že u 15 % objednávek dotujete dopravu o více než 40 Kč. 
            Ceny DPD stouply, ale váš web stále nabízí starý tarif.</p>
            <small style="color: #666;">Možný roční dopad: + 1.2M CZK k zisku.</small>
        </div>
        """, unsafe_allow_html=True)
        st.button("Aplikovat opravu jedním kliknutím")

    st.write("")
    
    # GRAF - Čistý bílý podklad, modrá linie
    st.markdown("### Vývoj výkonnosti")
    chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Tržby', 'Náklady'])
    st.line_chart(chart_data)
