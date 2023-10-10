import requests
import json




class RequestUtil:
    session = requests.session()

    # 发送请求
    def send_requests(self, method, url, headers, data, **kwargs):
        method = str(method).lower()
        rep = None

        if method == 'get':
            rep = RequestUtil.session.request(method=method,url=url,params=data,**kwargs)
        else:
            data = json.dumps(data)
            rep = RequestUtil.session.request(method=method,data=data,url=url,headers=headers,**kwargs)

        return rep.text



