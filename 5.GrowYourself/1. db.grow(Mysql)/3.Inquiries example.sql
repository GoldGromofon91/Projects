/* Характерные выборки(предстваления)*/
-- ТОП-3 опытных пользователя
SELECT  p2.profile_id,
	p2.gender,
	if(rang_user = 4, 'top farmer', 4) as `rang_user`
FROM profile as p2 
ORDER BY rang_user DESC 
LIMIT 3;
+------------+--------+------------+
| profile_id | gender | rang_user  |
+------------+--------+------------+
|        100 | m      | top farmer |
|         14 | f      | top farmer |
|          3 | m      | top farmer |
+------------+--------+------------+

-- Сколько пользователей женщин/мужчин
SELECT gender, 
	count(*) AS total 
FROM profile p2 
WHERE gender = 'f' OR gender = 'm'  
GROUP;
+--------+-------+
| gender | total |
+--------+-------+
| f      |    53 |
| m      |    47 |
+--------+-------+

-- Самый дружелюбный(количество подтвержденных заявок)
SELECT DISTINCTROW  target_id,count(*) as total
FROM friends_request fr 
WHERE status = 'подтвержден' -- 'отправлен','в ожидании','отклонен'
GROUP BY target_id 
ORDER BY total DESC
LIMIT 3;
+-----------+-------+
| target_id | total |
+-----------+-------+
|        14 |     2 |
|        98 |     2 |
|        29 |     2 |
+-----------+-------+

-- Самый популярный контент
SELECT content_id, count(from_user_id ) AS 'popular_content' FROM comments_content cc
GROUP BY content_id
ORDER BY popular_content DESC
LIMIT 10;
+------------+-----------------+
| content_id | popular_content |
+------------+-----------------+
|         47 |               6 |
|         23 |               5 |
|         22 |               4 |
|         28 |               4 |
|         32 |               4 |
|         34 |               4 |
|         10 |               4 |
|         19 |               4 |
|         42 |               4 |
|          8 |               3 |
+------------+-----------------+
-- Какой пользователь чаще всего комментирует записи пользователя все записи, записи пользователя (user.id=N)
SELECT from_user_id, count(from_user_id ) AS `count_comments`  FROM comments_content cc
GROUP BY from_user_id 
ORDER BY count_comments DESC;

-- Запрос на вывод цен товаров и каталогов
SELECT p.id, p.name, p.price, c.name FROM products AS `p`
INNER JOIN catalogs AS `c` ON c.id = p.catalog_id 

-- Количество пользователей в каждом городе
SELECT  p.profile_id, p.home_city, COUNT(*) AS total_in_city 
FROM profile AS p
GROUP BY p.profile_id; 
+------------+----------------------+---------------+
| profile_id | home_city            | total_in_city |
+------------+----------------------+---------------+
|          1 | Opalmouth            |             1 |
|          2 | Port Lawrence        |             1 |
|          3 | West Chetport        |             1 |
|          4 | Lake Berenice        |             1 |
|          5 | Pollichbury          |             1 |
                    ...
|         96 | New Burleychester    |             1 |
|         97 | Carolineland         |             1 |
|         98 | Faheyfort            |             1 |
|         99 | North Garrettbury    |             1 |
|        100 | New Elyssa           |             1 |
+------------+----------------------+---------------+

-- Количество заказанных товаров по городам
SELECT profile.home_city, orders_products.product_id, COUNT(product_id) AS total
FROM orders_products
INNER JOIN orders ON orders.id = orders_products.order_id
INNER JOIN users ON users.id = orders.user_id
INNER JOIN profile ON profile_id = users.id 
GROUP BY profile.home_city, orders_products.product_id 
ORDER BY total DESC
LIMIT 5;
+-------------------+------------+-------+
| home_city         | product_id | total |
+-------------------+------------+-------+
| West Chetport     |         10 |     2 |
| West Elliottshire |         11 |     2 |
| North Oscar       |          4 |     2 |
| Lake Lilianefort  |         16 |     1 |
| Heathcoteshire    |          1 |     1 |
+-------------------+------------+-------+

-- Процедура поиска товаров(аксессуаров) которые следует до-заказать(если товаров меньше = N)
DROP PROCEDURE IF EXISTS grow.sp_pre_order;
DELIMITER $$
$$
CREATE PROCEDURE grow.sp_pre_order(num INT)
BEGIN
	DECLARE min_count INT;
	SET min_count = num;
	SELECT stp.product_id, p.name, stp.value from grow.storehouses_products as stp
	INNER JOIN grow.products as p ON stp.product_id = p.id 
	where value <= min_count
	ORDER BY value DESC; 
END$$
DELIMITER ;

call sp_pre_order(30)
+------------+------------------------------------------------------+-------+
| product_id | name                                                 | value |
+------------+------------------------------------------------------+-------+
|          1 | Домашная теплица - PREMIUM                           |    25 |
|         17 | Датчик замера сопротивления                          |    20 |
|         18 | Видеокамер                                           |    17 |
|         12 | Саррацения                                           |    13 |
|         15 | Гриндер                                              |    12 |
|          9 | Банксия                                              |    11 |
|          8 | Алламанда                                            |    10 |
|         10 | Баухиния                                             |     9 |
|         14 | Майка                                                |     7 |
|         11 | Блетилла                                             |     5 |
|         16 | Питательный резервуар                                |     5 |
|          6 | Манго                                                |     3 |
+------------+------------------------------------------------------+-------+

-- Процедура для поиска людей кто совершил хотя бы 1 заказ
DROP PROCEDURE IF EXISTS grow.sp_most_orders;
DELIMITER $$
$$
CREATE PROCEDURE grow.sp_most_orders()
BEGIN
	SELECT (SELECT id FROM users WHERE user_id = users.id ) AS `user_id`,
	(SELECT first_name FROM users WHERE user_id = users.id ) AS `name_user`, 
	COUNT(*) AS total_orders 
	FROM orders 
	WHERE user_id IN (SELECT id FROM users u2)
	GROUP BY user_id
	ORDER BY total_orders DESC;
END
$$
DELIMITER ;

CALL sp_most_orders() 
+---------+------------+--------------+
| user_id | name_user  | total_orders |
+---------+------------+--------------+
|      97 | Cara       |            4 |
|      56 | Gail       |            4 |
|      11 | Melyssa    |            3 |
|      85 | Amparo     |            3 |
|      16 | Stan       |            3 |
|      54 | Myrl       |            3 |
|      96 | Amely      |            2 |
|       3 | Willow     |            2 |
|       5 | Trycia     |            2 |
|      91 | Ally       |            2 |
|      86 | Jennifer   |            2 |
|      15 | Samanta    |            2 |
|      84 | Amaya      |            2 |
|      75 | Gloria     |            2 |
|      29 | Stephen    |            2 |
|      66 | Zita       |            2 |
|      51 | Devyn      |            2 |
|      44 | Christiana |            2 |
|      45 | Bert       |            2 |
|      46 | Mose       |            1 |
              ...
|      95 | Luther     |            1 |
|       2 | Cielo      |            1 |
|      55 | Mac        |            1 |
+---------+------------+--------------+