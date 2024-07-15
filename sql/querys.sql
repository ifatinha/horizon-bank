SELECT fullname, email, phone, employee_number, manager_status FROM 
customer c 
join manager m
on m.manager_id = 1 and m.manager_id = c.id;

SELECT number, street, postal_code, neighborhood, city, state, country, address_type, is_primary, notes 
from address a
JOIN address_customer ac
on ac.id_address = a.id
JOIN customer c
on c.id = ac.id_customer and c.id = 1;

