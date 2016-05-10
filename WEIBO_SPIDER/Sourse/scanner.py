
import re


class tweet(object):
    content = ""
    forward = 0

    def __init__(self, content, forward):
        self.content = content
        self.forward = forward

class token_type:
    content = 0
    forward = 1

class token(object):
    type = token_type()
    value = ""
    def __init__(self, type, value):
        self.type = type
        self.value = value

topic_pattern_ = "<a[\S|\s]+>(#[\S|\s]+#)</a>([\S|\s]+)</div>"
notopic_pattern_ = ""

class scanner(object):
    def __init__(self):
        pass
    def get_tweet_list(self, stream):
        content_pattern = "feed_list_content"

        while(true):
            line = stream.readline()
            if(content_pattern, line):
                handle_content(stream)
            elif():
                # forward
                pass
            else:
                pass

    
    def handle_content(stream):

        line = stream.readline()
        # have topic
        if(re.search(topic_pattern, line)):
            return token(token_type.content, re.search(topic_pattern, line).group(1) + re.search(topic_pattern, line).group(2))

        # have not topic

            
            


        


