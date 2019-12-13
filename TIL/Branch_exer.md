### 상황 1. fast-foward

1. feature/test branch 생성 및 이동

   ```bash
   $ git checkout -b feature/test
   ```

#

2. 작업 완료 후 commit

   ```bash
   $ touch test.txt
   $ git add .
   $ git commit -m 'test func dev'
   ```

#


3. master 이동

   ```bash
   $ git checkout master
   ```
   
   ```bash
   $ git log --oneline
   db5c4da (HEAD -> feature/test) test func dev
   79ea0bc (origin/master, testbranch, master) mul - a.txt
   9181531 home main.html
   3ac347a multicam index.html
   # 이전 testbranch 뭔가 잘못함ㅎㅎ
   # 앞 7자리: 주소
   ```

#


4. master에 병합

   ```bash
   git merge feature/test
   ```

#


5. 결과 -> fast-foward (단순히 HEAD를 이동)

   ```bash
   $ git log --oneline
   db5c4da (HEAD -> master, feature/test) test func dev
   79ea0bc (origin/master, testbranch) mul - a.txt
   9181531 home main.html
   3ac347a multicam index.html
   ```

   HEAD: 현재 있는 위치

   앞 괄호: 해당 브린치 push 이력들

#

6. branch 삭제

   ```bash
   $ git branch -d feature/test
   ```

#

---

### 상황 2. merge commit

> feature 브랜치에서 작업하고 있는 동안
>
> master 브랜치에서 이력이 추가적으로 발생한 경우

#

1. feature/signout branch 생성 및 이동

   ```bash
   $ git checkout -b feature/signout
   
   ```

#

2. 작업 완료 후 commit

   ```bash
   $ git add .
   $ git commit -m 'complete signout'
   ```

#

3. master 이동

   ```bash
   $ git checkout master
   ```

#

4. master에 추가 commit 이 발생시키기!!*

* **다른 파일을 수정 혹은 생성하세요!**

  ```bash
  $ touch master.txt
  $ git add .
  $ git commit -m 'update master'
  ```

  ```bash
  $ git log --oneline
  ```

#

5. master에 병합

   ```bash
   (master) $ git merge feature/signout
   ```

#

6. 결과 -> 자동으로 *merge commit 발생*

   ```bash
   Merge made by the 'recursive' strategy.
    web/signout.txt | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 web/signout.txt
   ```

#

7. 그래프 확인하기

   ```bash
   $ git log --oneline --graph
   *   ba26cc9 (HEAD -> master) Merge branch 'feature/signout'
   |\
   | * 4165a74 (feature/signout) complete signout
   * | 41d5aa2 update master
   |/
   * db5c4da test func dev
   * 79ea0bc (origin/master) mul - a.txt
   * 9181531 home main.html
   * 3ac347a multicam index.html
   ```

#

8. branch 삭제

   ```bash
   $ git branch -d feature/signout
   ```

#

---

### 상황 3. merge commit 충돌

1. feature/board branch 생성 및 이동

   ```bash
   git checkout -b feature/board
   ```

#

2. 작업 완료 후 commit

   ```bash
   # file test.txt 수정
   $ git add .
   $ git commit -m 'hotfix test'
   ```

#


3. master 이동

   ```bash
   $ git checkout master
   ```

#


4. *master에 추가 commit 이 발생시키기!!*

   * **동일 파일을 수정 혹은 생성하세요!**

   ```bash
   # test.txt update
   $ git add .
   $ git commit -m 'master test'
   ```

#

5. master에 병합

   ```bash
   (master) $ git merge feature/board
   ```

#


6. 결과 -> *merge conflict발생*

   ```bash
   Auto-merging web/test.txt
   CONFLICT (content): Merge conflict in web/test.txt
   Automatic merge failed; fix conflicts and then commit the result.
   ```

#


7. 충돌 확인 및 해결

   ```
   <<<<<<< HEAD
   master test emer update
   success!
   =======
   hotfix 브랜치에서 수정
   >>>>>>> feature/board
   
   ```
   
   #
   
   ```bash
   $ git status
   On branch master
   Your branch is ahead of 'origin/master' by 5 commits.
     (use "git push" to publish your local commits)
   
   You have unmerged paths.
     (fix conflicts and run "git commit")
     (use "git merge --abort" to abort the merge)
   
   Unmerged paths:
     (use "git add <file>..." to mark resolution)
           both modified:   test.txt
   
   no changes added to commit (use "git add" and/or "git commit -a")
   
   ```

#


8. merge commit 진행

    ```bash
    $ git add .
    $ git commit
```
   
   * vim 편집기 화면이 나타납니다.
   * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
      * `w` : write
      * `q` : quit
   * 커밋이  확인 해봅시다.

#

9. 그래프 확인하기

   ```bash
   $ git log --oneline --graph
   ```

   ```bash
   *   ae6233f (HEAD -> master) Merge branch 'feature/board'
   |\
   | * df8c85a (feature/board) hotfix test
   | * 7d5c2db hotfix test
   * | ac0d6c3 master test
   |/
   *   ba26cc9 Merge branch 'feature/signout'
   |\
   | * 4165a74 complete signout
   * | 41d5aa2 update master
   |/
   * db5c4da test func dev
   * 79ea0bc (origin/master) mul - a.txt
   * 9181531 home main.html
   
   ```

#


10. branch 삭제

    ```bash
    $ git branch -d feature/board
    ```

#