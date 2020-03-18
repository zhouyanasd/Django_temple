import requests
import json
from mysite.settings import LOCAL_SEVER_ADDRESS,DEFAULT_PORT


class APIRequest(object):
    def __init__(self, url, parms, type):
        self.url = url
        self.parms = parms
        self.type = type
        self.IP = LOCAL_SEVER_ADDRESS+DEFAULT_PORT
        print(self.IP)

    def request(self):
        headers = {
            'User-agent': 'none/ofyourbusiness',
            'Spam': 'Eggs'
        }
        if self.type =='GET':
            resp = requests.get(self.IP+self.url)
        elif self.type == 'POST':
            print(self.IP+self.url)
            resp = requests.post(self.IP+self.url, data=self.parms, headers=headers)
        else:
            resp = None
        # Decoded text returned by the request
        text = resp.text
        data = json.loads(text)
        return data
