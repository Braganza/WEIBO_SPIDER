

#��ȡ΢����Ϣ

##user:΢���û�<br>
	��½
	��ȡĳ��(�û�)ҳ���html��Ϣ

##class weibo_msg:΢����Ϣ��һ����<br>
###var<br>
    #content
    #forward:ת����

##scanner:
	tweet	:	content
			|	forward
			;

	content :	���#����:����"feed_list_content"-> "<>"֮��
			|	δ���#����	
	
