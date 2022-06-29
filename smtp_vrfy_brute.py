#!/usr/bin/python3
import socket
import sys
import re

if len(sys.argv)!=3:
    print("script.py <Target> <Username List>")
    print("Example: ./script.py 192.168.1.1 users.txt")

else:
    
    # Get lines of user_list in order to break while loop.
    with open(sys.argv[2], "r") as fp:
        for count, line in enumerate(fp):
            pass
    user_list_lines = count+1

    target = sys.argv[1]
    # open user_list outside before loop so disconnect will not reset list.
    user_list = open(sys.argv[2], "r")
    verified_users_list = []

    # Track loop count to display line of file nex to user being verified.
    count = 0
    
    # Continue bruteforce / reconnect to target in case of disconnect.
    while user_list_lines:    

        print(f"\nLines remaining in user list: {user_list_lines}")
        
        print(f"Connecting to: {sys.argv[1]}")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,25))
        response = s.recv(2048)
        print(f"Connect response: {response.decode()}")

        for user in user_list:
            user_list_lines -= 1
            try:
                vrfy_attempt = f"VRFY {user}"
                count += 1

                print(f"{count} | {vrfy_attempt.strip()}         ", end="\r")
                s.send(vrfy_attempt.encode())
                response = s.recv(2048)

                if re.search(r"^252", response.decode()):
                    print(f"+ Verified user: {user}", end="")
                    verified_users_list.append(user.strip())
                    verified_users_string = ", ".join(verified_users_list)
                    print(f"++ Verified users list: {verified_users_string}")

            except (ConnectionResetError, BrokenPipeError) as e:
                print("\n\n* Connection Lost - Reconnecting *")
                print(f"++ Verified users list: {verified_users_string}")
                break

    print("\nBruteforce Complete.")
    print(f"++ Verified users list: {verified_users_string}")
