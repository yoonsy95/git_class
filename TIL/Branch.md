## Git Branch

> Git 개발 흐름에서 branch는 매우 중요하다
>
> 독립적인 개발환경을 제공하여 
> 동시에 다양한 작업을 진행할 수 있도록 만들어준다
>
> 일반적으로 브랜치의 이름은 해당 작업을 나타낸다

#

### 1. 기초 명령어

```bash
$ git branch                # check branch list
$ git branch branchName     # create branchName
$ git checkout branchName   # move branchName
$ git branch -d branchName  # delete branchName
```

```bash
$ git checkout -b branchName  # branchName 생성 및 이동
```

#

- branch 병합

```bash
(master) $ git merge feature
# master 브랜치로 featyre 브랜치 이력 가져오기(병합)
```

#

마크다운파일

https://gist.github.com/edutak/710434b90539b1f54d398af6f7c8216d

- 우측에서 raw 버튼 클릭, 복사 후 붙여넣기



pdf 파일

https://drive.google.com/file/d/1bkvYHMN2Rz8b0GZNw7GY5-flTOKF8pZj/view