from ynet import *

article = Article("https://www.ynet.co.il/articles/0,7340,L-5507756,00.html#autoplay")
comments = article.get_comments()

for comment in comments:
    print("-----------")
    print("Comment title:" + comment.title)
    print("Comment text:" + comment.text)
    print("Commentor name:" + comment.name)
    print("Comment likes:" + str(comment.likes))
