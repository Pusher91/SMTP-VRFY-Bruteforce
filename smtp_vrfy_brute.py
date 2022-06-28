import socket
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

    count = 0
    for user in user_list:
        try:
            vrfy_attempt = f"VRFY {user}"
            count += 1

            print(f"{count} | {vrfy_attempt.strip()}               ", end="\r")
            s.send(vrfy_attempt.encode())
            response = s.recv(2048)

            if re.search(r"^252", response.decode()):
                print(f"+ Verified user: {response.decode()}", end="")

        except (ConnectionResetError, BrokenPipeError) as e:
            print(f"\n\n* ConnectionResetError encountered - script unable to complete")
            raise SystemExit()

    print("\nBruteforce Complete.")
