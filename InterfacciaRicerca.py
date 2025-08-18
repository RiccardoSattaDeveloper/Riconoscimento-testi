import tkinter as tk # Libreria per creare interfacce grafiche.
import functools # Libreria per creare funzioni parziali con parametri preimpostati.
from GestoreDocumenti import GestoreDocumenti # Import della classe per gestire i documenti.

class InterfacciaRicerca:
    def __init__(self, gestore_documenti):
        self.gestore_documenti = gestore_documenti # Salva l'istanza di GestoreDocumenti.
        self.finestra = tk.Tk() # Crea la finestra principale Tkinter.
        self.finestra.title("Ricerca Documenti") # Imposta il titolo della finestra.
        self.frame_risultati = tk.Frame(self.finestra) # Frame dove saranno mostrati i risultati.
        self.crea_interfaccia() # Chiama il metodo per creare tutti i widget.

    def crea_interfaccia(self):
        frame_ricerca = tk.Frame(self.finestra) # Frame dedicato alla barra di ricerca.
        frame_ricerca.grid(sticky=tk.N, padx=10, pady=10) # Posizionamento del frame.

        tk.Label(frame_ricerca, text="Frase da cercare").grid(row=0, column=0, padx=5) # Etichetta per indicare il campo di ricerca.
        
        self.campo_ricerca = tk.Entry(frame_ricerca) # Campo di input per inserire la frase.
        self.campo_ricerca.grid(row=0, column=1, padx=5) # Posizionamento del campo di input.
        
        tk.Button(frame_ricerca, text="Trova", command=self.mostra_risultati).grid(row=1, columnspan=2, pady=5) # Pulsante per avviare la ricerca.

        self.frame_risultati.grid(row=0, column=2, padx=20, sticky=tk.N) # Frame per visualizzare i risultati della ricerca.

    def mostra_risultati(self):
        for widget in self.frame_risultati.winfo_children(): # Cancella i widget precedenti nel frame dei risultati.
            widget.destroy() 

        frase = self.campo_ricerca.get() # Legge la frase inserita dall'utente.
        risultati = self.gestore_documenti.cerca_frase(frase) # Cerca la frase nei documenti.

        if risultati: # Se ci sono risultati.
            for indice, nome_file in enumerate(risultati): # Cicla sui documenti trovati.
                apri_file = functools.partial(self.gestore_documenti.apri_documento, nome_file) # Crea un pulsante per aprire ciascun documento trovato.
                tk.Button(self.frame_risultati, text=nome_file, command=apri_file).grid(row=indice, sticky="w") # Posiziona il pulsante nel frame.
        else:
            tk.Label(self.frame_risultati, text="Nessun documento trovato", font=(None, 14, "bold")).grid() # Messaggio se nessun documento contiene la frase.

    def avvia(self):
        self.finestra.mainloop() # Avvia il loop principale di Tkinter, mantenendo la finestra aperta.