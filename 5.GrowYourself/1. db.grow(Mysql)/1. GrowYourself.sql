/* 
Описание: Текущая БД(grow) будет содержать на 1-м этапе 20 таблиц содержащих в 
ебе все данные о пользователях, товарах, акциях, базу знаний для нейронной 
сети(фото роста разных видов фруктов и цветов).

Решаемые задачи: База MysSQL на backend serever-е на 1-м этапе будет 
осуществлять запись и хранение данных, содержать несколько полезных 
хранимых процедур и представлений.
 */

DROP DATABASE IF EXISTS grow;
CREATE DATABASE grow;
USE grow;

-- ТАБЛИЦЫ СВЯЗАННЫЕ С КОММУНИКАЦИЕЙ ПОЛЬЗОВАТЕЛЕЙ
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL, -- serial?
	first_name VARCHAR(20),
	last_name VARCHAR(20),
	email VARCHAR(100) UNIQUE,
	password_hash VARCHAR (100),
	phone BIGINT UNSIGNED UNIQUE,
	
	PRIMARY KEY (id),
	INDEX user_name_idx(first_name,last_name)
);

DROP TABLE IF EXISTS profile;
CREATE TABLE profile (
	profile_id SERIAL,
	photo__profile_id BIGINT UNSIGNED NOT NULL,
	rang_user BIGINT UNSIGNED NOT NULL,
	gender CHAR(1),
	birthday DATE,
	home_city VARCHAR(100),
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW(),

	FOREIGN KEY (profile_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS all_rangs;
CREATE TABLE all_rangs(
	id SERIAL,
	name VARCHAR(50)
);

ALTER TABLE profile 
ADD CONSTRAINT fk_rang_user_to_all_rangs
FOREIGN KEY (rang_user) REFERENCES all_rangs(id);

DROP TABLE IF EXISTS message;
CREATE TABLE message(
	id SERIAL,
	from_user_id BIGINT UNSIGNED NOT NULL,
	to_user_id BIGINT UNSIGNED NOT NULL,
	body TEXT,
	status ENUM('не прочитано','прочитано'),
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW(),
	
	FOREIGN KEY (from_user_id) REFERENCES users(id),
	FOREIGN KEY (to_user_id) REFERENCES users(id)
);

/* Для изменения слов на английский
ALTER TABLE message
MODIFY COLUMN status ENUM('unread','read ');
*/

DROP TABLE IF EXISTS friends_request;
CREATE TABLE friends_request (
	initiator_id BIGINT UNSIGNED NOT NULL,
	target_id BIGINT UNSIGNED NOT NULL,
	status ENUM ('отправлен','в ожидании','подтвержден','отклонен'),
	time_request DATETIME DEFAULT NOW(), 
	time_confirm DATETIME ON UPDATE NOW(), 
	
	PRIMARY KEY (initiator_id, target_id),
	FOREIGN KEY (initiator_id) REFERENCES users(id),
	FOREIGN KEY (target_id) REFERENCES users(id),
	CHECK (initiator_id <> target_id)
);

/* Для изменения слов на английский
ALTER TABLE friends_request
MODIFY COLUMN status ENUM('send ',' pending ',' approved ',' rejected ');
*/

DROP TABLE IF EXISTS community; 
CREATE TABLE community (
	id SERIAL,
	name VARCHAR(200),
	admin_id BIGINT UNSIGNED NOT NULL,
	created_at DATETIME DEFAULT NOW(), 
	
	INDEX community_name_idx(name),
	FOREIGN KEY (admin_id) REFERENCES users(id)	
);

DROP TABLE IF EXISTS user_community; 
CREATE TABLE user_community (
	user_id BIGINT UNSIGNED NOT NULL,
	community_id BIGINT UNSIGNED NOT NULL,
  
	PRIMARY KEY (user_id, community_id), -- *чтобы не было 2 записей о пользователе и сообществе
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (community_id) REFERENCES community(id)
);

DROP TABLE IF EXISTS user_content; 
CREATE TABLE  user_content(
	id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL, 
	filename VARCHAR(255),
	type_id BIGINT UNSIGNED NOT NULL, 
	`size` INT UNSIGNED,
	body TEXT,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW(),
	
	FOREIGN KEY (user_id) REFERENCES users(id)
);

-- ******************************
-- ИЗМЕНЕНИЯ В таблице user_content
alter table user_content 
RENAME COLUMN file_obj to filename;

alter table user_content 
DROP foreign key  fk_filename_to_photo;
-- ******************************

DROP TABLE IF EXISTS media_types;
CREATE TABLE media_types(
	id SERIAL,
	name VARCHAR(20)	
);

DROP TABLE IF EXISTS comments_content;
CREATE TABLE comments_content (
	id SERIAL,
	content_id BIGINT UNSIGNED NOT NULL,
	from_user_id BIGINT UNSIGNED NOT NULL,
	body TEXT,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW(),
	
	FOREIGN KEY (content_id) REFERENCES user_content(id),
	FOREIGN KEY (from_user_id) REFERENCES users(id)
);

/* Таблицы media_photo и media_video (хранит ссылки просмотр потокового видео с онлайн камеры в шкафу, фотографии загруженные пользователем,
 * фотографии(с камеры online) для обработки нейронной сетью )*/

DROP TABLE IF EXISTS media_user;
CREATE TABLE media_user(
	user_id SERIAL,
	photo_albums_id BIGINT UNSIGNED NOT NULL,
	video_albums_id BIGINT UNSIGNED NOT NULL,
	created_at DATETIME DEFAULT NOW(),
	
	PRIMARY KEY(user_id),
	INDEX albums_name_idx(photo_albums_id)
);

DROP TABLE IF EXISTS photo_albums;
CREATE TABLE photo_albums(
	id SERIAL,
	name ENUM('downloads','knowledge_base'),
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW()
);

DROP TABLE IF EXISTS photo_file;
CREATE TABLE photo_file (
	id SERIAL,
	albums_id BIGINT UNSIGNED NOT NULL,
	file VARCHAR (50),
	created_at DATETIME DEFAULT NOW()
);

DROP TABLE IF EXISTS video_albums;
CREATE TABLE video_albums(
	id SERIAL,
	name ENUM('downloads','knowledge_base'),
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW()
);

DROP TABLE IF EXISTS video_file;
CREATE TABLE video_file (
	id SERIAL,
	albums_id BIGINT UNSIGNED NOT NULL,
	file VARCHAR (50),
	created_at DATETIME DEFAULT NOW()
);

-- ОРГАНИЗАЦИЯ СВЯЗЕЙ МЕЖДУ ТАБЛИЦАМИ
ALTER TABLE user_content 
ADD CONSTRAINT fk_type_id_to_media_types
FOREIGN KEY (type_id) REFERENCES media_types(id);

ALTER TABLE media_user 
ADD CONSTRAINT fk_media_to_user
FOREIGN KEY (user_id) REFERENCES users(id);

ALTER TABLE media_user 
ADD CONSTRAINT fk_photo_albums_id_to_albums
FOREIGN KEY (photo_albums_id) REFERENCES photo_albums(id);

ALTER TABLE media_user 
ADD CONSTRAINT fk_video_albums_id_to_albums
FOREIGN KEY (video_albums_id) REFERENCES video_albums(id);

ALTER TABLE photo_file 
ADD CONSTRAINT fk_photo_in_albums
FOREIGN KEY (albums_id) REFERENCES photo_albums(id);

ALTER TABLE video_file 
ADD CONSTRAINT fk_video_in_albums
FOREIGN KEY (albums_id) REFERENCES video_albums(id);

ALTER TABLE profile 
ADD CONSTRAINT fk_photo_profile_to_photo_file
FOREIGN KEY (photo__profile_id) REFERENCES photo_file(id);

ALTER TABLE user_content 
ADD CONSTRAINT fk_filename_to_photo
FOREIGN KEY (filename) REFERENCES photo_file(id);

ALTER TABLE user_content 
ADD CONSTRAINT fk_filename_to_video
FOREIGN KEY (filename) REFERENCES video_file(id);

ALTER TABLE profile 
ADD CONSTRAINT fk_photo_profile_to_photo_files
FOREIGN KEY (photo__profile_id) REFERENCES photo_file(id);

-- ТАБЛИЦЫ СВЯЗАННЫЕ С ПОКУПКОЙ ТОВАРОВ:
DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
  id SERIAL, -- serial?
  name VARCHAR(50),
  
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS products;
CREATE TABLE products (
	id SERIAL,
	name VARCHAR(255),
	desription TEXT,
	price DECIMAL (11,2),
	catalog_id BIGINT UNSIGNED NOT NULL,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW(),
	
	PRIMARY KEY(id),
	INDEX product_name_idx(name),
	FOREIGN KEY (catalog_id) REFERENCES catalogs(id)
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
	id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW(),
	
	
	KEY user_id_in_order_idx(user_id),
	FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS orders_products;
CREATE TABLE orders_products (
	id SERIAL,
	order_id BIGINT UNSIGNED NOT NULL,
	product_id BIGINT UNSIGNED NOT NULL,
	total INT UNSIGNED DEFAULT 1,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW(),
	
	FOREIGN KEY (order_id) REFERENCES orders(id),
	FOREIGN KEY (product_id) REFERENCES products(id)
);

DROP TABLE IF EXISTS storehouses;
CREATE TABLE storehouses (
	id SERIAL,
	name VARCHAR(50),
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW()
);

DROP TABLE IF EXISTS storehouses_products;
CREATE TABLE storehouses_products (
	id SERIAL,
	storehouse_id BIGINT UNSIGNED NOT NULL,
	product_id BIGINT UNSIGNED NOT NULL,
	value INT UNSIGNED COMMENT 'Остаток на складе',
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW(),
  
	FOREIGN KEY (storehouse_id) REFERENCES storehouses(id),
	FOREIGN KEY (product_id) REFERENCES products(id)

);
/* Таблица знаний(knowledge_base) для обучения нейронной сети, на этом этапе заполняться не будет.
DROP TABLE IF EXISTS knowledge_base;
CREATE TABLE knowledge_base (
	id SERIAL PRIMARY KEY,
	user_id BIGINT UNSIGNED NOT NULL,
	product_id BIGINT UNSIGNED NOT NULL, -- FK
	photo_file_id BIGINT UNSIGNED NOT NULL,
	storeknowledge BIGINT UNSIGNED NOT NULL,
    ....
	FOREIGN KEY (storehouse_id) REFERENCES storehouses(id),
	FOREIGN KEY (product_id) REFERENCES products(id)
	....
);*/