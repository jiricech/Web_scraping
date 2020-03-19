import requests

from bs4 import BeautifulSoup  #pip install beautifulsoup4, parsing the HTML using Beautifull Soup library



r=requests.get('https://onemocneni-aktualne.mzcr.cz/covid-19') #fetches web page from the URL and stores the result in a response object called r.

print(r.text[0:500])  #this r object has a text attribute which contains HTML code

soup=BeautifulSoup(r.text,'html.parser') #parser included in standard Python library-parsing text files formatted in HTML


resultstest=soup.find_all('p',attrs={'id':'count-test'}) #act as python list

resultssick=soup.find_all('p',attrs={'id':'count-sick'})
#print(resultstest[0:1])
#print(resultssick[0:1])#first record
#print(resultssick[-1]) #last record
#print(len(resultssick))
#print(len(resultstest))

first_resulttest=resultstest[0]
first_resultsick=resultssick[0]
first_resulttest.find('p')
print('The current number of tested is:'+first_resulttest.text +'','persons.')
print('The current number of sick is:'+first_resultsick.text + '','persons.')
#first_resulttest.find('p')#.text[0:-3]+'Number of tested'
#print (first_resulttest)


print(first_resultsick.contents) #python list containing a children

print(first_resulttest.contents[0:1])

#########################################Extracting the URL#########################################################################
"""
<a href="https://koronavirus.mzcr.cz/seznam-odberovych-center/" target="_blank" rel="noreferrer noopener" title="Seznam odběrových center COVID-19 (koronavirus.mzcr.cz)" aria-label="Seznam odběrových center COVID-19 na koronavirus.mzcr.cz">
                Seznam odběrových center COVID-19 <i class="fa fa-external-link-alt"></i>
              </a>

BEAUTIFUL SOAP methods and attributes
find(): searches for the first matching tag, and returns a Tag object.
find_all(): searches for all matching tags, and returns a ResultSet object.

We can extract information from a Tag object using attributes:
text: extracts the text of a Tag and returns a string.
contents: extracts the children of a Tag and returns list of Tags and strings.
"""
#resultURL=soup.find_all('a')
#print(resultURL)
#first_resulttest.find('a')
#first_resulttest.find('a')['href'] #tag and his value as dictionary,i.e. href is like a dictionary key.

####################################################################################################################################
#r=requests.get('any url')
#results=soup.find_all('span',attrs={'class':'short-desc'})

#print(len(results))

#results[0:3]

#soup=BeautifulSoup(r.text,'html.parser')

#records=[]
#for result in results:
    #date=result.find('strong').text[0:-1] +'string text'
    #lie=result.contents[1][1:-2]
    #explanation=result.find('a').text[1:-1]
    #url=result.find('a')['href']
    #records.append((date,lie,explanation,url))  #tuple of length 4


#################################################################################################################################

#from urllib import request

#resp=request.urlopen("https://en.wikipedia.org/wiki/Main_Page")
#print(resp.code)
#print(dir(urllib))
#print(resp.length)
#print(resp.peek())

#data = resp.read()
#html = data.decode("UTF-8")
#print(html)
#print("##########################################################################################################################################")

#resp=request.urlopen("https://www.google.com/search?q=socratia")

#from urllib import parse
#print(dir(parse))
#https://www.youtube.com/watch?v=EuC-yVzHhMI&t=5m56s
#params = {"v":"EuC-yVzHhMI","t":"5m56s"}
#querystring = parse.urlencode(params)
#print(params)
#url = "https://www.youtube.com/watch" + "?" + querystring
#resp = request.urlopen(url)

#html = resp.read().decode("utf-8")
#print(html[:20])
