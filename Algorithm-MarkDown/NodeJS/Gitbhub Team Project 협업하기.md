## Gitbhub Team Project 협업하기



---

<br>

#### Github의 사용되는 가장 큰 이유 중 하나인 협업을 위한 포스팅을 하려고 한다. Web이나 App 개발을 혼자 하기는 상당히 힘들기 때문에 Git 협업 방식을 반드시 숙지하고 있는 것이 좋다.

<br>



## ## Git Repository 협업 세팅

<br>

---

```
운영체제 : Mac OS Catalina
진행방식 : Terminal
가정 : 팀장이 Repository를 만들었고 Contributor로 추가된 상태.
```

---

<br>

> ### <center>**Branch List**</center>
>
> <center> <b>master</b> > <b>develop</b> > <b>working</b> </center>
>
> **master** : 최종 코드 관리 Branch
>
> **develop** : master 브랜치에 올리기 전 개발 코드 1차 관리
>
> **working** : 팀원들이 기본적으로 작업하는 공간
>
> ​	> working 브랜치에서 팀원별로 다시 branch를 나누는 경우도 꽤 많다.

<br>



### ## Git Repository Local 세팅

##### 필자의 경우 원격 Repo를 Upstream으로 설정해서 하는 편이다. 사실 Upstream은 Fork로 타 Repo를 가져온 후 최신 버전으로 동기화하기 위해 자주 쓰는 Command이니 필자를 따라와도 좋고 안 따라와도 좋다.

<br>

```shell
1. Repository 디렉터리로 들어간다.
	> cd desktop/teamRepository
2. Upstream을 설정해준다.
	> git remote add upstream "git url"
	> ex) git remote add upstream "https://github.com/leader/teamRepository.git"
	
```

이렇게 하면 우선적으로 Upstream (상위 브랜치 개념으로 이해하면 쉽다)으로 원격 Repository와 연결된다.

```shell
git remote -v
```

위 Command로 원격 저장소와 연결된 목록을 확인할 수 있다. 잘 연결된 상태라면

```shell
origin	"git remote URL" (fetch)
origin	"git remote URL" (push)
upstream	"git remote URL" (fetch)
upstream	"git remote URL" (push)
```

와 같이 뜰 것이다. 위에 보면 알겠듯이 origin으로 협업을 해도 되니 다시 한번 말하지만 origin과 upstream 중 무엇을 사용할지는 자유다!

<br>

### ## 작업 Team Project working branch에 올리기

다음으로 원격 저장소에 실제로 올리는 방법이다.

```shell
1. 작업한 Local branch인지 확인한다. 브랜치 실수하면 큰일날 수 있으니 꼭 확인해주자.
	> git branch
	
2. 새로 작업한 파일들을 Git이 track할 수 있도록 해주자.
	> git add .
	
3. Commit을 해서 Tracked 상태로 바꿔주자.
	> git commit -m "커밋 메시지"
	
4. 만약 Local에서도 작업중, push할 브랜치를 따로 관리한다면 push할 브랜치로 이동하자. 없다면 6번으로 Skip
	> git checkout 'push할 브랜치 이름'
	> ex) git checkout final
	
5. branch 동기화를 시켜준다. 즉, 작업본을 push할 local 브랜치와 합쳐야 한다.
	> git merge '작업한 브랜치'
	> ex) git merge sub
	
6. 원격 저장소에 push해주자!
	> git push upstream "push할 브랜치"
	> ex) git push upstream develop
	
7. github 원격 Repo를 확인해보면 최신본으로 동기화된 것을 확인할 수 있다!
```

<br>

<br>

이제 Local 과 원격 Repository 간 연결이 모두 완료됐다! 

안심하고 팀프로젝트를 즐기도록 하자.

<br>