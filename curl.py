import requests
r = requests.get('https://api.github.com/events')
print(r)
g=requests.post('https://httpbin.org/post',data={'key':'value'})
print(g)

payload={'key1':'value1','key2':'value2'}
r=requests.get('https://httpbin.org/get',params=payload)
print(r.url)

urllink='https://httpbin.org/get'
payload={'key1' : 'value1', 'key2':['value2','value3']}
r=requests.get(urllink,params=payload)
print(r.url)
