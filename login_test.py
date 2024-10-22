import requests
import argparse

print("██╗      ██████╗  ██████╗ ██╗███╗   ██╗    ████████╗███████╗███████╗████████╗")
print("██║     ██╔═══██╗██╔════╝ ██║████╗  ██║    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝")
print("██║     ██║   ██║██║  ███╗██║██╔██╗ ██║       ██║   █████╗  ███████╗   ██║   ")
print("██║     ██║   ██║██║   ██║██║██║╚██╗██║       ██║   ██╔══╝  ╚════██║   ██║   ")
print("███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║       ██║   ███████╗███████║   ██║   ")
print("╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝       ╚═╝   ╚══════╝╚══════╝   ╚═╝   ")
print("")
print("                             Writen by Single Core")
def hack_website(url, username, password):
    session = requests.Session()
    login_data = {
        'username': username,
        'password': password
    }
    response = session.post(url, data=login_data)
    
    if response.status_code == 200:
        print("Login successful!")
    else:
        print("Login failed.")

def main():
    parser = argparse.ArgumentParser(description='Hack a website')
    parser.add_argument('--url', help='URL of the website', required=True)
    parser.add_argument('--username', help='Username for login', required=True)
    parser.add_argument('--password', help='Password for login', required=True)
    
    args = parser.parse_args()
    
    hack_website(args.url, args.username, args.password)

if __name__ == '__main__':
    main()
