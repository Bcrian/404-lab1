import requests
pg = requests.get("http://www.google.com/")

print(pg.content)
print(pg.status_code)