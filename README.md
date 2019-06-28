# python-ynet
A Python library that allows you to post and view comments on news articles from ynet.co.il. <br />
Standalone .py releases are at https://github.com/sl4vkek/python-ynet/releases. <br />
Documentation is at https://sl4vkek.github.io/python-ynet/.
## Installation
### Install from PyPi
On windows: `py -m pip install ynet requests` <br/>

On linux: <br/>
```
$ sudo apt-get install -y python3 python3-pip
$ pip3 install ynet requests
```
### Install from source 
On linux: <br/>
```
$ git clone https://github.com/sl4vkek/python-ynet.git
$ cd python-ynet
$ python3 setup.py install
```

## Data
The following are data for developers so you could better understand how this library works

### API Endpoints
| API endpoint                                                                                                               	| Purpose                         	| GET / POST 	| Form Data                                                             	| Query data 	| Implementable 	|
|----------------------------------------------------------------------------------------------------------------------------	|---------------------------------	|------------	|-----------------------------------------------------------------------	|------------	|---------------	|
| (ynet.co.il)/Ext/Comp/ArticleLayout/Proc/ShowTalkBacksAjax/v2/0,12990,<article id>-desc-68-0-1,00.html                       	| Retrieve Comments               	| GET        	|                                                                       	|            	| Y             	|
| (ynet.co.il)/YediothPortal/Ext/TalkBack/CdaTalkBackTrans/0,2499,<article id>-0-68-546-0---0,00.html                          	| Post a Comment                  	| POST       	| WSGBRWSR (keep this to FF), name, email, Location, title, description 	|            	| Y             	|
| (ynet.co.il)/YediothPortal/Ext/TalkBack/CdaTalkBackTrans/0,2499,<article id>-0-68-13108-0---<comment id>,00.html             	| Post a Reply                    	| POST       	| WSGBRWSR (keep this to FF), name, email, Location, title, description 	|            	| Y             	|
| (ynet.co.il)/Ext/Comp/ArticleLayout/Proc/ShowTalkBacksAjaxNC2/0,12979,L-recmm-<article id (no L-)>-<comment id>-68-1,00.html 	| Like a Comment                  	| GET        	|                                                                       	| RN (?)     	| N             	|
| (ynet.co.il)/Ext/Comp/ArticleLayout/Proc/ShowTalkBacksAjaxNC2/0,12979,L-recmm-<article id (no L-)>-<comment id>-68-0,00.html 	| Dislike a Comment               	| GET        	|                                                                       	| RN (?)     	| N             	|
| (ynet.co.il)/Ext/Comp/ArticleLayout/Proc/ShowTalkBacksAjax/v2/0,12990,L-artinfo-<article id (no L-)>-68,00.html              	| Retrieve Statistics on Comments 	| GET        	|                                                                       	|            	| Y             	|
### Retrieving an Article's ID
![alt text](https://i.imgur.com/zLUrbmG.png) <br/>
Note that sometimes you need to remove "L-" in order to properly send the request

