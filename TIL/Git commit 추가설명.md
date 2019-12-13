## Git 추가설명

### 1. commit

> commit을 통해 이력을 확정하면 hash 값이 부여되며 
> 이 값을 통해 동일한 커밋인지 확인한다

```bash
# WD, staging area 변화 없을 때
# 변경사항 없을 때
$ git commit
nothing to commit, working tree clean

# WD 변화 있음, staging area 변화 있을 때
$ git commit
Untracked files:
		lee.txt

nothing added to commit but
untracked files present
```

#

#### commit 메시지 작성하기

> 부제: vim 활용법

```bash
$ git commit
```

- 편집모드(i: 끼워넣기)
  - 문서 편집 가능
  - 커밋 메시지 상세 // 상단
- 명령모드
  - `dd`: 해당 라인 삭제
  - `:wq`: 저장 및 종료
    - `w`: write(저장)
    - `q`: quit(종료)
  - `:q!`: 강제종료
    - `q`: quite(종료)
    - `!`: 강제

#

### log  활용하기

```bash
$ git log
$ git log --oneline
$ git log -1 # num
$ git log -1 --oneline
$ git log --oneline --graph
```

- HEAD: 현재 작업하고 있는 커밋 이력 및 브랜치에 대한 포인터

  ```bash
  ae6233f (HEAD -> master) Merge branch 'feature/board'
  # 현재 master 브랜치에 있으며
  # ae6233f 커밋 상태에 있음
  ```

- 예시)

  ```bash
  1d3160a (HEAD -> master) add lee.txt
  ae6233f Merge branch 'feature/board'
  
  # 현재 master 브랜치에서 1d3160a 커밋 했으며
  # feature/board 브랜치는 ae6233f 이력이다
  ```

  #

### 커밋 메시지 수정

> 아래의 명령어는 **커밋 이력을 변경**하기 때문에 조심해야 함
>
> 공개된 저장소(원격 저장소)에 push된 이력이라면 절대 해서는 안 됨

```bash
$ git commit --amend   # vim 창 나옴
```

#

#### 커밋시 특정 파일을 빠뜨렸을 때

만약, staging area에 특정 파일(omit_file.txt)을 올리지 않아서 커밋이 되지 않았을 때

```bash
$ git add omit_file.txt
$ git commit --amend
```

명령어 되돌림 commit 순간으로

#

### staging area

- 커밋 이력이 있는 파일 수정시

  ```bash
  $ git status
  On branch master
  Your branch is ahead of 'origin/master' by 10 commits.
    (use "git push" to publish your local commits)
  
  Changes not staged for commit: # 변경사항들, stage에 안된(커밋 위한)
  	# commit이 되기 위해서 == staged로 바꾸려면
    (use "git add <file>..." to update what will be committed)
    	# WD에 있는 변화 버리려거든 사용
    	# 커밋 이후 변경 사항 모두 삭제
    (use "git restore <file>..." to discard changes in working directory)
          modified:   lee.txt
  
  # staging area가 비어있으
  no changes added to commit (use "git add" and/or "git commit -a")
  
  ```

  ```bash
  $ git add lee.txt
  $ git status
  On branch master
  
  # 커밋 될 변화
  # 커밋 명령어 했을 때 아래 내용 이력에 남음
  Changes to be committed:
  	# unstage하기 위하여 restore <-> add
    (use "git restore --staged <file>..." to unstage)
          modified:   lee.txt
  
  ```

  #

- 커밋 이력이 없는 파일 수정시

  ```bash
  $ git status
  On branch master
  
  # tracking 되고 있지 않는 파일 == commit(이력)에 한 번도 관리된 적 없음
  Untracked files:
    (use "git add <file>..." to include in what will be committed)
          sy.txt
  
  # 커밋할 것도 없고(staging area가 비어있으며)
  # 트래킹 되고 있지 않는 파일도 있음
  nothing added to commit but untracked files present (use "git add" to track)
  
  ```
  
  #

#### add 취소하기

```bash
$ git restore --staged <file>
```

- 구버전 git에서는 아래 명령어 사용해야 한다

  ```bash
  $ git reset HEAD <file>
  ```

  #

###  Working directory 변화 삭제하기

> git에서 모든 commit 이력은 되돌릴 수 있으나
> 아래의 WD 이력을 삭제하는 것은 되돌릴 수가 없다

```bash
$ git restore <file>
```

- 구버전 git에서는 아래 명령어 사용해야 한다

  ```bash
  $ git checkout -- <file>
  ```

#

### Stash

> `stash`는 변경사항을 임시로 저장해놓는 공간

#### 예시상황

```
1. feature branch에서 a.txt 변경 후 커밋
2. master branch에서 a.txt를 수정(add / commit X)
3. merge
```

```bash
$ git merge test
# 현재 merge 명령어로 인해 아래의 파일이 엎어쓰여질 수 있다.
error: Your local changes to the following files would be overwritten by merge:
        a.txt
# commit 하거나 => 이력 확정을 하여 merge시 충돌나는 상황으로 만듦
# stash 해야 함 => working dir를 잠시 비워놓음
Please commit your changes or stash them before you merge.
Aborting
Updating 9b6e4fd..3f60273

```

##### 명령어

``` bash
# stash 공간에 저장
$ git stash   
Saved working directory and index state WIP on master: 9b6e4fd a.txt

# stash 공간 내용 확인
$ git stash list  
stash@{0}: WIP on master: 9b6e4fd a.txt

# stash 공간에서 적용(apply)하고 목록에서 삭제(drop)하기
$ git stash pop
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (27b9eb5e73e76d99fc4d5854b9f1bf2acb93d595)
```

#

#### 예시 상황 해결

```bash
$ git stash
$ git merge test
$ git stash pop
# 충돌 해결 후 작업 이어나가기
```

```bash
1st
<<<<<<< Updated upstream
test branch
=======
-------------
working..
>>>>>>> Stashed changes
```

#

### reset vs revert

> commit 이력을 되돌리는 작업을 한다

- **`reset`: 이력 삭제**

  - `--mixed`: default, 해당 커밋 이후 변경사항 staging area에 보관
  - `--hard`: 해당 커밋 이후 변경사항 모두 삭제 
  - `--soft`: 해당 커밋 이후 변경사항 및 working dir 내용까지 모두 보관

  ```bash
  $ git log --oneline
  6a807ec (HEAD -> master) a.txt
  3f60273 (test) a.txt test
  9b6e4fd a.txt
  
  ```

- **`revert`: 되돌렸다는 이력 남김**

  ```bash
  $ git log --oneline
  d2e1638 Revert "a.txt test"
  6a807ec a.txt
  3f60273 (test) a.txt test
  9b6e4fd a.txt
  
  ```

  











