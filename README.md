# SMTP-VRFY-Bruteforce
Bruteforce a user list against SMPT using VRFY

```bash
python smtp_vrfy_brute.py 10.129.80.226 xato-net-10-million-usernames.txt

Lines remaining in user list: 8295455
Connecting to: 10.129.80.226
Connect response: 220 debian.localdomain ESMTP Postfix (Debian/GNU)

+ Verified user: michael 
++ Verified users list: michael
23 | VRFY james           

* Connection Lost - Reconnecting *
++ Verified users list: michael

Lines remaining in user list: 8295432
Connecting to: 10.129.80.226
Connect response: 220 debian.localdomain ESMTP Postfix (Debian/GNU)

+ Verified user: mail    
++ Verified users list: michael, mail
46 | VRFY joseph          

* Connection Lost - Reconnecting *
++ Verified users list: michael, mail
      
```
