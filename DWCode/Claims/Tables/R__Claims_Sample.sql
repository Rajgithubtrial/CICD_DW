CREATE Schema if not exists  DW_STG_POC;

USE Schema DW_STG_POC;

CREATE TABLE if not exists Sample_Claims_STG
(Claim_ID NUMBER
, C_NAME VARCHAR2(10)
, C_ADDRESS VARCHAR2(300));

CREATE Schema if not exists  DW_TGT_POC;

USE Schema DW_TGT_POC;

CREATE TABLE if not exists Sample_Claims_TGT
(Claim_ID NUMBER
, C_NAME VARCHAR2(10)
, C_ADDRESS VARCHAR2(300)
);

CREATE TABLE if not exists Sample_Patient_LKP
(Claim_ID_ID NUMBER
, C_LANGUAGE VARCHAR2(10)
, CITY VARCHAR2(20)
, AREA VARCHAR2
	);