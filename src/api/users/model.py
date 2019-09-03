import sqlite3

class UserModel:
  def __init__(self, _id, email, password):
    self.id = _id
    self.email = email
    self.password = password

  @classmethod
  def find_all(cls):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "SELECT * FROM users"
    result = cursor.execute(query, (email,))
    rows = result.fetchall()
    users = list()

    if len(rows) > 0:
      users = [cls(*row) for row in rows]

    connection.close()
    return users

  @classmethod
  def find_by_email(cls, email):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE email=?"
    result = cursor.execute(query, (email,))
    row = result.fetchone()
    if row:
      user = cls(*row)
    else:
      user = None

    connection.close()
    return user

  @classmethod
  def find_by_id(cls, _id):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE id=?"
    result = cursor.execute(query, (_id,))
    row = result.fetchone()
    if row:
      user = cls(*row)
    else:
      user = None

    connection.close()
    return user

  @classmethod
  def create(cls, email, password):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = 'INSERT INTO users VALUES(NULL, ?, ?)'
    cursor.execute(query, (email, password))

    connection.commit()
    connection.close()

    return

  @classmethod
  def remove(cls, _id):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = 'DELETE FROM users WHERE id=?'
    cursor.execute(query, (_id,))

    connection.commit()
    connection.close()
    return
