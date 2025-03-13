# FROM : 이미지를 만들 때 base 가 되는 이미지를 지정합니다.
# RUN : 이미지를 만들 때 실행할 코드를 지정합니다.
# WORKDIR : 작업 directory 를 지정합니다. 해당 directory 가 없으면 새로 생성합니다. 
#           작업 directory 를 지정하면 그 이후 명령어는 해당 directory 를 기준으로 동작합니다.
# COPY : 파일이나 폴더를 이미지에 복사합니다. 
#        상대 경로를 사용할 경우, WORKDIR 로 지정한 directory 를 기준으로 복사합니다.
# ENTRYPOINT : 컨테이너가 실행될 때 시작할 프로세스를 입력합니다.
# CMD : 컨테이너가 실행될 때 ENTRYPOINT 에 전달할 argument 를 입력합니다.

FROM amd64/python:3.9-slim 

# 첫 번째 RUN 에서는 해당 Dockerfile 을 이용하여 Data Generator 를 띄울 때, 
# 컨테이너 안에 접근하여 psql을 사용하기 위해 postgresql-client 을 설치합니다.
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/app

# 두 번째 RUN 에서는 컨테이너에서 python 스크립트를 실행할 때 필요한 
# scikit-learn, pandas, psycopg2-binary 패키지들을 설치합니다.
# *참고 && 연산자는 앞의 코드가 실행 되어야만 뒤에가 실행됨
RUN pip install -U pip &&\
    pip install scikit-learn pandas psycopg2-binary

# 이번 챕터에서는 컨테이너에서 실행시키기 위해 앞서 작성한 data_generator.py를 복사합니다.
COPY data_generator.py data_generator.py

ENTRYPOINT ["python", "data_generator.py", "--db-host"]
# Change CMD to solve host finding error
CMD ["localhost"]