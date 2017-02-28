import urllib2
import json
import sys

nomisma = {} #apotikeysh timhs tvn kryptonomismatwn

 # H synarthsh aksianom dexetai dyo orismata to coins kai to date kai vriskei tis times
 # twn kryptonomismatwn th sygkekrimenh hmeromhnia
def aksianom(coins,date):
	zht = urllib2.Request("http://api.coindesk.com/v1/bpi/historical/close.json?start=%s&end=%s&currency=%s"%(date,date,coins))
   	antap = urllib2.urlopen(zht)
   	html =  antap.read()
   	html = html.split(':')
   	pros = html[2]
   	pros = pros.split('}')
   	nomisma[pros[0]]=coins

krypt = raw_input("Dwste ta kryptonimismata pou 8elete me keno.Paradeigma:eur usd gbp\n")
hmer = raw_input("Dwste thn hmerominia.Paradeigma:2015-05-12 \n")
krypt = krypt.split(' ') #xwrixei ta kryptonimismata me keno

a=len(krypt)

for i in range (a):
	aksianom(krypt[i],hmer) # klhsh ths synarthshs aksianom gia to ka8e
	 # kryptonomisma th sygkekrimenh hmerominia

for i in sorted(nomisma,key=float):
	print i,nomisma[i] # emfanish timwn twn kryptonomismatwn se
	  # auksoysa seira
