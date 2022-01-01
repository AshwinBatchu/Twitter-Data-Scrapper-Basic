from requests.models import parse_url
import tweepy

consumerkey = ' '
consumersecret = ' '
accesskey = ' '
accesssecret = ' '


auth = tweepy.OAuthHandler(consumerkey,consumersecret)
auth.set_access_token(accesskey,accesssecret)
api = tweepy.API(auth)


SEARCH_TEXT = str(input())
search = api.search_tweets(SEARCH_TEXT,result_type = 'recent',)
print(type(search))
for a in search :
    var = api.get_status(a.id)
    var.__dict__
    print(var.text)


    

    
