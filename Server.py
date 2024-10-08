import requests
import socket

def register_client(server_url,nickname,port=12345):
    URL=f"{server_url}/connect"
    params={'nickname':nickname,'port':port}

    response=requests.get(URL,params=params)

    if response.status_code == 200:
        print("Registered")
    else:
        print("Failed to register")


def list_device(server_url):
    URL=f"{server_url}/list"
    response=requests.get(URL)
    if response.status_code==200:
        return response.json()
    else:
        return {}


def connectTo(devices,target):
    try:
        target_ip,target_port=devices[target][0],int(devices[target][1])
        print(f"{target}--{target_ip}:{target_port}")
        client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect((target_ip,target_port))

        message=input("You: ")
        client_socket.send(message.encode())

        response=client_socket.recv(1024).decode()
        print(f"{target}: {response}")
        client_socket.close()
    except Exception as e:
        print(f"Error: {e}")

def unregister(server,nickname):
    URL=f"{server}/unregister"
    params={'nickname':nickname}
    response=requests.get(URL,params=params)

    if response.status_code == 200:
        print("Unregistered")
    else:
        print('error')


server='http://127.0.0.1:5000'
choice=''
nickname=input("Enter your username")
register_client(server,nickname)
while choice != 'exit':
    devices=list_device(server)['devices']
    print(devices)    
    choice=input("Enter Choice \n1. List of connected devices \n2. Connect to User\n")
    if choice.lower() == 'list' or choice == '1':
        print(devices)
    if choice.lower() == 'connect' or choice == '2':
        target=input("Enter the username of the device you want to connect to")
        connectTo(devices,target)
