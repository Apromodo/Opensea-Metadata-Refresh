import requests
import time

# change NFT Collection adres and change the range
url = "https://api.opensea.io/asset/0xfce5e89772359843521d18fcc958eb923842fdd3/"
update_flag = "/?force_update=true"

ids = [ i for i in range(1, 1000)]

for i in ids:
  req_url = url + str(i) + update_flag
  r = requests.get(req_url)
  print(i, r.status_code)
  time.sleep(0.1)
  
ids = [ i for i in range(1, 1000)]

for i in ids:
  req_url = url + str(i) + update_flag
  r = requests.get(req_url)
  print(i, r.status_code)
  time.sleep(0.1)
  
ids = [ i for i in range(1, 1000)]

for i in ids:
  req_url = url + str(i) + update_flag
  r = requests.get(req_url)
  print(i, r.status_code)
  time.sleep(0.1)

  ids = [ i for i in range(1, 1000)]

for i in ids:
  req_url = url + str(i) + update_flag
  r = requests.get(req_url)
  print(i, r.status_code)
  time.sleep(0.1)