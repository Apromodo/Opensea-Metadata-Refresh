import requests
import time

# change NFT Collection adres and change the range
url = "https://api.opensea.io/asset/0xfce5e89772359843521d18fcc958eb923842fdd3/"
UpdtFlag = "/?force_update=true"

reqUn = [ i for i in range(1, 1000)]
for i in reqUn:
  r_url = url + str(i) + UpdtFlag
  r = requests.get(r_url)
  print(i, r.status_code)
  time.sleep(0)
  
reqUn = [ i for i in range(1, 1000)]
for i in reqUn:
  r_url = url + str(i) + UpdtFlag
  r = requests.get(r_url)
  print(i, r.status_code)
  time.sleep(0)
  
reqUn = [ i for i in range(1, 1000)]
for i in reqUn:
  r_url = url + str(i) + UpdtFlag
  r = requests.get(r_url)
  print(i, r.status_code)
  time.sleep(0)

reqUn = [ i for i in range(1, 1000)]
for i in reqUn:
  r_url = url + str(i) + UpdtFlag
  r = requests.get(r_url)
  print(i, r.status_code)
  time.sleep(0)