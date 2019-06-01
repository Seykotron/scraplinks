
from bs4 import BeautifulSoup
import pandas as pd
import requests

session = requests.Session()

# We setup the headers to mimic a browser
session.headers.update({
    "accept-encoding" : "gzip, deflate, br",
    "accept-language": "es-ES,es;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "referer": "https://www.maxmovil.com/",
    "upgrade-insecure-requests": 1,
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
})

# First of all we setup our url, the one we want to scrape on
url = "https://www.maxmovil.com/es/moviles-libres.html"

# Now we make a request to get the content of that url
# Let me know in my social's if you need to know how to do the same but within a session in the webpage (for example for web's which requires an user and password)
result = requests.get( url )

# We can see if the request was successfull by looking at the status_code attribute of result
print( "StatusCode: %s" % result.status_code )
# You also can take a look into the headers that coches.net send to us
print( "Headers:\n%s" % result.headers  )

#print( "Content: \n%s" % result.content )

# Now we load the content of the request into our beautifulsoup class to do the magic
# The attribute *content* contains the html we want to parse on
soup = BeautifulSoup(result.content, "lxml")

# Now we search the nodes wich have the css class that we are interested, in this case our content are wrapped in a div with css class of details-area
elements = soup.find_all( "div", { "class" : "item-area" } )

mobiles = []

# I do enumerate to have access to the index of the element
for i,element in enumerate( elements ):
    # Now we search for the anchors inside that element
    anchors = element.find_all( "a" )
    element_url     = ""
    element_title   = ""
    price_txt       = ""
    price_number    = 0
    element_img     = ""
    for x,anchor in enumerate(anchors):
        # I do always preffer use the "get" method instead of ["href"] because it give us the hability of set it empty
        element_url = anchor.attrs.get("href","")

        # We can get the title which is in the "tittle" attribute
        element_title = anchor.attrs.get("title", "")

        # I do always do a "print" to check if its working, uncomment to see it, and also know what is the index of the href that we need
        #print( "%s %s" %( x,element_url) )

        # To reach the img we only have to retrieve the first child of the anchor
        img_tag = anchor.findChild()
        element_img = img_tag.attrs.get("src","")

        # In this case we need just the first so we can break the loop
        break

    # We print the url to check if everything is fine
    #print( element_url )

    # Now we get the price which is in a span with css class of "price"
    prices = element.find_all( "span", { "class" : "price" } )
    for price in prices:
        # With strip we clean the trailing blank spaces that always have the elements
        price_txt = price.text.strip()
        # We split the number by \xa0 wich are the & character to avoid &nbsp; and get only the number
        price_number = price_txt.split("\xa0")[0]
        break

    print( "+"*65 )
    print( "URL: %s" % element_url )
    print( "Title: %s" % element_title )
    print( "Price: %s €" % price_number )
    print( "Img: %s" % element_img )
    print( "+"*65 )

    mobiles.append( { "url" : element_url, "title": element_title, "price" : price_number, "img" : element_img } )
    df = pd.DataFrame( mobiles )
    print( "\n"*3 )
    print( df.head() )
