# Heroku

>  wikipedia

**헤로쿠**(Heroku)는 웹 애플리케이션 배치 모델로 사용되는 여러 [프로그래밍 언어](https://ko.wikipedia.org/wiki/프로그래밍_언어)를 지원하는 클라우드 [PaaS](https://ko.wikipedia.org/wiki/PaaS)이다. 최초의 [클라우드 플랫폼](https://ko.wikipedia.org/wiki/클라우드_컴퓨팅)들 가운데 하나인 헤로쿠는 2007년 6월 개발이 시작되었고 당시에는 [루비](https://ko.wikipedia.org/wiki/루비_(프로그래밍_언어)) 프로그래밍 언어만 지원하였으나 지금은 [자바](https://ko.wikipedia.org/wiki/자바_(프로그래밍_언어)), [Node.js](https://ko.wikipedia.org/wiki/Node.js), [스칼라](https://ko.wikipedia.org/wiki/스칼라_(프로그래밍_언어)), [클로저](https://ko.wikipedia.org/wiki/클로저), [파이썬](https://ko.wikipedia.org/wiki/파이썬), [PHP](https://ko.wikipedia.org/wiki/PHP), [고](https://ko.wikipedia.org/wiki/고)를 지원한다.[[1\]](https://ko.wikipedia.org/wiki/헤로쿠#cite_note-1)[[2\]](https://ko.wikipedia.org/wiki/헤로쿠#cite_note-2) 이러한 이유로, 헤로쿠는 개발자가 모든 언어 간 비슷한 방식으로 애플리케이션들을 빌드, 실행하고 스케일링할 수 있게 하므로 헤로쿠는 [폴리글롯 플랫폼](https://ko.wikipedia.org/w/index.php?title=폴리글롯&action=edit&redlink=1)으로 간주된다. 헤로쿠는 2010년 [세일즈포스닷컴](https://ko.wikipedia.org/wiki/세일즈포스닷컴)에 인수되었다.[[3\]](https://ko.wikipedia.org/wiki/헤로쿠#cite_note-3)



## Quickstart with Python in Windows 10

### Prepare

1. [Heroku](https://signup.heroku.com/dc) 계정 생성
2. [Python](https://www.python.org/downloads/windows/) 3.7 설치
3. [Postgres](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) 설치

### Installation

1. [64-bit installer](https://cli-assets.heroku.com/heroku-x64.exe) 설치

2. 터미널에서 heroku login

   ```bash
   $ heroku login
   ```

   ![image-20201019132301790](README.assets/image-20201019132301790.png)

   ![image-20201019132304519](README.assets/image-20201019132304519.png)



### Deploy

1. 프로젝트를 생성하고 `Procfile`을 생성한다.

   ```
   web: gunicorn gettingstarted.wsgi --log-file -
   ```

2. 소스 코드를 저장할 수 있는 Heroku app을 생성한다.

   ```bash
   $ heroku create <app_name>
   ```

3. 로컬 저장소의 어플리케이션을 업로드한다.

   ```bash
   $ git push heroku main
   ```

4. Heroku app을 실행할 수 있는 공간을 Scaling 한다.

   ```bash
   $ heroku ps:scale web=1
   ```

5. 생성된 app을 브라우저로 실행한다.

   ```bash
   $ heroku open
   ```



### Running in local environment

1. requirements.txt 작성

   ```
   django
   gunicorn
   django-heroku
   ```

2. Procfile.windows 작성

   ```
   web: python manage.py runserver 0.0.0.0:5000
   ```

3. django collectstatic 실행

   ```bash
   $ python manage.py collectstatic
   ```

4. heroku local web 실행

   ```bash
   $ heroku local web -f Procfile.windows
   ```

5. [http://localhost:5000](http://localhost:5000/) 확인



### One-off dynos

dyno는 Linux 기반의 작은 컨테이너이다. Heroku를 통해 app이 배포되고 실행되는 dyno를 formation dyno라고 하며, 이와 다르게 서버의 script, bash 등을 실행할 때, 일회성으로 사용하는 dyno를 one-off dyno라고 한다.

- Python 콘솔 실행

  ```bash
  $ heroku run python manage.py shell
  ```

- bash 터미널 실행(종료 시 `exit`으로 dyno를 제거)

  ```bash
  $ heroku run bash
  ```

  



## 참고

[https://github.com/heroku/python-getting-started](https://github.com/heroku/python-getting-started)

[https://github.com/heroku/python-getting-started](https://github.com/heroku/python-getting-started)