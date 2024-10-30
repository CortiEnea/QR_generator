# Generatore di QR

Il progetto generatore di QR è basato su Flask e come dice il nome,  serve per generare un codice QR con possibilità di personalizzare i seguenti punti:

- Link, ovvero l'indirizzo a cui punta il codice QR
- Colore di sfondo e colore dell'interno
- Immagine, sarà possibile inserire un'immagine al centro del codice

Inoltre, eseguendo l'accesso al sito, sarà possibile visualizare la storia di tutti i QR generati e vederne le specifiche.

## Configurazione:

Dopo aver scaricato il repository verificare quanto segue:

- Tramite il comando  ```pip install -r requirements.txt ``` sarà possibile installare i moduli necessari

- Verificare la presenza della cartella ```"./static```ovvero la cartella nella quale verranno salvate le immagini

- ### Creare il file .env:

    Nella cartella del progetto va creato il file .env, nel quale verranno salvate le informazioni relative alla connessiona a DB e la nostra secret key.
    
    All'interno del file aggiungere quindi:
    
    SECRET_KEY = 'inserire la propria secret key'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://nome_utente:password@localhost/nome_db'