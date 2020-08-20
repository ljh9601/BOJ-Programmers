## Node JS 기초 설정 및 가이드 (Express) for Mac



---

NodeJS는 JavaScript에서 Back-End 로 사용할 수 있게 하도록 한 Engine으로, 앞에서 말했듯 **Server Side** 언어이다.

<br>

NodeJS의 가장 큰 장점은 2가지 정도로 요약할 수 있다.

```
1. Server의 생성이 매우 단순하고, Light하며, 빠르다.

2. Front-end 와 Back-end 을 모두 Javascript 기반으로 할 수 있다.
```

지금부터 NodeJS 설치 과정을 설명하겠다. <br>



## ## NodeJS 설치 과정

<br>

---

```
운영체제 : Mac OS Catalina
NodeJS Version : v12.16.1
NPM version : 6.14.7
```

---

<br>



### ## Node 설치

이제 NodeJS를 설치할 차례다! 방법은 2가지가 있다.

```shell
1. brew install node
2. NodeJS 홈페이지에서 Install
```

<br>

필자는 2번 방법을 선택하여 진행하였다. 2번은 **npm도 같이 설치**가 진행되어 편하다.

Node 및 NPM 설치 확인은 설치 후 Terminal에서

```shell
node -v
npm --version
```

로 확인하면 된다.

<br>

### ## Express 설치

Node와 NPM을 설치했으면, 다음으로 Express를 설치해보자!

Express란,

```
http와 Connect 컴포넌트 기반 웹 프레임워크
MVC 구조
API Server, REST API, Full Stack 모두를 지원한다.
```



설치법 역시 매우 간단하다.

```shell
sudo npm install express --save
```

필자의 경우 express의 경우 관리자 권한을 요구하여 sudo를 추가하였다.



### ## Express-generator 설치

Express-generator는 Express 기반 프로젝트 템플릿을 만들어주는 아주아주 좋은 무기다.

```shell
npm install express-generator -g
```

global 옵션을 꼭 추가해주자.



### ## Express 프로젝트 생성

NodeJS 프로젝트를 만들기 위한 Template Folder를 생성한다.

```shell
express projectName
- projectName : 생성하고자 하는 프로젝트 이름
```



![](/Users/Janghaeng/Desktop/ljh9601.github.io/assets/img/NodeJS/nodejsTemplateFolderScreenshot.png)

디렉터리가 생성되고 Express 프로젝트가 생성된다.



### ## NPM 모듈 설치

이제 Node Module들을 express 프로젝트에 생성해주어야 한다.

```shell
cd nodeJSSample
npm install
```



이제 프로젝트 생성이 모두 완료됐다! 

5분만에 서버 만들기, Express의 최대 강점이 아닐까 싶다.