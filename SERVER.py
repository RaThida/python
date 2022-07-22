import socket
import select
waiting_messages = []
users = []
def add_new_user(user_socket):
    new_socket, address = user_socket.accept()
    users.append(new_socket)
    print("A user has joined")
def remove_user(user_socket):
    users.remove(user_socket)
    print("a user has left")
def send_waiting_messages(wlist):
    for message in waiting_messages:
        receiving_socket, data = message
        if receiving_socket in wlist:
            receiving_socket.send(data)
            waiting_messages.remove(message)
def spread_messages(message, sending_user):
    receiving_list = users
    receiving_list.remove(sending_user)
    for user in receiving_list:
        waiting_messages.append((user, message))
    print("a user has sent a message")
def main():
    server_socket = socket.socket()
    server_socket.bind(('172.16.0.245',2004 ))
    server_socket.listen(4)
    while True:
        rlist, wlist, xlist = select .select([server_socket] + users, users, [])
        for current_socket in rlist:
            if current_socket is server_socket:
                add_new_user(server_socket)
            else:
                data = current_socket.recv(1024)
                if data == 'quit':
                    remove_user(current_socket)
                else:
                    spread_messages(data, current_socket)
        send_waiting_messages(wlist)
if __name__ == '__main__':
    main()
