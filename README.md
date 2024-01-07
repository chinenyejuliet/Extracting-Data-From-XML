# Extracting-Data-From-XML

## Project Overview
This program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file and enter the sum. It will look through all the <comment> tags and find the <count> values sum the numbers

### Data Sources
The xml document used in this project is from Python for Everybody autograder assignment one of the [Coursera](www.coursera.org) online courses.

[Download XML file]( http://py4e-data.dr-chuck.net/comments_1879662.xml) 

```python3
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
```
