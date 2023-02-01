import time
from pythonosc.udp_client import SimpleUDPClient
IP, PORT = "127.0.0.1", 9000
client = SimpleUDPClient(IP, PORT) 

pw1 = 12
pw2 = 34
pw3 = 56

if __name__ == '__main__':
   
    while True:

        client.send_message(f'/avatar/parameters/TRI_Pwd', pw1)
        time.sleep(0.5)
        client.send_message(f'/avatar/parameters/TRI_Pwd', pw2)
        time.sleep(0.5)
        client.send_message(f'/avatar/parameters/TRI_Pwd', pw3)
        time.sleep(0.5)
    else:
        print('xd')
        

