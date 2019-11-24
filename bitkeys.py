import time, sys
from bit import Key
from tqdm import tqdm 

print(time.ctime(time.time()))  
limi=2500000

if len(sys.argv)>1:
  limi=int(sys.argv[1])

with tqdm(total=limi) as pbar:
  for i in range(limi):    # 125 sec @ 1000000  7900 addr|sec
    key = Key()
    adr = key.address
    if adr=='1JFvvcF9hEpvLNBNyPBarCH4xPtvPbf2gJ' or \
       adr=='1BZaHoUXNg5dJFsEt5zoeW8ZSAB2wywVMJ' or \
       adr=='1FQN5nWVPonuCDKCQWf3qopYMJvJBSi27F':   
      print("FOUND!!! ",i) 
      print("Addr: ",adr)
      wif = key.to_wif()
      print("WiF: ", wif)
      break
    pbar.update(1)  
  print("\n..nothing in %s attempts"%(limi))
print(time.ctime(time.time()))    