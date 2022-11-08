from bs4 import BeautifulSoup
import requests
import sys 

from pyfiglet import Figlet

class couleur:
		  	OK = '\033[91m' 
		  	ba= '\033[92m' 
		  		

figlet = Figlet(font='slant')
result = figlet.renderText("Ys jhonson")
dak= figlet.renderText("Le wana")

print(couleur.OK+result)
print(couleur.ba+dak)

print('\033[92m', 'crawl URL[+]\n')
try :
	ab = sys.argv[1]
	req = requests.get(ab)
	b = req.text
	soup = BeautifulSoup(b, 'html.parser')
	for link in soup.find_all('a'):
	   b= link.get('href')
	   if '=' in str(b) :
	   	bak = b
	   	if 'http' in bak :
	   		print('\033[92m' ,bak)
except :
	print('python program.py target.com')
