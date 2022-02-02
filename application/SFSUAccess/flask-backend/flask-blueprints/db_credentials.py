import pymysql as pymysql

connection = pymysql.connect(host='localhost',
                             user='admin',
                             password='password',
                             db='prod',
                             cursorclass=pymysql.cursors.DictCursor)
cur = connection.cursor()