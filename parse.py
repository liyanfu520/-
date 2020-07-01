from retrying import retry
import requests

#headers={"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.116 Mobile Safari/537.36"
}

@retry(stop_max_attempt_number=3)#让被装饰的函数反复执行三次，
def _parse_url(url):
    # reponse=requests.get(url,headers=headers)
    reponse=requests.post(url,headers=headers)
    return reponse.content.decode('utf-8')

def parse_url(url):
    try:
        html=_parse_url(url)
        return html
    except:
        return "None"