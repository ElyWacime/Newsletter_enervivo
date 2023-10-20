import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.text
    else:
        print("Failed to retrieve the web page!")
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
        description = input("Web scraping is not allowed please enter the description manully: ")
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
        title = input("Web scraping is not allowed please enter the title manully: ")
        return title
    
def generate_image(url):
    html_content = get_html_content(url)
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        body = soup.find('body')
        image = body.find("img")
        if image:
            print("image: success!")
        else:
            image = input("Please enter the image src code manully: ")
            return image
        return image['src'] if image else 0
    else:
        image = input("Web scraping is not allowed please enter the image src code manully: ")
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
        
    
def generate_dict(title, description, image, final_dict, section, i):
    final_dict[section][str(i)] = {"title": title,
                        "description": description,
                        "image": image}
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
    
print(generate_date("https://www.lafranceagricole.fr/ovins-et-caprins/article/844133/tech-ovin-une-edition-tournee-vers-la-durabilite"))