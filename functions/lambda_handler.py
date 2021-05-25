import cx_Oracle
import os
import logging
import traceback
import boto3
import json
import datetime as dt
from base64 import b64decode

# INSERT STATEMENT
insert = """INSERT INTO V_DATAMART.EV_MAIL_DELIVERY_STATUS (MAIL,MAILSTATUS,MESSAGEID,DATASTATUSMAIL,INS_DT,INS_DB_DTTM,MESSAGEIDSES,REGION,IDCLIENT,CAMPANIA,MENSAJE,SUBTYPEBOUNCE,TYPEBOUNCE) VALUES ('{}', '{}', '{}', to_timestamp('{}','YYYY-MM-DD HH24:MI:SS.FF'), to_timestamp('{}','YYYY-MM-DD HH24:MI:SS.FF'), to_timestamp('{}','YYYY-MM-DD HH24:MI:SS.FF'), '{}', '{}','{}', '{}', '{}', '{}', '{}')"""

# SELECT STATEMENT
select_statement = """SELECT COUNT(*) AS TEST_COUNT FROM DUAL"""

# These ENV vars are encrypted with lambda/env
username = os.environ['DBUSER']
password = os.environ['DBPASSWORD']
host = os.environ['ENDPOINT']
port = os.environ['PORT']
sid = os.environ['DATABASE']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def make_connection():
    dsn = cx_Oracle.makedsn(host, port, sid)
    con = cx_Oracle.connect(username, password, dsn)
    return con

def log_err(errmsg):
    logger.error(errmsg)
    return {"body": errmsg , "headers": {}, "statusCode": 400, "isBase64Encoded":"false"}

logger.info("Cold start complete.") 

def handler(event, context):
    select_from()

def select_from():
    try: 
        cnx = make_connection()
        cur = cnx.cursor()

        try:
            sql = select_statement
            print("SELECT : ", sql)
            cur.execute(sql)

            columns = [i[0] for i in cur.description]
            rows = [dict(zip(columns, row)) for row in cur]
            logger.info(rows)
            
            response = "Select Completado"
        except:
            log_err("ERROR: Cannot execute cursor.\n{}".format(traceback.format_exc()))
            return log_err("ERROR: Cannot execute cursor.\n{}".format(traceback.format_exc()))        
        return {'statusCode': 200,'body': str(response)}
    except:
        log_err("ERROR: Cannot connect to database from handler.\n{}".format(traceback.format_exc()))
        return log_err("ERROR: Cannot connect to database from handler.\n{}".format(traceback.format_exc()))
    finally:
        try:
            cnx.close()
        except:
            pass

  

def insert_into(mail,mailstatus,messageid,datastatusmail,ins_dt,ins_db_dttm,messageidses,region,idclient,campania,mensaje,subtypebounce,typebounce):
    try: 
        cnx = make_connection()
        cur = cnx.cursor()

        try:
            sql = insert.format(mail,mailstatus,messageid,datastatusmail,ins_dt,ins_db_dttm,messageidses,region,idclient,campania,mensaje,subtypebounce,typebounce)
            # print("INSERT: ", sql)
            cur.execute(sql)
            cnx.commit()
            response = "Insert Completado"
        except:
            log_err("ERROR: Cannot execute cursor.\n{}".format(traceback.format_exc()))
            return log_err("ERROR: Cannot execute cursor.\n{}".format(traceback.format_exc()))        
        return {'statusCode': 200,'body': str(response)}
    except:
        log_err("ERROR: Cannot connect to database from handler.\n{}".format(traceback.format_exc()))
        return log_err("ERROR: Cannot connect to database from handler.\n{}".format(traceback.format_exc()))
    finally:
        try:
            cnx.close()
        except:
            pass