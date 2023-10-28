
select departments.department_name
from departments left join employees on departments.department_id=employees.employee_id
where employees.department_id is null; 