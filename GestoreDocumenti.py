import glob # Libreria per cercare file con pattern.
import os # Libreria per interagire con il sistema operativo.
import sys # Libreria per rilevare il sistema operativo in uso.

class GestoreDocumenti:
    def __init__(self, percorso_cartella):
        self.percorso_cartella = percorso_cartella # Salva il percorso della cartella dei documenti.
        self.documenti = {} # Dizionario dove chiave = nome file, valore = testo in minuscolo.
        self.documenti_trovati = [] # Lista dei documenti che contengono la frase cercata.
        self.carica_documenti() # Carica subito i documenti presenti nella cartella.

    def carica_documenti(self):
        os.chdir(self.percorso_cartella) # Cambia la cartella corrente a quella dei documenti.
        for nome_file in glob.glob("*.txt"): # Cicla su tutti i file con estensione .txt.
            with open(nome_file, "r", encoding="utf-8", errors="ignore") as f: # Apre il file in lettura ignorando eventuali errori.
                testo = f.read().lower() # Legge tutto il testo e lo converte in minuscolo.
                self.documenti[nome_file] = testo # Salva il testo nel dizionario con chiave = nome file.

    def cerca_frase(self, frase):
        frase = frase.lower() # Converte la frase da cercare in minuscolo.
        self.documenti_trovati.clear() # Pulisce la lista dei documenti trovati in precedenza.
        for nome_file, testo in self.documenti.items(): # Cicla su ogni documento caricato.
            if frase in testo: # Controlla se la frase è presente nel testo.
                self.documenti_trovati.append(nome_file) # Aggiunge il nome del file alla lista dei documenti trovati.
        return self.documenti_trovati # Restituisce la lista dei documenti contenenti la frase.

    @staticmethod
    def apri_documento(nome_file):
        if sys.platform.startswith("linux"): # Controlla se il sistema operativo è Linux.
            os.system(f"xdg-open '{nome_file}' &") # Apre il file usando il comando Linux.
        elif sys.platform.startswith("win"): # Controlla se il sistema operativo è Windows.
            os.startfile(nome_file) # Apre il file usando il comando Windows.
        elif sys.platform.startswith("darwin"): # Controlla se il sistema operativo è macOS.
            os.system(f"open '{nome_file}' &") # Apre il file usando il comando macOS.