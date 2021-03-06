```
查找薪水涨幅超过15次的员工号emp_no以及其对应的涨幅次数t
CREATE TABLE `salaries` (
`emp_no` int(11) NOT NULL,
`salary` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`from_date`));
```
注：本题中的涨薪，其实可正可负，按写完后的理解

```
SELECT emp_no,count(emp_no) as t
FROM salaries
GROUP BY emp_no
HAVING t>15;
```