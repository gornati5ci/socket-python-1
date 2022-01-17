import socket
import os
import json
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
nomi=[]
ServerSocket.listen(5)


def threaded_client(connection):
  connection.send(str.encode('Welcome to the Servern'))
  while True:
    data = connection.recv(2048)
    print(data)
    if not data:
      break
    data=json.loads(data)
    if data['messaggio']=="stop()":
      os._exit(0)
    if data['nome']=="":
      if data['messaggio'] in nomi:
        data={'messaggio':"Nome già preso",'nome':''}
      else:
        data={'messaggio':"Benvenuto",'nome':data['messaggio']}
        nomi.append(data['nome'])
      data=json.dumps(data)
      connection.send(str.encode(data))
      continue
    data=json.dumps(data)
    for client in clients:
      try:
        client.send(str.encode(data))
      except:
        pass
  connection.close()
clients=[]
while True:
  Client, address = ServerSocket.accept()
  clients.append(Client)
  print('Connected to: ' + address[0] + ':' + str(address[1]))
  start_new_thread(threaded_client, (Client, ))
  ThreadCount += 1
  print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()