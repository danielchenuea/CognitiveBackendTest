from flask import Flask
import pandas as pd
import sqlite3

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
  resp_row = max_row[["id", 'track_name', 'size_bytes', 'price', 'prime_genre', 'rating_count_tot']]
  resp_row.to_csv('max_row.csv', index=False)

  return {"message": "max_rating generated"}
  
@app.route('/maior_rating_sql')
def maior_rating_sql():
  tabela = pd.read_csv('AppleStore.csv')
  
  genre_news_table = tabela[tabela['prime_genre'] == "News"]
  max_id = genre_news_table['rating_count_tot'].idxmax()
  max_row = genre_news_table.loc[[max_id]]

  con = sqlite3.connect("data.db")
  cursor = con.cursor()
  cursor.execute("CREATE TABLE if not exists rating(\
      id	    INTEGER UNIQUE,\
      track_name	TEXT,\
      size_bytes	INTEGER,\
      price	REAL,\
      prime_genre	TEXT,\
      rating_count_tot	INTEGER,\
      PRIMARY KEY(id)\
  )")

  for rows in max_row.itertuples():
    query = "insert into rating(id, track_name,size_bytes,price,prime_genre,rating_count_tot) values (?,?,?,?,?,?)"
    cursor.execute(query, (
      int(rows.id), 
      rows.track_name, 
      int(rows.size_bytes), 
      int(rows.price),
      rows.prime_genre,
      int(rows.rating_count_tot)))
    
  con.commit()
  con.close()
  

  return {"message": "max_rating sql generated"}

@app.route('/top10_bm_json')
def top10_bm_json():
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
  
@app.route('/top10_bm_csv')
def top10_bm_csv():
  tabela = pd.read_csv('AppleStore.csv')

  genre_media_table = tabela[tabela['prime_genre'].isin(["Music", "Books"])]
  top10 = genre_media_table['rating_count_tot'].nlargest(n=10).index.tolist()
  top_rows = genre_media_table.loc[top10]
  resp_rows = top_rows[["id", 'track_name', 'size_bytes', 'price', 'prime_genre', 'rating_count_tot']]
  resp_rows.to_csv('top10.csv', index=False)

  return {"message": "top10 generated"}

@app.route('/top10_bm_sql')
def top10_bm_sql():
  tabela = pd.read_csv('AppleStore.csv')
  
  genre_media_table = tabela[tabela['prime_genre'].isin(["Music", "Books"])]
  top10 = genre_media_table['rating_count_tot'].nlargest(n=10).index.tolist()
  top_rows = genre_media_table.loc[top10]

  con = sqlite3.connect("data.db")
  cursor = con.cursor()
  cursor.execute("CREATE TABLE if not exists top10(\
      id	    INTEGER UNIQUE,\
      track_name	TEXT,\
      size_bytes	INTEGER,\
      price	REAL,\
      prime_genre	TEXT,\
      rating_count_tot	INTEGER,\
      PRIMARY KEY(id)\
  )")

  for rows in top_rows.itertuples():
    query = "insert into top10(id, track_name,size_bytes,price,prime_genre,rating_count_tot) values (?,?,?,?,?,?)"
    cursor.execute(query, (
      int(rows.id), 
      rows.track_name, 
      int(rows.size_bytes), 
      int(rows.price),
      rows.prime_genre,
      int(rows.rating_count_tot)))
    
  con.commit()
  con.close()
  
  return {"message": "top10 sql generated"}
  
@app.route('/top1_bm_json')
def top1_bm_json():
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

@app.route('/top1_bm_csv')
def top1_bm_csv():
  tabela = pd.read_csv('AppleStore.csv')

  genre_media_table = tabela[tabela['prime_genre'].isin(["Music", "Books"])]
  top1 = genre_media_table['rating_count_tot'].nlargest(n=1).index.tolist()
  top_rows = genre_media_table.loc[top1]
  resp_rows = top_rows[["id", 'track_name', 'size_bytes', 'price', 'prime_genre', 'rating_count_tot']]
  resp_rows.to_csv('top1.csv', index=False)

  return {"message": "top1 generated"}


@app.route('/top1_bm_sql')
def top1_bm_sql():
  tabela = pd.read_csv('AppleStore.csv')
  
  genre_media_table = tabela[tabela['prime_genre'].isin(["Music", "Books"])]
  top1 = genre_media_table['rating_count_tot'].nlargest(n=1).index.tolist()
  top_rows = genre_media_table.loc[top1]

  con = sqlite3.connect("data.db")
  cursor = con.cursor()
  cursor.execute("CREATE TABLE if not exists top1(\
      id	    INTEGER UNIQUE,\
      track_name	TEXT,\
      size_bytes	INTEGER,\
      price	REAL,\
      prime_genre	TEXT,\
      rating_count_tot	INTEGER,\
      PRIMARY KEY(id)\
  )")

  for rows in top_rows.itertuples():
    query = "insert into top1(id, track_name,size_bytes,price,prime_genre,rating_count_tot) values (?,?,?,?,?,?)"
    cursor.execute(query, (
      int(rows.id), 
      rows.track_name, 
      int(rows.size_bytes), 
      int(rows.price),
      rows.prime_genre,
      int(rows.rating_count_tot)))
    
  con.commit()
  con.close()
  
  return {"message": "top1 sql generated"}

app.run(host='0.0.0.0')
