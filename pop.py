#!/usr/bin/env python3.6
from websocket import create_connection
import sys
import subprocess
import requests
import json
import time
import math
import ssl

header = {"Content-type": "application/json"}
def getallfree(ip,port):
        nmm=0
        nm=0
        total=0
        gas=0
        UrlLink="http://%s:%s" %(ip,port)
        aa=requests.put(url="%s/api/config" %UrlLink,json={"key": "bitcoin.fee.max","value": GAS},headers=header)
        print(aa)
        bb=requests.put(url="%s/api/config" %UrlLink,json={"key": "bitcoin.fee.perkb","value": Gas},headers=header)
        print (bb)
        cc=requests.put(url="%s/api/config" %UrlLink,json={"key": "auto.mine.round4","value": AUTO},headers=header)
        print (cc)
while 1 > 0 :
    ws = None
    fast = None
    try:
        ws = create_connection("wss://mempool.space/ws",sslopt={"cert_reqs": ssl.CERT_NONE})
        result =  ws.recv()
        data = json.loads(result)
        minFee = data["projectedBlocks"][0]["minFee"]
        slowfee = math.ceil(minFee)
        print ("MinFee of sat/vB:", slowfee)
    except:
        print ("get minFee err")
        time.sleep(3)
        continue
    ws.close()
    try:
        fast=requests.get(url="https://mempool.space/api/v1/fees/recommended",headers=header)
    except:
        print ("get recommended err")
        time.sleep(3)
        continue
    fastfee=fast.json()["fastestFee"]
    print("mempool获取的fastfree是：",fastfee)
    print("mempool获取的halfHourFee是：",slowfee)
    doubleslowfee=slowfee*2+3
    print("double fee is ：",doubleslowfee)
    if doubleslowfee>fastfee :
      finalfee=fastfee
    if doubleslowfee<=fastfee :
      finalfee=slowfee
    print("fastfee is wrong ：")
    print("final fee is ：",finalfee)
    Gas=(finalfee)*733
    GAS=int(Gas*0.5)
    AUTO="true"
    if slowfee > 10 :
        AUTO="false"
    print("bitcoin.fee.perkb is:",Gas)
    print("bitcoin.fee.max is:",GAS)
    print("auto.mine.round4:",AUTO)
    with open('IPLIST.txt',"r",encoding="utf-8") as f :
        try:
            data = f.read().strip().split('\n')	
            for d in data:
                ipp = d.split(':')[0]
                add = d.split(':')[1]
                print("ip:port",ipp,add)
                getallfree(ipp,add)
                print("sleep 11.....")
                time.sleep(0.2)
        except Exception as e:
            print(e)
            print("该轮次异常,跳过停止3s...........")
            time.sleep(1)		
            pass
    time.sleep(10)		
