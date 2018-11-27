import urllib.parse
import urllib.request

def generate_url(host,param):
    for k, v in param.items():
        param[k] = urllib.parse.quote(str(v))
    return (host+'?'+'&'.join(list(map(lambda key: "%s=%%(%s)s"%(key,key),param.keys()))))%param 

def request_get(host, param):
    url = generate_url(host, param)
    with urllib.request.urlopen(url) as f:
        html_doc = b''.join(f.readlines())
        return html_doc