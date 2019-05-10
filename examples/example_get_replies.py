# -*- coding: utf-8 -*-

from ynet import *

article = Article("https://www.ynet.co.il/articles/0,7340,L-5506634,00.html")

comment = article.GetCommentByCommentNum(3)
print("Found comment.")
print("Getting replies for comment...")
replies = comment.GetReplies()
for reply in replies:
    print("-----------")
    print("Comment title:" + reply.title)
    print("Comment text:" + reply.text)
    print("Commentor name:" + reply.name)
    print("Comment likes:" + str(reply.likes))
