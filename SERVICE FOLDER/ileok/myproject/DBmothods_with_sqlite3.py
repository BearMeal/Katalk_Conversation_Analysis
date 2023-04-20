import sqlite3

def create_connection(db_path):
    conn = sqlite3.connect(db_path)
    return conn

def execute_query(conn, query, data=None):
    cursor = conn.cursor()
    if data:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
    conn.commit()
    return cursor

def fetch_data(cursor):
    return cursor.fetchall()

#--------------------------------------------------

#db_path 설정 필수

db_path = 'db.sqlite3' 

# NaverMovieData
def create_data_naver(content, label):
    conn = create_connection(db_path)
    query = "INSERT INTO myapp_navermoviedata (content, label) VALUES (?, ?)"
    data = (content, label)
    execute_query(conn, query, data)
    conn.close()

def get_data_naver(idx):
    conn = create_connection(db_path)
    query = "SELECT * FROM myapp_navermoviedata WHERE id=?"
    data = (idx,)
    cursor = execute_query(conn, query, data)
    result = fetch_data(cursor)
    conn.close()
    return result

def get_all_data_naver():
    conn = create_connection(db_path)
    query = "SELECT * FROM myapp_navermoviedata"
    cursor = execute_query(conn, query)
    result = fetch_data(cursor)
    conn.close()
    return result

def delete_data_naver(idx):
    conn = create_connection(db_path)
    query = "DELETE FROM myapp_navermoviedata WHERE id=?"
    data = (idx,)
    execute_query(conn, query, data)
    conn.close()

# Sentiword_dict1
def create_data_senti1(content, label):
    conn = create_connection(db_path)
    query = "INSERT INTO myapp_sentiword_dict1 (content, label) VALUES (?, ?)"
    data = (content, label)
    execute_query(conn, query, data)
    conn.close()

def get_data_senti1(idx):
    conn = create_connection(db_path)
    query = "SELECT * FROM myapp_sentiword_dict1 WHERE id=?"
    data = (idx,)
    cursor = execute_query(conn, query, data)
    result = fetch_data(cursor)
    conn.close()
    return result

def get_all_data_senti1():
    conn = create_connection(db_path)
    query = "SELECT * FROM myapp_sentiword_dict1"
    cursor = execute_query(conn, query)
    result = fetch_data(cursor)
    conn.close()
    return result

def delete_data_senti1(idx):
    conn = create_connection(db_path)
    query = "DELETE FROM myapp_sentiword_dict1 WHERE id=?"
    data = (idx,)
    execute_query(conn, query, data)
    conn.close()

# Sentiword_dict2
def create_data_senti2(content, sentiment, frequency, degree1, degree2):
    conn = create_connection(db_path)
    query = "INSERT INTO myapp_sentiword_dict2 (content, sentiment, frequency, degree1, degree2) VALUES (?, ?, ?, ?, ?)"
    data = (content, sentiment, frequency, degree1, degree2)
    execute_query(conn, query, data)
    conn.close()

def get_data_senti2(idx):
    conn = create_connection(db_path)
    query = "SELECT * FROM myapp_sentiword_dict2 WHERE id=?"
    data = (idx,)
    cursor = execute_query(conn, query, data)
    result = fetch_data(cursor)
    conn.close()
    return result

def get_all_data_senti2():
    conn = create_connection(db_path)
    query = "SELECT * FROM myapp_sentiword_dict2"
    cursor = execute_query(conn, query)
    result = fetch_data(cursor)
    conn.close()
    return result

def delete_data_senti2(idx):
    conn = create_connection(db_path)
    query = "DELETE FROM myapp_sentiword_dict2 WHERE id=?"
    data = (idx,)
    execute_query(conn, query, data)
    conn.close()

# User_kakao_data
def create_data_kakao(sender, content, time):
    conn = create_connection(db_path)
    query = "INSERT INTO myapp_user_kakao_data (sender, content, time) VALUES (?, ?, ?)"
    data = (sender, content, time)
    execute_query(conn, query, data)
    conn.close()

def get_data_kakao(idx):
    conn = create_connection(db_path)
    query = "SELECT * FROM myapp_user_kakao_data WHERE id=?"
    data = (idx,)
    cursor = execute_query(conn, query, data)
    result = fetch_data(cursor)
    conn.close()
    return result

def get_all_data_kakao():
    conn = create_connection(db_path)
    query = "SELECT * FROM myapp_user_kakao_data"
    cursor = execute_query(conn, query)
    result = fetch_data(cursor)
    conn.close()
    return result

def delete_data_kakao(idx):
    conn = create_connection(db_path)
    query = "DELETE FROM myapp_user_kakao_data WHERE id=?"
    data = (idx,)
    execute_query(conn, query, data)
    conn.close()

# korean
def create_data_korean(content, label):
    conn = sqlite3.connect(db_path)
    query = "INSERT INTO myapp_korean (id, content, label) VALUES (?, ?)"
    data = (id, content, label)
    conn.execute(conn, query, data)
    conn.commit()
    conn.close()

def get_data_korean(idx):
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM myapp_korean WHERE id=?"
    data = (idx,)
    cursor = conn.execute(conn, query, data)
    result = cursor.fetchone()
    conn.close()
    return result

def get_all_data_korean():
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM myapp_korean"
    cursor = conn.execute(conn, query)
    result = cursor.fetchall()
    conn.close()
    return result

def delete_data_korean(idx):
    conn = sqlite3.connect(db_path)
    query = "DELETE FROM myapp_korean WHERE id=?"
    data = (idx,)
    conn.execute(conn, query, data)
    conn.commit()
    conn.close()
