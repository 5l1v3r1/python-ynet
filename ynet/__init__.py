import requests
from os.path import basename
from urllib.parse import urlparse
from datetime import date
import json

class Comment:
    
    def __init__(self, article_url='' ,name='', email='', location='', title='', text='', likes=0, commentNum=0, commentDate=None, commentId=0):
        self.article_url = article_url
        self.name = name
        self.email = email
        self.location = location
        self.title = title
        self.text = text
        self.likes = likes
        self.commentNum = commentNum
        self.commentDate = commentDate
        
    def Post(self, useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"):
        r = requests.post(self.article_url, params={'WSGBRWSR':'FF', 'name':self.name,\
        'email':self.email, 'Location':self.location, 'title':self.title, 'description':self.text}, headers={'User-Agent':useragent})
        return r.text

class Article:

    def __init__(self, article_url):
        self.article_url = article_url
        self.article_id = basename(urlparse(article_url).path).split(',')[2]

    def GetComments(self):
        comments = []
        r = requests.get("https://www.ynet.co.il/Ext/Comp/ArticleLayout/Proc/ShowTalkBacksAjax/v2/0,12990,"+ self.article_id + "-desc-68-0-1,00.html", params={'User-Agent':\
                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}).text
        comments_json = json.loads(r)['rows']
        for comment_dict in comments_json:
            _comment_date = comment_dict['the_date'].split('.')
            comment_date = date(year=int(_comment_date[2]), month=int(_comment_date[1]), day=int(_comment_date[0]))
            comments.append(Comment(article_url=self.article_url,\
                                    name=comment_dict['name'], \
                                    title=comment_dict['title'], \
                                    location=comment_dict['location'], \
                                    commentDate=comment_date, \
                                    commentNum=comment_dict['tc'], \
                                    likes=comment_dict['ts'], \
                                    commentId=comment_dict['id'] \
                                    
                ))
        return comments
