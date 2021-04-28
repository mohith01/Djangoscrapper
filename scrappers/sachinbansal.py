import requests
from bs4 import BeautifulSoup


def bansal_scrap(l=[-1,2,0],start=0,end=None):
    s = requests.get("https://sachinpullil.com/blog/",headers={"User-Agent":"XY"})
    b = BeautifulSoup(s.text,'html.parser')

    b = list(b.select('.elementor-column'))

    for i in l:
        del b[i]


    bansal_stuff = []

    for i in range(len(b)):
        try:
            t1 = b[i].select('.elementor-image-box-title')[0].a.get('href')
            t2 = b[i].select('.elementor-image-box-title')[0].a.get_text()
            t3 = b[i].get_text()
            bansal_stuff.append({"url":t1,"title":t2,"desc":t3.replace(t2,'')})
        except:
            pass
    
    return bansal_stuff[start:end]



