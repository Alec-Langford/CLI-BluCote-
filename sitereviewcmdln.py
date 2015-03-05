#!/usr/bin/python
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
        return r.content,repr(x)


def gsb_check(x):
    if "http" not in x:
        x="http%3A%2F%2F"+x
    url="https://sb-ssl.google.com/safebrowsing/api/lookup?client=demo-app&key=AIzaSyD3kccdlWrye4B_3-PV7sz_DazUOTugZmI&appver=1.5.2&pver=3.1&url="+"%s"%x
    r=requests.get(url)
    return bool(r.text)


def urlfix(x):
    x=x.replace("hxxp","http")
    x=x.replace("[.]",".")
    x=x.replace("[tt]","tt")
    if x.startswith("http://"):
        return x
    else:return "http://"+x


if __name__ == "__main__":
    t=sys.argv[-1]

    if t.startswith("/"):
        p=t
    else:
        p=os.getcwd()+"/"+t
    p=os.path.isfile(p)

    if t=="-h":
        print """
        Usage Cases:

        Single site:
        sitereviewcmdln.py google.com

        File(One domain per line):
        sitereviewcmdln.py domains.txt

        STDin read:
        sitereviewcmdln.py -s

        Help:
        sitereviewcmdln.py -h
        """



    if t=="-s":
        print "ENTERING stdin MODE PRESS CTRL+D TO END!"
        z=sys.stdin.readlines()
        c=[urlparse.urlparse(urlfix(item).strip()).hostname for item in z if item]
        print "\nstdin Closed"
        uc=[]
        for item in c:
            if item not in uc:
                uc.append(item)


        for item in uc:

            print check(item)
            time.sleep(2)

    elif p:
        z=open(t, "r").readlines()
        c=[urlparse.urlparse(urlfix(item).strip()).hostname for item in z if item]
        #c=[item for item in open(t, "r").readlines()]


        uc=[]
        for item in c:
            if item not in uc:
                uc.append(item)
        for item in uc:
            #print item.strip()
            print check(item)
            time.sleep(2)

    else:

        r=check(t)
        print r
