import requests
r = requests.get('https://api.github.com/events')
print (r.json)

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("https://httpbin.org/post", data=payload)
print (r.text)

r = requests.get('https://skill-edge-g8s.djingo.ext.fti.net/v1/skill-tv/info')
print(r.status_code)
print(r.headers['Content-Type'])


env=['skill-edge','integration','staging','prod']
skill=['skill-tv','skill-ecare']
def check_health(x,y):
    r=requests.get("https://"+x+"-g8s.djingo.ext.fti.net/v1/"+y+"/info")
    return(r.status_code)
 
if __name__=="__main__":
        print("test basic health requests")