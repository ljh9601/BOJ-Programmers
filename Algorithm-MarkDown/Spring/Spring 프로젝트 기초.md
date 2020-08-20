## Spring-boot 프로젝트 생성 with JDBC, PostgreSQL



---



오늘은 Java Spring-boot를 사용하여 프로젝트를 생성해보려고 한다.

<br>

Spring Framework란, 

>**동적 웹사이트를 개발하기 위한 Java Open Source Framework**로,
>
>정확한 정의는
>
>**JAVA Enterprise 개발을 위한 Open Source Application Framework** 이다.

<br>

그리고 많은 사람들이 궁금해하는 **Spring이랑 Spring-boot의 차이**를 간단하게 설명하면,

> <center><b>Spring Framework의 복잡한 구조와 설정 문제를 간소화하기 위해 나온 것이 바로 Spring-boot 이다.</b></center>

<br>

Spring Framework의 주요 특징들은 다음과 같다.

```
1. POJO (Plain Old Java Object)
	> 일반적인 Java Code로 구현하는 방식 그대로 Spring에서 사용할 수 있다.

2. DI(Dependency Injection)
	> Spring Framework에서는 IoC (inversion of Control)을 전제로 코드의 실행이 일어나게 		 되는데, 이는 코드의 호출을 개발자가 결정하는 것이 아닌 프레임워크가 결정하는 구조이기 때문에 발		 생한다. 이를 전제로 하여, 특정 객체에 외부 객체를 연결하는 형태를 의존성 주입이라고 하는데, 			Spring의 경우 Annotation이나 bean으로 간편하게 의존성 주입이 가능하다. 의존성 주입은 		  POJO를 가능하게 하는 원동력이기도 하다!
	
3. AOP(Aspect Oriented Programming)
	> AOP를 번역하면 관점 지향 프로그래밍인데, 즉 개발자가 개발에 있어서 트랜잭션 처리, 로깅 등의 			반복 작업을 반복하지 않고 모듈화시켜 관리할 수 있도록 지원해준다. 이로 인해 개발자는 반복되는 		코드의 양을 줄이고, 개발 로직에만 집중할 수 있다.
	
4. 대한민국 공공기관의 웹 서비스 개발 시 사용을 권장하고 있는 전자정부 표준프레임워크이다.
	> 이 말인즉 대한민국에서 사용을 권장하는 웹 프레임워크이니, 사용해서 절대 손해볼 일은 없다.
```

<br>

지금부터 Spring 설치 과정을 설명하겠다. 참고로 JDK는 이미 설치됐다고 가정하겠다. <br>



## ## Spring 프로젝트 생성 과정

<br>

---

```
운영체제 : Mac OS Catalina
STS Version : 4.3.0.RELEASE
JDK Version : 1.8.0
PostgreSQL Version : 11
```

---

<br>



### ## STS 설치

STS (Spring Tool Suite)를 설치해보자. 방법은 2가지가 있다.

```shell
1. Eclipse에서 Plugin 설치
2. STS 공식 홈페이지에서 다운로드
```

<br>

어떤 방법을 사용해도 상관은 없다. Eclipse를 사용할 거라면 1번, STS를 사용할 거라면 2번을 클릭하면 된다!

필자는 2번 방법을 선택하여 진행하였다.

**1번 방법**은 Eclipse를 실행한 후

> **Help** > **Eclipse Marketplace** > **Spring 검색** > **Spring Tools 4 (aka Spring Tool Suite 4) 4.5.0 (버전별 상이) RELEASE Download** > **Eclipse 재실행** 

**2번 방법**은

> **[STS 공식 다운로드 홈페이지](https://spring.io/tools#suite-three)** 에 접속한 후, OS에 맞게 다운로드 받아주면 된다!



<br>

### ## Spring Project 생성

STS를 설치했으면, 다음으로 본격적으로 프로젝트를 생성해볼 차례다.

<br>

#### 1. File > New > Spring Starter Project

![](/assets/img/springImg/springProjectMaking1.png)

<br>

#### 2. JDBC API, PostgreSQL Driver, Spring Security, Spring Web 선택

#### ![](/assets/img/springImg/Spring-dependency.png) 

<br>

#### 3. Finish

Finish 버튼을 누르면 새로운 프로젝트가 생성된다.



<br>

### ## PostgreSQL 설치

PostgreSQL을 설치해보자. postgreSQL 설치방법 역시 2가지다.

```shell
1. brew install postgresql
2. 공식 홈페이지에서 다운로드
```

2번 방법은 **[PostgreSQL 공식 홈페이지](https://www.postgresql.org/download/)** 에서 다운로드하면 된다.

<br>

### ## Spring과 PostgreSQL 및 JDBC 연동

가장 중요한 파트다! 사실 이 부분 때문에 이 글을 볼 사람이 제일 많을 거라고 생각한다.

일단 pom.xml에 필요한 dependency가 다 설치되었는지 확인해보자.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.3.1.RELEASE</version>
		<relativePath/> <!-- lookup parent from repository -->
	</parent>
	<groupId>com.practice</groupId>
	<artifactId>spring_security</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>spring_security</name>
	<description>Demo Project for Security Spring Practice</description>

	<properties>
		<java.version>1.8</java.version>
	</properties>

	<dependencies>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter</artifactId>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
			<exclusions>
				<exclusion>
					<groupId>org.junit.vintage</groupId>
					<artifactId>junit-vintage-engine</artifactId>
				</exclusion>
			</exclusions>
		</dependency>
		<dependency>
    		<groupId>org.springframework.boot</groupId>
    		<artifactId>spring-boot-starter-web</artifactId>
		</dependency>
		<!-- https://mvnrepository.com/artifact/org.postgresql/postgresql -->
		<dependency>
    		<groupId>org.postgresql</groupId>
    		<artifactId>postgresql</artifactId>
    		</dependency>
		<!-- https://mvnrepository.com/artifact/org.mybatis/mybatis-spring -->
		<dependency>
    		<groupId>org.mybatis</groupId>
    		<artifactId>mybatis-spring</artifactId>
    		<version>2.0.5</version>
		</dependency>
		<!-- https://mvnrepository.com/artifact/org.mybatis/mybatis -->
		<dependency>
    		<groupId>org.mybatis</groupId>
    		<artifactId>mybatis</artifactId>
    		<version>3.5.5</version>
		</dependency>
		<!-- https://mvnrepository.com/artifact/org.springframework/spring-jdbc -->
		<dependency>
    		<groupId>org.springframework</groupId>
    		<artifactId>spring-jdbc</artifactId>
    	</dependency>
    	<!-- https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-jdbc -->
		<dependency>
		    <groupId>org.springframework.boot</groupId>
		    <artifactId>spring-boot-starter-jdbc</artifactId>
		    <version>2.3.2.RELEASE</version>
		</dependency>
	</dependencies>
	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
			</plugin>
		</plugins>
	</build>
</project>

```

<br>

#### ## src/main/java에 Controller, Service, Mapper, Dao, Dto 등 MVC 구조에 맞는 Package 생성하기

![](/assets/img/springImg/Spring-package-explorer.png) 

Spring Framework는 MVC 기반이기 때문에 다들 공부를 하고 왔을 것이라고 생각하겠다.

<br>

#### ## DatabaseConfig.java 파일 만들기

> **1. Src/main/java에서 Config package를 하나 만들자!**
>
> **2. 새로 만든 config 패키지에 databaseConfig.java 파일을 만들자**

<br>

**DatabaseConfig.java**

```java
package com.practice.security.Config;

import javax.sql.DataSource;
import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.SqlSessionTemplate;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;
import org.springframework.transaction.annotation.EnableTransactionManagement;
 
@Configuration
@MapperScan(basePackages="com.practice.security.Mapper") // Mapper 패키지 위치 입력하면 된다.
@EnableTransactionManagement
public class DatabaseConfig {
 
    @Bean
    public SqlSessionFactory sqlSessionFactory(DataSource dataSource) throws Exception {
        final SqlSessionFactoryBean sessionFactory = new SqlSessionFactoryBean();
        sessionFactory.setDataSource(dataSource);
        PathMatchingResourcePatternResolver resolver = new PathMatchingResourcePatternResolver();
      	// sql 파일들 위치 입력하면 된다.
        sessionFactory.setMapperLocations(resolver.getResources("sql/*.xml")); 
  
        return sessionFactory.getObject();
    }
    
    @Bean
    public SqlSessionTemplate sqlSessionTemplate(SqlSessionFactory sqlSessionFactory) throws Exception {
      final SqlSessionTemplate sqlSessionTemplate = new SqlSessionTemplate(sqlSessionFactory);
      return sqlSessionTemplate;
    }
}
```



### ## Controller, Service, Mapper, SQL 등 구현

간단한 스프링부트 프로젝트 Github 링크를 걸어놨으니, 여기서 필요한 컨트롤러나 서비스를 따가서 테스트해보면 될 것이다.

<br>

[Github으로 바로가기](https://github.com/ljh9601/Spring-Security-Example)

<br>



이제 프로젝트 생성과 JDBC, PostgreSQL 연동이 모두 완료됐다! 

물론 PostgreSQL 데이터베이스 정보가 있어야 저 소스가 돌아가니, 테스트할 테이블 정보를 미리 넣어두는 걸 까먹지 말자.

<br><br>