# Echo server program
import socket
import threading
import time
from multiprocessing import Process

#server = '192.168.0.1'
server = '' # bilo koja adresa
port = 50005
allConnections = []

def fnc():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((server, port))
        s.listen(2)
        print("Waiting for a connection, Server Started")
        ocekivano_clienta = 2
        num_of_connected_clients = 0
        cl_counter = 0
        while num_of_connected_clients != ocekivano_clienta:
            conn, addr = s.accept()
            print("Connected to:", addr)
            allConnections.append(conn)
            cl_counter += 1
            #id_of_client = allConnections[num_of_connected_clients].recv(2048).decode()
            if cl_counter == 1:
                print("connectovan prvi client")
                you_are_first = "1"
                allConnections[0].sendall(you_are_first.encode('utf8'))
            #print(id_of_client)
            if cl_counter == 2:
                print("connected second")
                wait = "go"
                second = "2"
                allConnections[1].sendall(second.encode('utf8'))
                allConnections[0].sendall(wait.encode('utf8'))
                allConnections[1].sendall(wait.encode('utf8'))

                #t1 = threading.Thread(name="Hello1", target=recevee)  # tell thread what the target function is
                #t1.start()  # tell the thread to execute the target
                #t12 = threading.Thread(name="Hello1", target=recevee2)  # tell thread what the target function is
                #t12.start()  # tell the thread to execute the target
                start_processing_data(allConnections)

                while True:
                    #da se main ne zavrsi
                    marko = "tatic"
                    #print(marko)
                    time.sleep(5)

            num_of_connected_clients += 1

def start_processing_data(connections_process):
    recv_process_client1 = Process(target=recevee, args=(connections_process[0], connections_process[1]))
    recv_process_client2 = Process(target=recevee2, args=(connections_process[1], connections_process[0]))

    recv_process_client1.start()
    recv_process_client2.start()


def recevee(client1, client2):
    while True:
        message_is = client2.recv(2048).decode()
        client1.sendall(message_is.encode('utf8'))
        client2.sendall(message_is.encode('utf8'))

def recevee2(client2, client1):
    while True:
        message_is = client1.recv(2048).decode()
        client1.sendall(message_is.encode('utf8'))
        client2.sendall(message_is.encode('utf8'))

if __name__ == '__main__':
    fnc()

