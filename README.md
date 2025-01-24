
# Circolari Facili.ai

## Problema

Le circolari scolastiche sono spesso difficili da capire perché usano un linguaggio complicato e tecnico. Questo può confondere gli studenti, che non riescono a capire bene le informazioni importanti.

## Soluzione

**Circolari Facili.ai** è un'app che usa l'intelligenza artificiale per leggere le circolari scolastiche e trasformarle in versioni più semplici. In questo modo, gli studenti riescono a capire facilmente cosa c'è scritto senza perdere informazioni importanti.

---

## Funzionalità principale

- **Semplificazione dei PDF**: L'app legge i file PDF delle circolari e li trasforma in versioni semplificate e facilmente comprensibili.

---

Ecco una proposta di documentazione per il tuo progetto da caricare su GitHub:

---

## Struttura del progetto

```
.
├── .streamlit/      # Configurazione specifica di Streamlit
├── .env             # File di configurazione delle variabili d'ambiente
└── main.py          # Script principale dell'applicazione Streamlit
```

---

## Requisiti

Per eseguire il progetto, assicurati di avere installati i seguenti strumenti:

- **Python 3.8+**
- **Streamlit** (ultima versione)
- **pip** (per la gestione dei pacchetti Python)

---

## Installazione

1. Clona il repository:

   ```bash
   git clone https://github.com/tuo-utente/circolari-facili-ai.git
   cd circolari-facili-ai
   ```

2. Crea un ambiente virtuale:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Per macOS/Linux
   venv\Scripts\activate     # Per Windows
   ```

3. Installa le dipendenze richieste:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura le variabili d'ambiente nel file `.env`. Esempio di configurazione:

   ```
   GEMINI_API_KEY=tuo_api_key
   OTHER_CONFIG=valore
   ```

---

## Come eseguire il progetto

Esegui il file principale con Streamlit:

```bash
streamlit run main.py
```

L'app sarà accessibile nel tuo browser all'indirizzo `http://localhost:8501`.

---

## Configurazione di Streamlit

Il progetto utilizza il file `.streamlit/config.toml` per personalizzare l'aspetto e il comportamento dell'app. Ecco un esempio di configurazione:

```toml
[theme]
primaryColor = "#6c5ce7"
backgroundColor = "#f1f2f6"
textColor = "#2f3542"
font = "sans serif"
```

## Licenza

Questo progetto è distribuito sotto la licenza [MIT](LICENSE).

--- 

Fammi sapere se vuoi aggiungere sezioni specifiche!
