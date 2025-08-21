import glob 
import os
import sys

class GestoreDocumenti:
    def __init__(self, percorso_cartella):
        self.percorso_cartella = percorso_cartella 
        self.documenti = {} 
        self.documenti_trovati = []
        self.carica_documenti()

    def carica_documenti(self):
        os.chdir(self.percorso_cartella) 
        for nome_file in glob.glob("*.txt"): 
            with open(nome_file, "r", encoding="utf-8", errors="ignore") as f: 
                testo = f.read().lower()
                self.documenti[nome_file] = testo 

    def cerca_frase(self, frase):
        frase = frase.lower()
        self.documenti_trovati.clear()
        for nome_file, testo in self.documenti.items(): 
            if frase in testo: 
                self.documenti_trovati.append(nome_file) 
        return self.documenti_trovati 

    @staticmethod
    def apri_documento(nome_file):
        if sys.platform.startswith("linux"): 
            os.system(f"xdg-open '{nome_file}' &")
        elif sys.platform.startswith("win"):
            os.startfile(nome_file) 
        elif sys.platform.startswith("darwin"):
            os.system(f"open '{nome_file}' &")
