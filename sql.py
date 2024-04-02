import mysql.connector

from cleandata2 import grouped_elements

# 假设您已经按照之前的步骤准备了 grouped_elements

# 连接到 MySQL 数据库
# 请替换以下的连接参数为您自己的数据库信息
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="data"
)
cur = conn.cursor()

# 准备插入数据的 SQL 语句
insert_query = 'INSERT INTO trade_data (cat_id, month, label_list) VALUES (%s, %s, %s)'

for key, value in grouped_elements.items():
    cat_id, month = key.strip("()").split(',')
    label_list_str = "<"  # 开始标记
    for day, labels in sorted(value.items()):
        labels_str = "{" + ",".join(map(str, labels)) + "}"  # 每日标签
        label_list_str += labels_str
    label_list_str += ">"  # 结束标记

    # 执行插入操作
    cur.execute(insert_query, (cat_id, month, label_list_str))

# 提交事务
conn.commit()

# 关闭连接
cur.close()
conn.close()
