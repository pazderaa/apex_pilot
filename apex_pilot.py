import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Apex AI | Váš virtuální CEO", page_icon="🦅", layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def go_to(page_name):
    st.session_state.page = page_name

def generate_mock_data():
    dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
    data = pd.DataFrame({
        'Datum': dates,
        'Návštěvnost': np.random.randint(1000, 5000, size=30),
        'Tržby (CZK)': np.random.randint(20000, 100000, size=30),
        'Útrata Ads (CZK)': np.random.randint(5000, 25000, size=30)
    })
    return data.set_index('Datum')

def landing_page():
    st.markdown("<h1 style='text-align: center; font-size: 4rem; color: #1E88E5;'>Apex Business Pilot AI 🦅</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: gray;'>Nehádejte, proč váš byznys neroste. Nechte AI najít trhliny.</h3>", unsafe_allow_html=True)
    
    st.write("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Marketing & Ads**\n\nAI analyzuje ROAS, CTR a únavu kreativy. Řekne vám, kterou reklamu vypnout.")
    with col2:
        st.warning("**Web & UX**\n\nDetekce úzkých hrdel na webu. Zjistěte, proč lidé opouštějí košík na mobilu.")
    with col3:
        st.success("**CRM & Retence**\n\nAnalýza LTV zákazníků. Odhalíme, proč se klienti nevracejí a jak je reaktivovat.")
    
    st.write("")
    st.write("")
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    with col_btn2:
        if st.button("Spustit aplikaci (Přihlášení)", use_container_width=True, type="primary"):
            go_to('login')

def login_page():
    st.title("🔐 Přihlášení do klientské zóny")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            st.text_input("Pracovní E-mail", value="reditel@mujeshop.cz")
            st.text_input("Heslo", type="password", value="123456")
            
            st.write("*(Mockup: Data zdrojů (Meta Ads, GA4, Shoptet) jsou již fiktivně napojena)*")
            
            submitted = st.form_submit_button("Přihlásit a analyzovat data", type="primary", use_container_width=True)
            if submitted:
                with st.spinner("AI stahuje data z Meta Ads API, Google Analytics a CRM..."):
                    time.sleep(2) # Simulace načítání
                go_to('dashboard')

def dashboard_page():
    st.sidebar.title("🦅 Apex Pilot")
    st.sidebar.write("Vítejte, **řediteli**.")
    st.sidebar.write("---")
    if st.sidebar.button("Log Out"):
        go_to('landing')
    
    st.title("⚡ Holistický Audit Podniku (Říjen 2026)")
    st.write("AI zanalyzovalo 125 430 datových bodů z vašich systémů. Zde je výsledek.")
    
    # Hlavní metriky
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Celkové Tržby (30 dní)", "1 450 000 Kč", "12 %")
    col2.metric("Marketingový Spend", "320 000 Kč", "-5 % (Ušetřeno)")
    col3.metric("Konverzní poměr", "1.8 %", "-0.4 %")
    col4.metric("Prům. hodnota (AOV)", "1 850 Kč", "2 %")
    
    st.write("---")
    
    # Taby pro detailní analýzu
    tab1, tab2, tab3, tab4 = st.tabs(["🔥 Ranní AI Svodka (Urgentní)", "📈 Marketing & Ads", "💻 Web & UX", "👥 CRM & Zákazníci"])
    
    with tab1:
        st.subheader("CEO Svodka: Co musíte vyřešit DNES")
        st.error("**Kritický problém: Mobilní checkout**\n\nVčera po updatu webu klesla konverze na iOS zařízeních o 40 %. Lidé nedokážou kliknout na tlačítko 'Zaplatit', protože ho překrývá banner s cookies. **Ušlý zisk za 24h: cca 18 500 Kč.**")
        st.warning("**Varování: Reklamní kampaň 'Podzimní výprodej' krvácí**\n\nCena za proklik (CPC) u této kampaně na FB stoupla za 3 dny o 150 %. Kreativa je 'vyhořelá' (Frequency > 4.5). AI doporučuje kampaň okamžitě pozastavit.")
        st.success("**Příležitost: Skrytý bestseller**\n\nProdukt 'Zimní bunda X' má organicky o 300 % více zobrazení, ale nemá žádnou reklamu. Alokujte sem 1000 Kč/den, předpokládané ROAS je 6.5.")
        
        st.line_chart(generate_mock_data()[['Tržby (CZK)', 'Útrata Ads (CZK)']])
        
    with tab2:
        st.subheader("Analýza Marketingu (PNO & ROAS)")
        st.write("Vaše reklamy generují návštěvnost, ale ne efektivní zisk.")
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.info("💡 **AI Insight: Špatné cílení na TikToku**\n\nTikTok ads vám přivádí uživatele ve věku 14-18 let. Váš průměrný produkt ale stojí 4000 Kč. Tito lidé tvoří 30 % trafficu, ale 0.1 % nákupů. Zrušte TikTok kampaň nebo tam nasaďte levnější produkty (tzv. tripwires).")
        with col_m2:
            st.bar_chart(pd.DataFrame({'ROAS (Návratnost)': [2.1, 4.5, 0.8, 5.2]}, index=['Facebook', 'Google Search', 'TikTok', 'E-mail']))

    with tab3:
        st.subheader("Web & UX: Proč uživatelé odcházejí?")
        st.write("AI prošlo data z Google Analytics a Hotjaru.")
        st.warning("📉 **Bounce Rate na produktové stránce 'Kategorie Y' je 78 %**")
        st.write("👉 **AI Zjištění:** Stránka se na mobilním 4G připojení načítá 6.8 sekundy. Obrázky nejsou optimalizované (mají přes 4 MB).")
        st.write("👉 **Akční krok pro vývojáře:** Zkonvertujte obrázky do formátu WebP a nasaďte lazy-loading. Očekávané zvýšení konverzí: + 0.5 %.")

    with tab4:
        st.subheader("CRM & Retence (LTV)")
        st.write("Získat nového klienta vás stojí 850 Kč (CAC). Musíte si je udržet.")
        st.success("🤝 **Retenční okno je otevřené**\n\nAI zjistilo vzorec: Lidé, kteří nakoupí 'Kávovar X', mají 60% šanci, že do 30 dnů koupí i filtry a zrnkovou kávu. **Ale vy jim žádný e-mail neposíláte!**")
        st.write("👉 **Akční krok pro marketing:** Spusťte automatický e-mail přesně 21 dní po nákupu kávovaru se slevou 10 % na zrnkovou kávu. Potenciál dodatečných tržeb: 45 000 Kč měsíčně.")

if st.session_state.page == 'landing':
    landing_page()
elif st.session_state.page == 'login':
    login_page()
elif st.session_state.page == 'dashboard':
    dashboard_page()