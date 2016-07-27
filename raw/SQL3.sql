实验步骤：
一、还原实验2的数据（表和数据）
二、完成以下查询内容：
1、查询女生中年龄大于19岁的学生姓名；
2、查询计算机系的学生学号、姓名、出生年份，按出生年份降序显示（给出生年份起个别名）；
3、查询没有先行课的课程号、课程名；
4、查询选修了课程的学生学号；
5、查询年龄在18到20岁之间的学生学号、姓名、性别；
6、查询是计算机系或数学系的学生姓名，年龄；
7、查询课程名含有‘系统’的全部信息；
8、查询学号倒数第二位是‘2’的学生姓名、院系；
9、对选课表记录按照学号升序、学号一样的按成绩降序进行排序；
10、查询被选修了的课程号；
11、查询学分大于3的课程号和课程名；
12、查询每个学生的平均成绩；（输出学号、平均成绩）
13、查询每个学生的平均成绩；（输出学号、姓名、平均成绩）

PS：本次实验和上次实验写一个实验报告

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



实验实践SQL语句：
1'
select sname
from student
where ssex='Ů' and sage > 19;

2'
select sno,sname,2014 - sage as Birth
from student
where sdept = 'cs' 
order by Birth DESC;

3'

select cno,cname
from course
where cpno is  null;

4'

select distinct sno
from sc;

5'
select sno,sname,ssex
from student
where sage between 18 and 20;

6'

select sname,sage
from student
where sdept in ('cs','ma');

7'

select *
from course
where cname like '%ϵͳ%' ;

8'

select sname,sdept
from student
where sno like '%2_' ;

9'
select *
from sc
order by sno, grade desc;

10'
select distinct cno
from sc;

11'
select cno,cname
from course
where ccredit > 3;

12'
select sno,AVG(grade) as avg_grade
from sc 
group by sno;

13'
select sc.sno,student.sname,avg(sc.grade) 
from sc ,student 
where sc.sno=student.sno
group by sc.sno,student.sname;



