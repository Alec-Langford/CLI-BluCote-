import sys, os, bs4, simplejson
import requests, time


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

if __name__ == "__main__":
    t=sys.argv[-1]
    if os.path.isfile(t):
        for item in open(t, "r").readlines():
            print check(item)
            time.sleep(2)

    else:
        print check(t)