import mysql.connector

def export_labels_by_month_v3(cat_id):
    try:
        # 连接到 MySQL 数据库
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="data"
        )
        cur = conn.cursor()

        # 查询指定 cat_id 对应的行，并按 month 排序
        query = "SELECT month, label_list FROM trade_data WHERE cat_id = %s ORDER BY month"
        cur.execute(query, (cat_id,))

        # 准备输出到文本文件
        output_file = f"{cat_id}_labels_with_original_format.txt"
        with open(output_file, 'w') as f:
            for month, label_list in cur:
                # 直接写入每行的 month 和 label_list，保持 label_list 的原始格式
                f.write(f"{label_list}\n")

        print(f"Labels with original format exported to {output_file}.")

    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")

    finally:
        # 确保即使在发生异常的情况下也关闭数据库连接
        if conn.is_connected():
            cur.close()
            conn.close()

# 示例调用
export_labels_by_month_v3("50007011")
