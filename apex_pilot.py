import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime, timedelta
import time

# --- 1. KONFIGURACE STRÁNKY ---
st.set_page_config(
    page_title="APEX | Business Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. PREMIUM CSS (Inter Font, Vercel/Linear Dark Theme) ---
st.markdown("""
    <style>
    /* Import prémiového fontu Inter */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Aplikace fontu na celou aplikaci */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
    }

    /* Vynucení hlubokého dark modu a skrytí zbytečností */
    .stApp {
        background-color: #09090b !important; /* Zinc 950 */
        color: #f4f4f5 !important;
    }
    
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Moderní Sidebar */
    [data-testid="stSidebar"] {
        background-color: #000000 !important;
        border-right: 1px solid #27272a !important;
    }

    /* Čistší vstupy a tlačítka */
    .stTextInput input {
        background-color: #18181b !important;
        border: 1px solid #27272a !important;
        color: white !important;
        border-radius: 8px !important;
    }
    
    .stButton>button {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        border: none !important;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #e4e4e7 !important;
        transform: translateY(-1px);
    }

    /* Vlastní stylování karet pro AI Insights (nahrazuje rozbité expandery) */
    .insight-card {
        background-color: #18181b;
        border: 1px solid #27272a;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 16px;
        transition: border-color 0.3s ease;
    }
    .insight-card:hover {
        border-color: #52525b;
    }
    .insight-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 16px;
        font-weight: 600;
        font-size: 1.1rem;
    }
    .badge-critical { background: rgba(239, 68, 68, 0.1); color: #ef4444; padding: 4px 10px; border-radius: 6px; font-size: 0.8rem; border: 1px solid rgba(239, 68, 68, 0.2);}
    .badge-opportunity { background: rgba(16, 185, 129, 0.1); color: #10b981; padding: 4px 10px; border-radius: 6px; font-size: 0.8rem; border: 1px solid rgba(16, 185, 129, 0.2);}
    .insight-text { color: #a1a1aa; font-size: 0.95rem; line-height: 1.6; }
    .insight-action { color: #f4f4f5; font-weight: 500; margin-top: 16px; padding-top: 16px; border-top: 1px solid #27272a; }
    
    /* Vlastní KPI Metriky */
    .kpi-container {
        background-color: #18181b;
        border: 1px solid #27272a;
        border-radius: 12px;
        padding: 20px;
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    .kpi-label { color: #a1a1aa; font-size: 0.85rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px; }
    .kpi-value { font-size: 2rem; font-weight: 700; color: #ffffff; }
    .kpi-delta-up { color: #10b981; font-size: 0.9rem; font-weight: 500; }
    .kpi-delta-down { color: #ef4444; font-size: 0.9rem; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

# --- 3. STAVOVÁ LOGIKA ---
if 'route' not in st.session_state:
    st.session_state.route = 'landing'

def navigate(route):
    st.session_state.route = route

# --- 4. DATA ENGINE (Simulace dat s transparentním stylem) ---
@st.cache_data
def get_chart_data():
    dates = [datetime.now() - timedelta(days=x) for x in range(30)]
    data = pd.DataFrame({
        'Date': dates,
        'Revenue': np.random.normal(80000, 15000, 30).cumsum() + 200000,
        'Expenses': np.random.normal(50000, 8000, 30).cumsum() + 100000,
    })
    return data

# --- 5. STRÁNKY ---

def render_landing():
    # Centrování obsahu pomocí sloupců
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown("<h1 style='text-align: center; font-size: 4.5rem; font-weight: 800; letter-spacing: -2px; margin-bottom: 0;'>APEX</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #a1a1aa; font-size: 1.2rem; margin-top: -10px; margin-bottom: 40px;'>Kognitivní systém pro řízení e-commerce.</p>", unsafe_allow_html=True)
        
        # Grid pro features
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            <div class='insight-card' style='text-align: center; padding: 30px;'>
                <h3 style='margin: 0 0 10px 0;'>API Konektory</h3>
                <p style='color: #a1a1aa; font-size: 0.9rem;'>Nativní napojení na Shoptet, Meta Ads, Google Analytics a Stripe v reálném čase.</p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class='insight-card' style='text-align: center; padding: 30px;'>
                <h3 style='margin: 0 0 10px 0;'>AI Syntéza</h3>
                <p style='color: #a1a1aa; font-size: 0.9rem;'>Algoritmy detekují anomálie v maržích dřív, než se propíšou do účetnictví.</p>
            </div>
            """, unsafe_allow_html=True)

        st.write("")
        if st.button("Přejít do klientského portálu →", use_container_width=True):
            navigate('login')
            st.rerun()

def render_login():
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.markdown("<h2 style='text-align: center; font-weight: 700;'>Autentizace</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #a1a1aa; margin-bottom: 30px;'>Zadejte své přístupové údaje do Apex platformy.</p>", unsafe_allow_html=True)
        
        with st.container():
            st.text_input("Pracovní E-mail", value="ceo@techgear.cz")
            st.text_input("Zabezpečovací klíč", type="password", value="********")
            st.write("")
            if st.button("Přihlásit se do systému", use_container_width=True):
                with st.spinner("Ověřuji klíče a kompiluji data podniku..."):
                    time.sleep(1.5)
                navigate('dashboard')
                st.rerun()
        
        if st.button("← Zpět na hlavní stranu", type="tertiary"):
            navigate('landing')
            st.rerun()

def render_dashboard():
    # SIDEBAR
    with st.sidebar:
        st.markdown("<h2 style='font-weight: 800; letter-spacing: -1px;'>APEX</h2>", unsafe_allow_html=True)
        st.markdown("<div style='color: #a1a1aa; font-size: 0.8rem; margin-bottom: 30px;'>Workspace: <b>TechGear s.r.o.</b></div>", unsafe_allow_html=True)
        
        # Custom menu styling
        menu = st.radio("", ["⚡ Command Center", "🎯 Marketing ROI", "📦 Logistika", "⚙️ Nastavení API"], label_visibility="collapsed")
        
        st.markdown("<div style='margin-top: 100%; border-top: 1px solid #27272a; padding-top: 20px;'></div>", unsafe_allow_html=True)
        if st.button("Odhlásit", use_container_width=True):
            navigate('landing')
            st.rerun()

    # MAIN DASHBOARD AREA
    if menu == "⚡ Command Center":
        st.markdown("<h2 style='font-weight: 700; margin-bottom: 20px;'>Command Center</h2>", unsafe_allow_html=True)
        
        # 4x Premium KPI KARTY
        col1, col2, col3, col4 = st.columns(4)
        
        col1.markdown("""
        <div class="kpi-container">
            <div class="kpi-label">Obrat (Posledních 30 dní)</div>
            <div class="kpi-value">4.2M CZK</div>
            <div class="kpi-delta-up">↑ +12.4% vs minulý měsíc</div>
        </div>
        """, unsafe_allow_html=True)
        
        col2.markdown("""
        <div class="kpi-container">
            <div class="kpi-label">Čistá Marže</div>
            <div class="kpi-value">18.2%</div>
            <div class="kpi-delta-down">↓ -1.1% vlivem nákladů na Ads</div>
        </div>
        """, unsafe_allow_html=True)

        col3.markdown("""
        <div class="kpi-container">
            <div class="kpi-label">Akviziční Náklad (CAC)</div>
            <div class="kpi-value">640 CZK</div>
            <div class="kpi-delta-up">↑ Zlepšení o 45 CZK</div>
        </div>
        """, unsafe_allow_html=True)

        col4.markdown("""
        <div class="kpi-container">
            <div class="kpi-label">AI Health Score</div>
            <div class="kpi-value">92/100</div>
            <div style="color: #a1a1aa; font-size: 0.9rem; font-weight: 500;">Optimalizace v běhu</div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        st.write("")

        # AI ZJIŠTĚNÍ - CUSTOM HTML MÍSTO STREAMLIT EXPANDERU
        st.markdown("<h4 style='font-weight: 600; margin-bottom: 15px;'>Kognitivní Výstupy</h4>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-card">
            <div class="insight-header">
                <span>🚨 Ztráta marže na logistice</span>
                <span class="badge-critical">KRITICKÉ - Ušlý zisk 32k/týden</span>
            </div>
            <div class="insight-text">
                Autonomní sken dat ze Shoptetu a fakturace DPD ukázal anomálii. U 15 % objednávek s váhou nad 10 kg zákazníci platí fixní sazbu dopravy 99 Kč, přestože vaše reálné náklady u dopravce stouply na 145 Kč. Marži z produktu tak částečně pálíte na dotování dopravy.
            </div>
            <div class="insight-action">
                💡 Doporučená akce AI: Přepsat pravidla dopravy v Shoptetu (Váha > 10kg = 149 Kč).
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="insight-card">
            <div class="insight-header">
                <span>✨ Příležitost v retenci B2B</span>
                <span class="badge-opportunity">PŘÍLEŽITOST - Potenciál +120k/měsíc</span>
            </div>
            <div class="insight-text">
                Analýza CRM dat odhalila skupinu 14 IČO zákazníků, kteří u vás nakupují pravidelně každé úterý, ale nevyužívají B2B program. LTV (Lifetime value) těchto zákazníků je 3x vyšší než průměr. Necháváte peníze na stole tím, že s nimi aktivně nekomunikujete.
            </div>
            <div class="insight-action">
                💡 Doporučená akce AI: Spustit automatizaci e-mailu přes Klaviyo s nabídkou VIP B2B ceníku.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        st.write("")

        # GRAF (Čistý, temný Altair chart)
        st.markdown("<h4 style='font-weight: 600; margin-bottom: 15px;'>Finanční Trajektorie</h4>", unsafe_allow_html=True)
        df = get_chart_data()
        chart_data = df.melt('Date', value_vars=['Revenue', 'Expenses'], var_name='Metric', value_name='CZK')
        
        chart = alt.Chart(chart_data).mark_area(opacity=0.6, interpolate='monotone').encode(
            x=alt.X('Date:T', axis=alt.Axis(title='', grid=False, labelColor='#a1a1aa', domainColor='#27272a')),
            y=alt.Y('CZK:Q', axis=alt.Axis(gridColor='#27272a', labelColor='#a1a1aa', domain=False, tickSize=0)),
            color=alt.Color('Metric:N', scale=alt.Scale(range=['#ffffff', '#3b82f6']), legend=alt.Legend(title="", orient="top-right", labelColor='#a1a1aa'))
        ).properties(
            height=350,
            background='transparent' # Zajišťuje, že graf nemá vlastní černé pozadí
        ).configure_view(
            strokeWidth=0
        )
        
        st.altair_chart(chart, use_container_width=True)

    else:
        # Placeholder pro ostatní menu
        st.markdown(f"<h2 style='font-weight: 700; margin-bottom: 20px;'>{menu}</h2>", unsafe_allow_html=True)
        st.markdown("<div style='color: #a1a1aa;'>Tento modul je v ukázkové verzi uzamčen. Probíhá stahování dat.</div>", unsafe_allow_html=True)

# --- ROUTER ---
if st.session_state.route == 'landing':
    render_landing()
elif st.session_state.route == 'login':
    render_login()
elif st.session_state.route == 'dashboard':
    render_dashboard()
