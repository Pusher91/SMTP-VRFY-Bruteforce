# SMTP-VRFY-Bruteforce
Enumerate users using SMTP's VRFY command

If the connection is lost (i.e. the target drops the connection after too many attempts) it will reconnect and continue bruteforcing where it left off.

Generates output file automatically.

```console
python smtp_vrfy_brute.py 10.129.80.226 xato-net-10-million-usernames.txt

Lines remaining in user list: 8295455
Connecting to: 10.129.80.226
Connection response: 220 debian.localdomain ESMTP Postfix (Debian/GNU)

+ Verified user: michael 
++ Verified users list: michael
23 | VRFY james           

* Connection Lost - Reconnecting *
++ Verified users list: michael

Lines remaining in user list: 8295432
Connecting to: 10.129.80.226
Connection response: 220 debian.localdomain ESMTP Postfix (Debian/GNU)

+ Verified user: mail    
++ Verified users list: michael, mail
46 | VRFY joseph          

* Connection Lost - Reconnecting *
++ Verified users list: michael, mail

Lines remaining in user list: 8295409
Connecting to: 10.129.80.226
^CTraceback (most recent call last):
  File "/home/kali/Documents/htb/Trick/smtp_vrfy_brute.py", line 36, in <module>
    response = s.recv(2048)
KeyboardInterrupt

```


##Output File
```console
cat smtp-vrfy-bruteforce.out      
Target: 10.129.80.226
Wordlist used: xato-net-10-million-usernames.txt
Target header: 220 debian.localdomain ESMTP Postfix (Debian/GNU)

Verified Users:
michael
mail
```
