# # 1.1 DB Connection
# import psycopg2
# # psycopg2 를 이용하여 DB 에 접근하기 위해서는 connect 함수를 이용해야 합니다.
# # connect 함수를 아래와 같이 작성하여 db_connect 라는 connector 인스턴스를 생성합니다.
# # 여기서 기억해야할 것은 일반적으로 DB 에 연결할 때 user, password, host, port, database 의 총 5가지 정보가 필요하다는 것입니다.
# db_connect = psycopg2.connect(
#     user="llseungjun", 
#     password="22tmdwns",
#     host="localhost",
#     port=5432,
#     database="mydatabase",
# )

# # 1.2 Table Creation Query

# # iris dataset의 포멧에 맞게 작성
# # PostgreSQL에서 float64, int64의 데이터 포멧은 지원하지 않기에 각각 float8, int 로 선언해 주어야 합니다. 
# # 또한 column 이름은 sepal length (cm) 에 포함되어 있는 ( 때문에 이용할 수 없기 때문에 해당 부분을 제거해야 합니다.
# # 위의 내용을 반영한 query 는 다음과 같이 작성할 수 있습니다.
# create_table_query = """
# CREATE TABLE IF NOT EXISTS iris_data (
#     id SERIAL PRIMARY KEY,
#     timestamp timestamp,
#     sepal_length float8,
#     sepal_width float8,
#     petal_length float8,
#     petal_width float8,
#     target int
# );"""

# # 이제 작성한 query 를 DB 에 전달해야 합니다. 전달을 위해서는 아래의 과정을 수행하면 됩니다
# # 1. Connector 에서 cursor 를 열고, cursor 에 query 를 전달합니다.
# cur = db_connect.cursor()
# cur.execute(create_table_query)

# # 2. 전달된 query 를 실행하기 위해 connector 에 commit 을 합니다.
# db_connect.commit()

# # 3.Cursor 의 사용이 끝나면 cursor 를 close 합니다.
# cur.close()

# 위에서 설명한 3개의 과정은 아래처럼 하나의 프로세스로 처리할 수 있습니다.
# with db_connect.cursor() as cur:
#     cur.execute(create_table_query)
#     db_connect.commit()

# 위에서 작성한 코드를 이용하여 함수 형태로 작성합니다.
# def create_table(db_connect):
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS iris_data (
#         id SERIAL PRIMARY KEY,
#         timestamp timestamp,
#         sepal_length float8,
#         sepal_width float8,
#         petal_length float8,
#         petal_width float8,
#         target int
#     );"""
#     print(create_table_query)
#     with db_connect.cursor() as cur:
#         cur.execute(create_table_query)
#         db_connect.commit()

# 위에서 작성한 코드를 모아서 table_creator.py 로 작성합니다.
import psycopg2

def create_table(db_connect):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS iris_data (
        id SERIAL PRIMARY KEY,
        timestamp timestamp,
        sepal_length float8,
        sepal_width float8,
        petal_length float8,
        petal_width float8,
        target int
    );"""
    print(create_table_query)
    with db_connect.cursor() as cur:
        cur.execute(create_table_query)
        db_connect.commit()

if __name__ == "__main__":
    db_connect = psycopg2.connect(
        user="llseungjun", 
        password="22tmdwns",
        host="localhost",
        port=5432,
        database="mydatabase",
    )
    create_table(db_connect)