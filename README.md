# veriblock-auto-pop
auto-pop-miner

1 INSTALL PYTHON and path 

2 pip install websocket-client

  pip install websocket
	
  pip install requests
	
 
3 CHANGE THE POP MINER PORT IN POPMINER AND WRITE DOWN IT IN IPLIST.TXT
FOR EXAMPLE:

auto.mine.round1=false

auto.mine.round2=false

auto.mine.round3=false

auto.mine.round4=true

http.api.port=8044

bitcoin.minrelayfee.enabled=false


4 set the slowfee in pop.py, now is 10

if the fee is more than 10 ,pop miner will set auto.mine.round4 to false ,or ,it will be true and fit the net
 
 
 5 python pop.py
