from ynet import *

article = Article('https://www.ynet.co.il/articles/0,7340,L-5506282,00.html')

anonymous_comments = article.get_comments_by_writer('')

print('The following ynet comments are written by people who chose to not post their name')
for anonymous_comment in anonymous_comments:
    print("-----------")
    print("Comment title:" + anonymous_comment.title)
    print("Comment text:" + anonymous_comment.text)
    print("Comment likes:" + str(anonymous_comment.likes))
