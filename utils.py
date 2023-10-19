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
        print("description: succsess!") if description else 0
        return description['content'] if description else 0
    
def generate_title(url):
    html_content = get_html_content(url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.find('title')
        print("title: success!") if title else 0
        return title.get_text() if title else 0
    
def generate_image(url):
    html_content = get_html_content(url)
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        body = soup.find('body')
        image = body.find("img")
        print("image: success!") if image else 0
        return image['src'] if image else 0
    
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

'''print(generate_title("https://tecsol.blogs.com/mon_weblog/2023/07/loi-dacc%C3%A9l%C3%A9ration-sur-les-%C3%A9nergies-renouvelables-aer-quelles-opportunit%C3%A9s-pour-le-photovolta%C3%AFque-sur.html"))

print("----------------")

print(generate_description("https://tecsol.blogs.com/mon_weblog/2023/07/loi-dacc%C3%A9l%C3%A9ration-sur-les-%C3%A9nergies-renouvelables-aer-quelles-opportunit%C3%A9s-pour-le-photovolta%C3%AFque-sur.html"))

print("----------------")

print(generate_image("https://tecsol.blogs.com/mon_weblog/2023/07/loi-dacc%C3%A9l%C3%A9ration-sur-les-%C3%A9nergies-renouvelables-aer-quelles-opportunit%C3%A9s-pour-le-photovolta%C3%AFque-sur.html"))'''