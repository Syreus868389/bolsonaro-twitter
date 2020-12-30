import tweepy
import pandas as pd

consumer_key="**********"
consumer_secret="*************"

access_token="**********"
access_token_secret="**********"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

id='128372940'

text, rt, favs, date, link = ([] for i in range(5))
tweets=tweepy.Cursor(api.user_timeline, user_id=id, tweet_mode='extended', include_rts=False).items(3200)
for status in tweets:
    text.append(status.full_text)
    rt.append(status.retweet_count)
    favs.append(status.favorite_count)
    date.append(status.created_at)
    link.append('https://twitter.com/jairbolsonaro/status/{}'.format(status.id))


column_names=['Text', 'Retweets', 'Favs', 'Date', 'URL']

df=pd.DataFrame(list(zip(text,rt,favs,date,link)), columns=column_names)
df.to_excel('bolsonaro.xlsx')
