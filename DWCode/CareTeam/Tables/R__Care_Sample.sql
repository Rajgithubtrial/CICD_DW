CREATE Schema if not exists  DW_STG_POC;

USE Schema DW_STG_POC;

CREATE TABLE if not exists Sample7_Care_STG
(Patient_ID NUMBER
, P_NAME VARCHAR2(10)
, P_ADDRESS VARCHAR2(300));

CREATE Schema if not exists DW_TGT_POC;

USE Schema DW_TGT_POC;


CREATE TABLE if not exists Sample7_Care_TGT
(Patient_ID NUMBER
, P_NAME VARCHAR2(10)
, P_ADDRESS VARCHAR2(300)
);

CREATE TABLE if not exists Sample8_Care_TGT
(Patient_ID NUMBER
, P_NAME VARCHAR2(10)
, P_ADDRESS VARCHAR2(300)
);