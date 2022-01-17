import socket
import json
import sys

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233
NOME=""

print('Connessione in corso')
try:
  ClientSocket.connect((host, port))
except socket.error as e:
  print(str(e))

Response = ClientSocket.recv(1024)
while True:
  print("Inserisci il tuo nickname")
  nome=input(">>>")
  data={'messaggio':nome,'nome':NOME}
  data=json.dumps(data)
  ClientSocket.send(str.encode(data))
  Response = ClientSocket.recv(1024)
  data=Response.decode('utf-8')
  data=json.loads(data)
  if data['nome']!="":
    print(data['messaggio'])
    print(data)
    NOME=data['nome']
    break
  else:
    print(data['messaggio'])
while True:
  # msg = input('>>>')
  try:
    # data={'messaggio':msg,'nome':NOME}
    # data=json.dumps(data)
    # ClientSocket.send(str.encode(data))
    Response = ClientSocket.recv(1024)
    data=Response.decode('utf-8')
    data=json.loads(data)
    print(f"{data['nome']}:{data['messaggio']}")
  except KeyboardInterrupt:
    print("Dentro")
    sys.exit(0)
ClientSocket.close()