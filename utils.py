import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_html_content(url):
    try:        
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
        else:
            print("Failed to retrieve the web page!")
        return 0
    except requests.exceptions.ConnectionError:
        return 0

def generate_description(url):
    html_content = get_html_content(url)
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        description = soup.find('meta', attrs={'name': 'description'})
        if description:
            print("description: success!")
        else:
            description = input("Please enter the description manualy: ")
            return description
        return description['content'] if description else 0
    else:
        description = input("Please enter the description manully: ")
        return description
    
def generate_title(url):
    html_content = get_html_content(url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.find('title')
        if title == None:
            title = soup.find('h1')
        if title:
            print("title: success!")
        else:
            title = input("Please enter the title manully: ")
            return title
        return title.get_text() if title else 0
    else:
        title = input("Please enter the title manully: ")
        return title
    

"""def generate_image(url):
    html_content = get_html_content(url)
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        
        images = soup.find_all("img")
        
        for image in images:
            src = image.get('src')
            
            if src and '.svg' not in src and ".png" not in src:
                if "https" not in src:
                    parsed_url = urlparse(url)
                    domaine = parsed_url.netloc
                    src = "https://" + domaine + src
                    print("Image: success!")
                    return src
                print("Image: success!")
                return src

        image = input("No suitable image found. Please enter the image src code manually: ")
        return image
        
    else:
        image = input("Web scraping is not allowed. Please enter the image src code manually: ")
        return image"""

def generate_image(article):
    image = None
    while (image == None):
        image = input(f"Please enter the image source code for {article}: ")
    return image

def generate_date(url):
    html_content = get_html_content(url)
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        meta_tag = soup.find('meta', attrs={'property': 'og:updated_time'})
        if meta_tag:
            title = meta_tag["content"]
            return title
        else:
            time_tag = soup.find('time', attrs={'itemprop': 'dateCreated'})
            if time_tag:
                title = time_tag.get_text(strip=True)
                return title
            else:
                return None
    else:
        date = input("Please enter the date: ")
        return date
        
    
def generate_dict(url, domaine, title, description, image, final_dict, section, i, date):
    final_dict[section][str(i)] = {"title": title,
                        "description": description,
                        "image": image,
                        "date": date,
                        "domaine": domaine,
                        "url": url}
    return final_dict

def send_post_reauest(data, url):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        print("POST request: success!")
    else:
        print(f"POST request failed with status code {response.status_code}: {response.text}")

def extract_all_images(url):
    res = requests.get(url, headers={"User-Agent": "Mozilla/5,0"})
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        images = soup.find_all("img")
        return images
    
def edit_newsletter_date(newsletter_key):
    try:
        with open("index.html", "r") as file:
            file_contents = file.read()
    except FileNotFoundError:
        print("Couldn't find the html file!")
    try:
        if "EDIT THIS STRING" in file_contents:
            new_content = file_contents.replace("**EDIT THIS STRING**", newsletter_key)
            try:
                with open("newsletter.html", "w") as file:
                    file.write(new_content)
            except FileNotFoundError:
                print("Couldn't find the html file!")
    except UnboundLocalError:
        return 0
    
def generate_description_for_newsletter():
    description = input("Please enter the description for the newsletter: ")
    return description

def change_description(description):
    change = input(f"Is this the description that you wanna publish?\n{description}\n(answer: y/n): ")
    if change == "n":
        new_description = input("Please enter the new description: ")
        return new_description
    else:
        return description
    
def change_title(title):
    change = input(f"Is this the title that you wanna publish?\n{title}\n(answer: y/n): ")
    if change == "n":
        new_title = input("Please enter the new description: ")
        return new_title
    else:
        return title