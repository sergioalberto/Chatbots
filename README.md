# Chatbots
Here you can find some demos using Google and IBM SDKs in Python


### Install the dependencies

```sh
 pip install configparser
 pip install flask
 pip install Flask-Session
 pip install redis
 pip install beaker
 easy_install python-memcached
 pip install apiai
 easy_install --upgrade watson-developer-cloud (pip install --upgrade watson-developer-cloud)
```

### Run terminal demo
```sh
python demo.py -conf configFile.ini -sdk Google
```
![Alt text](demo/controllers/static/img/terminal.png?raw=true "Terminal Chatbot")

### Run chatbot web
```sh
python chatbot.py -conf configFile.ini -sdk Google
```
![Alt text](demo/controllers/static/img/chatWeb.png?raw=true "Web Chatbot")

License
----

MIT

**Free Software!**
