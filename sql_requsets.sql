SELECT * FROM tasks WHERE user_id = 1;

SELECT * 
FROM tasks 
WHERE status_id IN (SELECT id FROM status WHERE name = 'new');

UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'in progress')
WHERE id = 5;

SELECT * 
FROM users 
WHERE id NOT IN (SELECT user_id FROM tasks);


INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Нове Завдання', 'Опис нового завдання, яке потрібно виконати.', 1, 2);

SELECT * 
FROM tasks 
WHERE status_id != (SELECT id FROM status WHERE name = 'завершено');


DELETE FROM tasks
WHERE id = 10;


SELECT *
FROM users
WHERE email LIKE '%@example.com';

UPDATE users
SET fullname = 'Mosya'
WHERE id = 1;

SELECT s.name, COUNT(t.id) AS task_count
FROM tasks t
JOIN status s ON t.status_id = s.id
GROUP BY s.name;


SELECT t.*
FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';


SELECT *
FROM tasks
WHERE description IS NULL OR description = 'Then involve economy protect line image. Occur data traditional drug.
Likely start move history. At five crime real true. Call last attorney.';


SELECT u.fullname, t.title, t.description
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
INNER JOIN status s ON t.status_id = s.id
WHERE s.name = 'in progress';

SELECT u.fullname, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;

