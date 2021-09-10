#coporate with: hongbo zhong
import requests
pg = requests.get("https://raw.githubusercontent.com/Bcrian/404-lab1/master/lab1.py", allow_redirects=True)
open("lab1_copy.py", "wb").write(pg.content)

print(pg.content)
