# 🏦 Python OOP Banking System

Un sistema bancario interattivo e completo sviluppato in Python, basato rigorosamente sui paradigmi della Programmazione Orientata agli Oggetti (OOP). Questo progetto simula le operazioni di un vero sportello bancomat (ATM), garantendo la persistenza dei dati e controlli di sicurezza sugli accessi.

## 🚀 Funzionalità Principali

* **Gestione Multi-Conto**: Architettura espandibile con supporto per conti Corrente (*Checking*) e Risparmio (*Savings*), sfruttando l'ereditarietà e il polimorfismo.
* **Operazioni Transazionali**: Esecuzione sicura di versamenti, prelievi e trasferimenti diretti tra conti diversi.
* **Sicurezza e Autenticazione**: Implementazione di un sistema di blocco tramite PIN segreto richiesto per autorizzare le operazioni in uscita (prelievi e bonifici).
* **Persistenza dei Dati**: Salvataggio automatico dello stato della banca, dei saldi e dello storico completo delle transazioni all'interno di un database `JSON` locale.
* **Validazione Input**: Interfaccia utente a prova di crash (gestione strutturata delle eccezioni tramite blocchi `try-except` per prevenire input non validi).

## 🛠️ Tecnologie Utilizzate

* **Linguaggio**: Python 3
* **Architettura**: Object-Oriented Programming (OOP)
* **Storage**: JSON (Libreria nativa `json`, `os`)
* **Controllo Versione**: Git & GitHub

## 💻 Come testare il progetto in locale

1. Clona la repository sul tuo computer:
   ```bash
   git clone https://github.com/davidegalano05-design/Banking-System.git
