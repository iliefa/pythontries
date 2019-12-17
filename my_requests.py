import requests

env=['skill-edge','integration','staging','prod']
skill=['skill-tv','skill-ecare']
def check_health(x,y):
    r=requests.get("https://"+x+"-g8s.djingo.ext.fti.net/v1/"+y+"/info")
    return(r.status_code)
for i in env:
    for j in skill:
        print(check_health(i,j))