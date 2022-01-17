import socket
import json

HOST = '127.0.0.1'  # Indirizzo dell'interfaccia standard di loopback (localhost)
PORT = 65432        # Porta di ascolto, la lista di quelle utilizzabili parte da >1023)

def eseguiCalcolo(data):
  primoNumero=data['primoNumero']
  operazione=data['operazione']
  secondoNumero=data['secondoNumero']
  if operazione=="+":
    return str(primoNumero+secondoNumero)
  elif operazione=="-":
    return str(primoNumero-secondoNumero)
  elif operazione=="*":
    return str(primoNumero*secondoNumero)
  elif operazione=="/":
    if secondoNumero==0:
      return "Non puoi dividere per 0"
    else:
      return str(primoNumero/secondoNumero)
  elif operazione=="%":
    return str(primoNumero%secondoNumero)
  return "Operazione non riconosciuta"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  print("[*] In ascolto su %s:%d" % (HOST, PORT))
  clientsocket, address = s.accept()
  with clientsocket as cs:
      print('Connessione da', address)
      while True:
          data = cs.recv(1024) # Attendo che il server riceva le informazioni
          # Se il server riceve un vettore vuoto presume che il client si sia disconnesso
          if not data:
            break
          # Decodifico il vettore di byte ricevuto dal client
          data=data.decode()
          # Trasformo da stringa a json
          data=json.loads(data)
          # Eseguo i calcoli.
          ris=eseguiCalcolo(data)
          # Restituisco la stringa
          cs.sendall(ris.encode("UTF-8"))