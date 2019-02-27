import urllib.request

from bs4 import BeautifulSoup

import pymysql

movielist = []

url = "https://movie.douban.com/top250"

def get_html(url):
    res = urllib.request.urlopen(url)
    html = res.read().decode()
    return html


def parse_html(htmlfile):
    '''
    解析html
    '''
    mysoup = BeautifulSoup(htmlfile,'html.parser')
    movie_zone = mysoup.find('ol')
    movie_list = movie_zone.find_all('li')
    for movie in movie_list:
        movie_name = movie.find('span',attrs={'class':'title'}).getText()
        movielist.append(movie_name)
        nextpage = mysoup.find('span',attrs={'class':'next'}).find('a')
    if nextpage:
        new_url = url + nextpage['href']
        parse_html(get_html(new_url))


#
# def save_data(movielist):
#     conn = pymysql.connect(host='localhost',user='root',password='mysql',db='test')
#     mycursor = conn.cursor()
#
#     # sql = 'CREATE TABLE t_movie(ID VARCHAR(10),name VARCHAR(20))DEFAULT CHARSET=utf8'
#     # mycursor.execute(sql)
#     sql = ''
#     for id,movie in enumerate(movielist):
#         sql = "INSERT INTO t_movie VALUES(%s,%s)"
#         mycursor.execute(sql,(id,movie))
#     conn.commit()
#     mycursor.close()
#     conn.close()


reshtml = get_html(url)
parse_html(reshtml)
print(movielist)
