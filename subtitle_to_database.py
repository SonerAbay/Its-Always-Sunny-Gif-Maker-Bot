import re
import sqlite3
import os
from itertools import groupby


def exec(path,episode_id):
    chunks = []
    with open(path, 'r') as f:
        group = ""
        for line in f:
            if line !="\n":
                group += line + " "
            else:
                # gereksiz boşlukları, empty lineları, dashleri siler
                group = " ".join(group.split()).replace('-', '').lower()
                # html tagi siler
                group = re.sub('<[^>]*>', '', group)
                group = re.sub(r'\[.*?\]', '', group)
                #group = group.replace('\n', ' ').replace('\r', '').replace('-', '').lower()
                print(group)
                chunks.append(group)
                group = ""

    conn = None
    try:
        conn = sqlite3.connect("db/subtitles.db")
    except sqlite3.Error as e:
        print(e)

    # reklam yazıları sonda oluyor pop
    chunks.pop()
    for c in chunks:

        times = re.findall(r"\d{1}\:\d{2}\:\d{2}\,\d{3}", c)

        if len(times) > 0:
            start_time = int(times[0][2:4]) * 60 + int(times[0][5:7])

            # only substract 1 if its bigger or equal to 1
            if start_time >= 1:
                start_time -= 1

            end_time = int(times[1][2:4]) * 60 + int(times[1][5:7]) + 1

            # c yi boslukla split edip 4 bosluktan itibaren geriye kalani alırsak text gelir
            text = " ".join(c.split()[4:])
            cur = conn.cursor()
            cur.execute("INSERT OR IGNORE INTO lines(text,start_time,end_time,episode_id) VALUES(?,?,?,?)",
                        (text, start_time, end_time, episode_id))
        else:
            print("---------------------BOS VERI")

    conn.commit()
    cur.close()

def main():

    path = 'srt\\'
    files = {}
    episode_id = ""
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files[os.path.join(r, file)] = file[:-4]

    print(files)
    for path, episode in files.items():
        exec(path, episode)


if __name__ == "__main__":
    main()
