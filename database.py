import psycopg2
con=psycopg2.connect(database="has")
cur=con.cursor()
cur.execute("CREATE TABLE blog7(id serial,filename text,imagedata text)")
con.commit()
con.close()
