import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime, timedelta
import time

# --- POKROČILÁ KONFIGURACE ---
st.set_page_config(
    page_title="APEX AI | Enterprise Intelligence",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS PRO ČISTÝ ENTERPRISE LIGHT THEME ---
st.markdown("""
    <style>
    /* Hlavní pozadí - velmi jemná šedá pro kontrast s bílými kartami */
    .stApp { background-color: #f8fafc; }
    
    /* Úprava metrik do podoby bílých karet s jemným stínem */
    div[data-testid="metric-container"] {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    
    /* Vzhled postranního panelu */
    div[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
    
    /* Titulky a texty do profi tmavě modré/břidlicové */
    h1, h2, h3, h4, h5, h6, p, span {
        color: #0f172a;
    }
    
    /* Expandery (Karty s detaily) */
    div[data-testid="stExpander"] {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    }
    
    /* Změna barvy primárních tlačítek na korporátní modrou */
    .stButton>button[data-baseweb="button"] {
        border-radius: 8px;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIKA A STAV ---
if 'auth' not in st.session_state:
    st.session_state.auth = False

def simulate_finance_data():
    dates = [datetime.now() - timedelta(days=x) for x in range(30)]
    data = pd.DataFrame({
        'Day': dates,
        'Revenue': np.random.normal(120000, 15000, 30).cumsum() + 500000,
        'Expenses': np.random.normal(80000, 5000, 30).cumsum() + 300000,
    })
    data['Profit'] = data['Revenue'] - data['Expenses']
    return data

# --- SIDEBAR NAVIGACE ---
def render_sidebar():
    with st.sidebar:
        st.markdown("<h2 style='color: #2563eb; font-weight: 800; margin-bottom: 0;'>💠 APEX AI</h2>", unsafe_allow_html=True)
        st.caption("Enterprise Operating System v3.0")
        st.divider()
        
        st.markdown("**Klientský profil:**")
        st.markdown("<h4 style='margin-top:0;'>TechGear s.r.o.</h4>", unsafe_allow_html=True)
        st.caption("Obrat: 120M CZK / Aktivní napojení: 8")
        
        st.write("")
        menu = st.radio("Řídící panely", [
            "📊 Executive Dashboard", 
            "🎯 Marketing & Akvizice", 
            "⚙️ Operativa & Logistika", 
            "💰 Cashflow & Finance"
        ])
        
        st.spacer = st.container()
        st.write("---")
        if st.button("Odhlásit bezpečně"):
            st.session_state.auth = False
            st.rerun()
        return menu

# --- PŘIHLAŠOVACÍ OBRAZOVKA (LOGIN) ---
if not st.session_state.auth:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.markdown("<h1 style='text-align: center; color: #2563eb; font-size: 3rem;'>💠 APEX AI</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #64748b; margin-bottom: 2rem;'>Holistic Business Intelligence</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("### Zabezpečený přístup")
            st.text_input("Pracovní E-mail", value="ceo@techgear.cz")
            st.text_input("Zabezpečovací klíč (API/Password)", type="password", value="**********")
            
            if st.button("Autentizovat a načíst data podniku", use_container_width=True, type="primary"):
                with st.spinner("Navazuji šifrované spojení s ERP, CRM a reklamními systémy..."):
                    time.sleep(1.5)
                st.session_state.auth = True
                st.rerun()
else:
    # --- HLAVNÍ APLIKACE (BĚŽÍCÍ PO PŘIHLÁŠENÍ) ---
    menu = render_sidebar()
    fin_df = simulate_finance_data()

    if menu == "📊 Executive Dashboard":
        st.title("Holistický přehled podniku")
        st.markdown("Automatická syntéza dat z **Pohoda ERP**, **Shoptet**, **Meta Ads** a **Google Analytics 4**.")
        
        # TOP Metriky
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Měsíční obrat (MTD)", "8 450 000 CZK", "12.4 %")
        col2.metric("Čistá marže (Net Margin)", "18.2 %", "-1.1 %", delta_color="inverse")
        col3.metric("Customer Acquisition Cost", "640 CZK", "45 CZK")
        col4.metric("AI Health Score", "88 / 100", "Stabilní")
        
        st.write("---")
        
        # AI Upozornění - Vypadá jako profesionální auditní zpráva
        st.subheader("🚨 Kritická AI Zjištění (Posledních 24h)")
        
        with st.expander("📉 Ztráta marže vlivem logistiky (Priorita: VYSOKÁ)", expanded=True):
            st.markdown("""
            **Analýza:** Systém zaznamenal, že u 15 % objednávek v kategorii *Těžké váhy* dotujete dopravu. Průměrná cena dopravy u DPD stoupla, ale váš košík stále nabízí fixní sazbu 99 Kč. 
            
            **Dopad na zisk:** Ztrácíte přibližně **32 000 Kč týdně** na rozdílu mezi vybranou a zaplacenou dopravou.
            
            **Akční krok:** Navrhujeme automaticky upravit ceník dopravy v Shoptet API na základě váhy košíku.
            """)
            col_btn, _ = st.columns([1, 3])
            with col_btn:
                if st.button("Aplikovat dynamickou dopravu", type="primary"):
                    st.success("API požadavek odeslán do Shoptetu. Změna se projeví do 5 minut.")

        with st.expander("📈 Nevyužitý potenciál u B2B klientů (Priorita: STŘEDNÍ)"):
            st.markdown("Identifikovali jsme 14 IČO zákazníků, kteří nakupují pravidelně každé úterý materiál za více než 10 000 Kč, ale nevyužívají váš věrnostní program. Odeslání automatického e-mailu s nabídkou VIP účtu může zvýšit jejich LTV o 30 %.")

        # Zobrazení Grafu v bílém kontextu
        st.write("")
        st.subheader("Vývoj tržeb a nákladů (30 dní)")
        chart_data = fin_df.melt('Day', value_vars=['Revenue', 'Expenses'], var_name='Typ', value_name='Hodnota')
        chart = alt.Chart(chart_data).mark_area(opacity=0.4).encode(
            x=alt.X('Day:T', title='Datum'),
            y=alt.Y('Hodnota:Q', title='CZK'),
            color=alt.Color('Typ:N', scale=alt.Scale(range=['#2563eb', '#ef4444'])), # Modrá pro Revenue, Červená pro výdaje
            tooltip=['Day', 'Typ', 'Hodnota']
        ).properties(height=350)
        st.altair_chart(chart, use_container_width=True)

    elif menu == "🎯 Marketing & Akvizice":
        st.title("Výkonnost Marketingu")
        st.markdown("Detailní rozpad návratnosti investic (ROAS) a akvizičních nákladů (CAC) přes všechny kanály.")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Celkový Spend (30 dní)", "450 000 CZK")
        col2.metric("Průměrné PNO", "14.5 %", "-2.1 %", delta_color="inverse")
        col3.metric("Návratnost zákazníka (LTV:CAC)", "4.2x", "Zdravé")

        st.write("---")
        st.subheader("Audit reklamních platforem")
        
        # Simulace tabulky
        audit_data = pd.DataFrame({
            "Kanál": ["Meta Ads (FB/IG)", "Google Search", "Google PMax", "TikTok", "E-mailing"],
            "Spend (CZK)": [180000, 120000, 100000, 40000, 10000],
            "CAC (CZK)": [750, 420, 510, 1200, 45],
            "ROAS": [3.2, 5.8, 4.5, 1.1, 28.5],
            "AI Status": ["Optimalizovat", "Škálovat", "Stabilní", "Kritické - Vypnout", "Škálovat"]
        })
        
        # Stylování tabulky
        st.dataframe(
            audit_data.style.apply(lambda x: ['background: #fee2e2; color: #991b1b' if v == 'Kritické - Vypnout' 
                                            else 'background: #dcfce7; color: #166534' if 'Škálovat' in str(v) 
                                            else '' for v in x], axis=1),
            use_container_width=True,
            hide_index=True
        )

    elif menu == "💰 Cashflow & Finance":
        st.title("Řízení Cashflow")
        st.markdown("Předikce likvidity a analýza vázaného kapitálu na základě dat z účetnictví.")
        
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("### Peněžní Runway")
                st.markdown("<h2 style='color: #166534;'>14.5 měsíců</h2>", unsafe_allow_html=True)
                st.write("Při současném Burn Rate (spalování hotovosti) máte zajištěný provoz na více než rok bez externího financování.")
        
        with col2:
            with st.container(border=True):
                st.markdown("### Vázaný kapitál ve skladu")
                st.markdown("<h2 style='color: #991b1b;'>4 250 000 CZK</h2>", unsafe_allow_html=True)
                st.write("30 % vašich skladových zásob se nepohnulo déle než 90 dní (tzv. Dead Stock). AI doporučuje okamžitý flash-sale k uvolnění hotovosti.")

    elif menu == "⚙️ Operativa & Logistika":
        st.title("Provozní efektivita")
        st.write("Sledujte rychlost expedice a chybovost napříč vašimi sklady.")
        st.info("Zde by byly hluboké statistiky z vašeho WMS (Warehouse Management System). Prozatím ve fázi připojování konektoru.")
