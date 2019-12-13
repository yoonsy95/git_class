# Git 기초

---

> Git은 분산형버전관리시스템(DVCS)
>
> 소스코드 이력 확인하고 협업단계에서 활용 가능함



## 0. 기본 설정

---

윈도우에서 git을 활용하기 위해서는 git bash 필요함

[설치링크](https://gitforwindows.org/)

설치 이후에 commit을 작성하는 author 설정 필요함

``` bash
$ git config --global user.name yoonsy
$ git config --global user.email yegyo95@gmail.com
```

설정 내용을 확인하기 위해서는 아래 명령어 입력

```bash
$ git config --global -l

user.email=yegyo95@gmail.com
user.name=yoonsy
```



### gitignore

프로젝트 진행시 `git`으로 관리하지 아니할 파일이나 폴더들 설정할 수 있음

```
*.xlsx              # 확장자가 xlsx인 파일
a.txt               # a.txt 파일
.ipynb_checkpoints  # .ipynb_checkpoints folder
```

프로젝트 시작시 어떠한 내용을 담아야할지 모르겠다면 [gitignore](https://www.gitignore.io/)로 검색

ex) `python`, ` r`, `jupyter notebook`



## 로컬 저장소에서 활용하기

`add`-`commit`-`push`

### 1. git 저장소 설정

특정 프로젝트 폴더에서 git을 활용하기 위해서는 아래의 명령어 입력

``` bash
# copy: enter + tab + backspace
git init

Initialized empty Git repository in C:/Users/student/Desktop/exer/.git/
student@M160419 MINGW64 ~/Desktop/exer (master)
$ 
```

- 해당 dir 내 `.git`이라는 숨김폴더가 생성ㄷ외며 모든 git과 관련된 동작은 해당 폴더에 기록됨
- git bash에서 `(master)`라는 브랜치 정보가 표기됨



### 2. add

git에서 커밋한 대상 파일을 `staging area`로 이동시키는 명령어

```bash
$ git add a.txt # 특정 파일 stage
$ git add imgs/ # 특정 폴더 stage
$ git add . # all dir & file stage
```

- `add` 전 상태

  ``` bash
  $ git status
  On branch master
  
  No commits yet
  
  Untracked files: # git 이력에 담기지 않은 파일 생성
    (use "git add <file>..." to include in what will be committed)
    # git add 명령어를 통하여 commit할 곳에 추가하렴
          a.txt
          b.txt
  
  nothing added to commit but untracked files present (use "git add" to track)
  
  ```

  

- `add` 후 상태

  ```bash
  $ git add a.txt
  
  student@M160419 MINGW64 ~/Desktop/exer (master)
  $ git status
  On branch master
  
  No commits yet
  
  Changes to be committed: # commit될 변경사항 // unstage: commit 취소
    (use "git rm --cached <file>..." to unstage)
          new file:   a.txt
  
  Untracked files: # tracking되지 않고 있는 파일목록
    (use "git add <file>..." to include in what will be committed)
          b.txt
  ```



**항상 `git status` 명령어를 통해 현재 상태 확인하는 것이 중요함!**



### 3. commit

git에서 이력을 남기기 위해서는 항상 `commit`을 통하여 진행한다

`commit`을 남길 때에는 항상 commit msg 작성

메시지는 해당 이력에 대한 정보를 담는다

``` bash
$ git commit -m 'commit msg'
```

커밋 이력 확인 위하여 아래의 명령어 활용

``` bash
$ git log

commit b693d52621994bc89cce8742fff42233e7626195 (HEAD -> master)
Author: yoonsy <yegyo95@gmail.com>
Date:   Mon Dec 9 14:27:11 2019 +0900

    add files

$ git status
On branch master
nothing to commit, working tree clean

```

이후 변경사항 발생 시 `add` -> `commit`을 실행

`add`: commit할 대상 파일 선정

`commit`: 이력 확정



## 원격저장소(remote repository) 활용하기

> 원격 저장소를 제공해주는 서비스는 다양하다
>
> 우리는 github를 기준으로 활용해보겠다

### 0. 기본 설정

Github에 비어있는 저장소(repository) 생성

``` bash
git init
```





## 1. 원격 저장소 설정

``` bash
$ git remote add origin https:// ~
```

원격저장소(`remote`)를 `origin`이라는 이름으로 url( `https://~`) 설정함

``` bash
$ git remote add origin https://github.com/yoonseockyoung/gittest.git
$ git push -u origin master
```

아래의 명령어를 통하여 저장된 원격저장소 목록 확인 가능함

``` bash
$ git remote -v
origin  https://github.com/yoonseockyoung/gittest.git (fetch)
origin  https://github.com/yoonseockyoung/gittest.git (push)
```

잘못 설정되었을시 아래 명렁을 통해 삭제 가능

``` bash
$ git remote rm origin
$ git remote -v
```



### 2. push

원격 저장소에 업로드하기 위해서 `push`명령어 필요함

```bash
$ git push origin master
```

`origin`으로 설정된 원격 저장소에 `push`한다

이후에 변경된 사항(`commit`)이 발생하였을 때 `git push origin master`명령어를 통하여 매번 업로드를 해줄수 있다.

