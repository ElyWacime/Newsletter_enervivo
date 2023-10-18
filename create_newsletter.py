from utils import *
import json

FINAL_DICT = {}

def generate_article_for_event_agri():
    articles = None
    while type(articles) != int:   
        articles = input(
            "How many articles would you like to genarate in Evènements agrivoltaïques? "
        )
        try:
            articles = int(articles)
        except ValueError:
            print('Please pick an integer!')
    if 'Evenements_agrivoltaiques' not in FINAL_DICT:
        FINAL_DICT['Evenements_agrivoltaiques'] = {}
    i = 0
    while(i < articles):
        url = input(f"Enter the link for the {i+1} article: ")
        description = generate_description(url)
        title = generate_title(url)
        image = generate_image(url)
        generate_dict(title=title, image=image, description=description,
                    section="Evenements_agrivoltaiques", final_dict=FINAL_DICT, i=i)
        i+=1

def generate_article_for_march_regl():
    articles = None
    while type(articles) != int:    
        articles = input(
            "How many articles would you like to genarate in Marché & Règlementation? "
        )
        try:
            articles = int(articles)
        except ValueError:
            print('Please pick an integer!')
        
    if 'Marche_&_Reglementation' not in FINAL_DICT:
        FINAL_DICT['Marche_&_Reglementation'] = {}
    i = 0
    while(i < articles):
        url = input(f"Enter the link for the {i+1} article: ")
        description = generate_description(url)
        title = generate_title(url)
        image = generate_image(url)
        generate_dict(title=title, image=image, description=description,
                    section="Marche_&_Reglementation", final_dict=FINAL_DICT, i=i)
        i+=1

def generate_article_for_tech_entpr():
    articles = None
    while type(articles) != int:    
        articles = input(
            "How many articles would you like to genarate in Technologie, R&D et entreprises? "
        )
        try:
            articles = int(articles)
        except ValueError:
            print('Please pick an integer!')
        
    if 'Technologie, R&D et entreprises' not in FINAL_DICT:
        FINAL_DICT['Technologie, R&D et entreprises'] = {}
    i = 0
    while(i < articles):
        url = input(f"Enter the link for the {i+1} article: ")
        description = generate_description(url)
        title = generate_title(url)
        image = generate_image(url)
        generate_dict(title=title, image=image, description=description,
                    section="Technologie, R&D et entreprises", final_dict=FINAL_DICT, i=i)
        i+=1

def generate_article_for_monde():
    articles = None
    while type(articles) != int:    
        articles = input(
            "How many articles would you like to genarate in monde? "
        )
        try:
            articles = int(articles)
        except ValueError:
            print('Please pick an integer!')
        
    if 'monde' not in FINAL_DICT:
        FINAL_DICT['monde'] = {}
    i = 0
    while(i < articles):
        url = input(f"Enter the link for the {i+1} article: ")
        description = generate_description(url)
        title = generate_title(url)
        image = generate_image(url)
        generate_dict(title=title, image=image, description=description,
                    section="monde", final_dict=FINAL_DICT, i=i)
        i+=1

generate_article_for_event_agri()
"""generate_article_for_march_regl()
generate_article_for_tech_entpr()
generate_article_for_monde()"""

newsletter_key = input("Please enter the date of your newsletter month/year (example: janvier23, september23): ")

data = json.dumps(FINAL_DICT)
send_post_reauest(data=data, url=f"http://127.0.0.1:5000/store?key={newsletter_key}")
print(data)