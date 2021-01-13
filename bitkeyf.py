import time, sys
from bit import Key
from tqdm import tqdm 
print('--')
print(time.ctime(time.time()),'-Begin')  
limi=2500000

fname='100top.txt'
filetext = open(fname).read()

if len(sys.argv)>1:
  limi=int(sys.argv[1])

with tqdm(total=limi) as pbar:
  for i in range(limi):    # 125 sec @ 1000000  7900 addr|sec
    key = Key()
    adr = key.address
#...
    if adr in filetext:
      print("FOUND!!! ",i) 
      print("Addr: ",adr)
      wif = key.to_wif()
      print("WiF: ", wif)
      break
    pbar.update(1)  
  print("..nothing for %s attempts"%(limi),' - top100 wallets checked')
print(time.ctime(time.time()),'-End.')    


# https://ofek.dev/bit/guide/keys.html#creation
# https://bitinfocharts.com/ru/top-100-dormant_5y-bitcoin-addresses.html