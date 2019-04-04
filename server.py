import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def check_in_file(data):
    freq = {}
    buffer= open('server_file.txt','r')
    file_map={}

    # line= 'This is a server'
    for line in buffer.read().split():
        if line in file_map:
            file_map[line]+=1
        else:
            file_map[line]=1

    for word in data:
        if word in file_map.keys():
            freq[word]=file_map.get(word)
        else:
            freq[word]=0

    return freq

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = ((conn.recv(1024)).decode('ascii')).split()
            if not data:
                break
            freq = bytes(str(check_in_file(data)),'utf-8')
            conn.sendall(freq)
