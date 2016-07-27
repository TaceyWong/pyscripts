
CREATE TABLE Student
(
	Sno NUMERIC(6)
		CONSTRAINT C1 CHECK (Sno BETWEEN 20120001 AND 20129999),
	Sname CHAR(20)
		CONSTRAINT C2 NOT NULL,
	Ssex CHAR(2)
		CONSTRAINT C3 CHECK(Ssex IN ('男','女')),
	Sage NUMERIC(3)
		CONSTRAINT C4 CHECK (Sage < 30),
	CONSTRAINT StudentKey PRIMARY KEY(Sno),	
	
	
);

CREATE TABLE Course
(
	Cno CHAR(4) ,
	Cname CHAR(40)
		CONSTRAINT C1 NOT NULL,
	Cpno CHAR(4),
	Ccredit SMALLINT
		CONSTRAINT C2 CHECK (Ccredit BETWEEN 1 AND 10),
	
	
	CONSTRAINT T1 FOREIGN KEY (Cpno)  REFERENCES Course (Cno),	
	CONSTRAINT CourseKey PRIMARY KEY(Cno),	
	
	
);



CREATE TABLE SC
(
	Sno NUMERIC(6)
		CONSTRAINT s1 CHECK (Sno BETWEEN 20120001 AND 20129999),
	Cno CHAR(4) ,
	Grade SMALLINT,
	CONSTRAINT SCKey PRIMARY KEY(Sno,Cno),
	CONSTRAINT sc1 FOREIGN KEY (Sno) REFERENCES Student (Sno),
	CONSTRAINT sc2 FOREIGN KEY (Cno) REFERENCES Course (Cno),
	
);


INSERT 
INTO Student(Sno,Sname,Ssex,Sage)
VALUES('20120001','李勇','男','20');
INSERT 
INTO Student(Sno,Sname,Ssex,Sage)
VALUES('20120002','刘晨','女','19');
INSERT 
INTO Student(Sno,Sname,Ssex,Sage)
VALUES('20120003','王敏','女','18');
INSERT 
INTO Student(Sno,Sname,Ssex,Sage)
VALUES('20120004','张立','男','19');

INSERT 
INTO Course(Cno,Cname,Cpno,Ccredit)
VALUES ('1','数据库','5','4');
INSERT 
INTO Course(Cno,Cname,Cpno,Ccredit)
VALUES ('2','数学','','2');
INSERT 
INTO Course(Cno,Cname,Cpno,Ccredit)
VALUES ('3','信息系统','1','4');
INSERT 
INTO Course(Cno,Cname,Cpno,Ccredit)
VALUES ('4','操作系统','6','3');
INSERT 
INTO Course(Cno,Cname,Cpno,Ccredit)
VALUES ('5','数据结构','7','4');
INSERT 
INTO Course(Cno,Cname,Cpno,Ccredit)
VALUES ('6','数据处理','','2');
INSERT 
INTO Course(Cno,Cname,Cpno,Ccredit)
VALUES ('7','PASCAL语言','6','4');


INSERT 
INTO SC(Sno,Cno,Grade)
VALUES ('20120001','1','92');
NSERT 
INTO SC(Sno,Cno,Grade)
VALUES ('20120001','2','85');
NSERT 
INTO SC(Sno,Cno,Grade)
VALUES ('2012001','3','88');
NSERT 
INTO SC(Sno,Cno,Grade)
VALUES ('2012002','2','90');
NSERT 
INTO SC(Sno,Cno,Grade)
VALUES ('2012002','3','80');

