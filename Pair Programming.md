# Pair Programming


## Part1
1. 가상환경을 설정하고, git repository를 만듭니다. ( __.gitignore 생성__ ) 적절하게 커밋.
2. 기본환경 세팅 (__한국 시간__, __한국어__, __정적 파일 위치__, __템플릿 폴더 위치__)
3. django를 이용해 blog앱을 생성합니다.  
4. `runserver`를 통해 It worked를 확인합니다.

## Part2
1. model에서 Post를 만듭니다. Post에는 __글쓴이__(Foreign key), __제목__, __내용__, __생성시간__이 있습니다.  
2. Post DB에 적용시킵니다.
3. `createsuperuser`로 관리자 아이디를 하나 생성합니다.
4. admin에 Post를 추가해서 `localhost/admin`에 Post가 있는지 확인합니다. ( admin에서 Post를 5개 정도 만듭니다.)


## Part3
1. Post list를 보여주는 MTV패턴을 구현합니다. 
  - Post의 `제목`만 리스트로 나열 합니다.
  - url > view > template
  - 최신 순으로 정렬합니다.

2. Post list 제목에 링크를 걸어서 Post detail로 가는 MTV 패턴을 구현합니다.
  - 제목, 내용, 글쓴이, 생성시간을 보여줍니다. (나름 레이아웃을 노력해봅니다.)
  - 뒤로가기 버튼을 이용해서 Post list로 돌아가는 버튼을 만듭니다.

## Part4
1. Post add를 만들고, form 태그를 이용해서 Post요청으로 Post 모델을 추가합니다.  
2. Post list에서 Post를 추가하는 버튼을 구현합니다.
3. 마지막으로 requirements.txt를 만듭니다.

## 추가로..
- 커밋은 기능 구분이 되는 경우, 그때 마다 해줍니다.  
- Post에 \_\_str\_\_함수를 정의해줍니다.  
- Post detail에서 올바른 pk가 아닐 경우 404에러를 반환합니다.  