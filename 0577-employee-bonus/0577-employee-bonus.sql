# Write your MySQL query statement below
-- create table employee(empId int primary key, name varchar(50) not null, supervisor int, salary int);
-- insert into employee values(3, 'Brad',null,4000),(1,'John',3,1000),(2,'Dan',3,2000),(4,'Thomas',3,4000);
-- create  table bonus(empId int,bonus int);
-- insert into bonus values(2,500),(4,2000);

-- alter table bonus add constraint fk_emp_bonus foreign key (empId) references employee(empId);

select e.name, b.bonus from employee e left join bonus b on e.empId = b.empId where b.bonus<1000 or b.bonus is null; 

