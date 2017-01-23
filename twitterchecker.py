import requests
import string
from config import *
import sys

def checktwitter(twitterurl,username,savelist):
    try:
        userurl = twitterurl+username
        page = requests.get(userurl)
        print "[+]Checking " +str(userurl)
        if str('404 Not Found') in str(page.headers):
            print "[+]Username " +username+ " available"
            savelist.write(username+ "\n")
        else:
            print "[-]Username " +username+ " unavailable"
                    #print page.headers
    except Exception:
        pass

def main():
    twitterurl = 'https://www.twitter.com/'

    try:
        twitterlist = open(readfilename,'r')
    except IOError:
        sys.exit("[-]Invalid username filename!")
    try:
        savelist = open(writefilename,'w')
    except IOError:
            sys.exit("[+]Invalid save file")

    for line in twitterlist.readlines():
        try:
            username = line.strip('\n')
            if len(username) <= 4:
                continue
            if "'" in username:
                continue
        except Exception:
            pass
        checktwitter(twitterurl,username,savelist)
    print "[+]Done!"

if __name__ == '__main__':
    main()
