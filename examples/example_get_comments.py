from ynet import *

article = Article("https://www.ynet.co.il/articles/0,7340,L-5506634,00.html")
comments = article.GetComments()

for comment in article.GetComments():
    print("-----------")
    print("Comment title:" + comment.title)
    print("Comment text:" + comment.text)
    print("Commentor name:" + comment.name)
    print("Comment likes:" + str(comment.likes))
