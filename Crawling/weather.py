from bs4 import BeautifulSoup
import requests
import telegram

BOT_TOKEN = "0123456789:AAAAAAAAAAAAAAAAAAAAAAAAAAA"
bot = telegram.Bot(token=BOT_TOKEN)
chat_id = -123456789

html = requests.get('https://search.naver.com/search.naver?query=서울+날씨')
#pprint(html.text)

soup = BeautifulSoup(html.text, 'html.parser')

try:
    data1 = soup.find('div', {'class': 'weather_box'})
    find_address = data1.find('span', {'class':'btn_select'}).text
    message = '현재 위치: '+find_address+'\n'
    #print('현재 위치: '+find_address)

    find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
    find_mintemp = data1.find('span',{'class': 'min'}).text
    find_maxtemp = data1.find('span',{'class': 'max'}).text
    message += '현재 온도: '+find_currenttemp+'℃ (' + find_mintemp+'/'+find_maxtemp + ')\n'
    #print('현재 온도: '+find_currenttemp+'℃ (' + find_mintemp+'/'+find_maxtemp + ')')

    find_cast_txt = data1.find('p',{'class': 'cast_txt'}).text
    message += ' - ' + find_cast_txt + '\n\n'
    #print(find_cast_txt)

    sensible = data1.find('span',{'class': 'sensible'}).text
    message += sensible + '\n'
    #print(sensible)

    data2 = data1.findAll('dd')
    find_dust = data2[0].find('span', {'class':'num'}).text
    find_ultra_dust = data2[1].find('span', {'class':'num'}).text
    find_ozone = data2[2].find('span', {'class':'num'}).text

    message += '현재 미세먼지: '+find_dust + '\n현재 초미세먼지: ' + find_ultra_dust + '\n현재 오존지수: '+find_ozone
    #print('현재 미세먼지: '+find_dust)
    #print('현재 초미세먼지: '+find_ultra_dust)
    #print('현재 오존지수: '+find_ozone)


except Exception as e:
    message += '\n 오류 발생으로 일부만 불러왔습니다.'

#print(message)
bot.sendMessage(chat_id, '{}'.format(message))
