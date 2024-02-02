import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.execute("""
CREATE TABLE test(
id PR
)
""")