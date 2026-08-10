from bank import Bank

# Funzione aiutante per gestire gli errori di digitazione sui numeri
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\n>>> Errore: Inserisci un importo numerico valido (es. 10 o 50.50).")

def main():
    bank = Bank("Tech Bank")
    
    while True:
        print(f"\n{'='*10} BENVENUTO IN {bank.name.upper()} {'='*10}")
        print("1. Apri un nuovo conto")
        print("2. Visualizza Saldo")
        print("3. Fai un Versamento")
        print("4. Fai un Prelievo")
        print("5. Esci")
        
        scelta = input("\nSeleziona un'operazione (1-5): ")
        
        if scelta == '1':
            tipo = input("Tipo di conto (savings/checking): ")
            num = input("Numero conto (es. S123): ")
            nome = input("Nome intestatario: ")
            pin = input("Imposta un PIN segreto (es. 1234): ")
            success, msg = bank.create_account(tipo, num, nome, pin)
            print(f"\n>>> {msg}")
            
        elif scelta == '2':
            num = input("Numero conto: ")
            conto = bank.get_account(num)
            if conto:
                print(f"\n>>> Saldo attuale di {conto.owner_name}: ${conto.get_balance():.2f}")
            else:
                print("\n>>> Errore: Conto non trovato.")
                
        elif scelta == '3':
            num = input("Numero conto: ")
            conto = bank.get_account(num)
            if conto:
                # Usiamo la nostra nuova funzione blindata per l'input
                importo = get_float_input("Importo da versare: ")
                success, msg = conto.deposit(importo)
                bank.save_data() 
                print(f"\n>>> {msg}")
            else:
                print("\n>>> Errore: Conto non trovato.")
                
        elif scelta == '4':
            num = input("Numero conto: ")
            conto = bank.get_account(num)
            if conto:
                # Usiamo la nostra nuova funzione blindata per l'input
                importo = get_float_input("Importo da prelevare: ")
                pin = input("Inserisci il tuo PIN: ")
                success, msg = conto.withdraw(importo, pin)
                if success:
                    bank.save_data() 
                print(f"\n>>> {msg}")
            else:
                print("\n>>> Errore: Conto non trovato.")
                
        elif scelta == '5':
            print("\nGrazie per aver scelto i nostri servizi. Arrivederci!\n")
            break
            
        else:
            print("\n>>> Scelta non valida, riprova.")

if __name__ == "__main__":
    main()