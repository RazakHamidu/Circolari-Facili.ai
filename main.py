# Importa le librerie necessarie
import streamlit as st  # Per creare l'interfaccia utente
import pdfplumber
import os  # Per gestire i file e le variabili di ambiente
import google.generativeai as genai  # Per usare il modello generativo di Google
from dotenv import load_dotenv  # Per caricare le variabili di ambiente da un file .env

# Carica le variabili di ambiente dal file .env
load_dotenv()

# Imposta il titolo della pagina web
st.set_page_config(page_title="Circolari Facili")

st.title('Circolari Facili. ai 🏫📄')
st.subheader("Rendi le circolari scolastiche facili da comprendere  ")
# Recupera la chiave API per accedere al modello generativo di Google
GEMINI_API = os.getenv("GEMINI_API_KEY")

# Configura l'API di Google con la chiave recuperata
genai.configure(api_key=GEMINI_API)

# Crea una sezione per caricare un file PDF
uploaded_file = st.file_uploader("Carica il circolare", type=["pdf"])

# Se l'utente carica un file
if uploaded_file is not None:
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
           testo_pdf = page.extract_text()

  

    # Definisce le istruzioni per il modello generativo (comprimere il testo in modo semplice)
    prompt_system = """
    Prendi il contenuto di questo documento PDF e 
    trasformalo in un testo semplificato e chiaro. 
    Mantieni i punti principali, elimina i dettagli superflui e riorganizza 
    le informazioni in modo da renderle facilmente comprensibili per un 
    pubblico non esperto. Sottolinea i concetti fondamentali e, se necessario, 
    utilizza elenchi puntati per facilitare la lettura."
    Adatta il contenuto per un pubblico di studenti delle scuole superiori"""

    # Inizializza il modello generativo con il nome e le istruzioni
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=prompt_system)

    # Usa il modello per generare una versione semplificata del testo estratto dal PDF
    response = model.generate_content(f"{testo_pdf}")

    # Mostra il testo semplificato nell'interfaccia utente di Streamlit
    with st.container(border=True):
        st.markdown(response.text)  # Visualizza il testo semplificato
