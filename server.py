import socket
import virtual


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1",1234))
server.listen(1)

user , adress = server.accept()

game = virtual.Game(mass)





    
    
       
    

