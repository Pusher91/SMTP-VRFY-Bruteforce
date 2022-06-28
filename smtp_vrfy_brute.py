import socket
import os
import sys
import re

if len(sys.argv)!=3:
    print("script.py <Target> <Username List>")
    print("Example: ./script.py 192.168.1.1 users.txt")

else:
    target = sys.argv[1]
    user_list = open(sys.argv[2], "r")
    
    print(f"\nConnecting to {sys.argv[1]}")
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,25))
    response = s.recv(2048)
    
    print(f"Connect response: {response.decode()}")

    for user in user_list:
        print(f"Verifying: {user.strip()}               ", end="\r")
        vrfy_attempt = (f"VRFY " + user).encode()
        s.send((f"VRFY " + user).encode())
        response = s.recv(2048)

        if re.search(r"^252", response.decode()):
            print(f"Verified user: {response.decode()}", end="")

    print("\nBruteforce Complete.")
