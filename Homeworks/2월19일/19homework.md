# DB / Model 기초 (CRUD)

```
학습해야 할 내용
- Django CRUD
```

1. Django에서는 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행위를 특정한 웹 사이트에 요청하게 하는 공격을 막는 기능을 기본적으로 동작시킨다. 위의 공격은 무엇을 의미 하는가?

   ### csrf (Cross-site Request Forgery)

   ### 데이터를 훔치려고 하는 것보단 데이터를 더 쓰고 삭제를 하고 싶어하는 장난꾸러기가 하는 공격입니다.

2. 기본적으로 Django에서 views.py에 함수들을 정의할 때 request인자 값을 넣어주어야 한다. request를 황용해서 아래의 폼을 통해서 들어온 데이터를 가져오는 코드를 작성하세요.

   > html.html

   ```html
   <form action="/create/" method="POST">
       <input type="text" name="title">
       <input type="submit" value="submit">
       {% csrf_token %}
   </form>
   ```

   > views.py

   ```python
   def create(request):
       title=request.POST.get('title')
       return render(request,{'title':title})
   ```

3. 다음은 사용자가 이미 작성한 글을 수정하기 위해서 기존의 글을 보여주는 edit페이지를 위한 views.py의 코드이다.

   > views.py

   ```python
   def edit(request, id):
       post = Post.objects.get(id=id)
       return render(request, 'board/edit.html', {'post':post})
   ```

   아래의 코드에 기존의 데이터를 보여줄 수 있도록 코드를 수정하세요.

   > board/edit.html

   ```html
   <form action="/posts/{{post.id}}/update/" method="POST">
       {% csrf_token %}
       <input type="text" name="title" value="{{post.title}}">
       <input type="text" name="content" value="{{post.content}}">
       <input type="submit" value="submit">
   </form>
   ```
