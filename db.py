import  pymysql as ps
import time
import os

test = ("test")

def main():
 try:
    os.system("clear")
    time.sleep(2)

    cn=ps.connect(host='localhost',port=3306,user='root',password='sahil@1923',db='sahil')
    
    cmd=cn.cursor()
    
    query="select * from Miner"
    
    cmd.execute(query)
    
    rows=cmd.fetchall()
    
    # print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()    
    cn.close()

 except Exception as e:
    print(e)

main()
