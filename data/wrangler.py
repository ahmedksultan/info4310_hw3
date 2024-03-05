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

tag_ctr = {}
nbhd_ctr = {}

with open("yelp_boston.csv", mode="r") as f:
    csvfile = csv.reader(f)
    
    for line in csvfile:
        
        formatted = re.sub(r"[\[\],.;@#?'!]+", '', line[3])
        formatted_tags = formatted.split('" ')[1::2]
        
        for tag in formatted_tags:
            tag = tag.strip('"')
            # trying to get sense check
            if tag in tag_ctr.keys():
                tag_ctr[tag] += 1
            else:
                tag_ctr[tag] = 1
            
        nbhd = line[7]
        if line[7] in nbhd_ctr.keys():
            nbhd_ctr[line[7]] += 1
        else:
            nbhd_ctr[line[7]] = 1
            


tag_ctr_sorted = dict(sorted(tag_ctr.items(), key=lambda item : item[1], reverse=True))
nbhd_ctr_sorted = dict(sorted(nbhd_ctr.items(), key=lambda item : item[1], reverse=True))


print(len(tag_ctr_sorted.keys()))

print(tag_ctr_sorted)

print(len(nbhd_ctr_sorted.keys()))

print(nbhd_ctr_sorted)

