from ynet import *

article = Article("https://www.ynet.co.il/articles/0,7340,L-5475445,00.html")

for comment in article.GetComments():
    print("-----------")
    print("Comment title:" + comment.title)
    print("Comment text:" + comment.text)
    print("Commentor name:" + comment.name)
    print("Comment likes:" + str(comment.likes))
    print("-----------")
