import twint
from datetime import date
#import nest_asyncio

#nest_asyncio.apply()
today = date.today()

c = twint.Config()
c.Lang = "en"
# c.Search = "#foodwaste" or "#zerowaste" or "#sustainability" or "#ecofriendly"
# c.Limit = 20
c.Username = "edward09690585"
c.Since = "2017-1-1"
c.until= today.strftime("%b-%d-%Y")

c.Store_csv = True
c.Custom_csv = ["date", "time", "username", "tweet", "link", "likes", "retweets", "replies", "mentions", "hashtags"]
c.Pandas = True
c.Output = "eco1friendly.csv"

twint.run.Search(c)

