try:
    import requests
    import googlesearch
    from googlesearch import search
    import fake_useragent
    from fake_useragent import UserAgent
    from requests import Timeout
except ModuleNotFoundError as e:
    import os
    if 'fake_useragent' in str(e):
        os.system('pip3 install fake_useragent')
    elif 'googlesearch' in str(e):
        os.system('pip3 install google')
    else:
        print(f"Module not found: {str(e)}")
        os.system('pip3 install requests')
logo="""
,------.                ,--.                         
|  .-.  \  ,---. ,--.--.|  |,-. ,---. ,--.--.,-----. 
|  |  \  :| .-. ||  .--'|     /| .-. :|  .--'`-.  /  
|  '--'  /' '-' '|  |   |  \  \\\\   --.|  |    /  `-. 
`-------'  `---' `--'   `--'`--'`----'`--'   `-----' 
"""
def enter(self):
    global dork
    for results in search(dork, num=int(1), user_agent=UserAgent().chrome, stop=None, pause=1, start=0):
        try:
            headers = {"User-Agent": UserAgent().chrome}
            response = requests.get(results, headers=headers, timeout=9)
            print(str(response.status_code) + '-' + results)
        except Timeout:
            print('Timeout' + '-' + results)
        except Exception as e:
            print(e)
    print("Done..")
if __name__ == '__main__':
    print(logo)
    dork = input("[+] Insert Dork : ")
    print('\n')
    enter(dork)
