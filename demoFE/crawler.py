from bs4 import BeautifulSoup
import requests

def crawl(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    title = soup.findAll('h1',attrs={'class': 'article-title'})[0].text
    desc = soup.findAll('h2',attrs={'class': 'sapo'})[0].text
    content = soup.findAll('div',attrs={'class': 'content fck'})[0]
    content_p = content.findAll('p', recursive=False)
    content_text = ''
    img_container = soup.findAll('div', attrs={'class': 'VCSortableInPreviewMode'})
    for item in img_container:
        try:
            print(item.img['data-original'])
        except:
            pass


    # for p in content_p:
    #     content_text += p.text
    # return {
    #     'article_title': title,
    #     'article_desc': desc,
    #     'article_content': content_text
    # }

url ='https://tuoitre.vn/tong-bi-thu-nguyen-phu-trong-chu-tri-hop-bo-chinh-tri-ban-bi-thu-2022091017315747.htm'
crawl(url)