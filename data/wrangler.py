import csv
import re

'''
{'asianfusion', 'lounges', 'seafood', 'juicebars', 'coffee', 
'french', 'donuts', 'armenian', 'ukrainian', 'bangladeshi', 'cantonese', 
'foodtrucks', 'catering', 'hotdogs', 'cocktailbars', 'greek', 'sandwiches', 
'mideastern', 'halal', 'polish', 'desserts', 'delis', 'chinese', 
'pakistani', 'spanish', 'sushi', 'cupcakes', 'bars', 'salad', 'dimsum', 
'falafel', 'wine_bars', 'burgers', 'himalayan', 'cheesesteaks', 'diners', 
'mongolian', 'mexican', 'latin', 'gluten_free', 'shopping', 'steak', 
'grocery', 'raw_food', 'bakeries', 'bubbletea', 'cheese', 'tapasmallplates', 
'korean', 'cafes', 'vegan', 'foodstands', 'breakfast_brunch', 'italian',
 'pubs', 'newamerican', 'tradamerican', 'pizza', 'hotpot', 'ramen', 
 'turkish', 'icecream', 'mediterranean', 'gastropubs', 'japanese', 
 'vietnamese', 'ethnicmarkets', 'vegetarian', 'thai', 'belgian', 'indpak'}
 (71)
'''

tags = set()

with open("yelp_boston.csv", mode="r") as f:
    csvfile = csv.reader(f)
    for line in csvfile:
        formatted = re.sub(r"[\[\],.;@#?'!]+", '', line[3])
        formatted_tags = formatted.split('" ')[1::2]
        for tag in formatted_tags:
            tags.add(tag.strip('"'))

print(tags)
print(len(tags))