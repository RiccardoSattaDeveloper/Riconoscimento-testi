import tkinter as tk 
import functools
from GestoreDocumenti import GestoreDocumenti 

class InterfacciaRicerca:
    def __init__(self, gestore_documenti):
        self.gestore_documenti = gestore_documenti 
        self.finestra = tk.Tk()
        self.finestra.title("Ricerca Documenti") 
        self.frame_risultati = tk.Frame(self.finestra) 
        self.crea_interfaccia() 
        
    def crea_interfaccia(self):
        frame_ricerca = tk.Frame(self.finestra) 
        frame_ricerca.grid(sticky=tk.N, padx=10, pady=10)

        tk.Label(frame_ricerca, text="Frase da cercare").grid(row=0, column=0, padx=5) 
        
        self.campo_ricerca = tk.Entry(frame_ricerca)
        self.campo_ricerca.grid(row=0, column=1, padx=5)
        
        tk.Button(frame_ricerca, text="Trova", command=self.mostra_risultati).grid(row=1, columnspan=2, pady=5) 

        self.frame_risultati.grid(row=0, column=2, padx=20, sticky=tk.N) 

    def mostra_risultati(self):
        for widget in self.frame_risultati.winfo_children():
            widget.destroy() 

        frase = self.campo_ricerca.get()
        risultati = self.gestore_documenti.cerca_frase(frase) 

        if risultati: 
            for indice, nome_file in enumerate(risultati): 
                apri_file = functools.partial(self.gestore_documenti.apri_documento, nome_file) 
                tk.Button(self.frame_risultati, text=nome_file, command=apri_file).grid(row=indice, sticky="w") 
        else:
            tk.Label(self.frame_risultati, text="Nessun documento trovato", font=(None, 14, "bold")).grid() 

    def avvia(self):
        self.finestra.mainloop()
