## Docker names 자동완성 (zsh)

- zsh completion 설치

```
$ brew install zsh-completion
```

- docker completion 설치

```
$ brew install docker-completion
```

- ~/.zsh/completion/ 폴더를 만들어 파일 복사

```
$ mkdir -p ~/.zsh/completion
$ curl -L https://raw.githubusercontent.com/docker/compose/master/contrib/completion/zsh/_docker-compose > ~/.zsh/completion/_docker-compose
```

- ~/.zshrc에 아래 내용 추가

```
# fpath에 경로 추가
fpath=(~/.zsh/completion $fpath)
# compinit 실행
autoload -Uz compinit && compinit -i
```
- Shell reload
