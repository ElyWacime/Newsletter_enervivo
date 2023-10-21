from utils import *
import json
from urllib.parse import urlparse

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
    if 'Evènements agrivoltaïques' not in FINAL_DICT:
        FINAL_DICT['Evènements agrivoltaïques'] = {}
    i = 0
    while(i < articles):
        url = input(f"Enter the link for the {i+1} article: ")
        description = generate_description(url)
        description = change_description(description)
        title = generate_title(url)
        title = change_title(title)
        image = generate_image(url)
        date = generate_date(url)
        parsed_url = urlparse(url)
        domaine = parsed_url.netloc
        generate_dict(url=url, domaine=domaine, date=date, title=title, image=image, description=description,
                    section="Evènements agrivoltaïques", final_dict=FINAL_DICT, i=i)
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
        
    if 'Marché & Règlementation' not in FINAL_DICT:
        FINAL_DICT['Marché & Règlementation'] = {}
    i = 0
    while(i < articles):
        url = input(f"Enter the link for the {i+1} article: ")
        description = generate_description(url)
        description = change_description(description)
        title = generate_title(url)
        title = change_title(title)
        image = generate_image(url)
        date = generate_date(url)
        parsed_url = urlparse(url)
        domaine = parsed_url.netloc
        generate_dict(url=url, domaine=domaine, date=date, title=title, image=image, description=description,
                    section="Marché & Règlementation", final_dict=FINAL_DICT, i=i)
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
        description = change_description(description)
        title = generate_title(url)
        title = change_title(title)
        image = generate_image(url)
        date = generate_date(url)
        parsed_url = urlparse(url)
        domaine = parsed_url.netloc
        generate_dict(url=url, domaine=domaine, date=date, title=title, image=image, description=description,
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
        description = change_description(description)
        title = generate_title(url)
        title = change_title(title)
        image = generate_image(url)
        date = generate_date(url)
        parsed_url = urlparse(url)
        domaine = parsed_url.netloc
        generate_dict(url=url, domaine=domaine, date=date, title=title, image=image, description=description,
                    section="monde", final_dict=FINAL_DICT, i=i)
        i+=1

def generate_actualite():
    articles = None
    while type(articles) != int:    
        articles = input(
            "How many actuality would you like to genarate? "
        )
        try:
            articles = int(articles)
        except ValueError:
            print('Please pick an integer!')
        
    if "Les actualités d'EnerVivo" not in FINAL_DICT:
        FINAL_DICT["Les actualités d'EnerVivo"] = {}
    i = 0
    while(i < articles):
        url = input(f"Enter the link for the {i+1} actuality: ")
        description = generate_description("https://thisIsAJoke.io")
        title = generate_title("https://thisIsAJoke.io")
        image = generate_image(title)
        date = generate_date("https://thisIsAJoke.io")
        generate_dict(url=url, domaine="enervivo.fr", date=date, title=title, image=image, description=description,
                    section="Les actualités d'EnerVivo", final_dict=FINAL_DICT, i=i)
        i+=1

def main():
    generate_article_for_event_agri()
    generate_article_for_march_regl()
    generate_article_for_tech_entpr()
    generate_article_for_monde()
    generate_actualite()

    newsletter_key = input("Please enter the date of your newsletter month/year (example: janvier23, september23): ")
    FINAL_DICT["newsletter_description"] = generate_description_for_newsletter()
    data = json.dumps(FINAL_DICT)
    send_post_reauest(data=data, url=f"http://api.enervivo.fr/store?key={newsletter_key}")
    edit_newsletter_date(newsletter_key)
    print(data)

main()