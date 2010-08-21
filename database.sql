-- CREATE the database
   -- We currently use this.
CREATE TABLE item (id INTEGER PRIMARY KEY AUTOINCREMENT, title, time, description, price, area, people_num);

-- CREATE TABLE item (
--        id          INTEGER PRIMARY KEY,
--        title       TEXT,
--        time        TEXT DEFAULT now(),
--        description TEXT,
--        price       REAL,
--        area        TEXT,
--        people_num  INTEGER
-- );

-- c.execute('''create table verycd(
-- 	verycdid integer primary key,
-- 	title text,
-- 	status text,
-- 	brief text,
-- 	pubtime text,
-- 	updtime text,
-- 	category1 text,
-- 	category2 text,
-- 	ed2k text,
-- 	content text
-- )''')

--------------------------------------------------
-- INSERT data
INSERT INTO item (title, time, description, price, area, people_num)
       VALUES ("女鞋", datetime('now'), "女鞋说明", "30", "济南", 54);
