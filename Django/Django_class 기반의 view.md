# class 기반의 view

- HTTP 요청 메소드에 따라 처리 기능이 달라질때 IF를 사용하지 않고 요청 메소드 별로 구분할 수 있다.(클래스 내부의 함수명으로 구분)
- 코드의 재사용성이 높아지고, 생산성이 높아짐
- 다중상속이 가능하여 제네릭뷰, 믹스인 클래스 사용 가능
- 장점 : 구조화, 상속

### URLconf

- urls.py에 class view를 사용한다고 선언해준다.


```python
# urls.py
# MyView라는 클래스 뷰를 사용

from django.conf.urls import url
from myapp.views import AboutView

urlpatterns = [
	url(r'^about/$', AboutView.as_view())
	]
```

#### as_view()

- as_view()는 url 해석기에서 class view로 진입하기 위한 매소드
- 클래스의 인스턴스를 생성하고 그 인스턴스의 dispatch() 매소드를 호출
- dispatch() 메소드는 요청을 검사하여 HTTP 요청 메소드를 알아낸 다음, 인스턴스 내에 해당 이름을 갖는 메소드로 요청을 중계한다
- 요청에 맞는 메소드가 없으면 에러 발생 

> MyView.as_view() -> MyView(class) -> MyView(Instance) -> GET or POST -> 메소드 매칭

### views.py

```python
# views.py
# /about/ url로 요청이 들어오면 about.html을 보여주는 TemplateView

from django.views.generic import TemplateView

class AboutView(TemplateView):
	template_name = 'about.html'
```

```python
# views.py
# MyForm 폼클래스를 적용하여 about.html을 보여주고

from django.views.generic.edif import FormView
 
class AboutView(FormView):
    form_class = MyForm
    template_name = 'about.html'
    success_url = 'thanks'
 
    def form_valid(self, form):
        # cleaned_data로 관련 로직 처리
        return super(MyFormView, self).form_valid(form)
```  
  
- form_class : 사용자에 보여줄 폼을 정의한 forms.py 파일 내의 클래스명
- template_name : 폼을 포함하여 렌더링할 템플릿 파일 이름
- success_url : MyFormView 처리가 정상적으로 완료되었을 때 리다이렉트시킬 URL
- form_valid() 함수 : 유효한 폼 데이터로 처리할 로직 코딩, 반스시 super() 함수 호출.


##### 참고문서 http://unifox.tistory.com [Python Django]


## generic view 사용 예

- 'name' 필드 하나만 가지는 WorkOut 모델이 있음.

```python
# views.py

from django.views.generic import ListView, DetailView

class WorkOut(ListView):
	model = WorkOut
	
class WorkOutDetail(DetailView):
    model = WorkOut
```

```python
# urls.py

from django.conf.urls import url
from .views import WorkOutList, WorkOutDetail

urlpatterns = [
    url(r'^$', WorkOutList.as_view()),
    url(r'^(?P<pk>\d+)/$', WorkOutDetail.as_view(), name='detail'),
]
```

```html
<!-- workout/workout_list.html -->

<body>
    {% for li in object_list %}
        <p>
            <a href="{% url 'detail' li.pk %}">
                {{ li.name }}
            </a>
        </p>
    {% endfor %}

</body>
```

```html
<!-- workout/workout_detail.html -->
<body>
    {{ object.name }}
</body>
```

- ListView는 자동으로 object\_list라는 컨텍스트 변수를 생성한다.
- DetailView는 자동으로 object라는 컨텍스트 변수를 생성한다.
- html 파일 이름은 꼭 저렇게 써야한다. (모델명의 소문자\_detail 또는 모델명의 소문자\_list)

  
  
- 기타 여러가지 View 클래스가 있음. [참고 : 장고 제네릭뷰](https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/#createview)


	





	