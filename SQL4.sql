张志鹏请假实验5

1、查询选修了1号课的学生姓名（用三种方法实现）
2、查询没有选修1号课的学生学生姓名（用三种方法实现）
3、查询数据库课程的最高分；
4、查询每个学生的选课情况；（输出学号、姓名、课程号、成绩）
5、查询选择了1号课或3号课的学生姓名；
6、查询每个学院的学生人数；
7、查询计算机系的女生所有信息；
8、查询跟刘晨一个院系的学生学号、姓名；
9、查询选修人数超过2的课程号、课程名；
10、查询男女生人数；
11、按总成绩降序显示学生的学号、姓名、总成绩；
12、查询没有选修数据库的学生姓名
13、查询计算机学院男生中比该学院所有女生年龄都大的学号、姓名、年龄；
14、查询比自己平均成绩低的学生学号、课程号、课程名；
15、查询至少选修了学号为200215122学生所有选课的学生学号；

还原数据库代码：
create table student
(sno char(9) primary key ,
sname char(20) unique,
ssex char(9),
sage int,
sdept char(20)
);
create table course
(cno char(4) primary key,
 cname char(40),
 cpno char(4),
 ccredit smallint,
 foreign key (cpno) references course(cno)
  
);

create table sc
(sno char(9),
 cno char(4),
 grade smallint,
 foreign key (sno) references student(sno),
 foreign key (cno) references course(cno)
);
insert
into student (sno,sname,ssex,sage,sdept)
values('200215121','李勇','男',20,'cs');
insert
into student (sno,sname,ssex,sage,sdept)
values('200215122','刘晨','女',19,'cs');
insert
into student (sno,sname,ssex,sage,sdept)
values('200215123','王敏','女',18,'ma');
insert
into student (sno,sname,ssex,sage,sdept)
values('200215125','张立','男',19,'is');

insert
into course (cno,cname,cpno,ccredit)
values('2','数学',null,'2');
insert
into course (cno,cname,cpno,ccredit)
values('6','数据处理',null,'2');
insert
into course (cno,cname,cpno,ccredit)
values('4','操作系统','6','3');
insert
into course (cno,cname,cpno,ccredit)
values('7','PSCAL语言','6','4');
insert
into course (cno,cname,cpno,ccredit)
values('5','数据结构','7','4');
insert
into course (cno,cname,cpno,ccredit)
values('1','数据库','5','4');
insert
into course (cno,cname,cpno,ccredit)
values('3','信息系统','1','4');

insert
into sc (sno,cno,grade)
values('200215121','1','92');
insert
into sc (sno,cno,grade)
values('200215121','2','85');
insert
into sc (sno,cno,grade)
values('200215121','3','88');
insert
into sc (sno,cno,grade)
values('200215122','2','90');
insert
into sc (sno,cno,grade)
values('200215122','3','80');



试验实践SQL:
1、
①
select student.sname
from student,sc
where student.sno = sc.sno AND sc.cno = '1';
②
select sname
from student
where sno in 
	(
		select sno
		from sc
		where cno = '1'
	);
③
select sname
from student
where exists
	(
		select *
		from sc
		where sno = student.sno and cno = '1'
	);

2、
①
select sname
from student
where not exists
	(
		select *
		from sc
		where sno = student.sno and cno = '1'
	);
②
select distinct sname
from student
where sno not in
	(
		select sno
		from sc
		where sno = student.sno and cno = '1'
	);


3、
select max(grade)
from sc
where cno = '1'
4、select student.sno,sname,sc.cno,grade
from student,sc,course
where student.sno = sc.sno and sc.cno = course.cno;
【该语句未选课的无法查询】
5、
select distinct sname
from student ,sc
where cno = '1' or cno ='3';
6、
select sdept,count(distinct sno)
from student
group by sdept;

7、
select *
from student 
where sdept = 'cs' and ssex = '女';
8、
select sname,sno
from student
where sdept in 
	(
		select sdept 
		from student
		where sname = '刘晨'
	)
	and sname != '刘晨';

9、
select cname,cno
from course
where cno in
	(
		select cno
		from sc
		group by cno
		having count(*)>2
	);
10、
select ssex ,COUNT(sno)
from student
group by ssex;
11、
select sc.sno,student.sname,sum(sc.grade) as 总成绩
from sc ,student 
where sc.sno=student.sno
group by sc.sno,student.sname
order by 总成绩 desc
;
12、
select sname
from student
where sno not in 
	(
		select distinct sno
		from sc
		where cno = '1'
	);
13、
