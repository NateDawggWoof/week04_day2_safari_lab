import psycopg2  
import psycopg2.extras as ext

def run_sql(sql, values = None): # value is there when creating or update
    conn = None
    results = []
    try:
        # connecting which db
        conn=psycopg2.connect("dbname='safari_park'")
        # turn database result into dict type
        cur = conn.cursor(cursor_factory=ext.DictCursor)  
        # run the query with values (if needed)
        cur.execute(sql, values)
        # confirm it
        conn.commit()
        # assign results
        results = cur.fetchall()
        # disconnecting db
        cur.close()           
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # disconnecting db anyway
        if conn is not None:
            conn.close()
    return results