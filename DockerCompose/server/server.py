#!/usr/bin/env python3

# python 시스템 라이브러리 import
# 서버에서 'index.html'을 다운받기 위한 라이브러리
# 파이썬과 함께 설치되어 있기 때문에 따로 추가적으로 설치할 것은 x
import http.server
import socketserver

#서버에서 client의 요청을 처리하는 변수
handler = http.server.SimpleHTTPRequestHandler

# port 1234에서 server를 시작하도록 정의

with socketserver.TCPServer(("", 1234), handler) as httpd:
    # client의 요청을 기다리면서 서버를 계속 실해앟도록 하는 명령
    httpd.serve_forever()