from bs4 import BeautifulSoup

with open("index.html") as file:
    html_doc = file.read()

obj = BeautifulSoup(html_doc, "html.parser")

head = obj.head
div_content_1 = obj.body.div.contents[1]
div_content_2 = obj.body.div.contents[3].contents[1]

for child in obj.body.div.children:
    if child != "\n":
        print(child)

for child in obj.body.div.descendants:
    if child != "\n":
        print(child)

h2 = obj.body.h2
div = h2.parent
div2 = div.next_sibling.next_sibling

third_li = obj.find(class_="ucuncu")
second_li = third_li.previous_sibling.previous_sibling
first_li = second_li.find_previous_sibling('li')

lis = third_li.find_previous_siblings('li')

ul = first_li.parent.parent
div = first_li.find_parent('div')

print(div)