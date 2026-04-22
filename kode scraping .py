

from google_play_scraper import app, reviews, Sort, reviews_all
import pandas as pd

scrapreview,continue_token = reviews(
    'com.shopee.id',
    lang='id',
    country='id',
    sort=Sort.NEWEST,
    count=10020
)

df=pd.DataFrame.from_records(scrapreview)

df.to_csv('scrapreview-ml.csv')
