
# Emmet Syntax

## Elements
태그를 타이핑 한 뒤 `tab`키
~~~
div [tab]


<div></div>
~~~


## Nesting operators

### 1. Child >
하위에 태그 생성
~~~
div>ul>li [tab]


<div>
  <ul>
    <li></li>
  </ul>
</div>
~~~

### 2. Sibling +
같은 레벨에 각각 태그 생성
~~~
div+p+bq [tab]


<div></div>
<p></p>
<blockquote></blockquote>
~~~

### 3. Climb-up ^
^의 갯수만큼 아래 라인에 태그 생성
~~~
div+div>p>span+em [tab]


<div></div>
<div>
    <p><span></span><em></em></p>
</div>
~~~

~~~
div+div>p>span+em^bq [tab]


<div></div>
<div>
    <p><span></span><em></em></p>
    <blockquote></blockquote>
</div>
~~~

~~~
div+div>p>span+em^^^bq [tab]


<div></div>
<div>
    <p><span></span><em></em></p>
</div>
<blockquote></blockquote>
~~~

### 4. Multiplication *
지정한 갯수만큼 태그 생성
~~~
ul>li*5 [tab]


<ul>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
</ul>
~~~

~~~
ul>li{항목}*5 [tab]


<ul>
    <li>항목</li>
    <li>항목</li>
    <li>항목</li>
    <li>항목</li>
    <li>항목</li>
</ul>
~~~

### 5. Grouping ()
복잡하게 사용 시, 그룹핑 가능
~~~
div>(header>ul>li*2>a)+footer>p [tab]


<div>
    <header>
        <ul>
            <li><a href=""></a></li>
            <li><a href=""></a></li>
        </ul>
    </header>
    <footer>
        <p></p>
    </footer>
</div>
~~~

~~~
(div>dl>(dt+dd)*3)+footer>p [tab]


<div>
    <dl>
        <dt></dt>
        <dd></dd>
        <dt></dt>
        <dd></dd>
        <dt></dt>
        <dd></dd>
    </dl>
</div>
<footer>
    <p></p>
</footer>
~~~


## Attribute operators

### 1. ID and Class
~~~
div#header+div.page+div#footer.class1.class2.class3 [tab]


<div id="header"></div>
<div class="page"></div>
<div id="footer" class="class1 class2 class3"></div>
~~~

### 2. Custom attributes
~~~
td[title="Hello world!" colspan=3] [tab]


<td title="Hello world!" colspan="3"></td>
~~~

### 3. Item numbering $
~~~
ul>li.item$*5 [tab]


<ul>
    <li class="item1"></li>
    <li class="item2"></li>
    <li class="item3"></li>
    <li class="item4"></li>
    <li class="item5"></li>
</ul>
~~~

~~~
ul>li.item$$$5 [tab]


<ul>
    <li class="item001"></li>
    <li class="item002"></li>
    <li class="item003"></li>
    <li class="item004"></li>
    <li class="item005"></li>
</ul>
~~~

### 4. Changing numbering base and direction

~~~
ul>li.item$@-*5 [tab]


<ul>
    <li class="item5"></li>
    <li class="item4"></li>
    <li class="item3"></li>
    <li class="item2"></li>
    <li class="item1"></li>
</ul>
~~~

~~~
ul>li.item$@3*5 [tab]


<ul>
    <li class="item3"></li>
    <li class="item4"></li>
    <li class="item5"></li>
    <li class="item6"></li>
    <li class="item7"></li>
</ul>
~~~

~~~
ul>li.item$@-3*5 [tab]


<ul>
    <li class="item7"></li>
    <li class="item6"></li>
    <li class="item5"></li>
    <li class="item4"></li>
    <li class="item3"></li>
</ul>
~~~


## Text {}

~~~
a{click me} [tab]

<a href="">Click me</a>
~~~

~~~
a{Click}+b{Here} [tab]


<a href="">CLick</a><b>Here</b>
~~~

~~~
a>{Click}+b{Here} [tab]


<a href="">Click<b>Here</b></a>
~~~

~~~
p>{Click }+a{here}+{ to continue} [tab]


<p>Click <a href="">here</a> to continue</p>
~~~

~~~
p{Click }+a{here}+{ to continue} [tab]


<p>Click </p>
<a href="">here</a> to continue
~~~

## Notes on abbreviation formatting
스페이스는 Emmet의 종료를 뜻하는 심벌로, abbreviation에 사용할 수 없다.
~~~
(header > ul.nav > li*5) + footer
~~~
이 abbreviation은 작동하지 않는다.

항상 새로운 라인에 사용할 필요는 없다.
(태그 중간에서도 사용 가능)



# Implicit tag names 절대 태그 이름

#### 많이 사용되는 태그는 생략할 수 있다.

~~~
.content [tab]


<div class="content"></div>
~~~

### 생략 가능한 태그들
- `div` / `div` 태그 하위의 `div`
- `span` 태그 하위의 `span`
- `ul`이나 `ol` 태그 하위의 `li`
- `table`, `tbody`, `thead`, `tfoot` 태그 하위의 `tr`
- `tr` 태그 하위의 `td`
- `select`, `optgroup` 태그 하위의 `option`

~~~
<ul class="nav">
.content [tab]
</ul>


<ul class="nav">
<li class="content"></li>
</ul>
~~~



# "Lorem Ipsum" generator 더미 텍스트 생성기
#### 더미 텍스트 블럭을 생성
~~~
lorem [tab]

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rem reprehenderit voluptate voluptatibus quis dicta ipsam error distinctio amet quos pariatur dolorem quasi debitis, laudantium earum unde fugit officiis harum. Alias.
~~~

#### 더미텍스트를 지정한 단어 수만큼 생성
~~~
lorem100 [tab]

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam quis impedit asperiores assumenda porro veritatis et illo id sed facere sint nulla praesentium vel maxime distinctio commodi, excepturi veniam necessitatibus exercitationem, dolore cum eaque libero! Sed animi neque, eius reiciendis aspernatur id odit soluta facere quos quas quis eveniet repudiandae in ut nemo quam iusto hic, voluptatum repellat reprehenderit accusamus molestias optio. Blanditiis sit architecto, quos incidunt dolor repellat? Nostrum explicabo ratione pariatur, accusantium totam doloribus necessitatibus ut minima aperiam assumenda excepturi sunt est exercitationem ab suscipit animi nesciunt tempore alias veniam eaque doloremque reprehenderit vitae, harum molestias! Facere, a?
~~~

#### p 태그 안에 생성된 더미 텍스트가 4개
~~~
p*4>lorem [tab]

<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde ab sed corporis soluta aliquam veniam repellendus blanditiis ratione accusantium dolores cum, optio doloremque facilis assumenda nam odio adipisci obcaecati atque.</p>
<p>Numquam accusantium quam dignissimos nisi tenetur repellat eius ad praesentium, assumenda deserunt vitae, magni corporis. Inventore, sunt. Libero consequuntur recusandae totam praesentium in dolores eligendi fugit ipsa illo cumque. Iure.</p>
<p>Nulla pariatur omnis quae, dolorum odit amet, a culpa ad, explicabo perspiciatis placeat. Eligendi nobis voluptas nulla aspernatur perspiciatis voluptate doloremque, dolores error, amet ad eos, quaerat, dolor ratione unde!</p>
<p>Excepturi quia, saepe ab eum iste temporibus libero veniam, explicabo vero itaque voluptatibus omnis nostrum. Itaque dolores architecto esse laboriosam. Vitae voluptas reiciendis voluptate itaque voluptatem cum voluptates ab modi.</p>
~~~

#### generic-list 클래스로 만들어진 ul 태그 하위에 item 클래스의 10단어 짜리 더미텍스트가 4개
~~~
ul.generic-list>lorem10.item*4 [tab]

<ul class="generic-list">
    <li class="item">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Hic, distinctio.</li>
    <li class="item">Officiis ducimus itaque eius nihil possimus reiciendis quod dignissimos consequatur!</li>
    <li class="item">Repellat modi ea fugiat enim, repellendus? Fuga odit iste quisquam.</li>
    <li class="item">Dolorum nesciunt, modi voluptates error voluptatum quod laboriosam cumque placeat.</li>
</ul>
~~~
