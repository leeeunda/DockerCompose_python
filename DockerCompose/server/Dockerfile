# FROM : base image 설정
# Dockerhub에서 python image import
# 이미지 이름 -> python, version-> latest 
FROM python:latest
LABEL mantainer="daun0219@gmail.com"

# 첫번째 파라미터는 host 위 파일의 이름  
# 두번째 파라미터는 이미지에 넣을 파일의 경로
# python code 실행하기 위해 server.py 파일과 index.html 파일 import
ADD server.py /server/
ADD index.html /server/

#작업할 폴더 설정 명령어가 실행되는 위치.
WORKDIR /server/
