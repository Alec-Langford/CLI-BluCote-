
import requests
import urllib
import os
import sys
import socket


tlds = ["com", "net", "info", "biz", "org"]



'''
    try:
        x = p + "." + t
        n = socket.gethostbyname(x)
        return "%s,%s\n"%(x,n)
    except socket.gaierror:
        return "No Address %s"%p
        '''


def check_name(n):
    try:
        x = socket.gethostbyname(n)

        return (x,n)
    except socket.gaierror:
       # print "No address %s"%n
        return (False,n)


def gen_name(p):
    l=[p+'.'+item for item in tlds]
    return l

def check(n):
    return map(check_name,gen_name(n))

if __name__ == "__main__":

    print sys.argv[1:]
    a = sys.argv[1:]
    for item in a:
        for i in map(check_name,gen_name(item)):
            print i

'''
#f = open("post.txt", "r")
#d = f.read().split("\n")
#o=open("postIPs.csv","w")

for item in d:
    for t in tlds:
        try:
            x = item + "." + t
            n = socket.gethostbyname(x)
            o.write("%s,%s\n"%(x,n))
        except socket.gaierror:
            pass
o.close()


'''