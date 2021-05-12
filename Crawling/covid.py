
from bs4 import BeautifulSoup
import requests
import telegram

BOT_TOKEN = "0123456789:AAAAAAAAAAAAAAAAAAAAAAAAAAA"
bot = telegram.Bot(token=BOT_TOKEN)
chat_id = -123456789

html = requests.get('https://search.naver.com/search.naver?query=코로나+확진자')
#pprint(html.text)

soup = BeautifulSoup(html.text, 'html.parser')

try:
    status = soup.find('div', {'class': 'status_info'})

    data1 = status.find('li', {'class': 'info_01'})
    data1_total = data1.find('p', {'class': 'info_num'}).text
    data1_count = data1.find('em', {'class': 'info_variation'}).text

    data2 = status.find('li', {'class': 'info_02'})
    data2_total = data2.find('p', {'class': 'info_num'}).text
    data2_count = data2.find('em', {'class': 'info_variation'}).text

    data3 = status.find('li', {'class': 'info_03'})
    data3_total = data3.find('p', {'class': 'info_num'}).text
    data3_count = data3.find('em', {'class': 'info_variation'}).text

    data4 = status.find('li', {'class': 'info_04'})
    data4_total = data4.find('p', {'class': 'info_num'}).text
    data4_count = data4.find('em', {'class': 'info_variation'}).text

    #print(data1 + '▲\n' + data2 + '▲\n' + data3 + '▲\n' + data4 + '▲\n')
    message = '확진환자: ' + data1_count + '↑ (총 ' +  data1_total + '명)\n'
    message += '검사진행: ' + data2_count + '↑ (총 ' +  data2_total + '명)\n'
    message += '격리해제: ' + data3_count + '↑ (총 ' +  data3_total + '명)\n'
    message += '사망자: ' + data4_count + '↑ (총 ' +  data4_total + '명)\n'

    status_today = soup.find('div', {'class': 'status_today'})
    today = status_today.find('li', {'class': 'info_01'}).text
    국내 = status_today.find('li', {'class': 'info_02'}).text
    해외 = status_today.find('li', {'class': 'info_03'}).text

    #print(today + ':' + 국내 + '명,' + 해외 + '명')
    message += '\n' + today + '\n - ' + 국내 + '명\n - ' + 해외 + '명'
    #print(message)
except Exception as e:
    message += '\n 오류 발생으로 일부만 불러왔습니다.'

#print(message)

bot.sendMessage(chat_id, '{}'.format(message))

