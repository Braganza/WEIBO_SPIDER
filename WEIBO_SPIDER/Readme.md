

#爬取微博信息

##user:微博用户<br>
	登陆
	获取某个(用户)页面的html信息

##class weibo_msg:微博信息（一条）<br>
###var<br>
    #content
    #forward:转发量

##scanner:
	tweet	:	content
			|	forward
			;

	content :	添加#话题:含有"feed_list_content"-> "<>"之后
			|	未添加#话题	
	
