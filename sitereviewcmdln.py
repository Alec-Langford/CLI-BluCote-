import sys, os, bs4, simplejson
import requests, time,urlparse


def check(x):
    "string"
    url = "http://sitereview.bluecoat.com/rest/categorization"
    payload = {'url': x}
    headers = {'Referer': 'http://www.sitereview.bluecoat.com/siterevew.jsp'}
    r = requests.post(url, data=payload, headers=headers)


    i = simplejson.loads(r.content)
    try:
        b = bs4.BeautifulSoup(i["categorization"]).get_text()
        return (i["url"] + ": " + b )
    except KeyError:
        return r.content


def gsb_check(x):
    if "http" not in x:
        x="http%3A%2F%2F"+x
    url="https://sb-ssl.google.com/safebrowsing/api/lookup?client=demo-app&key=AIzaSyD3kccdlWrye4B_3-PV7sz_DazUOTugZmI&appver=1.5.2&pver=3.1&url="+"%s"%x
    r=requests.get(url)
    return bool(r.text)




if __name__ == "__main__":
    t=sys.argv[-1]
    if os.path.isfile(t):
        c=[urlparse.urlparse(item.lower().replace("hxxp","http").strip()).hostname for item in open(t, "r").readlines()]
        for item in set(c):
            print check(item)
            time.sleep(2)

    else:
        print check(t)