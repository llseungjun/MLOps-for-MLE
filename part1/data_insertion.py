# 1.1 Iris 데이터 불러오기
# Iris 데이터를 불러온 뒤, 2) Table Creation 챕터에서 생성된 테이블의 column 이름과 일치하도록 수정합니다.
import pandas as pd
import psycopg2
from sklearn.datasets import load_iris

# X, y = load_iris(return_X_y=True, as_frame=True)
# df = pd.concat([X, y], axis="columns")
# rename_rule = {
#     "sepal length (cm)": "sepal_length",
#     "sepal width (cm)": "sepal_width",
#     "petal length (cm)": "petal_length",
#     "petal width (cm)": "petal_width",
# }
# df = df.rename(columns=rename_rule)
def get_data():
    X, y = load_iris(return_X_y=True, as_frame=True)
    df = pd.concat([X, y], axis="columns")
    rename_rule = {
        "sepal length (cm)": "sepal_length",
        "sepal width (cm)": "sepal_width",
        "petal length (cm)": "petal_length",
        "petal width (cm)": "petal_width",
    }
    df = df.rename(columns=rename_rule)
    return df

# 1.2 Data Insertion Query 작성
def insert_data(db_connect, data):
    insert_row_query = f"""
    INSERT INTO iris_data
        (timestamp, sepal_length, sepal_width, petal_length, petal_width, target)
        VALUES (
            NOW(),
            {data.sepal_length},
            {data.sepal_width},
            {data.petal_length},
            {data.petal_width},
            {data.target}
        );"""
    print(insert_row_query)
    with db_connect.cursor() as cur:
        cur.execute(insert_row_query)
        db_connect.commit()

if __name__ == "__main__":
    db_connect = psycopg2.connect(
        user="llseungjun", 
        password="22tmdwns",
        host="localhost",
        port=5432,
        database="mydatabase",
    )
    df = get_data()
    insert_data(db_connect, df.sample(1).squeeze())