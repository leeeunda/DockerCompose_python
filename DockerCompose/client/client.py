#!/usr/bin/env python3

# python 시스템 라이브러리 import
# 서버에서 'index.html'을 다운받기 위한 라이브러리
# 파이썬과 함께 설치되어 있기 때문에 따로 추가적으로 설치할 것은 x
import urllib.request

# 'http://localhost:1234/'에 대한 request를 포함하는 변수 fp
# localhost: 서버가 local 서버
# 1234: 서버의 port 주소
fp = urllib.request.urlopen("http://localhost:1234/")

# 'encodedContent' 인코딩된 server response ('index.html').
# 'decodedContent' 디코딩된 server response (what we want to display).
encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")

# server file: 'index.html'출력
print(decodedContent)

# server 연결 close
fp.close()