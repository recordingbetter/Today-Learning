# Django Models, Fields, Relation을 그림으로 만들기

장고를 공부하면서 FileMaker에서 늘 보았던 테이블 간의 관계가 보이지 않아 답답했었다. 
장고의 models, fields와 이들의 관계를 그림으로 보여주는 프로그램이 있어 포스트 한다.

### Graphviz - Graph Visualization Software

[http://www.graphviz.org](http://www.graphviz.org)

- dot, neato, fdp, sfdp, circo 파일들을 그림으로 보여주는 프로그램
- [다운로드](http://www.graphviz.org/Download..php)에서 적합한 운영체제의 설치 파일을 다운로드 한다.


### dot 파일 만들기

- Django\_extensions를 설치했다면, graph\_models 명령으로 dot 파일을 만들 수 있다.

```
# [앱이름] 모델을 그림으로 만들기 위한 소스를 model.dot 파일에 저장
$ python manager.py graph_models [앱이름] > model.dot

# post 앱과 member 앱의 모델을 그림으로 만들기 위한 소스를 model_graph.dot 파일에 저장
$ python manager.py graph_models post member > model_graph.dot
```

### dot 파일 열기

- 설치된 Graphviz 프로그램에서 생성된 dot 파일을 연다.
- 그래프는 svg 형식이라 축소, 확대시 깨지지 않는다.
- pdf로 저장 가능
- 