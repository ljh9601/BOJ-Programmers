## Github Repository Local과 원격 연결하기



---

Github은 마이크로소프트의 웹 서비스로, Source Code를 호스팅하고, 협업 기능을 지원하는, 현재 가장 인지도가 높은 Social Coding Platform이다.

<br>

Github을 사용하는 가장 큰 이유는 2가지로 정리할 수 있다.

```
1. 스스로의 프로그래밍을 웹으로 편리하게 관리할 수 있다.
	> Commit 기록을 통해 언제, 어떤 작업을 했는지도 확인할 수 있고, 
	> Commit, stash 기록 등을 통해 안정적이고 효율적인 Version Control이 가능하다.

2. 프로젝트 단위 협업에 용이하다.
	> Branch 단위 관리가 가능해 협업 중 모듈, 기능 단위 등으로 나누어 협업이 가능하다.
```

<br>

Git 은 설치되어있다고 가정한 후 진행하겠다.

물론 Git UI 등으로 편리하게 관리가 되지만, 결국에 Command에 대해 잘 모르면 후에 어찌해야 할지 모르는 사태가 오니 Terminal 혹은 Shell로 사용법을 익혀두는 것을 추천한다.

<br>



## ## Git Repository 연결 과정

<br>

---

```
운영체제 : Mac OS Catalina
진행방식 : Terminal
```

---

<br>



### ## Git Repository 생성하기

우선 Local과 연결할 Git Repository를 Github에다가 생성해주자.

```shell
1. Github 홈페이지로 들어간다.
2. 로그인 후, New Repository 버튼을 클릭해 Repo를 생성한다.
3. Readme(Repo 설명 파일), .gitignore(원격 Repo에 Push하지 않을 파일 설정(개인정보 포함 파일 등)) > 선택사항이다!
4. Repository 생성
```

<br>

### ## Local 컴퓨터에 Clone하기

Repository를 만들었으면, 다음으로 Local에 Clone해올 차례다! 이 부분은 생략해도 된다.

방법은 2가지가 있다.

```shell
1. 해당 Repository로 들어가 초록색 Code 버튼을 누른다.
	> Download Zip을 통해 압축파일 형태로 받아온 후 압축을 풀어준다.
	> Terminal or Shell로 'git clone "Repository URL"'을 입력한다.
		ex) git clone https://github.com/ljh9601/myRepository.git
```

<br>

### ## Local 과 원격 Repository 연결하기

Clone은 했지만 아직 Git은 Local의 어떤 폴더가 원격 Repository와 연결되어있는지 모르는 상태이다.

설정을 추가해주자.

```shell
1. clone해온 directory로 이동한다.
	> ex) cd desktop/myRepository
	
2. git init . 입력.
	> Local에서 .git 파일을 만들어주는데 git software가 저 파일을 보고 연결할 수 있는 폴더라는 것을 인식한다.
	
3. git remote add "원격 브랜치로 설정할 단축이름" "git code 주소" 입력.
	> 가장 중요한 원격 Repo와 연결해주는 명령인데, 이 명령을 통해 Git이 비로소 이 로컬과 MyRepository가 연결됐다는 것을 알게 된다.
	> ex) git remote add origin https://github.com/ljh9601/myRepository.git
	> origin 위치는 편한 이름으로 설정해도 좋다.
	
4. Local 컴퓨터에 Clone해온 상태라면 Skip해도 좋다.
	> Git Repository를 생성하면 default branch로 master branch가 생성되고, origin은 3번에서 설정한 단축 이름으로 써준다.
	> ex) git pull origin master
```

<br>

<br>

이제 Local 과 원격 Repository 간 연결이 모두 완료됐다! 

다음 포스팅에서는 기본적인 Commit, Push 방법에 대해 알아보겠다.

<br>