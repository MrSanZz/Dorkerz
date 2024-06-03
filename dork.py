try:
    import requests
    import googlesearch
    from googlesearch import search
    import fake_useragent
    from fake_useragent import UserAgent
    from requests import Timeout
except ModuleNotFoundError:
    import os
    os.system("pip3 install fake_useragent && pip3 install google")
logo="""
,------.                ,--.                         
|  .-.  \  ,---. ,--.--.|  |,-. ,---. ,--.--.,-----. 
|  |  \  :| .-. ||  .--'|     /| .-. :|  .--'`-.  /  
|  '--'  /' '-' '|  |   |  \  \\\   --.|  |    /  `-. 
`-------'  `---' `--'   `--'`--'`----'`--'   `-----' 
"""
ua = UserAgent()
def enter(self):
    for results in search(dork, num=int(2), user_agent=ua.chrome, stop=None, pause=2, start=0):
        try:
            headers = {"User-Agent": ua.chrome}
            response = requests.get(results, headers=headers, timeout=9)
            print(str(response) + '-' + results)
        except Timeout:
            print('Timeout' + '-' + results)
        except:
            continue
    print("Done..")
if __name__ == '__main__':
    print(logo)
    global dork
    dork = input("[+] Insert Dork : ")
    print('\n')
    enter(dork)
