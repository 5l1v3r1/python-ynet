# -*- coding: utf-8 -*-

from ynet import *

article = Article("https://www.ynet.co.il/articles/0,7340,L-5506634,00.html")

comment = article.GetCommentByCommentNum(3)
print('Found comment:' + comment.title)
print('Comment text:' + comment.text)
print('Sending reply...')
reply = Comment(article_url=article.article_url,\
                name='python-ynet bot reply test',\
                email='fuckoff@gmail.com', \
                location='your mom\' butthole', \
                title='Test reply using python-ynet', \
                text='github.com/sl4vkek/python-ynet')
comment.Reply(reply)
