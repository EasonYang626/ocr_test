import pymysql
# 常用模块读写mysql
def get_conn():
    # 获取mysql连接
    # return mysql connection
    return pymysql.connect(
        host = '62.234.108.132',
        user = 'root',
        password = 'Yang7850512!',
        database = 'ocr',
        charset = 'utf8'
    )

def query_data(sql):
    # 根据查询的sql语句 返回查询结果
    # param sql:SQl语句
    # return list[dict]
    conn = get_conn()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        # 关闭连接
        conn.close()

def insert_or_update_data(sql):
    # 执行insert或update的sql
    # param sql : insert or update sql
    # return : 不返回内容
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        # 注意这里 只有commit才可以生效
        conn.commit()
    finally:
        # 关闭连接
        conn.close()    
