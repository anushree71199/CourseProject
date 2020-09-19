"""
Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_960597.json (Sum ends with 36)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
"""
#CODE
import json
import urllib.request,urllib.parse,urllib.error
url=input("Enter: ")
data=urllib.request.urlopen(url).read().decode()
item=json.loads(data)
print("Count: ",len(item))
sum=0
for i in range(0,len(item["comments"])):
sum=sum+int(item["comments"][i]["count"])
print(sum)