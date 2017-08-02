# GIT

버전 관리 도구

## Quick Start

### pull request

- 다른 브랜치에서 master 브랜치에 push하면 pull request를 할 수 있다.
- github 사이트에서 pull request
  
base - merge를 당하는 쪽  
compare - merge할 내용  
  
merge 내용 확인 후 merge request  

### 보통의 경우 순서

#### local

- git branch [branch name]
- git checkout [branch name]
- 작업 하고
- git add [file names]
- git commit -v
- commit 내용 적고
- git push orogin [branch name]

#### github

- origin/[branch name] -> origin/master Pull Request
- 확인 후 Merge Request

#### local

- git checkout master
- git pull origin master



### 버전 관리

- 작업을 진행하면서 변경, 수정 이력을 관리

### 버전 관리 시스템을 사용하는 이유

- 무언가 잘 못되었을때 복구할 수 있다.
- 프로젝트 진행 중 어느 지점으로 돌아갈 수 있다.
- 여러사람이 같은 프로젝트에 있을때 소스코드를 공유할 수 있다.
- 소스코드를 누가 수정했는지 추적 할 수있다.- 소스코드의 변경 사항 추적을 통해 의미를 추론 할 수 있다.

### GIT의 목표

- 빠른 속도
- 단순한 구조
- 비선형적인 개발 (동시 다발적인 브랜치)
- 완벽한 분산
- Linux 커널같은 대형 프로젝트에도 유용할 것

### GIT의 기초

- 버전 간의 차이를 기록하는 것이 아니라 각 버전의 스냅샷을 기록
	- 속도가 빠르다
	- 용량이 크다
- 로컬 저장소에서 버전 관리가 가능 (오프라인 작업 가능)
	- 온라인 상태일때 리모트 저장소에 커밋 가능
- 버전 데이터(커밋)는 체크섬으로 관리
- 같은 GIT 내부가 같은 체크섬이 생기지 않는다.
	- 체크섬 : 40자 길이의 16진수 문자열

|Working directory|Wtageing area|Git directory|
|---|---|---|
|   <---checkout |the project |
|Stage fixes-->||
||commit-->|

- Working Directory : 작업 중인 디렉토리
- Staging Area : commit할 파일에 대한 정보를 저장
- Git directory : commit한 파일의 스냅샷 정보를 저장

### 저장소

- 사용자가 변경한 모든 내용을 추적하는 공간
- 저장소를 은행 계좌로 비유할 수 있다.
	- 저장소의 이력 -> 거래내역
	- 커밋 -> 입금/출금 내역

## GIT 최초 설정

1. `/etc/gitconfig` 파일: 시스템의 모든 사용자와 모든 저장소에 적용되는 설정이다. `git config --system` 옵션으로 이 파일을 읽고 쓸 수 있다.

2. `~/.gitconfig`, `~/.config/git/config` 파일: 특정 사용자에게만 적용되는 설정이다. `git config --global` 옵션으로 이 파일을 읽고 쓸 수 있다.

3. `.git/config`: 이 파일은 Git 디렉토리에 있고 특정 저장소(혹은 현재 작업 중인 프로젝트)에만 적용된다

#### 사용자 정보 설정

- 최초 한번만 설정하면 됨

```terminal
$ git config --global user.name "이름"
$ git config --global user.email "이메일"
```

#### 편집기 설정

```
$ git config --global core.editor emacs
```

#### 설정 확인

```
$ git config --list
```

#### 도움말 (오프라인 가능)

```
$ git help
```

## GIT 저장소 만들기 (로컬)

#### Index / Working Tree

- Index : 새 커밋이 되기 직전의 단계 (stage area)
- Working Tree : 현재 작업하고 있는 파일

#### 버전 관리할 디렉토리에서 git 저장소를 만들고 초기화

```
$ git init
```

#### 디렉토리에 추가된 파일을 git 저장소에 추가

```
$ git add [file name]
```

#### git 상태 확인

```
$ git status
```

버전 관리 중인 디렉토리의 파일들의 상태를 보여줌.

#### 파일의 상태

- Untracked : 버전관리에 제외되어있는 파일 $ git add [file name]으로 추가하면 Staged 상태가 된다.
- Unmodified : 버전관리 중(Tracked)이며 이전 commit과 비교하여 수정이 되지 않은 파일
- Modified : 버전관리 중(Tracked)이며 이전 commit과 비교하여 수정된 파일
- Staged : Tracked 파일 중, Modified 파일을 commit 하기 위해 Staged 상대로 만든다.

#### 버전 관리에 제외할 파일 리스트 .gitignore

``` 
vim .gitignore
```

- commit에서 제외할 파일의 리스트를 작성한다. (패턴으로 작성 가능)
	- 아무것도 없는 라인이나, `#`로 시작하는 라인은 무시한다.
	- 표준 Glob 패턴을 사용한다.
	- 슬래시(/)로 시작하면 하위 디렉토리에 적용되지(Recursivity) 않는다.
	- 디렉토리는 슬래시(/)를 끝에 사용하는 것으로 표현한다.
	- 느낌표(!)로 시작하는 패턴의 파일은 무시하지 않는다. 
	- * 는 하나도 없거나 모든 문자.
	- ** 아무 디렉토리
	- [abc] 는 a, b, c 중 1개의 문자
	- [0-9] 숫자 1개
- https://www.gitignore.io 에서 `macOS`로 생성하여 붙여넣기 해도 됨

#### modified, not staged files

```
$ git diff
```

#### Staging Area

```
$ git diff --staged //or
$ git diff --cached
```

#### COMMIT!

```
$ git commit
```

Leave commit message on vim editor.

```
$ git commit -m "commit message"
```

#### Staging 과정 생략하기

```
$ git commit -a
```

tracked file을 자동으로 staging area에 넣어준다.

#### 파일 삭제 rm

```
$ git rm [file name]
```

tracked file을 삭제(staging area에서 삭제)한 뒤에 commit 해야 함.
삭제할 파일이 staging area에 있다면 `-f` 옵션으로 강제 삭제

#### 파일 이름 변경 mv

```
$ git mv [from name] [to name]
```
commit 하지 않아도 됨

#### git log

```
$ git log				//로그 확인
$ git log -p			//자세한 로그 확인
$ git log -3			//최근 3개의 커밋로그만 확인
$ git log --oneline	//각 로그를 1줄씩
$ git log --graph	//브랜치를 그래프로
$ git log --all		//전체 로그 확
$ git log --decorate //브랜치 보이게
$ git log --oneling --graph --decorate --all //완성형

$ git config --global alias.adog "log --all --decorate --oneline --graph"		// git adog 명령으로 완성형 입력

```

#### 버전 되돌리기

```
$ git commit --amend //직전 커밋 내용에 덮어쓴다.
$ git checkout [체크섬의 처음 일부문자]	//로컬 파일을 이전 버전으로 

```

#### 파일을 unstaged로 변경

```
$ git reset HEAD [file name]
```

#### modified 파일 되돌리기

```
$ git checkout -- [file name]
```
수정하기 전으로 되돌림 (위험..)

## 리모트 저장소

#### 리모트 저장소 확인

```
$ git remote //or
$ git remote -v
$ git remote show [리모트 저장소 단축이름]
```

#### 리모트 저장소 추가 add

먼저 github 등에 저장소를 만든다. (url 복사)

```
$ git remote add [리모트 저장소 단축이름] [url]
```

#### 리모트 저장소에 파일 복사 push

```
$ git push origin master
$ git push [리모트 저장소 단축이름] [브랜치]
```

#### 기존 저장소를 복사 clone

- 리모트, 로컬 모두 가능

```
$ git clone [url] [생성할 드렉토리이름]
```

#### fork / clone / pull request

- 리모트 저장소를 fork하면 리모트에 저장소가 생긴다. 
- 그 리모트 저장소를 clone하면 로컬에 저장소가 생긴다.
- pull하면 clone했던 리모트 저장소에 업데이트된다.
- 원본에 push를 하고 싶으면 pull request 한다.

#### 리모트 저장소 이름 바꾸기 rename

```
$ git remote rename [기존이름] [새이름]
```

#### 리모트 저장소 삭제 rm

```
$ git remote rm [리모트 저장소 단축이름]
```

#### tag

- lightweight tag : 최슨 커밋으로 이동하지 않음. 특정 커밋을 가르킴.
- annotated tag : 태그를 만든 사람 이름, 이메일 메세지 등을 저장. `-a`


```
$ git tag -a [태그이름] -m "메세지" 	//annotated tag
$ git tag [태그이름] 					//lightweight tag
```

```
$ git push origin v1.0
$ git push origin --tags			//여러개의 태그 푸시
```

- 태깅 후에 푸시. 그냥 푸시로는 안됨.
- 저장소(github)의 release 리스트에 있음. 링크 제공


## Git 브랜치

버전의 가지

#### 브랜치 만들기

```
$ git branch [이름]
$ git branch -v 					// 브랜치 리스트 확인
$ git checkout -b [브랜치이름]	// 브랜피를 만들고 그 브랜치로 이동

```

- 브랜치는 커밋을 가르킴
- 태그도 브랜치와 같이 커밋을 가르킴.
- 커밋은 스냅샷을 가르킴. 
- 스냅샷은 blob의 데이터를 가지고 있음

#### 작업 브랜치 변경

```
$ git checkout [브랜치이름]
```

- 브랜치를 변경하면 해당 브랜치가 가지고 있는 커밋으로 이동. 
- 해당 브랜치가 가지고 있는 커밋 버전으로 로컬 파일이 바뀜

#### 브랜치 이름 변경

```
$ git branch - [기존이름] [새이름]
```


## Merge

```
$ git merge hotfix
```

- 현재 브랜치에 hotfix의 변경 내용을 merge
- production에서 $ git merge hotfix 하면 hotfix가 production으로 합쳐짐

#### 브랜치 삭제

```
$ git branch -d [삭제할 브랜치]
```

#### 파일 충돌 conflict

__같은 파일이 수정된 브랜치를 merge할 경우, 해당 파일을 수정하라고 메세지가 뜨며, 파일 내부에 브랜치 별 내용을 구분해놓음.__

`$ git status` 충돌이 일어난 내용 확인.
해당 파일 내용을 정리한 뒤에 `$ git add` 후 `$ git commit` 하면 merge 됨.

#### fetch / pull

- fetch 리모트에 있는 내용을 로컬로 받아옴. 로컬과 merge 하지 않음
- pull 리모트에 있는 내용을 로컬로 받아오면서 merge 작업까지 함.


```
$ git push origin serverfix:serverfix
```

- “로컬의 serverfix 브랜치를 리모트 저장소의 serverfix 브랜치로 Push 하라” 라는 뜻이다.

#### 리모트에서 브랜치 삭제
```
$ git push origin --delete serverfix
```



## rebase

- 브랜치를 합쳐줌. merge랑은 다름.
- **이미 공개 저장소에 Push 한 커밋을 Rebase 하지 마라**
- [https://git-scm.com/book/ko/v2/Git-브랜치-Rebase-하기]()


## Stashing

```
$ git stash

$ git stash save
```

- tracked, modified 파일들을 staging area에 임시로 보관
- git status에는 commit 한 것 처럼 나옴.

#### stash list

```
$ git stash list
```

#### stash apply

```
$ git stash apply				//가장 최근의 stash를 적용한다. (modified/added)
$ git stash apply stash@{1}	//1번 stash를 적용한다. (modified/added)
```

#### stash apply --index

```
$ git stash apply --index		//가장 최근의 stash를 적용한다. (staged)
```

#### stash drop 삭제

```
$ git stash drop stash@{1}		//해당 stash 삭제
$ git stash pop stash@{1}		//해당 stash를 적용하고 바로 삭제
```

#### stash (일부 파일만 커밋하고 나머지는 나중에 처리하고 싶을때)

```
$ git stash --keep-index
```
- 이미 staged된 파일은 stash하지 않음

#### stash including untracked files

```
$ git stash --include-untracked

$ git dtash -u
```

#### stash를 적용한 브랜치 만들기

```
$ git stash branch [branch name]
```

- stash 이후 modified가 생겼을때 stash 당시의 commit을 checkout 한 뒤 새로운 브랜치를 만들고 적용한다.

#### working directory의 파일 지우기

```
$ git clean					// working directory의 untracked 파일 삭제
$ git stash -all				//파일 삭제 전에 stash 한다.
$ git clean -f -d			//-f 강제로 -d 하위폴더까지
$ git clean -n				//삭제될 파이을 미리 보여줌. 실제 삭제되진 않음,
$ git clean -x				//.gitignore에 있는 파일까지 삭제
```

## 검색 도구

### git grep

- 커밋트리의 내용, 워킹 디렉토리의 내용을 문자열이나 정규표현식으로 검색할 수 있다.

```
$ git grep -n [검색어]			//검색 결과를 줄 번호와 함께 보여준다.
$ git grep --count [검색어]		//검색 결과의 갯수를 보여줌
$ git grep -p [검색어]			//함수나 메서드를 검색하여 보여줌
$ git grep --and	[검색어]			//한 라인에 검색어가 여러개 있는 줄검색
```

### 로그 검색

- 히스토리에서 언제 추가되거나 변경되었는지 검색

```
$ git log -S [검색어] --oneline		//검색어가 처음 추가된 커밋, 없어진 커밋을 검색
$ git log -G [정규표현식]				//정규표현식으로 검색
$ git log -L :[함수명]:[파일명]		//파일 내에 함수나 라인의 히스토리 검색
```

## 히스토리 단장

- 사람들과 코드(저장소)를 공유하기 전에 commit history 정리해야된다.

#### 마지막 커밋 수정

```
$ git commit --amend				//마지막 커밋 메세지를 수정할 수 있게 열어줌
```
- **rebase와 같이 이미 push한 커밋은 수정하면 안된다.**

#### 커밋 메세지 여러개 수정
- 직전 커밋이 아닌 예전의 커밋 수정
- 개별 커밋을 수정하지 않고 특정 시점부터 현재 위치(HEAD)까지의 커밋을 rebase
- `-i` 옵션으로 대화형 작업 가능 **(log의 순서와 반대로 나온다)**

```
$ git rebase -i HEAD~3				//마지막 커밋 3개를 수정
```

- 커밋 메세지 수정 화면에서 `pick`를 `edit`로 변경하면 그 커밋에서 멈춘다.
- 저장하고 편집기를 종료하면 Git은 목록에 있는 커밋 중에서 가장 오래된 커밋으로 이동
- 이후 설명에 따라, 아래 명령 실행.

```
$ git commit --amend
$ git rebase --continue
```

#### 커밋 순서 바꾸기

- 대화형 rebase 도구로 커밋을 삭제하거나 순서를 조정할 수 있다.

```
pick f7f3f6d changed my name a bit
pick 310154e updated README formatting and added blame
pick a5f4a0d added cat-file
```

커밋 메시지를 아래와 같이 수정하면 `added cas-file` 커밋은 삭제되고 다른 두 커밋은 순서가 바뀐다.

```
pick 310154e updated README formatting and added blame
pick f7f3f6d changed my name a bit
```

#### 커밋 합치기

- 대화형 rebase 도구로 커밋을 합칠 수 있다.
- `pick` 대신 `squash`로 변경하면 해당 커밋과 이전 커밋을 merge 커밋 메세지도 merge

#### 커밋 분리

- 기존의 커밋을 해제하고 stage를 여러개로 분리하고, 다시 커밋.
- 대화형 rebase 도구를 사용

```
pick f7f3f6d changed my name a bit
edit 310154e updated README formatting and added blame
pick a5f4a0d added cat-file
```

커밋 310154e를 2개의 커밋으로 분리하려면,
대화형 rebase 화면에서 해당 커밋을 `edit`로 변경한다.
커밋 해제는 `git reset HEAD^` -> 수정했던 파일들이 unstaged 상태가 된다.
그 다음 파일들을 staged 한 뒤에 원하는만큼 커밋한 뒤, `git rebase --continue`을 실행하면 rebase 작업이 끝난다.

```
$ git reset HEAD^							//커밋해제
$ git add README							//파일 추가1
$ git commit -m 'updated README formatting'	//새로운 커밋1
$ git add lib/simplegit.rb					//파일 추가2
$ git commit -m 'added blame'				//새로운 커밋2
$ git rebase --continue						//rebase 작업 종료
```

결과

```
$ git log -4 --pretty=format:"%h %s"
1c002dd added cat-file						//기존 a5f4a0d
9b29157 added blame							//새로운 커밋2
35cfb2b updated README formatting			//새로운 커밋
f3cc40e changed my name a bit				//기존 f7f3f6d
```

- **이 작업은 커밋의 체크섬을 변경시키므로 remote에 push한 커밋을 수정하면 안된다.**

### filter-branch 수정해야할 커밋이 많은 경우

- push한 이후에는 사용하면 안된다.

##### 모든 커밋에서 특정 파일 삭제

```
$ git filter-branch --tree-filter 'rm -f passwords.txt' HEAD
```

- 모든 파일과 커밋을 정리하고 브랜치 포인터를 복원해준다.
- 테스트 브랜치에서 테스트 후 마스터 브랜치에 적용하는 것이 좋다.
- `--all` 옵션으로 모든 브랜치에 적용 가능

## git reset과 checkout

### reset


##### 트리 : 실제 파일의 묶음

|트리|역할|
|---|---|
|HEAD|마지막 커밋 스냅샷. 다음 커밋의 부모. 현재 브랜치|
|index|다음에 커밋할 스냅샷 (stage)|
|working directiry|샌드박스, 로컬 작업 공간|

##### reset 과정

1. HEAD 이동 : 현재 브랜치가 가리키는 커밋을 변경 
	- `$ git reset --soft HEAD~` `--soft` 옵션으로 이 과정에서 멈출 수 있다.

2. index 업데이트 : index를 HEAD가 가리키는 스냅샷으로 업데이트
	- `$ git reset --mixed HEAD~` `--mixed` 옵션으로 이 과정에서 멈출 수 있다. **(reset의 옵션이 생략되면 이 옵션으로 실행된다)**

3. working directory 업데이트 : working directory 파일을 index 내용으로 업데이트 한다.
	- `$ git reset --hard HEAD~` `--hard` 옵션으로 이 과정에서 멈출 수 있다.

##### 경로를 주고 reset

```
$ git reset [커밋 체크섬] [파일이름]		//명시된 커밋에서 파일 스냅샷을 가져온다
```

##### 커밋 합치기

### checkout

- branch 스냅샷을 기준으로 세 트리를 조작한다.
- working directory의 파일이 날아갈 일이 없음.
- working directory에서 merge 작업을 시도 후 변경하지 않은 파일만 업데이트
- **HEAD 자체를 다른 브랜치로 옮김. (cf. reset은 HEAD가 가리키는 브랜치를 변경)**



# 브랜치 추적

- 리모트 트래킹 브랜치를 로컬 브랜치로 Checkout 하면 자동으로 "트래킹(Tracking) 브랜치"가 만들어진다 (트래킹 하는 대상 브랜치를 "Upstream 브랜치" 라고 부른다). 트래킹 브랜치는 리모트 브랜치와 직접적인 연결고리가 있는 로컬 브랜치이다. 트래킹 브랜치에서 git pull 명령을 내리면 리모트 저장소로부터 데이터를 내려받아 연결된 리모트 브랜치와 자동으로 Merge 한다.  
  
- 서버로부터 저장소를 Clone을 하면 Git은 자동으로 master 브랜치를 `origin/master` 브랜치의 트래킹 브랜치로 만든다. 트래킹 브랜치를 직접 만들 수 있는데 리모트를 `origin`이 아닌 다른 리모트로 할 수도 있고, 브랜치도 `master`가 아닌 다른 브랜치로 추적하게 할 수 있다. `git checkout -b [branch] [remotename]/[branch]` 명령으로 간단히 트래킹 브랜치를 만들 수 있다. `--track` 옵션을 사용하여 로컬 브랜치 이름을 자동으로 생성할 수 있다.  
	
```
$ git checkout --track origin/serverfix

Branch serverfix set up to track remote branch serverfix from origin.
Switched to a new branch 'serverfix'
```

- 이 명령은 매우 자주 쓰여서 더 생략할 수 있다. 입력한 브랜치가 있는 (a) 리모트가 딱 하나 있고 (b) 로컬에는 없으면 Git은 트래킹 브랜치를 만들어 준다.

```
$ git checkout serverfix

Branch serverfix set up to track remote branch serverfix from origin.
Switched to a new branch 'serverfix'
```

- 리모트 브랜치와 다른 이름으로 브랜치를 만들려면 로컬 브랜치의 이름을 아래와 같이 다르게 지정한다.

```
$ git checkout -b sf origin/serverfix

Branch sf set up to track remote branch serverfix from origin.
Switched to a new branch 'sf'
```

- 이제 sf 브랜치에서 Push 나 Pull 하면 자동으로 `origin/serverfix`로 데이터를 보내거나 가져온다.

이미 로컬에 존재하는 브랜치가 리모트의 특정 브랜치를 추적하게 하려면 git branch 명령에 `-u`나 `--set-upstream-to` 옵션을 붙여서 아래와 같이 설정한다.

```
$ git branch -u origin/serverfix

Branch serverfix set up to track remote branch serverfix from origin.
```

### subtree / submodule

### getrrit code review

- 코드 리뷰 사이트.
- 안드로이드 프로젝트가 사용 중
- 대기업에들 사용한다
- 서브밋

### hooks

- commit 등 특정 이벤트에 자동으로 실행되는 스크립트
- .git 폴더에 샘플들이 들어있음. 사용시 .sample 삭제

### 코드 작성, 수정 완료 후

```
$ git fetch$ git merge origin master
# 여기에서 conflict를 잡아주고 가야함. 없으면 이득 
# 그리고 반드시 테스트!!!
$ git push
```

### redis

- 메모리 db
- 파일시스템을 사용하지 않아 빠르다
- 세션 관리할때 사용
















 

















