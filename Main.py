from GestoreDocumenti import GestoreDocumenti # Importa la classe per gestire i documenti.
from InterfacciaRicerca import InterfacciaRicerca # Importa la classe per l’interfaccia grafica di ricerca.

percorso_documenti = "/home/ricky/Scrivania/Riconoscimento testi/Testi di Fabrio De Andrè" # Percorso della cartella con i documenti.

gestore = GestoreDocumenti(percorso_documenti) # Crea un’istanza del gestore dei documenti caricando i file.

interfaccia = InterfacciaRicerca(gestore) # Crea l’interfaccia grafica passando il gestore dei documenti.

interfaccia.avvia() # Avvia l’interfaccia grafica, mostrando la finestra all’utente.