import urllib.request
link = "https://www.imdb.com/title/tt4154796/"
fp = urllib.request.urlopen(link)
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(html)