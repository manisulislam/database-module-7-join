select m.first_name, e.first_name
from employees as e
join employees as m
on e.employee_id=m.manager_id;