import psycopg2

try:
    conn = psycopg2.connect(
        dbname="my_python_app",   
        user="postgres",          
        password="ВАШ_ПАРОЛЬ",    
        host="localhost",
        port="5432"
    )
    print("✅ Подключение к PostgreSQL успешно")
except Exception as e:
    print("❌ Ошибка подключения:", e)
    exit()

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username TEXT NOT NULL
    );
""")
conn.commit()
print("🧱 Таблица 'users' создана (или уже существовала)")

users = [("Alice",), ("Bob",), ("Charlie",)]
cur.executemany("INSERT INTO users (username) VALUES (%s);", users)
conn.commit()
print("👥 Добавлены пользователи:", [u[0] for u in users])

cur.execute("SELECT username FROM users;")
rows = cur.fetchall()

print("\n📋 Список пользователей:")
for row in rows:
    print("-", row[0])

cur.close()
conn.close()
print("\n🔒 Соединение закрыто.")
