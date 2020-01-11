import sqlite3
from playhouse.sqlite_ext import SqliteExtDatabase

conn = None
try:
    conn = sqlite3.connect("/mnt/c/Users/soner/Documents/MYGITHUB/SUNNY/chinook/subtitles.db")
except sqlite3.Error as e:
    print(e)

line = raw_input("Enter a line from sunny you jabroni: ")
cur = conn.cursor()
sql = "SELECT * from episode inner join lines on episode.episode_id = lines.episode_id WHERE text MATCH '{}' ORDER BY rank".format(line)
cur.execute(sql)

result = cur.fetchall()

print("Season {}, episode {} - {}. \nYou can watch it at: {}\n{}".format(result[0][1],result[0][3],result[0][2],result[0][4],str(result[0][7]/60)+':'+str(result[0][7]%60)))