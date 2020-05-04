import db

keyword = '测试'
end = 6
beg = 3
insert_sql = """
            insert history (question , time)
            values('%s' , %s)
            """
insert_sql = insert_sql % (keyword, end - beg)
db.insert_or_update_data(insert_sql)
query_sql = 'select * from history'
print(db.query_data(query_sql))
