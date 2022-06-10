import socket,time



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1",1234))
server.listen(1)


user , adress = server.accept()


while True:
    
    data = user.recv(1024)
    
    print(data.decode("utf-8"))
    
    time.sleep(3)
    
    user.send(b"Back")
    
    
       
    

