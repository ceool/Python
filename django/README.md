## AWS EC2와 RDS를 이용한 장고 DB 연동 웹
![2](https://user-images.githubusercontent.com/62891711/104141093-518b2380-53f8-11eb-94c7-11814dcd6509.png)
![3](https://user-images.githubusercontent.com/62891711/104141096-52bc5080-53f8-11eb-97ef-93e05de55e31.png)
![제목 없음](https://user-images.githubusercontent.com/62891711/104141049-096c0100-53f8-11eb-8061-6c018b357ac5.png)



생성시 RDS 파라미터 그룹 character_set 검색해서 전부 utf-8<br>
 collation_connection = utf8_general_ci<br>
 collation_server = utf8_general_ci<br>
<br>
django-admin startproject mysite<br>
python manage.py startapp polls<br>
<br>
### mysite/settings.py 수정
```
LANGUAGE_CODE = 'ko-kr' 
TIME_ZONE = 'Asia/Seoul'
#오류뜨면 USE_TZ = False

host 추가
ALLOWED_HOSTS = ['example.com', 'www.example.com', 'localhost', '2.2.2.2'] 등

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_db',
        'USER': 'admin',
        'PASSWORD': '비밀번호',
        'HOST': 'database-1.********.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}


INSTALLED_APPS = [
    'polls.apps.PollsConfig',   #이건 startapp한 이름의 폴더의 apps.py의 클래스 이름.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```
-----------------------------------------------------<br>
<br><br>
python manage.py inspectdb -> startapp * 이면 */models.py 수정<br>
or python manage.py inspectdb > */models.py<br>
<br><br>

### startapp polls 이면, polls/admin.py 수정
```
from django.contrib import admin
from .models import 모델 클래스 이름

# 클래스를 어드민 사이트에 등록한다.
admin.site.register(모델 클래스 이름)
```
-----------------------------------------<br>
<br>
python manage.py makemigrations<br>
python manage.py migrate<br>
python manage.py createsuperuser<br>
계정 생성<br>
<br>

### 프로젝트이름/urls.py 추가
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('스타트앱이름.urls')),
]
```
-----------------------------------------<br>
<br>
스타트앱이름/templates/스타트앱이름/index.html 작성<br>
<br>
### 스타트앱이름/views.py 작성
```
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.all() #Blog에 있는 모든 객체를 불러와 blogs에 저장
    context = {'blogs':blogs}

    return render(request, 'polls/index.html', context) # index.html에 context 내용 삽입
```
-----------------------------------------<br>
<br>
<br>
python manage.py runserver 0.0.0.0:80<br>
<br>
<br>
INSERT INTO polls_blog VALUES (3, '테스트3', '테스트3 입니다.', NOW(), NOW());<br>
DELETE FROM polls_blog WHERE ID = '1';<br>

<br><br>
```
EC2: ssh -i "test-01.pem" ubuntu@******.compute-1.amazonaws.com
DB: mysql -u admin -p -h database-1.*****.us-east-1.rds.amazonaws.com
```
![4](https://user-images.githubusercontent.com/62891711/104141196-dfffa500-53f8-11eb-9d6c-f90dc39053c8.png)
![5](https://user-images.githubusercontent.com/62891711/104141222-150bf780-53f9-11eb-9efb-9e5decc5213b.png)


