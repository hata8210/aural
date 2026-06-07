# 数据库查询与导出工具

此脚本用于从本地 PostgreSQL 数据库查询数据并导出为 CSV 文件。

## 环境要求

- Python 3.x
- `psycopg2-binary` 库

## 安装依赖

在 `aiops` conda 环境下，运行以下命令安装数据库驱动：

```bash
pip install psycopg2-binary
```

## 使用方法

### 1. 使用默认查询 (查询 profiles 表)

```bash
python query_to_csv.py
```

### 2. 使用自定义查询

```bash
python query_to_csv.py "SELECT * FROM projects WHERE name = 'My Project';"
```

## 数据库配置

配置信息已根据 `后端与数据库.md` 硬编码在脚本中：
- **Host:** 127.0.0.1
- **Port:** 54322
- **User:** postgres
- **Password:** postgres
- **Database:** postgres

## 输出文件

导出的 CSV 文件将保存在 `db_demo/` 目录下，文件名格式为 `query_result_YYYYMMDD_HHMMSS.csv`。
