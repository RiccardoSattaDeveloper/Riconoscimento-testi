from GestoreDocumenti import GestoreDocumenti 
from InterfacciaRicerca import InterfacciaRicerca 

percorso_documenti = "/home/ricky/Scrivania/Riconoscimento testi/Testi di Fabrio De Andrè" 

gestore = GestoreDocumenti(percorso_documenti) 

interfaccia = InterfacciaRicerca(gestore) 

interfaccia.avvia()
