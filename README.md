# scraplinks
Project to show how to scrape a web to get all the links of a specific section

First of all you need to install your dependencies, in this time you will need those who are in requirements.txt

Just run in your virtual enviroment of python3 the next command:

pip install -r requirements.txt

Now you have to know the target you want to scrape, in this case I will scrape www.maxmovil.com which is a vertical of mobile phones in Spain.

This url will be the base:
  - https://www.maxmovil.com/es/moviles-libres.html

I will get all the url's to the details of a mobile, the image, the price and the name and show it in a pandas dataframe. In pandas its very easy to export to excel, csv, etc, thats why.

![Alt text](/../master/maxmovil.png?raw=true "Maxmovil.net")

Now I want to find where are the url of each link, for that I use the "Inspect Element" tool of google, find in the text (Command+F in Mac, Ctrl + F in Windows/Linux) and in this particular case I search for the price (because the brand of the car could appear in Select's Boxes):

![Alt text](/../master/finding_anchor.png?raw=true "Maxmovil.net")

We can see in the image that the anchor is wrapped in a div with css class "item-area", we would have to find childs with the anchor, image, title and price!


This scene will help us to:
  - Get an attribute of an HTML Element
  - Get the text inside of an HTML element
  - Travel to the child of an element and get the text
  - Get the url of an image in the website

Once you complete the "tutorial" you will be able to do that by yourself and earn some extra cash scrapping some webs for fun&profit!!

Thank you!

Follow me on:
  - [Twitter](https://www.twitter.com/s3ik0tr0n)
  - [Instagram](https://www.instagram.com/romerodelosllanos)
  - [LinkedIn](https://www.linkedin.com/in/miguel-angel-romero-de-los-llanos-94607747/)
