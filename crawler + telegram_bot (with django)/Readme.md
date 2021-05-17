#### git clone으로 긁어온 뒤, pip로 설치
```
pip3 install django django_extensions djangorestframework requests bs4 python-telegram-bot
```

#### settings.py 수정
```
# 본인 DNS 및 IP를 허용해줌

ALLOWED_HOSTS = ['52.78.190.249']
```

<br>

#### 관리자 생성
```
python3 manage.py createsuperuser
```

#### 장고 실행
```
python3 manage.py runscript crawler
python3 manage.py runserver 0.0.0.0:80
```

#### 백그라운드 실행
```
nohup python3 manage.py runserver 0.0.0.0:80 &
```

<br>


#### 크론탭 등록
```
$ crontab -e

* * * * * cd /root/Python/crawler/web && python3 manage.py runscript crawler
# - 1분마다

*/3 * * * * cd /root/Python/crawler/web && python3 manage.py runscript crawler 
# - 3분마다
```

<br>
<br>

### 전체적인 흐름
```
pip3 install bs4 requests
pip3 install python-telegram-bot

pip3 install django
pip3 install django_extensions
 - settings.py에 django_extensions 추가
```

#### 모델 변경 및 추가시
```
python manage.py makemigrations
python manage.py migrate
```
python manage.py runscript crawler

#### api 사용
```
pip3 install djangorestframework
```

serializers.py 생성 <br>
views.py 수정 <br>
urls.py 수정 <br>

<br>

손쉽게 사용 가능
