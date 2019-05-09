# -*- coding: utf-8 -*-

from ynet import *

article = Article("https://www.ynet.co.il/articles/0,7340,L-5506634,00.html")
comments = article.GetComments()

for comment in comments:
    if comment.title == 'דימונד גרין':
        replies = comment.GetReplies()
        for reply in replies:
            print(reply.title)
