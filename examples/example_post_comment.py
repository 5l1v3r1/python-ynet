from ynet import *

comment = Comment(
    Article("https://www.ynet.co.il/articles/0,7340,L-5502137,00.html"),
    name='python-ynet bot example',
    email='notyourbusiness@gmail.com',
    location='Example location',
    title='python-ynet bot example',
    text='python-ynet bot example',
)

print(comment.post())
