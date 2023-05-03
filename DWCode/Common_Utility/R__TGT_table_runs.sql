CREATE Schema if not exists DW_TGT_POC;

USE Schema DW_TGT_POC;

create table if not exists R_TGT_Deploymnt (
	Deployment VARCHAR(30),
	Load_Date  TIMESTAMP_NTZ (9) default current_timestamp()

);

INSERT INTO R_TGT_Deploymnt (Deployment) VALUES ('TEST run time 2: ');