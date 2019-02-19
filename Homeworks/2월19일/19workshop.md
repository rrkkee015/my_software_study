# Python 활용 SQL

> Background

```
- SQL
- Django Model
```

> Goal

```
Django Modeling
```

> Problem

- 문제

  자신의 반에 있는 사람들의 데이터를 저장하는 Student 모델을 생성합니다.

  Student모델이 가져야 할 필드는 아래와 같습니다.

- name(이름) : CharField

  email(이메일) : CharField

  birthday(생년월일) : DateField

  age(나이) : IntegerField

  > Student/info/models.py

  ```python
  from django.db import models
  
  # Create your models here.
  class Info(models.Model):
      name=models.CharField(max_length=10)
      email=models.CharField(max_length=100)
      birthday=models.DateField()
      age=models.IntegerField()
  ```

- 17workshop에서 만든 모델을 활용해서 학생들의 정보를 저장하는 CRUD 페이지를 구현하세요

  ## HTML

  >index.html

  ```html
  <h1><a href="/info/student_list/">학생기록부</a></h1>
  ```

  > student_list.html

  ```html
  <h1>학생기록부</h1>
  <a href="/info/add/">학생 추가하기</a>
  {% for i in stu_list %}
  <p><a href="/info/{{i.id}}/detail/">{{i.id}}</a>, {{i.name}}</p>
  {% endfor %}
  ```

  >add.html

  ```html
  <form action="/info/create/" method="POST">
      <p>이름</p>
      <input type="text" name="name"/>
      <p>이메일</p>
      <input type="text" name="email"/>
      <p>생일</p>
      <input type="date" name="birthday"/>
      <p>나이</p>
      <input type="number" min="1" max="100" name="age"/>
      <input type="submit" value="Submit"/>
      {% csrf_token %}
  </form>
  ```

  > detail.html

  ```html
  <h1>{{student_detail.name}}</h1>
  <p>이메일 : {{student_detail.email}}</p>
  <p>생일 : {{student_detail.birthday}}</p>
  <p>나이 : {{student_detail.age}}</p>
  <a href="/info/{{student_detail.id}}/edit/">수정</a>
  <a href="/info/{{student_detail.id}}/delete/">삭제</a>
  ```

  > edit.html

  ```html
  <form action="/info/{{student_detail.id}}/update/" method="POST">
      <p>이름</p>
      <input type="text" name="name" value="{{student_detail.name}}"/>
      <p>이메일</p>
      <input type="text" name="email" value="{{student_detail.email}}"/>
      <p>생일</p>
      <input type="date" name="birthday" value="{{birthday}}"/>
      <p>나이</p>
      <input type="number" min="1" max="100" name="age" value="{{student_detail.age}}"/>
      <input type="submit" value="Submit"/>
      {% csrf_token %}
  </form>
  ```

  ## Python

  > urls.py

  ```python
  from django.contrib import admin
  from django.urls import path, include
  from info import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('',views.index),
      path('info/',include('info.urls')),
  ]
  
  ```

  > info/urls.py

  ```python
  from django.urls import path
  from . import views
  
  app_name = 'info'
  
  urlpatterns = [
      path('student_list/',views.student_list, name="student_list"),
      path('add/',views.add),
      path('create/',views.create),
      path('<int:num>/detail/',views.detail, name="detail"),
      path('<int:num>/edit/',views.edit),
      path('<int:num>/update/',views.update),
      path('<int:num>/delete/',views.delete),
  ]
  ```

  > views.py

  ```python
  from django.shortcuts import render, redirect
  from .models import Info
  from datetime import datetime
  # Create your views here.
  
  def index(request):
      return render(request, 'info/index.html')
      
  def student_list(request):
      stu_list=Info.objects.all()
      return render(request, 'info/student_list.html', {'stu_list':stu_list})
      
  def add(request):
      return render(request, 'info/add.html')
      
  def create(request):
      name=request.POST.get("name")
      email=request.POST.get("email")
      birthday=request.POST.get("birthday")
      age=request.POST.get("age")
      
      Info(name=name,email=email,birthday=birthday,age=age).save()
      
      return redirect('info:student_list')
  
  def detail(request, num):
      student_detail=Info.objects.filter(id=num).first()
      return render(request, 'info/detail.html/', {'student_detail':student_detail})
  
  def edit(request, num):
      student_detail=Info.objects.filter(id=num).first()
      birthday=datetime.strftime(student_detail.birthday,"%Y-%m-%d")
      return render(request, 'info/edit.html/', {'student_detail':student_detail,'birthday':birthday})
  
  def update(request, num):
      name=request.POST.get('name')
      email=request.POST.get('email')
      birthday=request.POST.get('birthday')
      age=request.POST.get('age')
      student_detail=Info.objects.filter(id=num).first()
      student_detail.name=name
      student_detail.email=email
      student_detail.birthday=birthday
      student_detail.age=age
      student_detail.save()
      return redirect('info:detail', num)
      
  def delete(request, num):
      Info.objects.filter(id=num).first().delete()
      return redirect('info:student_list')
      
  ```

### 파일 위치

```
Student/
	info/
		migrations/
		templates/
			info/
				add.html
				detail.html
				edit.html
				index.html
				student_list.html
		__init__.py
		admin.py
		apps.py
        models.py
        tests.py
        urls.py
        views.py
	student/
		__init.py
		settings.py
		urls.py
		wsgi.py
    db.sqlite3
    manage.py
```

