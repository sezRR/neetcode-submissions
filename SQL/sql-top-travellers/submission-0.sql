SELECT u.name, COALESCE(SUM(r.distance), 0) "travelled_distance" FROM users u
LEFT JOIN rides r ON r.user_id = u.id
GROUP BY u.id
ORDER BY "travelled_distance" DESC, u.name;