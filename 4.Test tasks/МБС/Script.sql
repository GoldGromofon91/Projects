INSERT INTO product (category_id,name,price)
VALUES (1,'Видеокарта AMD#1 ...',18300),
(1,'Видеокарта AMD#2 ...',16300),
(1,'Видеокарта AMD#3 ...',22900),
(1,'Видеокарта AMD#4 ...',21340),
(1,'Видеокарта NVIDIA#1 ...',28300),
(1,'Видеокарта NVIDIA#2 ...',23200),
(1,'Видеокарта NVIDIA#3 ...',22220),
(2,'Мат,Плата#1 ...',28300),
(2,'Мат,Плата#2 ...',28100),
(2,'Мат,Плата#3 ...',28200),
(2,'Мат,Плата#4 ...',28400),
(2,'Мат,Плата#5 ...',28500),
(3,'Процессор#1 ...',13300),
(3,'Процессор#2 ...',12300),
(3,'Процессор#3 ...',14300),
(3,'Процессор#4 ...',15300),
(4,'Акссесуар#1 ...',3300),
(4,'Акссесуар#2 ...',3400),
(4,'Акссесуар#3 ...',3500),
(4,'Акссесуар#4 ...',3600);


INSERT INTO property (name)
VALUES ('Количество в магазине'),
('Количество на складе'),
('Рассрочка');

INSERT INTO property (name)
VALUES ('Unique property');


INSERT INTO property_value (product_id,property_id,value)
VALUES (1,1,100),(1,2,20),(1,3,0),(2,1,23),(2,2,95),(2,3,1),(3,1,40),(3,2,54),(3,3,1),(4,1,230),(4,2,100),(4,3,1),(5,1,0),(5,2,0),(5,3,0),
(20,1,10),(20,2,20),(20,3,1);

INSERT INTO property_value (product_id,property_id,value)
VALUES (7,4,1),(8,4,1),(16,4,1);

ALTER TABLE product 
ADD CONSTRAINT FK_category_ID
FOREIGN KEY (category_id) REFERENCES category(id);

ALTER TABLE property_value 
ADD CONSTRAINT FK_property
FOREIGN KEY (property_id) REFERENCES property(id);

ALTER TABLE property_value 
ADD CONSTRAINT FK_property_product
FOREIGN KEY (product_id) REFERENCES product(id);


#id =1 id = 8(для него нет данных)
SELECT property_id,value 
FROM property_value AS pv 
WHERE pv.product_id = 1
property_id|value|
-----------|-----|
          1|  100|
          2|   20|
          3|    0|

#получить список названий уникальных свойств товара по названию категории (свойство должно быть только у 1 товара в категории). 

SET @usr = 'Видеокарты';
SELECT (SELECT name FROM property p3 WHERE p3.id = pv.property_id) AS Property_Name,
	p2.id, 
	p2.name,
	p2.price 
FROM product p2  
INNER JOIN property_value pv on pv.product_id = p2.id 
WHERE  category_id = (SELECT id from category c2 WHERE name = @usr) AND pv.property_id = 4;






