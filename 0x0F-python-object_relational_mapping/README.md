# 0x0F - Python Object Relational Mapping

### creating a connection
db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)

### Getting a Cursor in MySQL Python
 cur = db.cursor()