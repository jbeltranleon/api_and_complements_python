from urllib.request import urlopen

url = "http://lorempixel.com/640/480/sports/"
placeholder = urlopen(url)
content = placeholder.read()

print (content)