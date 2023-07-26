#!/usr/bin/python3
import re

# open the input file for reading
file = open('mountain.html')
# read the entire file
text = file.read()
# split into lines
lines = text.splitlines()

print("0. Example: All tags.")
matches = re.findall(r'<[^>]+>', text)
for s in matches:
    print(s)
print("total: ", len(matches))

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")


print("1. All tags without attributes.")
print("total: ")

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

print("2. Start tags with 1 or more attributes.")
print("total: ")

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

print("3. Lines containing at least two tags, where those tags have a name with three or more characters.")
print("total:" )

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

print("4. Div tags with id that contains *im*.")
# Example: <div id="himg"> or <div class="imgc" id="imgcont">
print("total: ")

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

print("5. The value of the href attribute in the <a> tags.")
# Print just the values.  
# Example: http://app.dictionary.com/favorites
print("total: ")

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

print("6. Lines containing a <div> tag that has a class attribute with a value containing the string 'tx'.")
# Replace tx with TX and preserve other attributes (if any).
# Example: replace <div class="ftxt1" style="display:block;width:350px;"> with <div class="fTXt1" style="display:block;width:350px;">
print("total: ")

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

print("7. The content of all style tags.")
# Example: 
#   <style type="text/css">
#       ...
#       ...
#   </style>
print("total: ")

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

print("8. The synonyms of the word mountain listed in the file")
# Load mountain.html into a browser or text editor to see the list of synonyms.
print("total: ")

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")