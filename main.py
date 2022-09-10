from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def homepage():
  return 'Homepage'
  
@app.route('/max_rating_json')
def max_rating_json():
  tabela = pd.read_csv('AppleStore.csv')
  
  genre_news_table = tabela[tabela['prime_genre'] == "News"]
  max_id = genre_news_table['rating_count_tot'].idxmax()
  max_row = genre_news_table.loc[[max_id]]
  resp_rows = []
  for rows in max_row.itertuples():
    resp_rows.append({
      'id': int(rows.id),
      'track_name': rows.track_name,
      'size_bytes': int(rows.size_bytes),
      'price': int(rows.price),
      'prime_genre': rows.prime_genre,
      'rating_count_tot': int(rows.rating_count_tot)
    })

  return resp_rows

@app.route('/maior_rating_csv')
def maior_rating_csv():
  tabela = pd.read_csv('AppleStore.csv')
  
  genre_news_table = tabela[tabela['prime_genre'] == "News"]
  max_id = genre_news_table['rating_count_tot'].idxmax()
  max_row = genre_news_table.loc[[max_id]]
  max_row.to_csv('max_row.csv', index=False)

  return max_row

@app.route('/top10_bm')
def top10_bm():
  tabela = pd.read_csv('AppleStore.csv')

  genre_media_table = tabela[tabela['prime_genre'].isin(["Music", "Books"])]
  top10 = genre_media_table['rating_count_tot'].nlargest(n=10).index.tolist()
  top_rows = genre_media_table.loc[top10]
  resp_rows = []
  for rows in top_rows.itertuples():
    resp_rows.append({
      'id': int(rows.id),
      'track_name': rows.track_name,
      'size_bytes': int(rows.size_bytes),
      'price': int(rows.price),
      'prime_genre': rows.prime_genre,
      'rating_count_tot': int(rows.rating_count_tot)
    })

  return resp_rows
  
@app.route('/top1_bm')
def top1_bm():
  tabela = pd.read_csv('AppleStore.csv')

  genre_media_table = tabela[tabela['prime_genre'].isin(["Music", "Books"])]
  top1 = genre_media_table['rating_count_tot'].nlargest(n=1).index.tolist()
  top_rows = genre_media_table.loc[top1]
  resp_rows = []
  for rows in top_rows.itertuples():
    resp_rows.append({
      'id': int(rows.id),
      'track_name': rows.track_name,
      'size_bytes': int(rows.size_bytes),
      'price': int(rows.price),
      'prime_genre': rows.prime_genre,
      'rating_count_tot': int(rows.rating_count_tot)
    })

  return resp_rows


app.run(host='0.0.0.0')


'''
tabela = pd.read_csv('AppleStore.csv')

genre_media_table = tabela[tabela['prime_genre'].isin(["Music", "Books"])]
top10 = genre_media_table['rating_count_tot'].nlargest(n=10).index.tolist()
top_rows = genre_media_table.loc[top10]
resp_rows = []
print(top_rows)
for rows in top_rows.itertuples():
  resp_rows.append({
    'id': int(rows.id),
    'track_name': rows.track_name,
    'size_bytes': int(rows.size_bytes),
    'price': int(rows.price),
    'prime_genre': rows.prime_genre,
    'rating_count_tot': int(rows.rating_count_tot)
  })
print(resp_rows)'''