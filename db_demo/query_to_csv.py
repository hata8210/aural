import psycopg2
import csv
import os
import sys
from datetime import datetime

# 数据库连接信息 (根据 后端与数据库.md)
DB_CONFIG = {
    "host": "127.0.0.1",
    "port": "54322",
    "user": "postgres",
    "password": "postgres",
    "dbname": "postgres"
}

def export_query_to_csv(query, output_filename=None):
    """
    执行 SQL 查询并将结果导出为 CSV 文件。
    """
    if output_filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"query_result_{timestamp}.csv"
    
    # 确保在 db_demo 目录下生成
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_dir, output_filename)

    conn = None
    try:
        # 连接数据库
        print(f"正在连接数据库 {DB_CONFIG['host']}:{DB_CONFIG['port']}...")
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        # 执行查询
        print(f"执行查询: {query}")
        cur.execute(query)
        
        # 获取结果
        rows = cur.fetchall()
        
        # 获取列名
        colnames = [desc[0] for desc in cur.description]
        
        # 写入 CSV
        with open(output_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile)
            # 写入表头
            writer.writerow(colnames)
            # 写入数据
            writer.writerows(rows)
            
        print(f"成功导出 {len(rows)} 行数据到: {output_path}")
        return output_path
        
    except psycopg2.Error as e:
        print(f"数据库错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")
        if "psycopg2" in str(e):
            print("\n提示: 请确保已安装 psycopg2 库。")
            print("可以使用以下命令安装: pip install psycopg2-binary")
    finally:
        if conn:
            cur.close()
            conn.close()
            print("数据库连接已关闭。")

if __name__ == "__main__":
    # 默认查询示例 (可以根据需要修改)
    # 这里查询 profiles 表作为示例
    default_query = "SELECT id, email, name, role, \"createdAt\" FROM public.profiles LIMIT 50;"
    
    # 支持从命令行接收查询语句
    sql_query = sys.argv[1] if len(sys.argv) > 1 else default_query
    
    print("=== 数据库查询导出工具 ===")
    export_query_to_csv(sql_query)
