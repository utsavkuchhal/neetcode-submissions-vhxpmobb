-- Write your query below
SELECT name, 
    CASE WHEN 
    SUM(distance) IS NOT NULL THEN SUM(distance) ELSE 0
    END as travelled_distance
FROM users u LEFT JOIN rides r ON u.id = r.user_id
GROUP BY u.id order BY travelled_distance DESC, name;