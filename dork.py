try:
    import requests
    from googlesearch import search
    from fake_useragent import UserAgent
    from requests import Timeout
    import random
except ModuleNotFoundError as e:
    import os
    if 'fake_useragent' in str(e):
        os.system('pip3 install fake_useragent')
    elif 'googlesearch' in str(e):
        os.system('pip3 install google')
    else:
        print(f"Module not found: {str(e)}")
        os.system('pip3 install requests')
save_as = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(12))+'.txt'
logo="""
________                __
\______ \   ___________|  | __ ___________________
 |    |  \ /  _ \_  __ \  |/ // __ \_  __ \___   /
 |    `   (  <_> )  | \/    <\  ___/|  | \//    /
/_______  /\____/|__|  |__|_ \\\\___  >__|  /_____ \\
        \/                  \/    \/            \/
"""
def enter(self):
    global dork
    for results in search(dork, num=int(1), stop=None, pause=1, start=0):
        try:
            headers = {"User-Agent": UserAgent().chrome}
            response = requests.get(results, headers=headers, timeout=9)
            print(str(response.status_code) + '-' + results)
            if response.status_code == 200:
                open(f'{save_as}', 'a').write(str(results)+'\n')
            else:
                pass
        except Timeout:
            print('Timeout' + '-' + results)
        except Exception as e:
            print(e)
    print(f"[+] Done, save as {save_as}!")
if __name__ == '__main__':
    print(logo)
    dork = input("[+] Insert Dork : ")
    print('\n')
    enter(dork)
