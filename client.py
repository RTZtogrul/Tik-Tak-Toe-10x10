import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1",1234))



while True:
    
    client.send("qffq".encode("utf-8"))
    
    data = client.recv(1024)
    
    
    print(data.decode("utf-8"))
    
    time.sleep(1)
    
    
    