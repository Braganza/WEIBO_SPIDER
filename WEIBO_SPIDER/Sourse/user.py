

import unittest
import urllib
import urllib2
import base64
import scanner

class user(object):
    url = ""
    msg_list = []

    def __init__(self, username, password):
        login_in(username=username, password=password)

    def get_file(self, file_name):
        # open file
        try:
            in_file = open(file_name, 'r')
            return in_file;
        except:
            print("failed to open file!")

    def get_line(self, file):
        return file.readline()

    def get_html(self, url):
        # 伪造百度搜索
        headers = {'User-Agent':'Baiduspider+(+http://www.baidu.com/search/spider.htm)'} 
        request = urllib2.Request(url, headers=headers)
        return urllib2.urlopen(request)

    def get_msg_list(url):
        html = get_html(url)
        # 分析
        # return 生成的list

    
    # 登陆和获取网页分开
    def login_in(self, username, password):
        username = base64.b64encode(username.encode('utf-8')).decode('utf-8')

        postData = {
        "entry": "sso",
        "gateway": "1",
        "from": "null",
        "savestate": "30",
        "useticket": "0",
        "pagerefer": "",
        "vsnf": "1",
        "su": username,
        "service": "sso",
        "sp": password,
        "sr": "1440*900",
        "encoding": "UTF-8",
        "cdult": "3",
        "domain": "sina.com.cn",
        "prelt": "0",
        "returntype": "TEXT",
        }

        loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
        session = requests.Session()
        res = session.post(loginURL, data = postData)
        jsonStr = res.content.decode('gbk')
        info = json.loads(jsonStr)

        if info["retcode"] == "0":
            print("登录成功").decode('UTF-8').encode('GBK')

        else:
            print("登录失败，原因： %s" % info["reason"]).decode('UTF-8').encode('GBK')



