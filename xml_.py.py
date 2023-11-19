import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter location: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1879662.xml"
print("Retrieving ", url)
data = urllib.request.urlopen(url).read()
print("Retrieving", len(data.decode()), "characters")
tree = ET.fromstring(data.decode().strip())
tree_collection = tree.findall('comments/comment')
#print(tree_collection)
print('Count', len(tree_collection))
total = 0
for tree in tree_collection:
    nam = tree.find('name').text
    x = tree.find('count').text
    num = int(x)
    total = total + num
    #print(nam)
    #print(num)
print("SUM:",total)