import re
import sqlite3
import os


def fetch_srt(path,episode_id):
    chunks = []
    with open(path, 'r') as f:
        group = ""
        for line in f:
            if line !="\n":
                group += line + " "
            else:
                # deletes empty lines and dashes
                group = " ".join(group.split()).replace('-', '')
                # deleting tags
                group = re.sub('<[^>]*>', '', group)
                group = re.sub(r'\[.*?\]', '', group)
                print(group)
                chunks.append(group)
                group = ""
    create_db(chunks, episode_id)



def create_db(chunks, episode_id):

    # popping last chunks from .srt files since they are generally ads
    chunks.pop()

    conn = None
    try:
        conn = sqlite3.connect("db/subtitles.db")
    except sqlite3.Error as e:
        print(e)

    # extracting timestamps and texts
    for c in chunks:

        # finding timestamps H:MM:SS:XXX
        times = re.findall(r"\d{1}\:\d{2}\:\d{2}\,\d{3}", c)

        if len(times) > 0:
            start_time = int(times[0][2:4]) * 60 + int(times[0][5:7])

            # only substract 1 if its bigger or equal to 1
            if start_time >= 1:
                start_time -= 1

            end_time = int(times[1][2:4]) * 60 + int(times[1][5:7]) + 1

            # the text we want is after the 4th split
            text = " ".join(c.split()[4:])

            # only Letters numbers and spaces accepted
            regex = re.compile("^[A-Za-z0-9 ]*$")
            text = "".join(filter(regex.search, text))

            cur = conn.cursor()
            cur.execute("INSERT OR IGNORE INTO lines(text,start_time,end_time,episode_id) VALUES(?,?,?,?)",
                        (text, start_time, end_time, episode_id))
        else:
            print("-------ILLEGAL CHUNK---------")

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
        fetch_srt(path, episode)


if __name__ == "__main__":
    main()
