SELECT p.first_name, p.last_name, a.city, a.state FROM person p
LEFT JOIN address a USING(person_id);