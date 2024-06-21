from bs4 import BeautifulSoup
import requests
from colorama import Fore, Style
import art
import urllib3
import argparse


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def color():
     text = art.text2art("Find Parameter", font="blg")
     print(Fore.GREEN + Style.BRIGHT +text+'\nCoded by Jhonson\n'+ Style.RESET_ALL)

color()


def main(urls, balise1,protocol,condition):
   try:    
     for url in urls:
       req = requests.get(url,verify=False)
       soup = BeautifulSoup(req.text, 'html.parser')
      
       param1 = [link.get('href') for link in soup.find_all(balise1)]
       liste = list(dict.fromkeys(param1))
       
       for i in liste:
         if '=' in i and not 'http' in i:
          supp=str(req.url+i).replace('//','/')
          print(Fore.YELLOW + Style.BRIGHT +supp+ Style.RESET_ALL)

         
           
   except requests.exceptions.MissingSchema: 
        print('')
               
   
if __name__=='__main__':

     parser = argparse.ArgumentParser(description="Find parameter")
     parser.add_argument("-file", "--file", dest="file", help="list urls", required=False)
     args = parser.parse_args()
     
     
     
     with open(args.file,'r') as file:
      files=[list.strip() for list in file]
      for i in files:
         ifelse=['=','http',i]

     main(files,'a','http',ifelse)

