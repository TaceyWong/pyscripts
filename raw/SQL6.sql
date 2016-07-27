
本次试验在Kingbase下完成

数据完整性部分：（每个操作都要验证）

重新定义student表、course表、sc表，具体要求如下：
1、student表（注意定义约束用 constraint ）
sno   主码
sname 非空
ssex  取值男或女
sage  15岁到35岁之间
sdep  非空

course表
cno  主码
cname 唯一
cpno  外码
credit 非空

sc表
sno，cno 为主码
sno，cno，分别为外码 （定义违约处理方式）
grade 0-100分之间

2、修改student表的约束
将sage的取值范围改为 15-50岁

授权部分：

1、新建用户u1、u2，u3 （connect类型）

2、将对student、course、sc三个表的查询、增删改权限授予u1,同时u1具有继续授予其他用户的权利；

3、以u1身份登录，将对三个表的查询权利授给u2；

4、以u1身份登录，将对三个表的查询，增加、修改的权利授给u3；

5、回收u1的对三个表的增删改权利

触发器部分：（选作）
1、在student表建立触发器 count_student，当新来一个学生后，就向新表s_count（ssex，scount）对应的性别人数加1。

数据安全性部分：（注意，每个操作都要验证相应的权利）




create table student
(
	sno char(10) primary key,
	sname char(20) not null,
	ssex char(2) check (ssex in('男','女' )),
	sage smallint check(sage >= 15 and sage <= 35),
	sdept char(20)
);
create table course
(
	cno char(20) primary key,
	cname char(20) unique,
	cpno char(20),
	credit smallint not null,
	foreign key (cpno) references course(cno)
);
create table sc
(
	sno char(20) ,
	cno char(20) ,
	grade smallint check(grade>=0 and grade<=100),
	primary key (sno,cno),
	foreign key (sno) references student(sno),
	foreign key (cno) references course(cno)
);

grant all privileges
on table student,course,sc
to u1
with grant option;

grant select
on table student,course,sc
to u2;
grant select ,update,insert
on table student,course,sc
to u3;

revoke all  privileges
on table student,course,sc
from u1;

create table s_count
(
	ssex char(2) ,
	scount smallint
) ;
insert 
into s_count(ssex,scount )
select distinct ssex ,count(*)
from student 
where ssex = '男'
group by ssex;
insert 
into s_count(ssex,scount )
select distinct ssex , count(*)
from student 
where ssex = '女'
group by ssex;
