import socket
import json

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def inserimento(testo):
  print(testo)
  valore=input(">>>")
  return valore

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  while True:
    # Prendo il primo numero
    primoNumero=inserimento("Inserisci il primo numero. exit() per uscire")
    # Controllo se l'utente vuole uscire. In questo caso esco dal ciclo while. Il client chiuderà la connessione uscendo dal with
    if primoNumero=="exit()":
      break
    # Converto a float
    primoNumero=float(primoNumero)
    # Inserimento altri parametri
    operazione=inserimento("Inserisci l'operazione(+,-,*,/,%)")
    secondoNumero=float(inserimento("Inserisci il secondo numero"))
    # Preparo il messaggio. Attenzione al dumps
    messaggio=json.dumps({'primoNumero':primoNumero,'operazione':operazione,'secondoNumero':secondoNumero})
    # Invio il messaggio. Attenzione all'encode
    s.sendall(messaggio.encode("UTF-8"))
    # Aspetto la risposta del server
    data = s.recv(1024)
    # Stampo la risposta del server
    print('Risultato:', data.decode())