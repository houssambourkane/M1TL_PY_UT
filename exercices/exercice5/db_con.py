def connect_to_db(db_name):
  if db_name != "my_database":
    raise ConnectionError("Could not connect to the database")
  return "Connection successful"
