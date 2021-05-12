#pip install bs4 requests
from bs4 import BeautifulSoup
import requests
import telegram
from hotdeal.models import Deal
from datetime import datetime, timedelta
BOT_TOKEN = "0123456789:AAAAAAAAAAAAAAAAAAAAAAAAAAA"
bot = telegram.Bot(token=BOT_TOKEN)
chat_id = -123456789

response = requests.get("http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu")
soup = BeautifulSoup(response.text, "html.parser")

def run():
    
    ## delete deals older than 3days
    row, _ = Deal.objects.filter(created_at__lte=datetime.now() - timedelta(days=3)).delete()
    print(row, "deals deleted")
    # title = soup.find_all("font", class_="list_title")
    for item in soup.find_all("tr", {'class': ["list1", "list0"]}):
        try:
            image = "http://" + item.find("img", class_="thumb_border").get("src")[2:]
            title = item.find("font", class_="list_title").text.strip()
            link = item.find("font", class_="list_title").parent.get("href")
            link = "http://www.ppomppu.co.kr/zboard/" + link
            reply_count = int(item.find("span", class_="list_comment2").text)
            up_count = item.find_all("td")[-2].text
            up_count = int(up_count.split("-")[0])
            if(up_count > 0):
                if (Deal.objects.filter(link__iexact=link).count() == 0):
                    Deal(image_url=image, title=title, link = link, reply_count=reply_count, up_count=up_count).save()
                    bot.sendMessage(chat_id, '{} {}'.format(title, link))
        except Exception as e:
            continue
        # print(item.text)