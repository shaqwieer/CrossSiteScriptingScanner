from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import time


#this function crawls through a url to find othre urls, and recursivly 
#calls itself to go through each url it finds until there are no more urls
#it then stores all urls in (found_urls)
#it also handles the depth of the crawl with depth 1 being "example.com/tag/"
#and depth 2 being "example.com/tag1/tag2/"
def crawler(start_domain,found_urls, depth = 100):
    if (start_domain not in found_urls) and (len(urlparse(start_domain).path.split('/'))<=depth): #checking if url is already found and verifying its depth
        start = time.time() #a timer to close the connection
        while(True and (time.time()-start<10)):
            try:
                req = Request(start_domain) #open the url
                html = urlopen(req).read().decode('utf-8',"ignore")
                found_urls.append(start_domain) #add to found_urls
                print(start_domain)
                break
            except Exception as e:
                print(e)
                continue
        domain_html= BeautifulSoup(html,'html5lib')
        tags = domain_html.find_all("a",{"href": True}) #find all a tags with href values in them
        hrefs = []
        for tag in tags: #going through each tag and extracting the href
            href = tag['href']
            href_netloc = urlparse(href).netloc 
            if (href != '#'): #checking if href is local
                if (href_netloc == '' or href_netloc == urlparse(start_domain).netloc ): #checking if href is a path or if it is or another domain
                    if(href_netloc == ''):
                        href_new = urljoin(start_domain,href) # joining the path to the original domain
                        if href_new not in hrefs:    
                            hrefs.append(href_new)
                    elif href not in hrefs:    
                        hrefs.append(href)
        for href in hrefs:                    
            crawler(href,found_urls,depth) #recursion




    