# -*- coding: utf-8 -*-

# Mysql 配置
# HOSTNAME = 'localhost'
HOSTNAME = '118.89.143.159'
DATABASE = 'python_react_blog'
USERNAME = 'xilixjd'
PASSWORD = 'xilixjd'
DB_URI = 'mysql://{}:{}@{}:3306/{}'.format(USERNAME, PASSWORD, HOSTNAME, DATABASE)

# redis key
# 点赞
# 'zan_comment:{}'.format(comment_id)
# 查看文章
# 'blog:{}'.format(blog_id)

blog1_content = '''
# MySQL 必知必会
## 第3章 SHOW
### 3.1
```
SHOW COLUMNS FROM
```
对每个字段返回一行,行中包含字段名、数据 类型、是否允许NULL、键信息、默认值以及其他信息
## 第4章 检索数据
### 4.1 检索不同行
```
SELECT DISTINCT vend_id
FROM products;
```
### 4.2 限制结果
```
SELECT DISTINCT vend_id
FROM products
LIMIT 5, 5；
```
从第 6 行开始，再输出 5 行
### 4.3 完全限定
```
SELECT products.prod_name
FROM crashcourse.products;
```
位于 crashcourse 数据库中的 products 表的 prod_name 字段

## 第5章 排序检索数据
### 5.1 按多个列排序
```
SELECT prod_id, prod_price, prod_name
FROM products
ORDER BY prod_price, prod_name
```
首先按价格，然后再按名称排序
### 5.2 DESC 降序 ASC 升序
## 第6章 过滤数据
### 6.1 WHERE
#### 6.1.1
```
SELECT prod_name, prod_price
FROM products
WHERE prod_price = 2.50;
```
所有 prod_price 为 2.50 的行
#### 6.1.2
```
SELECT prod_name, prod_price
FROM products
WHERE prod_price BETWEEN 5 AND 10;
```
范围取值
#### 6.1.3 判断空值
```
SELECT prod_name, prod_price
FROM products
WHERE prod_price IS NULL;
```
## 第7章 数据过滤
### 7.1 组合 WHERE 子句
#### 7.1.1 AND
```
SELECT prod_name, prod_price
FROM products
WHERE vend_id = 1003 AND prod_price <= 10;
```
#### 7.1.2 OR
```
SELECT prod_name, prod_price
FROM products
WHERE vend_id = 1003 OR vend_id = 1002;
```
#### 7.1.3 计算次序
```
SELECT prod_name, prod_price
FROM products
WHERE vend_id = 1003 OR vend_id = 1002 AND prod_price >= 10;
```
AND 优先级高
由供应商1003制造的任何价格为10美元(含)以上的产品,或者由供应商1002制造的任何产品,而不管其价格如何

**解决办法：加括号**
```
SELECT prod_name, prod_price
FROM products
WHERE （vend_id = 1003 OR vend_id = 1002） AND prod_price >= 10;
```
### 7.2 IN 操作符
```
SELECT prod_name, prod_price
FROM products
WHERE vend_id IN (1002, 1003);
```
此SELECT语句检索供应商1002和1003制造的所有产品。
### 7.3 NOT 操作符
```
SELECT prod_name, prod_price
FROM products
WHERE vend_id NOT IN (1002, 1003);
```
## 第8章 用通配符进行过滤
### 8.1 LIKE 操作符
#### 8.1.1 % 通配符
```
SELECT prod_name, prod_price
FROM products
WHERE prod_name LIKE 'jet%'
```
此例子使用了搜索模式'jet%'。在执行这条子句时,将检索任意以jet起头的词
```
%anvil% 包含 anvir 的任何值
s%e s开头 e结尾
```
#### 8.1.2 下划线（_）通配符
与 % 一样，但是只匹配单个字符
% 能匹配0个字符不一样, _ 总是匹配一个字符
## 第9章 正则表达式进行搜索
### 9.1 .
```
SELECT prod_name
FROM products
WHERE prod_name REGEXP '.000'
ORDER BY prod_name
```
. 表示匹配任意一个字符
**LIKE需使用通配符，不然不返回如**
```
SELECT prod_name
FROM products
WHERE prod_name LIKE '1000'
ORDER BY prod_name
```
不返回数据
> 为区分大小写,可使用BINARY关键字,如WHERE prod_name REGEXP BINARY 'JetPack .000'。
### 9.2 | 或
```
SELECT prod_name
FROM products
WHERE prod_name REGEXP '1000|2000|300'
ORDER BY prod_name
```
### 9.3 匹配几个字符
```
REGEXP '[123] Ton'
```
匹配1或2或3
[^123]匹配除这些字符外的任何东西
### 9.4 匹配范围
[1-3] 相当于 [123]
### 9.5 匹配特殊字符
```
\\- 查找 -, \\. 查找.
```
### 9.6 匹配多个实例
```
\\([0-9] sticks?\\)
[0-9]匹配任意数字(这个例子中为1和5),sticks?匹配stick 和sticks
```
```
[[:digit:]]{4}匹配连在一起的任意4位数字
```
### 9.7 定位符
```
^ 开头
& 结尾
```
## 第10章 创建计算字段
### 10.1 计算字段
> 计算字段并不实际存在于数据库表中。计算段是运行时在SELECT语句 内创建的。
### 10.2 拼接字段
vendors 表要按照 name(location) 的形式列出
```
SELECT Concat(vend_name, '(', vend_country, ')')
FROM vendors
ORDER BY vend_name
```
#### 10.2.1 使用别名
```
SELECT Concat(vend_name, '(', vend_country, ')') AS
vend_title
FROM vendors
ORDER BY vend_name
```
以 vend_name 为字段打印值
### 10.3 执行算术计算
```
SELECT  prod_id,
        quantity,
        item_price,
        quantity*item_price AS expande_price
FROM orderitems
WHERE oreder_num = 20005
```
## 第11章 使用数据处理函数
### 11.1 使用函数
#### 11.1.1 文本处理函数
```
SELECT vend_name, Upper(vend_name) AS vend_name_upcase
FROM vendors
ORDER BY vend_name
```
```
Soundex()函数 匹配所有发音类似于参数的
```
```
WHERE Date(order_date) = '2015-09-01'
只想要日期，过滤时间，时间函数 Time()
```

## 第12章 汇总数据
### 12.1 聚集函数
> 使用这些函数,MySQL查询可用于检索数据

#### 12.1.1 AVG()函数
```
SELECT AVG(prod_price) AS avg_price
FROM products
```
返回一个列的平均值

#### 12.1.2 COUNT()函数
```
COUNT(*)选择所有行
COUNT(column) 对 column列有值得行进行计数
```

#### 12.1.3 MAX()、MIN()、SUM()函数
MAX()列中最大的值
MIN()最小值
SUM()总和
```
SELECT SUM(item_price*quantity) AS total_price
```

### 12.2 聚集不同值
```
SELECT AVG(DISTINCT prod_price) AS avg_price
```
去掉重复值

### 12.3 组合聚集函数
```
SELECT COUNT(*) AS num_items,
        MIN(prod_price) AS price_min,
        MAX(prod_price) AS price_max,
        AVG(prod_price) AS price_avg
```

## 第13章 分组数据
### 13.1 创建分组
```
SELECT vend_id, COUNT(*) AS num_prods
FROM products
GROUP BY vend_id;
```
结果
```
vend_id     num_prods
   1001     3
   1002     2
   1003     7
```

### 13.2 过滤分组 HAVING
```
SELECT cust_id, COUNT(*) AS orders
FROM orders
GROUP BY cust_id
HAVING COUNT(*) >= 2;
```
结果
```
cust_id     orders
  10001     2
```
> WHERE 在数据分组前进行过滤，HAVING在数据分组后进行过滤。

#### 13.2.1 同时使用WHERE HAVING
```
SELECT vend_id, COUNT(*) AS num_prods
FROM products
WHERE prod_price >= 10
GROUP BY vend_id
HAVING COUNT(*) >= 2
```
WHERE 过滤所有 prod_price 至少为 10 的行
然后按 vend_id 分组， HAVING 过滤计数为 2 或以上的分组，结果：
```
vend_id     num_prods
   1003     4
   1005     2
```
不使用 WHERE 结果
```
vend_id     num_prods
   1001     3
   1002     2
   1003     7
   1005     2
```

### 13.3 分组和排序
GROUP BY 输出的不是分组的顺序，如：
```
SELECT order_num, SUM(quantity*item_price) AS ordertotal
FROM orderitems
GROUP BY order_num
HAVING SUM(quantity*item_price) >= 50;
```
结果
```
order_num		ordertotal
  20005		149.87
  20006		55.00
```
为按总计订单价格排序输出，需添加 ORDER_BY 语句：
```
SELECT order_num, SUM(quantity*item_price) AS ordertotal
FROM orderitems
GROUP BY order_num
HAVING SUM(quantity*item_price) >= 50
ORDER BY ordertotal;
```
结果
```
order_num		ordertotal
  20006		55.00
  20005		149.87
```

### 13.4 SELECT 子句顺序
SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY -> LIMIT

## 第14章 使用子查询
### 14.1 利用子查询进行过滤
```
SELECT cust_name, cust_contact
FROM customers
WHERE cust_id IN (SELECT cust_id
   FROM orders
   WHERE order_num IN (SELECT order_num
     FROM orderitems
     WHERE prod_id = 'TNT2'
     ));
```
从内到外

### 14.2 作为计算字段使用子查询
需要显示 customers 表中每个客户的订单总数，订单与客户ID存储在 orders 表中
```
SELECT cust_name,
cust_state,
(SELECT COUNT(*)
 FROM orders
 WHERE orders.cust_id = customers.cust_id) AS orders
FROM customers
ORDER BY cust_name;
```
结果
```
cust_name		cust_state		orders
Coyote Inc.		MI				2
E Fudd			IL				1
```

## ==第15章 联结表==
### 15.1 创建联结
```
SELECT vend_name, prod_name, prod_price
FROM vendors, products
WHERE vendors.vend_id = products.vend_id
ORDER BY vend_name, prod_name;
```
结果
```
vend_name	prod_name		prod_price
ACME			Brid seed		10.00
ACME			Carrots			2.50
Anvils R Us		Detonator		13.00
```
#### 15.1.1 笛卡尔积
> 没有联结条件的表关系返回的结果为笛卡尔积
检出数目为第一个表的行数乘以第二个表的行数，结果显然不对

#### 15.1.2 内部联结
```
SELECT vend_name, prod_name, prod_price
FROM vendors INNER JOIN products
ON vendor.vend_id = products.vend_id;
```
返回结果与以上相同

#### 15.1.3 用联结查询来查询14章的例子
```
SELECT cust_name, cust_contact
FROM customers, orders, ordritems
WHERE customers.cust_id = orders.cust_id
AND orderitems.order_num = orders.order_num
AND prod_id = 'TNT2';
```

## ==第16章 创建表别名==


### 16.1 使用表别名
```
SELECT cust_name, cust_contact
FROM customers AS c, orders AS o, orderitems AS oi
WHERE c.cust_id = o.cust_id
AND oi.order_num = o.order_num
AND prod_id = 'TNT2';
```

### 16.2 使用不同类型的联结
#### 16.2.1 自联结
找出都是这个供应商的货物
```
SELECT prod_id, prod_name
FROM products
WHERE vend_id = (SELECT vend_id
   FROM products
   WHERE prod_id = 'DTNTR');
```
相当于
```
SELECT p1.prod_id, p2.prod_name
FROM products AS p1, products AS p2
WHERE p1.vend_id = p2.vend_id
AND p2.prod_id = 'DTNTR';
```
#### 16.2.2 自然联结
通配符只对第一个表使用。所有其他列明确列 出,所以没有重复的列被检索出来。

#### 16.2.3 外部联结
检索所有客户机器订单：
```
SELECT customers.cust_id, orders.order_num
FROM customers INNER JOIN orders
ON customers.cust_id = orders.cust_id;
```
为了检索所有客户，包括没有订单的客户
```
SELECT customers.cust_id, orders.order_num
FROM customers LEFT OUTER JOIN orders
ON customers.cust_id = orders.cust_id;
```
从左边的表选择所有行

### ==16.3 使用带聚集函数的联结==
检索所有客户及每个客户所下的订单数
```
SELECT customers.cust_name,
customers.cust_id,
COUNT(orders.order_num) AS num_ord
FROM customers INNER JOIN orders
ON customers.cust_id = orders.cust_id
GROUP BY customers.cust_id;
```
此SELECT语句使用INNER JOIN将customers和orders表互相关联。
GROUP BY子句按客户分组数据,因此,函数调用COUNT (orders.order_num)对每个客户的订单计数,将它作为num_ord返回。
```
SELECT customers.cust_name,
customers.cust_id,
COUNT(orders.order_num) AS num_ord
FROM customers LEFT OUTER JOIN orders
ON customers.cust_id = orders.cust_id
GROUP BY customers.cust_id;
```
个例子使用左外部联结来包含所有客户,甚至包含那些没有
任何下订单的客户。结果显示也包含了客户Mouse House,它 有0个订单。

## 第17章 组合查询
### 17.1 创建组合查询
####  17.1.1
```
SELECT vend_id, prod_id, prod_price
FROM products
WHERE prod_price <= 5
UNION
SELECT vend_id, prod_id, prod_price
FROM products
WHERE vend_id IN (1001,1002);
```
第一条SELECT检索价格不高于5的所有物品。第二条SELECT使 用IN找出供应商1001和1002生产的所有物品。
结果为两者的合集
####  17.1.2  包含或取消重复的行
UNION从查询结果集中自动去除了重复的行
如果 想返回所有匹配行,可使用UNION ALL而不是UNION

## 第18章 理解全文本搜索
### 18.1 启用全文搜索
#### 18.1.1
```
CREATE TABLE productnotes
(
note_id		int
FULLTEXT(note_text)
)
```
对它进行索引
```
SELECT note_text
FROM productnotes
WHERE Match(note_text) Against('rabbit');
```
Match(note_text)指示MySQL针对指定的 列进行搜索,Against('rabbit')指定词rabbit作为搜索文本。由于有 两行包含词rabbit,这两个行被返回。

#### 18.1.2 使用查询拓展
```
SELECT note_text
FROM productnotes
WHERE Match(note_text) Against('anvils' WITH QUERY EXPANSION);
```
这次返回了7行。第一行包含词anvils,因此等级最高。第二
行与anvils无关,但因为它包含第一行中的两个词(customer 和recommend),所以也被检索出来。第3行也包含这两个相同的词,但它 们在文本中的位置更靠后且分开得更远,因此也包含这一行,但等级为 第三。第三行确实也没有涉及anvils(按它们的产品名)。
#### 18.1.3 布尔文本搜索
```
SELECT note_text
FROM productnotes
WHERE Match(note_text) Against('heavy -rope*' IN BOOLEAN MODE);
```
这次只返回一行。这一次仍然匹配词heavy,但-rope*明确地指示MySQL排除包含rope*(任何以rope开始的词,包括 ropes)的行,这就是为什么上一个例子中的第一行被排除的原因。
> -排除一个词,而* 是截断操作符(可想象为用于词尾的一个通配符)

## 第19章 插入数据
### 19.1 插入完整的行
```
INSERT INTO Customers
VALUES( NULL,
'Pep',
'190 Main Street',
'Los Angeles',
'CA',
'90046',
'USA',
NULL,
NULL
);
```
不安全，应指定列名
### 19.2 插入多行
```
INSERT INTO customers(cust_name,
cust_address,
cust_city,
cust_state,
cust_zip,
cust_country
)
VALUES(
'Pep',
'190 Main Street',
'Los Angeles',
'CA',
'90046',
'USA'
),
VALUES(
'Pep',
'190 Main Street',
'Los Angeles',
'CA',
'90046',
'USA'
);
```
### 19.3 插入检索出的数据
```
INSERT INTO customers(cust_name,
cust_address,
cust_city,
cust_state,
cust_zip,
cust_country
)
SELECT cust_name,
cust_address,
cust_city,
cust_state,
cust_zip,
cust_country
FROM custnew;
```
## 第20章 更新和删除数据
### 20.1 更新
更新单列
```
UPDATE customers
SET cust_email = 'elmer@fudd.com'
WHERE cust_id = 10005;
```
更新多列
```
UPDATE customers
SET cust_email = 'elmer@fudd.com',
cust_name = 'The Fudds'
WHERE cust_id = 10005;
```

### 20.2 删除数据
```
DELETE FROM customers
WHERE cust_id = 10006;
```

## 第21章 创建和操纵表
### 21.1
```
CREATE TABLE customers
(
cust_id		int		NOT NULL AUTO_INCREMENT,
cust_name 	char(50) NOT NULL,
) ENGINE=InnoDB;
```
### 21.2 更新表
给表添加一个列
```
ALTER TABLE vendors
ADD vend_phone CHAR(20);
```
删除刚刚添加的列
```
ALTER TABLE vendors
DROP COLUMN vend_phone ;
```

### 21.3 删除表

### 21.4 重命名表

## 第22章 使用视图
```
CREATE VIEW productcustomers AS
SELECT cust_name, cust_contact, prod_id
FROM customers, orders, orderitems
WHERE customers.cust_id = orders.cust_id
AND orderitems.order_num = orders.order_num;
```
即一张虚拟表

## ==第23章 使用存储过程==
场景：
-  为了处理订单,需要核对以保证库存中有相应的物品。
-  如果库存有物品,这些物品需要预定以便不将它们再卖给别的人,并且要减少可用的物品数量以反映正确的库存量。
-  库存中没有的物品需要订购,这需要与供应商进行某种交互。 
- 关于哪些物品入库(并且可以立即发货)和哪些物品退订,需要通知相应的客户。

### 23.1 使用存储过程

#### 23.1.1 执行存储过程
```
CALL productpricing(@pricelow,
 @pricehigh,
 @priceaverage
);
```

#### 23.1.2 创建存储过程
```
CREATE PROCEDURE productpricing()
BEGIN
SELECT Avg(prod_price) AS priceaverage
FROM products;
END;
```
此存储过程名为productpricing,用CREATE PROCEDURE productpricing()语 句定义。如果存储过程接受参数,它们将在()中列举出来。此存储过程没 有参数,但后跟的()仍然需要。BEGIN和END语句用来限定存储过程体,过 程体本身仅是一个简单的SELECT语句(使用第12章介绍的Avg()函数)。

#### 23.1.3 删除存储过程
```
DROP PROCEDURE productpricing;
```

#### 23.1.3 使用参数
```
CREATE PROCEDURE productpricing(
OUT p1 DECIMAL(8,2),
OUT ph DECIMAL(8,2),
OUT pa DECIMAL(8,2)
)
BEGIN
SELECT Min(prod_price)
INTO p1
FROM products;
SELECT Max(prod_price)
INTO ph
FROM products;
SELECT Avg(prod_price)
INTO pa
FROM products;
END;
```
此存储过程接受3个参数:pl存储产品最低价格,ph存储产品最高价格,pa存储产品平均价格。每个参数必须具有指定的类 型,这里使用十进制值。关键字OUT指出相应的参数用来从存储过程传出 一个值(返回给调用者)。MySQL支持IN(传递给存储过程)、OUT(从存 储过程传出,如这里所用)和INOUT(对存储过程传入和传出)类型的参 数。存储过程的代码位于BEGIN和END语句内,如前所见,它们是一系列SELECT语句,用来检索值,然后保存到相应的变量(通过指定INTO关键 字)。

使用 IN 和 OUT 参数的例子：
```
CREATE PROCEDURE ordertotal(
IN onumber INT,
OUT ototal DECIMAL(8,2)
)
BEGIN
SELECT Sum(item_price*quantity)
FROM orderitems
WHERE order_num = onumber
INTO ototal;
END;
```
onumber定义为IN,因为订单号被传入存储过程。ototal定义为OUT,因为要从存储过程返回合计。SELECT语句使用这两个 参数,WHERE子句使用onumber选择正确的行,INTO使用ototal存储计算 出来的合计。

调用：
```
CALL ordertotal(20005, @total);
```

为了得到另一个订单的合计显示,需要再次调用存储过程,然后重 新显示变量:
```
CALL ordertotal(20009, @total);
SELECT @total;
```

#### 23.1.4 建立智能存储过程
```
CREATE PROCEDURE ordertotal(
IN onumber INT,
IN taxable BOOLEAN,
OUT ototal DECIMAL(8,2)
)
BEGIN
DECLARE total DECIMAL(8,2);
DECLARE taxrate INT DEFAULT 6;
SELECT Sum(item_price*quantity)
FROM orderitems
WHERE order_num = onumber
INTO total;
IF taxable THEN
SELECT total +(total/100*taxrate) INTO total;
END IF;
SELECT total INTO ototal;
END;
```
调用：
```
CALL ordertotal(20009, 0, @total);
SELECT @total;
```

## 第24章 使用游标
```
CREATE PROCEDURE processorders()
BEGIN
DECLARE done BOOLEAN DEFAULT 0;
DECLARE o INT;
DECLARE t DECIMAL(8,2);

DECLARE ordernumbers CURSOR
FOR
SELECT order_num FROM orders;

DECLARE CONTINUE HANDLER FOR SQLSTATE '02000' SET done='1';
CREATE TABLE IF NOT EXISTS ordertotals
(ordernum INT, total DECIMAL(8,2));

OPEN ordernumbers;

REPEAT
FETCH ordernumbers INTO o;
CALL ordertotal(0, 1, t);
INSERT INTO ordertotals(order_num, total)
VALUES(o, t);

UNTIL done END REPEAT;

CLOSE ordernumbers;
END;
```
在这个例子中,我们增加了另一个名为t的变量(存储每个订单的合计)。此存储过程还在运行中创建了一个新表(如果它不 存在的话),名为ordertotals。这个表将保存存储过程生成的结果。FETCH 像以前一样取每个order_num,然后用CALL执行另一个存储过程(我们在 前一章中创建)来计算每个订单的带税的合计(结果存储到t)。最后, 用INSERT保存每个订单的订单号和合计。

## 第25章 使用触发器
### 25.1 创建触发器
```
CREATE TRIGGER neworder AFTER INSERT ON products
FOR EACH ROW SELECT 'Product added';
```
在这个例子中,文本Product added将对每个插入的行显示一次。

### 25.2 删除触发器
DROP TRIGGER newproduct;

### 25.3 使用触发器
#### 25.3.1
-  在INSERT触发器代码内,可引用一个名为NEW的虚拟表,访问被 插入的行;
-  在BEFORE INSERT触发器中,NEW中的值也可以被更新(允许更改 被插入的值);
-  对于AUTO_INCREMENT列,NEW在INSERT执行之前包含0,在INSERT 执行之后包含新的自动生成值。

```
CREATE TRIGGER neworder AFTER INSERT ON orders
FOR EACH ROW SELECT NEW.order_num;
```
在插入一个新订单到orders表时,MySQL生 成一个新订单号并保存到order_num中。触发器从NEW. order_num取得 这个值并返回它。此触发器必须按照AFTER INSERT执行。
为测试这个触发器,试着插入一下新行,如下所示:
```
INSERT INTO orders(order_date, cust_id)
VALUES(Now(), 10001);
```
结果
```
order_num
20010
```
orders包含3个列。order_date和cust_id必须给出, order_num由MySQL自动生成,而现在order_num还自动被返
回。

#### 25.3.2 DELETE 触发器
- 在DELETE触发器代码内,你可以引用一个名为OLD的虚拟表,访 问被删除的行;
- OLD中的值全都是只读的,不能更新。
```
CREATE TRIGGER deleteorder BEFORE DELETE ON orders
FOR EACH ROW
BEGIN
INSERT INTO archive_orders(order_num, order_date, cust_id)
VALUES(OLD.order_num, OLD.order_date, OLD.cust_id);
END;
```
在任意订单被删除前将执行此触发器。它使用一条INSERT语句将OLD中的值(要被删除的订单)保存到一个名为archive_ orders的存档表中(为实际使用这个例子,你需要用与orders相同的列 创建一个名为archive_orders的表)。

#### 25.3.3 UPDATE 触发器
- 在UPDATE触发器代码中,你可以引用一个名为OLD的虚拟表访问 以前(UPDATE语句前)的值,引用一个名为NEW的虚拟表访问新 更新的值;
-  在BEFORE UPDATE触发器中,NEW中的值可能也被更新(允许更改 将要用于UPDATE语句中的值);
-  OLD中的值全都是只读的,不能更新。
```
CREATE TRIGGER updatevendor BEFORE UPDATE ON vendors
FOR EACH ROW SET NEW.vend_state = Upper(NEW.vend_state);
```
每次更新一个行时,NEW.vend_state中的值(将用来更新表行的值)都用Upper(NEW.vend_state)替换。

## 第28章 安全管理
### 28.1 访问控制
-  多数用户只需要对表进行读和写,但少数用户甚至需要能创建和 删除表;-
-  某些用户需要读表,但可能不需要更新表;
-  你可能想允许用户添加数据,但不允许他们删除数据;
-  某些用户(管理员)可能需要处理用户账号的权限,但多数用户
不需要;
-  你可能想让用户通过存储过程访问数据,但不允许他们直接访问
数据;
-  你可能想根据用户登录的地点限制对某些功能的访问。
'''

blog2_content = '''
# 单页web应用 JavaScript 从前端到后端

## 第1章 第一个单页应用
### 1.1 浏览器调试的新方法
打开 console ，在 source 里面，可以设置断点，允许一步步的执行。

## 第2章 温故 JavaScript
内容讲的很好，很清晰，例子举得非常详尽，==把其他书说不清的内容说出来了==

几乎是看到的书里面把闭包，原型，继承，作用域，变量提升，执行环境讲的最好的一本书

### 2.6.2 自执行匿名函数
为自执行匿名函数传递参数
```
(function (what_to_eat) {
    cosole.log(what_to_eat);
}) ('sandwich');
```
==这个函数对于单页应用来说很有用，因为他可以不污染全局名字空间==

```
(function ($) {         // 在此之前，$ 都代表 prototype 函数，他是一个库
    console.log($);
}) (jQuery);
```

### 2.6.3 模块模式
```
var prison = (function() {
    var prison_name = 'Mike',
        jail_item = '20 year term';

    return {
        prisoner: function() {
            return prison_name + jail_item;   // prison_name 和 jail_item 仿佛是
        },                                  // 这个返回的这个对象的私有变量一样
        setJailTerm: function(term) {
            jail_item = term;
        }
    }
}) ();
```
闭包：
```
var prison = (function() {
    var prisoner = 'Josh Powell';
    return {
        prisoner: function() {
            return prisoner;
        }
    }
}) ();
```
> 闭包是阻止垃圾回收器将变量从内存中移除的方法，使得在创建变量的执行环境的外面能访问到该变量。
'''

blog3_content = '''
# JavaScript 语言精粹
总结：本书在这个时间可能算比较老了，但其中也有一些精华，除了以下列出的，对我最有帮助的可能是其中的正则表达式那一块了。说实话，最近看这类 JS 介绍的书太多了，还是多学学框架及设计模式或者但也应用比较好
## 第4章 函数
### 4.1 Function.prototype.method
通过给 Function.prototype 增加一个 method 方法， 下次给对象增加方法的时候就不用键入 prototype 这几个字符。
```
Function.prototype.method = function(name, func) {
    this.prototype[name] = func;
};

// 例子
Number.method('integer', function() {
    return Math[this < 0? 'cell' : 'floor'](this);
});
```
## 第5章 继承

### 5.1 伪类
```
var Mammal = function(name) {
    this.name = name;
};
var Mammal.prototype.get_name = function() {
    return this.name;
};

var myMammal = new Mammal("Mammal");
var name = myMammal.get_name();

var Cat = function(name) {
    this.name = name;
    this.saying = "meow";
}
Cat.prototype = new Mammal();
Cat.prototype.get_name = function(n) {
    return this.name + this.says();
};

// 隐藏一些丑陋的细节
Function.method("inherits", function(Parent) {
    this.prototype = new Parent();
    return this;
});
var Cat = function (name) {
    this.name = name;
    this.saying = 'meow';
}
.inherits(Mammal)
.method('get_name', function() {
    return this.says() + this.name;
})
```

## 5.2 函数化
```
var mammal = function(spec) {
    var that = {};
    that.get_name = function() {
        return spec.name;
    };
    return that;
};
var myMammal = mammal({name: 'Herb'});

Object.method('superior', function(name) {
    var that = this;
    method = that[name];
    return function() {
        return method.apply(that, arguments);
    }
});

var coolcat = function(spec) {
    var that = cat(spec),
        super_get_name = that.superior('get_name');
    that.get_name = function(n) {
        return 'like' + super_get_name() + 'bady';
    };
};
var myCoolCat = coolcat({name: 'Bix'});
var name = myCoolCat.get_name();
```

## 第7章 正则表达式
### 7.1例子 写一个匹配 http 网址的正则
正则的介绍和写正则的思想、规范很好

```
？？？？
// 字面量对象
// 匹配 字符串的正则表达式
var regexp = /"(?:\\.|[^\\\"])*"/g

// RegExp 对象
var my_regexp = new RegExp(" ", 'g');
```

## 第 8 章 方法
### 8.1 比较函数
```
var by = function(name) {
    return function(o, p) {
        var a, b;
        if (typeof o === "object" && typeof p === "object" && o && p) {
            a = o[name];
            b = p[name];
            if (a === b) {
                return 0;
            }
            if (typeof a === typeof b) {
                return typeof a < typeof b ? -1 : 1;
            }
        } else {
            throw {
                name: "Error",
                message: "Expected an Object"
            }
        }
    }
};

var s = [
    {first: 'Joe', last: 'Besser'},
    {first: 'Moe', last: 'Howard'}
    {first: 'Joe', last: 'Derita'}
];
// 按 "first" key 值排序
s.sort(by('first'));
```

多键值排序：
```
var by = function(name, minor) {
    return function(o, p) {
        var a, b;
        if (typeof o === "object" && typeof p === "object" && o && p) {
            a = o[name];
            b = p[name];
            if (a === b) {
                return typeof minor === 'function' ? minor(o, p) : 0;
            }
            if (typeof a === typeof b) {
                return typeof a < typeof b ? -1 : 1;
            }
        } else {
            throw {
                name: "Error",
                message: "Expected an Object"
            }
        }
    }
};

// 先 按 "last" key 排序，再按 "first" 排序
s.sort(by('last', by('first')));
```

### 8.2 Array

#### 8.2.1 array.concat()

```
var a = ['a', 'b', 'c'];
var b = ['x', 'y', 'z'];
var c = a.concat(b, true);
// c ['a', 'b', 'c', 'x', 'y', 'z', true]
```

#### 8.2.2 array.join()
```
var a = ['a', 'b', 'c'];
var c = a.join(''); // abc
```

#### 8.2.3 array.slice(start, end)

从 start 起 复制到
end，默认值是数组长度
```
var a = ['a', 'b', 'c'];
var b = a.slice(0, 1) // ['a']
var c = a.slice(1); // ['b', 'c']
var d = a.slice(1, 2); // ['b']
```

#### 8.2.4 array.splice(start, deleteCount, item)
start 是从 array 中移除元素开始位置。 deleteCount 是要移除的元素个数。

```
var a = ['a', 'b', 'c'];
var r = a.splice(1, 1, 'ache', 'bug');
// a ['a', 'b', 'c']
// r ['b']

```

#### 8.2.4 array.unshift()

```
var a = ['a', 'b', 'c'];
var r = a.unshift('?', '@');

// a ['?', '@', 'a', 'b', 'c']
// r 5
```
### 8.3 String

#### 8.3.1 string.charAt(pos)
```
var name = 'Curly';
var init = name.charAt(0); // 'C'
```

#### 8.3.2 string.charCodeAt(pos)
返回 pos 位置的字符的字符位码
```
var name = 'Curly';
var init = name.charCodeAt(0); // 67
```

#### 8.3.3 string.indexOf(searchString, position)
```
var text = 'Mississippi';
var p = text.indexOf('ss'); // 2
p = text.indexOf('ss', 3); // 5
p = text.indexOf('ss', 6); // -1
```

#### 8.3.4 string.localeCompare(that)
```

```
'''

blog4_content = '''
# 《JavaScript高级程序设计》读书笔记
# 第3章 基本概念
## 3.1 && 和 ||
### 3.1.1 && 逻辑与
（1）如果第一个操作数是对象，则返回第二个操作数；

（2）如果第二个操作数是对象，则只有在第一个操作数的求值结果为 true 时，才会返回该对象；

（3）如果两个操作数都是对象，则返回第二个操作数；
### 3.1.2 || 逻辑或
（1）如果第一个操作数是对象，则返回第一个操作数；

（2）如果第一个操作数的求值结果为 false，则返回第二个操作数；

（3）如果两个操作数都是对象，则返回第一个操作数；
# 第5章 引用类型
## 5.1 arguments.callee
经典的递归调用

```
function factorial (num) {
    if (num <= 1) {
        return 1;
    } else {
        return num * arguments.callee(num - 1);
    }
}
```
## 5.2 arguments.callee.caller
这个属性保存了调用当前函数的函数的引用
```
function outer() {
    inner();
}

// 这个函数会打印 outer() 的源码
function inner() {
    alert(arguments.callee.caller); // inner.caller
}

```
## 5.3 函数的属性和方法
### 5.3.1 length 属性
> 希望接受命名参数的个数
### 5.3.2 prototype 属性
第 6 章详细介绍
### ==5.3.3 apply() 方法 (不太明白第一个参数)==
> 这两个方法的用途都是在特定的作用域中调用函数，实际上等于设置函数体内 this 对象的值。

```
function sum(num1, num2) {
    return num1 + num2;
}

function callsum1(num1, num2) {
    return sum.apply(this, arguments);
}

function callsum2(num1, num2) {
    return sum.apply(this, [num1, num2]);
}
```
### 5.3.4 call()
```
function sum(num1, num2) {
    return num1 + num2;
}

function callsum1(num1, num2) {
    return sum.call(this, num1, num2);
}
```
> 事实上，传递参数并非 apply() 和 call() 的真正用武之地，它们真正强大的地方是能够扩充函数赖以运行的作用域。

```
window.color = "red";
var o = {color: "blue"};

function sayColor() {
    alert(this.color);
}

sayColor.call(this); // red
sayColor.call(window); // red
sayColor.call(o); // blue
```
> 扩充作用域最大的好处是，对象不需要与方法有任何隅合关系

> ES5 还定义了一个方法：==bind()==。这个方法会创建一个函数的实例，其 this 值会被绑定到传给 bind() 函数的值。例如：

```
window.color = "red";
var o = {color: "blue"};

function sayColor() {
    alert(this.color);
}

var objectSayColor = sayColor.bind(o);
objectSayColor(); // blue
```
## 5.4 eval()方法
```
var msg = "hello world";
eval("alert(msg)");

```
# 第6章 面向对象的程序设计
## 6.1 数据属性和访问器属性
### 6.1.1 数据属性
- [[Configurable]]
- [[Enumerable]]
- [[Writable]]
- [[Value]]

```
var person = {};
Object.defineProperty(person, "name", {
    configurable: false,
    value: "Nicholas"
});

alert(person.name);// "Nicholas"
delete person.name;
alert(person.name); // "Nicholas"
```

### 6.1.2 访问器属性
- [[Get]]
- [[Set]]

```
var book = {
    _year: 2004, // 加下划线表示只能通过
                //对象方法访问的属性
    edition: 1
}

Object.defineProperty(book, "year", {
    get: function() {
        return this._year;
    }
    set: function(newValue) {
        if (newValue > 2014) {
            this._year = newValue;
            this.edition += newValue - 2014;
        }
    }
})

book.year = 2005;
alert(book.edition); // 2
```

## 6.2 定义多属性

```
var book = {};
Object.defineProperties(book, {
    _year: {
        writable: true,
        value: 2014
    }
    edition: {
        writable: true,
        value: 1
    },
    year: {
        get: function() {
            return this._year;
        }
        set: function(newValue){

        }
    }

})
```

## 6.3 读取属性的特性

```
var book = {};
Object.defineProperties(book, {
    _year: {
        writable: true,
        value: 2014
    }
    edition: {
        writable: true,
        value: 1
    },
    year: {
        get: function() {
            return this._year;
        }
        set: function(newValue){

        }
    }

})

var descriptor = Object.getOwnPropertyDescriptor(book, "_year");
alert(descriptor._year); // 2014
alert(descriptor.configurable); //false
alert(typeof descritptor.get) // "undefined"

var descriptor = Object.getOwnPropertyDscirptor(book, "year");
alert(descriptor.value); // "undefined"
alert(descirptor.enumerable); //false
alert(typeof descriptor.get); // "function"
```

## 6.4 构造函数用同一个 Function 实例的办法

> 有缺点，如果对象要定义很多方法，那么就要定义很多全局函数

```
function Person(name, age, job){
    this.name = name;
    this.age = age;
    this.job = job;
    this.sayName = sayName;
}

function sayName() {
    alert(this.name);
}
```

## ==6.5 原型模式==
> 每个函数都有个 prototype 属性，这个属性是一个指针，指向一个对象，而这个对象的用途是包含可以由特定类型的所有实例共享的属性和方法。使用原型对象的好处是可以让所有对象实例共享它所包含的属性和方法。

```
function Person() {
}

Person.prototype.name = "Nicholas";
Person.prototype.age = 29;
Person.prototype.sayName = function() {
    alert(this.name);
}

var person1 = new Person();
var person2 = new Person();
alert(person1.sayName == person2.sayName); // true

```

### 6.5.1 理解原型对象

> p148 原型对象图

> Person.prototype.constructor 指向 Person。当调用构造函数创建一个新实例后，该实例的内部将包含一个指针，指向构造函数的原型对象。==这个连接存在于实例与构造函数的原型对象之间，而不是存在于实例与构造函数之间。==

> 实例不能重写原型中的值

```
person1.name = "Greg";
alert(person1); // "Greg"
alert(person2); // "Nicholas"
```

### 6.5.2 确定该属性到底存在于对象中还是原型中

```
function hasPrototypeProperty(object, name) {
    return !object.hasOwnProperty(name) && (name in object); // 前者判断是否是实例中属性
                    // 后者只要有这个属性一定返回 true
}
```

### 6.5.3 Object.keys()

> 得到所有实例的属性，无论是否可枚举，或得到原型的所有可枚举属性

```
var keys = Object.keys(Person.prototype);

var p1keys = Object.keys(person1);
```

### 6.5.4 重设构造函数

函数创建时，会同时创建他的 prototype 对象，这个对象也会自动获得 constructor 属性，如果重写默认的 prototype 对象，constructor 属性也就变成了新对象的 constructor 属性（指向 Object），不再指向 Person 函数。则有：

```
var friend = new Person();
alert(friend.constructor == Object); // true
```

因此可以试一试：

```
Object.defineProperty(Person.prototype, "constructor", {
    enumerable: false,
    value: Person
})
```

### 6.5.5 原型对象的问题

```
function Person(){
}

Person.prototype = {
    constructor: Person,
    friends: ["shelby", "Court"]
}

var person1 = new Person();
var person2 = new Person();

person1.friends.push("van");

alert(person1.friends); // ["shelby", "Court", "van"]
alert(person2.friends); // ["shelby", "Court", "van"]
```

组合使用构造函数模式和原型模式：

```
function Person(){
    this.friends = ["shelby", "Court"]
}

Person.prototype = {
    constructor: Person
}

var person1 = new Person();
var person2 = new Person();

person1.friends.push("van");

alert(person1.friends); // ["shelby", "Court", "van"]
alert(person2.friends); // ["shelby", "Court"]
```

### 6.5.6 寄生构造函数模式
p160 不建议使用


### 6.5.7 稳妥构建函数模式

```
function Person(name, age) {
    var o = new Object();
    o.sayName = function() {
        alert(name);
    }
    return o;
}

var friend = new Person("Nicholas", 23);
friend.sayName(); // "Nicholas"
```

## 6.6 继承
### 6.6.1 原型链

```
function SperType() {
    this.property = true;
}

SuperType.prototype.getSuperValue = function() {
    return this.property;
};

function SubType() {
    this.subproperty = false;
}

SubType.prototype = new SuperType();
SubType.prototype.getSubType = function() {
    return this.subproperty;
};

var instance = new SubType();
alert(instance.getSuperValue()); // true
```
'''
blog5_content = '''
# 前端开发面试题

[github](https://github.com/markyun/My-blog/blob/master/Front-end-Developer-Questions/Questions-and-Answers/README.md)
## <a name='preface'>前言</a> ##


[只看问题点这里 ](http://markyun.github.io/2015/Front-end-Developer-Questions/ "Questions")

[看全部问题和答案点这里](https://github.com/markyun/My-blog/tree/master/Front-end-Developer-Questions/Questions-and-Answers "Questions-and-Answers")

本文由我收集总结了一些前端面试题，初学者阅后也要用心钻研其中的原理，重要知识需要系统学习、透彻学习，形成自己的知识链。万不可投机取巧，临时抱佛脚只求面试侥幸混过关是错误的！也是不可能的！不可能的！不可能的！

前端还是一个年轻的行业，新的行业标准， 框架， 库都不断在更新和新增，正如赫门在2015深JS大会上的《前端服务化之路》主题演讲中说的一句话：“每18至24个月，前端都会难一倍”，这些变化使前端的能力更加丰富、创造的应用也会更加完美。所以关注各种前端技术，跟上快速变化的节奏，也是身为一个前端程序员必备的技能之一。

最近也收到许多微博私信的鼓励和更正题目信息，后面会经常更新题目和答案到[github博客](http://markyun.github.io/)。希望前端er达到既能使用也会表达，对理论知识有自己的理解。可根据下面的知识点一个一个去进阶学习，形成自己的职业技能链。

**面试有几点需注意：(来源[寒冬winter](http://weibo.com/wintercn "微博：寒冬winter") 老师，github:@wintercn)**

1. 面试题目： 根据你的等级和职位的变化，入门级到专家级，广度和深度都会有所增加。

1. 题目类型： 理论知识、算法、项目细节、技术视野、开放性题、工作案例。

1. 细节追问： 可以确保问到你开始不懂或面试官开始不懂为止，这样可以大大延展题目的区分度和深度，知道你的实际能力。因为这种知识关联是长时期的学习，临时抱佛脚绝对是记不住的。

1. 回答问题再棒，面试官（可能是你面试职位的直接领导），会考虑我要不要这个人做我的同事？所以态度很重要、除了能做事，还要会做人。（感觉更像是相亲( •̣̣̣̣̣̥́௰•̣̣̣̣̣̥̀ )）

1. 资深的前端开发能把absolute和relative弄混，这样的人不要也罢，因为团队需要的是：你这个人具有可以依靠的才能（靠谱）。



**前端开发知识点：**

	HTML&CSS：
		对Web标准的理解、浏览器内核差异、兼容性、hack、CSS基本功：布局、盒子模型、选择器优先级、
		HTML5、CSS3、Flexbox

	JavaScript：
        数据类型、运算、对象、Function、继承、闭包、作用域、原型链、事件、RegExp、JSON、Ajax、
		DOM、BOM、内存泄漏、跨域、异步装载、模板引擎、前端MVC、路由、模块化、Canvas、ECMAScript 6、Nodejs

	其他：
        移动端、响应式、自动化构建、HTTP、离线存储、WEB安全、优化、重构、团队协作、可维护、易用性、SEO、UED、架构、职业生涯、快速学习能力

作为一名前端工程师，**无论工作年头长短都应该掌握的知识点**：

此条由 王子墨 发表在 [攻城师的实验室](http://lab.yuanwai.wang/)

		1、DOM结构 —— 两个节点之间可能存在哪些关系以及如何在节点之间任意移动。

		2、DOM操作 —— 如何添加、移除、移动、复制、创建和查找节点等。

		3、事件 —— 如何使用事件，以及IE和标准DOM事件模型之间存在的差别。

		4、XMLHttpRequest —— 这是什么、怎样完整地执行一次GET请求、怎样检测错误。

		5、严格模式与混杂模式 —— 如何触发这两种模式，区分它们有何意义。

		6、盒模型 —— 外边距、内边距和边框之间的关系，及IE8以下版本的浏览器中的盒模型

		7、块级元素与行内元素 —— 怎么用CSS控制它们、以及如何合理的使用它们

		8、浮动元素 —— 怎么使用它们、它们有什么问题以及怎么解决这些问题。

		9、HTML与XHTML —— 二者有什么区别，你觉得应该使用哪一个并说出理由。

		10、JSON —— 作用、用途、设计结构。



**备注：**

	根据自己需要选择性阅读，面试题是对理论知识的总结，让自己学会应该如何表达。

	资料答案不够正确和全面，欢迎欢迎Star和提交issues。

	格式不断修改更新中。

	更新记录：
	2016年3月25日：新增ECMAScript6 相关问题


###更新时间:  2016-3-25



## <a name='html'>HTML</a>

- Doctype作用？标准模式与兼容模式各有什么区别?

		（1）、<!DOCTYPE>声明位于位于HTML文档中的第一行，处于 <html> 标签之前。告知浏览器的解析器用什么文档标准解析这个文档。DOCTYPE不存在或格式不正确会导致文档以兼容模式呈现。

		（2）、标准模式的排版 和JS运作模式都是以该浏览器支持的最高标准运行。在兼容模式中，页面以宽松的向后兼容的方式显示,模拟老式浏览器的行为以防止站点无法工作。

- HTML5 为什么只需要写 <!DOCTYPE HTML>？

		 HTML5 不基于 SGML，因此不需要对DTD进行引用，但是需要doctype来规范浏览器的行为（让浏览器按照它们应该的方式来运行）；

		 而HTML4.01基于SGML,所以需要对DTD进行引用，才能告知浏览器文档所使用的文档类型。

- 行内元素有哪些？块级元素有哪些？ 空(void)元素有那些？

		首先：CSS规范规定，每个元素都有display属性，确定该元素的类型，每个元素都有默认的display值，如div的display默认值为“block”，则为“块级”元素；span默认display属性值为“inline”，是“行内”元素。

		（1）行内元素有：a b span img input select strong（强调的语气）
		（2）块级元素有：div ul ol li dl dt dd h1 h2 h3 h4…p

		（3）常见的空元素：
			<br> <hr> <img> <input> <link> <meta>
			鲜为人知的是：
			<area> <base> <col> <command> <embed> <keygen> <param> <source> <track> <wbr>

		不同浏览器（版本）、HTML4（5）、CSS2等实际略有差异
		参考: http://stackoverflow.com/questions/6867254/browsers-default-css-for-html-elements



- 页面导入样式时，使用link和@import有什么区别？


		（1）link属于XHTML标签，除了加载CSS外，还能用于定义RSS, 定义rel连接属性等作用；而@import是CSS提供的，只能用于加载CSS;

		（2）页面被加载的时，link会同时被加载，而@import引用的CSS会等到页面被加载完再加载;

		（3）import是CSS2.1 提出的，只在IE5以上才能被识别，而link是XHTML标签，无兼容问题;


- 介绍一下你对浏览器内核的理解？

		主要分成两部分：渲染引擎(layout engineer或Rendering Engine)和JS引擎。
		渲染引擎：负责取得网页的内容（HTML、XML、图像等等）、整理讯息（例如加入CSS等），以及计算网页的显示方式，然后会输出至显示器或打印机。浏览器的内核的不同对于网页的语法解释会有不同，所以渲染的效果也不相同。所有网页浏览器、电子邮件客户端以及其它需要编辑、显示网络内容的应用程序都需要内核。

		JS引擎则：解析和执行javascript来实现网页的动态效果。

		最开始渲染引擎和JS引擎并没有区分的很明确，后来JS引擎越来越独立，内核就倾向于只指渲染引擎。

- 常见的浏览器内核有哪些？

        Trident内核：IE,MaxThon,TT,The World,360,搜狗浏览器等。[又称MSHTML]
		Gecko内核：Netscape6及以上版本，FF,MozillaSuite/SeaMonkey等
		Presto内核：Opera7及以上。      [Opera内核原为：Presto，现为：Blink;]
		Webkit内核：Safari,Chrome等。   [ Chrome的：Blink（WebKit的分支）]

      详细文章：[浏览器内核的解析和对比](http://www.cnblogs.com/fullhouse/archive/2011/12/19/2293455.html)



- html5有哪些新特性、移除了那些元素？如何处理HTML5新标签的浏览器兼容问题？如何区分 HTML 和
HTML5？


		* HTML5 现在已经不是 SGML 的子集，主要是关于图像，位置，存储，多任务等功能的增加。
			  绘画 canvas;
			  用于媒介回放的 video 和 audio 元素;
			  本地离线存储 localStorage 长期存储数据，浏览器关闭后数据不丢失;
	          sessionStorage 的数据在浏览器关闭后自动删除;
			  语意化更好的内容元素，比如 article、footer、header、nav、section;
			  表单控件，calendar、date、time、email、url、search;
			  新的技术webworker, websocket, Geolocation;

		  移除的元素：
			  纯表现的元素：basefont，big，center，font, s，strike，tt，u;
			  对可用性产生负面影响的元素：frame，frameset，noframes；

	    * 支持HTML5新标签：
			 IE8/IE7/IE6支持通过document.createElement方法产生的标签，
		  	 可以利用这一特性让这些浏览器支持HTML5新标签，
          	 浏览器支持新标签后，还需要添加标签默认的样式。

		     当然也可以直接使用成熟的框架、比如html5shim;
			 <!--[if lt IE 9]>
				<script> src="http://html5shim.googlecode.com/svn/trunk/html5.js"</script>
			 <![endif]-->

		* 如何区分HTML5： DOCTYPE声明\新增的结构元素\功能元素


- 简述一下你对HTML语义化的理解？

		用正确的标签做正确的事情。
	    html语义化让页面的内容结构化，结构更清晰，便于对浏览器、搜索引擎解析;
	    即使在没有样式CSS情况下也以一种文档格式显示，并且是容易阅读的;
	    搜索引擎的爬虫也依赖于HTML标记来确定上下文和各个关键字的权重，利于SEO;
	    使阅读源代码的人对网站更容易将网站分块，便于阅读维护理解。



- HTML5的离线储存怎么使用，工作原理能不能解释一下？

		在用户没有与因特网连接时，可以正常访问站点或应用，在用户与因特网连接时，更新用户机器上的缓存文件。
		原理：HTML5的离线存储是基于一个新建的.appcache文件的缓存机制(不是存储技术)，通过这个文件上的解析清单离线存储资源，这些资源就会像cookie一样被存储了下来。之后当网络在处于离线状态下时，浏览器会通过被离线存储的数据进行页面展示。


		如何使用：
		1、页面头部像下面一样加入一个manifest的属性；
		2、在cache.manifest文件的编写离线存储的资源；
			CACHE MANIFEST
			#v0.11
			CACHE:
			js/app.js
			css/style.css
			NETWORK:
			resourse/logo.png
			FALLBACK:
			/ /offline.html
		3、在离线状态时，操作window.applicationCache进行需求实现。

	详细的使用请参考：

	[HTML5 离线缓存-manifest简介](http://yanhaijing.com/html/2014/12/28/html5-manifest/)

	[有趣的HTML5：离线存储](http://segmentfault.com/a/1190000000732617)



- 浏览器是怎么对HTML5的离线储存资源进行管理和加载的呢？

		在线的情况下，浏览器发现html头部有manifest属性，它会请求manifest文件，如果是第一次访问app，那么浏览器就会根据manifest文件的内容下载相应的资源并且进行离线存储。如果已经访问过app并且资源已经离线存储了，那么浏览器就会使用离线的资源加载页面，然后浏览器会对比新的manifest文件与旧的manifest文件，如果文件没有发生改变，就不做任何操作，如果文件改变了，那么就会重新下载文件中的资源并进行离线存储。
		离线的情况下，浏览器就直接使用离线存储的资源。
	详细请参考：[有趣的HTML5：离线存储](http://segmentfault.com/a/1190000000732617)

- 请描述一下 cookies，sessionStorage 和 localStorage 的区别？

		cookie是网站为了标示用户身份而储存在用户本地终端（Client Side）上的数据（通常经过加密）。
		cookie数据始终在同源的http请求中携带（即使不需要），记会在浏览器和服务器间来回传递。
		sessionStorage和localStorage不会自动把数据发给服务器，仅在本地保存。

		存储大小：
			cookie数据大小不能超过4k。
			sessionStorage和localStorage 虽然也有存储大小的限制，但比cookie大得多，可以达到5M或更大。

		有期时间：
	    	localStorage    存储持久数据，浏览器关闭后数据不丢失除非主动删除数据；
        	sessionStorage  数据在当前浏览器窗口关闭后自动删除。
			cookie          设置的cookie过期时间之前一直有效，即使窗口或浏览器关闭

- iframe有那些缺点？

		*iframe会阻塞主页面的Onload事件；
		*搜索引擎的检索程序无法解读这种页面，不利于SEO;

		*iframe和主页面共享连接池，而浏览器对相同域的连接有限制，所以会影响页面的并行加载。

        使用iframe之前需要考虑这两个缺点。如果需要使用iframe，最好是通过javascript
        动态给iframe添加src属性值，这样可以绕开以上两个问题。

- Label的作用是什么？是怎么用的？

		label标签来定义表单控制间的关系,当用户选择该标签时，浏览器会自动将焦点转到和标签相关的表单控件上。

		<label for="Name">Number:</label>
		<input type=“text“name="Name" id="Name"/>

		<label>Date:<input type="text" name="B"/></label>

- HTML5的form如何关闭自动完成功能？

		给不想要提示的 form 或某个 input 设置为 autocomplete=off。


- 如何实现浏览器内多个标签页之间的通信? (阿里)

		WebSocket、SharedWorker；
		也可以调用localstorge、cookies等本地存储方式；

		localstorge另一个浏览上下文里被添加、修改或删除时，它都会触发一个事件，
		我们通过监听事件，控制它的值来进行页面信息通信；
		注意quirks：Safari 在无痕模式下设置localstorge值时会抛出 QuotaExceededError 的异常；

- webSocket如何兼容低浏览器？(阿里)

		Adobe Flash Socket 、
		ActiveX HTMLFile (IE) 、
		基于 multipart 编码发送 XHR 、
		基于长轮询的 XHR

- 页面可见性（Page Visibility API） 可以有哪些用途？

		通过 visibilityState 的值检测页面当前是否可见，以及打开网页的时间等;
		在页面被切换到其他后台进程的时候，自动暂停音乐或视频的播放；


- 如何在页面上实现一个圆形的可点击区域？

		1、map+area或者svg
		2、border-radius
		3、纯js实现 需要求一个点在不在圆上简单算法、获取鼠标坐标等等

- 实现不使用 border 画出1px高的线，在不同浏览器的标准模式与怪异模式下都能保持一致的效果。

		<div style="height:1px;overflow:hidden;background:red"></div>


- 网页验证码是干嘛的，是为了解决什么安全问题。

		区分用户是计算机还是人的公共全自动程序。可以防止恶意破解密码、刷票、论坛灌水；
		有效防止黑客对某一个特定注册用户用特定程序暴力破解方式进行不断的登陆尝试。

- title与h1的区别、b与strong的区别、i与em的区别？

		title属性没有明确意义只表示是个标题，H1则表示层次明确的标题，对页面信息的抓取也有很大的影响；

		strong是标明重点内容，有语气加强的含义，使用阅读设备阅读网络时：<strong>会重读，而<B>是展示强调内容。

		i内容展示为斜体，em表示强调的文本；

		Physical Style Elements -- 自然样式标签
		b, i, u, s, pre
		Semantic Style Elements -- 语义样式标签
		strong, em, ins, del, code
		应该准确使用语义样式标签, 但不能滥用, 如果不能确定时首选使用自然样式标签。


## <a name='css'>CSS</a>

- 介绍一下标准的CSS的盒子模型？低版本IE的盒子模型有什么不同的？

		（1）有两种， IE 盒子模型、W3C 盒子模型；
		（2）盒模型： 内容(content)、填充(padding)、边界(margin)、 边框(border)；
		（3）区  别： IE的content部分把 border 和 padding计算了进去;



- CSS选择符有哪些？哪些属性可以继承？

		*   1.id选择器（ # myid）
			2.类选择器（.myclassname）
			3.标签选择器（div, h1, p）
			4.相邻选择器（h1 + p）
			5.子选择器（ul > li）
			6.后代选择器（li a）
			7.通配符选择器（ * ）
			8.属性选择器（a[rel = "external"]）
			9.伪类选择器（a:hover, li:nth-child）

		*   可继承的样式： font-size font-family color, UL LI DL DD DT;

		*   不可继承的样式：border padding margin width height ;



- CSS优先级算法如何计算？

		*   优先级就近原则，同权重情况下样式定义最近者为准;

		*   载入样式以最后载入的定位为准;

		优先级为:
		   !important >  id > class > tag
		   	important 比 内联优先级高

- CSS3新增伪类有那些？

			举例：
			p:first-of-type	选择属于其父元素的首个 <p> 元素的每个 <p> 元素。
			p:last-of-type	选择属于其父元素的最后 <p> 元素的每个 <p> 元素。
	        p:only-of-type	选择属于其父元素唯一的 <p> 元素的每个 <p> 元素。
			p:only-child		选择属于其父元素的唯一子元素的每个 <p> 元素。
			p:nth-child(2)	选择属于其父元素的第二个子元素的每个 <p> 元素。

			:after			在元素之前添加内容,也可以用来做清除浮动。
			:before			在元素之后添加内容
	 	    :enabled
			:disabled 		控制表单控件的禁用状态。
			:checked        单选框或复选框被选中。

- 如何居中div？


	*  水平居中：给div设置一个宽度，然后添加margin:0 auto属性

			div{
				width:200px;
				margin:0 auto;
			 }

	*  让绝对定位的div居中

			div {
				position: absolute;
				width: 300px;
				height: 300px;
				margin: auto;
				top: 0;
				left: 0;
				bottom: 0;
				right: 0;
				background-color: pink;	/* 方便看效果 */
			}

	*  水平垂直居中一

			确定容器的宽高 宽500 高 300 的层
			设置层的外边距

			div {
				position: relative;		/* 相对定位或绝对定位均可 */
				width:500px;
				height:300px;
				top: 50%;
				left: 50%;
				margin: -150px 0 0 -250px;     	/* 外边距为自身宽高的一半 */
				background-color: pink;	 	/* 方便看效果 */

			 }

	*  水平垂直居中二

			未知容器的宽高，利用 `transform` 属性

			div {
				position: absolute;		/* 相对定位或绝对定位均可 */
				width:500px;
				height:300px;
				top: 50%;
				left: 50%;
				transform: translate(-50%, -50%);
				background-color: pink;	 	/* 方便看效果 */

			}

	*  水平垂直居中三

			利用 flex 布局
			实际使用时应考虑兼容性

			.container {
				display: flex;
				align-items: center; 		/* 垂直居中 */
				justify-content: center;	/* 水平居中 */

			}
			.container div {
				width: 100px;
				height: 100px;
				background-color: pink;		/* 方便看效果 */
			}


- display有哪些值？说明他们的作用。

		  block       	块类型。默认宽度为父元素宽度，可设置宽高，换行显示。
		  none        	缺省值。象行内元素类型一样显示。
		  inline      	行内元素类型。默认宽度为内容宽度，不可设置宽高，同行显示。
		  inline-block  默认宽度为内容宽度，可以设置宽高，同行显示。
		  list-item   	象块类型元素一样显示，并添加样式列表标记。
		  table       	此元素会作为块级表格来显示。
		  inherit     	规定应该从父元素继承 display 属性的值。


- position的值relative和absolute定位原点是？

		  absolute
			生成绝对定位的元素，相对于值不为 static的第一个父元素进行定位。
		  fixed （老IE不支持）
			生成绝对定位的元素，相对于浏览器窗口进行定位。
		  relative
			生成相对定位的元素，相对于其正常位置进行定位。
		  static
			默认值。没有定位，元素出现在正常的流中（忽略 top, bottom, left, right z-index 声明）。
		  inherit
			规定从父元素继承 position 属性的值。

- CSS3有哪些新特性？

		  新增各种CSS选择器	（: not(.input)：所有 class 不是“input”的节点）
  		  圆角		    （border-radius:8px）
		  多列布局	    （multi-column layout）
		  阴影和反射	（Shadow\Reflect）
		  文字特效		（text-shadow、）
		  文字渲染		（Text-decoration）
		  线性渐变		（gradient）
		  旋转		 	（transform）
          缩放,定位,倾斜,动画,多背景
		  例如:transform:\scale(0.85,0.90)\ translate(0px,-30px)\ skew(-9deg,0deg)\Animation:

- 请解释一下CSS3的Flexbox（弹性盒布局模型）,以及适用场景？

		 一个用于页面布局的全新CSS3功能，Flexbox可以把列表放在同一个方向（从上到下排列，从左到右），并让列表能延伸到占用可用的空间。
		 较为复杂的布局还可以通过嵌套一个伸缩容器（flex container）来实现。
		 采用Flex布局的元素，称为Flex容器（flex container），简称"容器"。
		 它的所有子元素自动成为容器成员，称为Flex项目（flex item），简称"项目"。
		 常规布局是基于块和内联流方向，而Flex布局是基于flex-flow流可以很方便的用来做局中，能对不同屏幕大小自适应。
		 在布局上有了比以前更加灵活的空间。

		 具体：http://www.w3cplus.com/css3/flexbox-basics.html

- 用纯CSS创建一个三角形的原理是什么？

		把上、左、右三条边隐藏掉（颜色设为 transparent）
		#demo {
		  width: 0;
		  height: 0;
		  border-width: 20px;
		  border-style: solid;
		  border-color: transparent transparent red transparent;
		}

- 一个满屏 品 字布局 如何设计?

		简单的方式：
			上面的div宽100%，
			下面的两个div分别宽50%，
			然后用float或者inline使其不换行即可

- css多列等高如何实现？

		利用padding-bottom|margin-bottom正负值相抵；
		设置父容器设置超出隐藏（overflow:hidden），这样子父容器的高度就还是它里面的列没有设定padding-bottom时的高度，
		当它里面的任 一列高度增加了，则父容器的高度被撑到里面最高那列的高度，
		其他比这列矮的列会用它们的padding-bottom补偿这部分高度差。


- 经常遇到的浏览器的兼容性有哪些？原因，解决方法是什么，常用hack的技巧 ？

	    * png24位的图片在iE6浏览器上出现背景，解决方案是做成PNG8.

		* 浏览器默认的margin和padding不同。解决方案是加一个全局的*{margin:0;padding:0;}来统一。

		* IE6双边距bug:块属性标签float后，又有横行的margin情况下，在ie6显示margin比设置的大。

		  浮动ie产生的双倍距离 #box{ float:left; width:10px; margin:0 0 0 100px;}

	      这种情况之下IE会产生20px的距离，解决方案是在float的标签样式控制中加入 ——_display:inline;将其转化为行内属性。(_这个符号只有ie6会识别)

		  渐进识别的方式，从总体中逐渐排除局部。

		  首先，巧妙的使用“\9”这一标记，将IE游览器从所有情况中分离出来。
		  接着，再次使用“+”将IE8和IE7、IE6分离开来，这样IE8已经独立识别。

          css
	          .bb{
		          background-color:red;/*所有识别*/
			      background-color:#00deff\9; /*IE6、7、8识别*/
			      +background-color:#a200ff;/*IE6、7识别*/
			      _background-color:#1e0bd1;/*IE6识别*/
	          }


		*  IE下,可以使用获取常规属性的方法来获取自定义属性,
		   也可以使用getAttribute()获取自定义属性;
           Firefox下,只能使用getAttribute()获取自定义属性。
           解决方法:统一通过getAttribute()获取自定义属性。

		*  IE下,even对象有x,y属性,但是没有pageX,pageY属性;
           Firefox下,event对象有pageX,pageY属性,但是没有x,y属性。

		*  解决方法：（条件注释）缺点是在IE浏览器下可能会增加额外的HTTP请求数。

		*  Chrome 中文界面下默认会将小于 12px 的文本强制按照 12px 显示,
		   可通过加入 CSS 属性 -webkit-text-size-adjust: none; 解决。

		超链接访问过后hover样式就不出现了 被点击访问过的超链接样式不在具有hover和active了解决方法是改变CSS属性的排列顺序:
	    L-V-H-A :  a:link {} a:visited {} a:hover {} a:active {}


- li与li之间有看不见的空白间隔是什么原因引起的？有什么解决办法？

		行框的排列会受到中间空白（回车\空格）等的影响，因为空格也属于字符,这些空白也会被应用样式，占据空间，所以会有间隔，把字符大小设为0，就没有空格了。


- 为什么要初始化CSS样式。

		- 因为浏览器的兼容问题，不同浏览器对有些标签的默认值是不同的，如果没对CSS初始化往往会出现浏览器之间的页面显示差异。

		- 当然，初始化样式会对SEO有一定的影响，但鱼和熊掌不可兼得，但力求影响最小的情况下初始化。

		最简单的初始化方法： * {padding: 0; margin: 0;} （强烈不建议）

		淘宝的样式初始化代码：
		body, h1, h2, h3, h4, h5, h6, hr, p, blockquote, dl, dt, dd, ul, ol, li, pre, form, fieldset, legend, button, input, textarea, th, td { margin:0; padding:0; }
		body, button, input, select, textarea { font:12px/1.5tahoma, arial, \5b8b\4f53; }
		h1, h2, h3, h4, h5, h6{ font-size:100%; }
		address, cite, dfn, em, var { font-style:normal; }
		code, kbd, pre, samp { font-family:couriernew, courier, monospace; }
		small{ font-size:12px; }
		ul, ol { list-style:none; }
		a { text-decoration:none; }
		a:hover { text-decoration:underline; }
		sup { vertical-align:text-top; }
		sub{ vertical-align:text-bottom; }
		legend { color:#000; }
		fieldset, img { border:0; }
		button, input, select, textarea { font-size:100%; }
		table { border-collapse:collapse; border-spacing:0; }


- absolute的containing block(容器块)计算方式跟正常流有什么不同？

		无论属于哪种，都要先找到其祖先元素中最近的 position 值不为 static 的元素，然后再判断：
		1、若此元素为 inline 元素，则 containing block 为能够包含这个元素生成的第一个和最后一个 inline box 的 padding box (除 margin, border 外的区域) 的最小矩形；
		2、否则,则由这个祖先元素的 padding box 构成。
		如果都找不到，则为 initial containing block。

		补充：
		1. static(默认的)/relative：简单说就是它的父元素的内容框（即去掉padding的部分）
		2. absolute: 向上找最近的定位为absolute/relative的元素
		3. fixed: 它的containing block一律为根元素(html/body)，根元素也是initial containing block

- CSS里的visibility属性有个collapse属性值是干嘛用的？在不同浏览器下以后什么区别？

- position跟display、margin collapse、overflow、float这些特性相互叠加后会怎么样？

- 对BFC规范(块级格式化上下文：block formatting context)的理解？

		（W3C CSS 2.1 规范中的一个概念,它是一个独立容器，决定了元素如何对其内容进行定位,以及与其他元素的关系和相互作用。）
		 一个页面是由很多个 Box 组成的,元素的类型和 display 属性,决定了这个 Box 的类型。
		 不同类型的 Box,会参与不同的 Formatting Context（决定如何渲染文档的容器）,因此Box内的元素会以不同的方式渲染,也就是说BFC内部的元素和外部的元素不会互相影响。
- css定义的权重

		以下是权重的规则：标签的权重为1，class的权重为10，id的权重为100，以下例子是演示各种定义的权重值：

		/*权重为1*/
		div{
		}
		/*权重为10*/
		.class1{
		}
		/*权重为100*/
		#id1{
		}
		/*权重为100+1=101*/
		#id1 div{
		}
		/*权重为10+1=11*/
		.class1 div{
		}
		/*权重为10+10+1=21*/
		.class1 .class2 div{
		}

		如果权重相同，则最后定义的样式会起作用，但是应该避免这种情况出现


- 请解释一下为什么需要清除浮动？清除浮动的方式

	清除浮动是为了清除使用浮动元素产生的影响。浮动的元素，高度会塌陷，而高度的塌陷使我们页面后面的布局不能正常显示。

		1、父级div定义height；
		2、父级div 也一起浮动；
		3、常规的使用一个class；
			.clearfix:before, .clearfix:after {
			    content: " ";
			    display: table;
			}
			.clearfix:after {
			    clear: both;
			}
			.clearfix {
			    *zoom: 1;
			}

		4、SASS编译的时候，浮动元素的父级div定义伪类:after
			&:after,&:before{
			    content: " ";
		        visibility: hidden;
		        display: block;
		        height: 0;
		        clear: both;
			}

		解析原理：
		1) display:block 使生成的元素以块级元素显示,占满剩余空间;
		2) height:0 避免生成内容破坏原有布局的高度。
		3) visibility:hidden 使生成的内容不可见，并允许可能被生成内容盖住的内容可以进行点击和交互;
		4）通过 content:"."生成内容作为最后一个元素，至于content里面是点还是其他都是可以的，例如oocss里面就有经典的 content:".",有些版本可能content 里面内容为空,一丝冰凉是不推荐这样做的,firefox直到7.0 content:”" 仍然会产生额外的空隙；
		5）zoom：1 触发IE hasLayout。

		通过分析发现，除了clear：both用来闭合浮动的，其他代码无非都是为了隐藏掉content生成的内容，这也就是其他版本的闭合浮动为什么会有font-size：0，line-height：0。


- zoom:1的清楚浮动原理?

		清楚浮动，触发hasLayout；
		Zoom属性是IE浏览器的专有属性，它可以设置或检索对象的缩放比例。解决ie下比较奇葩的bug。
		譬如外边距（margin）的重叠，浮动清除，触发ie的haslayout属性等。

		来龙去脉大概如下：
		当设置了zoom的值之后，所设置的元素就会就会扩大或者缩小，高度宽度就会重新计算了，这里一旦改变zoom值时其实也会发生重新渲染，运用这个原理，也就解决了ie下子元素浮动时候父元素不随着自动扩大的问题。

		Zoom属是IE浏览器的专有属性，火狐和老版本的webkit核心的浏览器都不支持这个属性。然而，zoom现在已经被逐步标准化，出现在 CSS 3.0 规范草案中。

		目前非ie由于不支持这个属性，它们又是通过什么属性来实现元素的缩放呢？
		可以通过css3里面的动画属性scale进行缩放。

- 移动端的布局用过媒体查询吗？


	假设你现在正用一台显示设备来阅读这篇文章，同时你也想把它投影到屏幕上，或者打印出来，
	而显示设备、屏幕投影和打印等这些媒介都有自己的特点，CSS就是为文档提供在不同媒介上展示的适配方法

	<!-- link元素中的CSS媒体查询 -->
	当媒体查询为真时，相关的样式表或样式规则会按照正常的级联规被应用。
	当媒体查询返回假， <link> 标签上带有媒体查询的样式表 仍将被下载 （只不过不会被应用）。

	<link rel="stylesheet" media="(max-width: 800px)" href="example.css" />

	<!-- 样式表中的CSS媒体查询 -->
	包含了一个媒体类型和至少一个使用 宽度、高度和颜色等媒体属性来限制样式表范围的表达式。
	CSS3加入的媒体查询使得无需修改内容便可以使样式应用于某些特定的设备范围。

	<style>
		@media (min-width: 700px) and (orientation: landscape){
		  .sidebar {
		    display: none;
		  }
		}
	</style>



- 使用 CSS 预处理器吗？喜欢那个？

		SASS (SASS、LESS没有本质区别，只因为团队前端都是用的SASS)


- CSS优化、提高性能的方法有哪些？

		关键选择器（key selector）。选择器的最后面的部分为关键选择器（即用来匹配目标元素的部分）；
		如果规则拥有 ID 选择器作为其关键选择器，则不要为规则增加标签。过滤掉无关的规则（这样样式系统就不会浪费时间去匹配它们了）；
		提取项目的通用公有样式，增强可复用性，按模块编写组件；增强项目的协同开发性、可维护性和可扩展性;
		使用预处理工具或构建工具（gulp对css进行语法检查、自动补前缀、打包压缩、自动优雅降级）；


- 浏览器是怎样解析CSS选择器的？

		样式系统从关键选择器开始匹配，然后左移查找规则选择器的祖先元素。
		只要选择器的子树一直在工作，样式系统就会持续左移，直到和规则匹配，或者是因为不匹配而放弃该规则。


- 在网页中的应该使用奇数还是偶数的字体？为什么呢？

- margin和padding分别适合什么场景使用？

		margin是用来隔开元素与元素的间距；padding是用来隔开元素与内容的间隔。
		margin用于布局分开元素使元素与元素互不相干；
		padding用于元素与内容之间的间隔，让内容（文字）与（包裹）元素之间有一段


- 抽离样式模块怎么写，说出思路，有无实践经验？[阿里航旅的面试题]

- 元素竖向的百分比设定是相对于容器的高度吗？

- 全屏滚动的原理是什么？用到了CSS的那些属性？

- 什么是响应式设计？响应式设计的基本原理是什么？如何兼容低版本的IE？

- 视差滚动效果，如何给每页做不同的动画？（回到顶部，向下滑动要再次出现，和只出现一次分别怎么做？）

- ::before 和 :after中双冒号和单冒号 有什么区别？解释一下这2个伪元素的作用。

		单冒号(:)用于CSS3伪类，双冒号(::)用于CSS3伪元素。（伪元素由双冒号和伪元素名称组成）
		双冒号是在当前规范中引入的，用于区分伪类和伪元素。不过浏览器需要同时支持旧的已经存在的伪元素写法，
		比如:first-line、:first-letter、:before、:after等，
		而新的在CSS3中引入的伪元素则不允许再支持旧的单冒号的写法。

		想让插入的内容出现在其它内容前，使用::before，否者，使用::after；
		在代码顺序上，::after生成的内容也比::before生成的内容靠后。
		如果按堆栈视角，::after生成的内容会在::before生成的内容之上


- 如何修改chrome记住密码后自动填充表单的黄色背景 ？

		input:-webkit-autofill, textarea:-webkit-autofill, select:-webkit-autofill {
		  background-color: rgb(250, 255, 189); /* #FAFFBD; */
		  background-image: none;
		  color: rgb(0, 0, 0);
		}

- 你对line-height是如何理解的？

- 设置元素浮动后，该元素的display值是多少？

		自动变成了 display:block

- 怎么让Chrome支持小于12px 的文字？

		1、用图片：如果是内容固定不变情况下，使用将小于12px文字内容切出做图片，这样不影响兼容也不影响美观。
		2、使用12px及12px以上字体大小：为了兼容各大主流浏览器，建议设计美工图时候设置大于或等于12px的字体大小，如果是接单的这个时候就需要给客户讲解小于12px浏览器不兼容等事宜。
		3、继续使用小于12px字体大小样式设置：如果不考虑chrome可以不用考虑兼容，同时在设置小于12px对象设置-webkit-text-size-adjust:none，做到最大兼容考虑。
		4、使用12px以上字体：为了兼容、为了代码更简单 从新考虑权重下兼容性。

- 让页面里的字体变清晰，变细用CSS怎么做？

		-webkit-font-smoothing: antialiased;

- font-style属性可以让它赋值为“oblique” oblique是什么意思？

		倾斜的字体样式

- position:fixed;在android下无效怎么处理？

		fixed的元素是相对整个页面固定位置的，你在屏幕上滑动只是在移动这个所谓的viewport，
		原来的网页还好好的在那，fixed的内容也没有变过位置，
		所以说并不是iOS不支持fixed，只是fixed的元素不是相对手机屏幕固定的。
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no"/>

- 如果需要手动写动画，你认为最小时间间隔是多久，为什么？（阿里）

		多数显示器默认频率是60Hz，即1秒刷新60次，所以理论上最小间隔为1/60＊1000ms ＝ 16.7ms

- display:inline-block 什么时候会显示间隙？(携程)

		移除空格、使用margin负值、使用font-size:0、letter-spacing、word-spacing

- overflow: scroll时不能平滑滚动的问题怎么处理？

- 有一个高度自适应的div，里面有两个div，一个高度100px，希望另一个填满剩下的高度。

- png、jpg、gif 这些图片格式解释一下，分别什么时候用。有没有了解过webp？


- 什么是Cookie 隔离？（或者说：请求资源的时候不要让它带cookie怎么做）

		如果静态文件都放在主域名下，那静态文件请求的时候都带有的cookie的数据提交给server的，非常浪费流量，
		所以不如隔离开。

		因为cookie有域的限制，因此不能跨域提交请求，故使用非主要域名的时候，请求头中就不会带有cookie数据，
		这样可以降低请求头的大小，降低请求时间，从而达到降低整体请求延时的目的。

		同时这种方式不会将cookie传入Web Server，也减少了Web Server对cookie的处理分析环节，
		提高了webserver的http请求的解析速度。


- style标签写在body后与body前有什么区别？


- 什么是CSS 预处理器 / 后处理器？

		- 预处理器例如：LESS、Sass、Stylus，用来预编译Sass或less，增强了css代码的复用性，
		  还有层级、mixin、变量、循环、函数等，具有很方便的UI组件模块化开发能力，极大的提高工作效率。

		- 后处理器例如：PostCSS，通常被视为在完成的样式表中根据CSS规范处理CSS，让其更有效；目前最常做的
		  是给CSS属性添加浏览器私有前缀，实现跨浏览器兼容性的问题。



## <a name='js'>JavaScript</a>


-  介绍js的基本数据类型。

		 Undefined、Null、Boolean、Number、String、
		 ECMAScript 2015 新增:Symbol(创建后独一无二且不可变的数据类型 )

-  介绍js有哪些内置对象？

		Object 是 JavaScript 中所有对象的父对象

		数据封装类对象：Object、Array、Boolean、Number 和 String
		其他对象：Function、Arguments、Math、Date、RegExp、Error

		参考：http://www.ibm.com/developerworks/cn/web/wa-objectsinjs-v1b/index.html

-  说几条写JavaScript的基本规范？

		1.不要在同一行声明多个变量。
		2.请使用 ===/!==来比较true/false或者数值
		3.使用对象字面量替代new Array这种形式
		4.不要使用全局函数。
		5.Switch语句必须带有default分支
		6.函数不应该有时候有返回值，有时候没有返回值。
		7.For循环必须使用大括号
		8.If语句必须使用大括号
		9.for-in循环中的变量 应该使用var关键字明确限定作用域，从而避免作用域污染。

-  JavaScript原型，原型链 ? 有什么特点？

		每个对象都会在其内部初始化一个属性，就是prototype(原型)，当我们访问一个对象的属性时，
		如果这个对象内部不存在这个属性，那么他就会去prototype里找这个属性，这个prototype又会有自己的prototype，
		于是就这样一直找下去，也就是我们平时所说的原型链的概念。
		关系：instance.constructor.prototype = instance.__proto__

		特点：
		JavaScript对象是通过引用来传递的，我们创建的每个新对象实体中并没有一份属于自己的原型副本。当我们修改原型时，与之相关的对象也会继承这一改变。


		 当我们需要一个属性的时，Javascript引擎会先看当前对象中是否有这个属性， 如果没有的话，
		 就会查找他的Prototype对象是否有这个属性，如此递推下去，一直检索到 Object 内建对象。
			function Func(){}
			Func.prototype.name = "Sean";
			Func.prototype.getInfo = function() {
			  return this.name;
			}
			var person = new Func();//现在可以参考var person = Object.create(oldObject);
			console.log(person.getInfo());//它拥有了Func的属性和方法
			//"Sean"
			console.log(Func.prototype);
			// Func { name="Sean", getInfo=function()}




-  JavaScript有几种类型的值？，你能画一下他们的内存图吗？

		栈：原始数据类型（Undefined，Null，Boolean，Number、String）
		堆：引用数据类型（对象、数组和函数）

		两种类型的区别是：存储位置不同；
		原始数据类型直接存储在栈(stack)中的简单数据段，占据空间小、大小固定，属于被频繁使用数据，所以放入栈中存储；
		引用数据类型存储在堆(heap)中的对象,占据空间大、大小不固定。如果存储在栈中，将会影响程序运行的性能；引用数据类型在栈中存储了指针，该指针指向堆中该实体的起始地址。当解释器寻找引用值时，会首先检索其在栈中的地址，取得地址后从堆中获得实体

	![Stated Clearly Image](http://www.w3school.com.cn/i/ct_js_value.gif)



-  Javascript如何实现继承？

		1、构造继承
		2、原型继承
		3、实例继承
		4、拷贝继承

		原型prototype机制或apply和call方法去实现较简单，建议使用构造函数与原型混合方式。
```javascript
		function Parent(){
        	this.name = 'wang';
		}

		function Child(){
			this.age = 28;
		}
		Child.prototype = new Parent();//继承了Parent，通过原型

		var demo = new Child();
		alert(demo.age);
		alert(demo.name);//得到被继承的属性

```
- JavaScript继承的几种实现方式？
  - 参考：[构造函数的继承](http://www.ruanyifeng.com/blog/2010/05/object-oriented_javascript_inheritance.html)，[非构造函数的继承](http://www.ruanyifeng.com/blog/2010/05/object-oriented_javascript_inheritance_continued.html)；


-  javascript创建对象的几种方式？

		javascript创建对象简单的说,无非就是使用内置对象或各种自定义对象，当然还可以用JSON；但写法有很多种，也能混合使用。


		1、对象字面量的方式

			person={firstname:"Mark",lastname:"Yun",age:25,eyecolor:"black"};

		2、用function来模拟无参的构造函数

			function Person(){}
			var person=new Person();//定义一个function，如果使用new"实例化",该function可以看作是一个Class
			person.name="Mark";
			person.age="25";
			person.work=function(){
			alert(person.name+" hello...");
			}
			person.work();

		3、用function来模拟参构造函数来实现（用this关键字定义构造的上下文属性）

			function Pet(name,age,hobby){
			   this.name=name;//this作用域：当前对象
			   this.age=age;
			   this.hobby=hobby;
			   this.eat=function(){
			      alert("我叫"+this.name+",我喜欢"+this.hobby+",是个程序员");
			   }
			}
			var maidou =new Pet("麦兜",25,"coding");//实例化、创建对象
			maidou.eat();//调用eat方法


		4、用工厂方式来创建（内置对象）

			 var wcDog =new Object();
			 wcDog.name="旺财";
			 wcDog.age=3;
			 wcDog.work=function(){
			   alert("我是"+wcDog.name+",汪汪汪......");
			 }
			 wcDog.work();


		5、用原型方式来创建

			function Dog(){

			 }
			 Dog.prototype.name="旺财";
			 Dog.prototype.eat=function(){
			 alert(this.name+"是个吃货");
			 }
			 var wangcai =new Dog();
			 wangcai.eat();


		5、用混合方式来创建

			function Car(name,price){
			  this.name=name;
			  this.price=price;
			}
			 Car.prototype.sell=function(){
			   alert("我是"+this.name+"，我现在卖"+this.price+"万元");
			  }
			var camry =new Car("凯美瑞",27);
			camry.sell();

-  Javascript作用链域?

		全局函数无法查看局部函数的内部细节，但局部函数可以查看其上层的函数细节，直至全局细节。
		当需要从局部函数查找某一属性或方法时，如果当前作用域没有找到，就会上溯到上层作用域查找，
		直至全局函数，这种组织形式就是作用域链。

-  谈谈This对象的理解。
  - this总是指向函数的直接调用者（而非间接调用者）；
  - 如果有new关键字，this指向new出来的那个对象；
  - 在事件中，this指向触发这个事件的对象，特殊的是，IE中的attachEvent中的this总是指向全局对象Window；

-  eval是做什么的？

		它的功能是把对应的字符串解析成JS代码并运行；
		应该避免使用eval，不安全，非常耗性能（2次，一次解析成js语句，一次执行）。
		由JSON字符串转换为JSON对象的时候可以用eval，var obj =eval('('+ str +')');

-  什么是window对象? 什么是document对象?


-  null，undefined 的区别？

		null 		表示一个对象是“没有值”的值，也就是值为“空”；
		undefined 	表示一个变量没有被声明，不存在这个值，或者被声明了但没有被赋值；

		undefined不是一个有效的JSON，而null是；
		undefined的类型(typeof)是undefined；
		null的类型(typeof)是object；


		Javascript将未赋值的变量默认值设为undefined；
		Javascript从来不会将变量设为null。它是用来让程序员表明某个用var声明的变量时没有值的。

	    typeof undefined
			//"undefined"
			undefined :是一个表示"无"的原始值或者说表示"缺少值"，就是此处应该有一个值，但是还没有定义。当尝试读取时会返回 undefined；
			例如变量被声明了，但没有赋值时，就等于undefined

		typeof null
			//"object"
			null : 是一个对象(空对象, 没有任何属性和方法)；
			例如作为函数的参数，表示该函数的参数不是对象；

		注意：
			在验证null时，一定要使用　=== ，因为 == 无法分别 null 和　undefined
 			null == undefined // true
  			null === undefined // false

		再来一个例子：

			null
			Q：有张三这个人么？
			A：有！
			Q：张三有房子么？
			A：没有！

			undefined
			Q：有张三这个人么？
			A：没有！

	参考阅读：[undefined与null的区别](http://www.ruanyifeng.com/blog/2014/03/undefined-vs-null.html)


-  写一个通用的事件侦听器函数。

			// event(事件)工具集，来源：github.com/markyun
			markyun.Event = {
				// 页面加载完成后
				readyEvent : function(fn) {
					if (fn==null) {
						fn=document;
					}
					var oldonload = window.onload;
					if (typeof window.onload != 'function') {
						window.onload = fn;
					} else {
						window.onload = function() {
							oldonload();
							fn();
						};
					}
				},
				// 视能力分别使用dom0||dom2||IE方式 来绑定事件
				// 参数： 操作的元素,事件名称 ,事件处理程序
				addEvent : function(element, type, handler) {
					if (element.addEventListener) {
						//事件类型、需要执行的函数、是否捕捉
						element.addEventListener(type, handler, false);
					} else if (element.attachEvent) {
						element.attachEvent('on' + type, function() {
							handler.call(element);
						});
					} else {
						element['on' + type] = handler;
					}
				},
				// 移除事件
				removeEvent : function(element, type, handler) {
					if (element.removeEventListener) {
						element.removeEventListener(type, handler, false);
					} else if (element.datachEvent) {
						element.detachEvent('on' + type, handler);
					} else {
						element['on' + type] = null;
					}
				},
				// 阻止事件 (主要是事件冒泡，因为IE不支持事件捕获)
				stopPropagation : function(ev) {
					if (ev.stopPropagation) {
						ev.stopPropagation();
					} else {
						ev.cancelBubble = true;
					}
				},
				// 取消事件的默认行为
				preventDefault : function(event) {
					if (event.preventDefault) {
						event.preventDefault();
					} else {
						event.returnValue = false;
					}
				},
				// 获取事件目标
				getTarget : function(event) {
					return event.target || event.srcElement;
				},
				// 获取event对象的引用，取到事件的所有信息，确保随时能使用event；
				getEvent : function(e) {
					var ev = e || window.event;
					if (!ev) {
						var c = this.getEvent.caller;
						while (c) {
							ev = c.arguments[0];
							if (ev && Event == ev.constructor) {
								break;
							}
							c = c.caller;
						}
					}
					return ev;
				}
			};

-  ["1", "2", "3"].map(parseInt) 答案是多少？

		parseInt() 函数能解析一个字符串，并返回一个整数，需要两个参数 (val, radix)，
		其中 radix 表示要解析的数字的基数。【该值介于 2 ~ 36 之间，并且字符串中的数字不能大于radix才能正确返回数字结果值】;
		但此处 map 传了 3 个 (element, index, array),我们重写parseInt函数测试一下是否符合上面的规则。

		function parseInt(str, radix) {
		    return str+'-'+radix;
		};
		var a=["1", "2", "3"];
		a.map(parseInt);  // ["1-0", "2-1", "3-2"] 不能大于radix

		因为二进制里面，没有数字3,导致出现超范围的radix赋值和不合法的进制解析，才会返回NaN
		所以["1", "2", "3"].map(parseInt) 答案也就是：[1, NaN, NaN]

		详细解析：http://blog.csdn.net/justjavac/article/details/19473199

-  事件是？IE与火狐的事件机制有什么区别？ 如何阻止冒泡？

		 1. 我们在网页中的某个操作（有的操作对应多个事件）。例如：当我们点击一个按钮就会产生一个事件。是可以被 JavaScript 侦测到的行为。
		 2. 事件处理机制：IE是事件冒泡、Firefox同时支持两种事件模型，也就是：捕获型事件和冒泡型事件；
		 3. ev.stopPropagation();（旧ie的方法 ev.cancelBubble = true;）


-  什么是闭包（closure），为什么要用它？

		闭包是指有权访问另一个函数作用域中变量的函数，创建闭包的最常见的方式就是在一个函数内创建另一个函数，通过另一个函数访问这个函数的局部变量,利用闭包可以突破作用链域，将函数内部的变量和方法传递到外部。

		闭包的特性：

		1.函数内再嵌套函数
		2.内部函数可以引用外层的参数和变量
		3.参数和变量不会被垃圾回收机制回收

		//li节点的onclick事件都能正确的弹出当前被点击的li索引
		 <ul id="testUL">
	        <li> index = 0</li>
	        <li> index = 1</li>
	        <li> index = 2</li>
	        <li> index = 3</li>
	    </ul>
		<script type="text/javascript">
		  	var nodes = document.getElementsByTagName("li");
			for(i = 0;i<nodes.length;i+= 1){
			    nodes[i].onclick = (function(i){
			              return function() {
			                 console.log(i);
			              } //不用闭包的话，值每次都是4
			            })(i);
			}
		</script>



		执行say667()后,say667()闭包内部变量会存在,而闭包内部函数的内部变量不会存在
		使得Javascript的垃圾回收机制GC不会收回say667()所占用的资源
		因为say667()的内部函数的执行需要依赖say667()中的变量
		这是对闭包作用的非常直白的描述

		  function say667() {
			// Local variable that ends up within closure
			var num = 666;
			var sayAlert = function() {
				alert(num);
			}
			num++;
			return sayAlert;
		}

		 var sayAlert = say667();
		 sayAlert()//执行结果应该弹出的667


-  javascript 代码中的"use strict";是什么意思 ? 使用它区别是什么？

		use strict是一种ECMAscript 5 添加的（严格）运行模式,这种模式使得 Javascript 在更严格的条件下运行,

		使JS编码更加规范化的模式,消除Javascript语法的一些不合理、不严谨之处，减少一些怪异行为。
		默认支持的糟糕特性都会被禁用，比如不能用with，也不能在意外的情况下给全局变量赋值;
		全局变量的显示声明,函数必须声明在顶层，不允许在非函数代码块内声明函数,arguments.callee也不允许使用；
		消除代码运行的一些不安全之处，保证代码运行的安全,限制函数中的arguments修改，严格模式下的eval函数的行为和非严格模式的也不相同;

		提高编译器效率，增加运行速度；
		为未来新版本的Javascript标准化做铺垫。


-  如何判断一个对象是否属于某个类？

 		  使用instanceof （待完善）
	       if(a instanceof Person){
	           alert('yes');
	       }

-  new操作符具体干了什么呢?

			 1、创建一个空对象，并且 this 变量引用该对象，同时还继承了该函数的原型。
	  	  	 2、属性和方法被加入到 this 引用的对象中。
	 		 3、新创建的对象由 this 所引用，并且最后隐式的返回 this 。

		var obj  = {};
		obj.__proto__ = Base.prototype;
		Base.call(obj);


-  用原生JavaScript的实现过什么功能吗？


-  Javascript中，有一个函数，执行时对象查找时，永远不会去查找原型，这个函数是？

		hasOwnProperty

		javaScript中hasOwnProperty函数方法是返回一个布尔值，指出一个对象是否具有指定名称的属性。此方法无法检查该对象的原型链中是否具有该属性；该属性必须是对象本身的一个成员。
		使用方法：
		object.hasOwnProperty(proName)
		其中参数object是必选项。一个对象的实例。
		proName是必选项。一个属性名称的字符串值。

		如果 object 具有指定名称的属性，那么JavaScript中hasOwnProperty函数方法返回 true，反之则返回 false。

-  JSON 的了解？

		JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。
		它是基于JavaScript的一个子集。数据格式简单, 易于读写, 占用带宽小
        如：{"age":"12", "name":"back"}

        JSON字符串转换为JSON对象:
		var obj =eval('('+ str +')');
		var obj = str.parseJSON();
		var obj = JSON.parse(str);

		JSON对象转换为JSON字符串：
		var last=obj.toJSONString();
		var last=JSON.stringify(obj);

-  `[].forEach.call($$("*"),function(a){a.style.outline="1px solid #"+(~~(Math.random()*(1<<24))).toString(16)})` 能解释一下这段代码的意思吗？


-  js延迟加载的方式有哪些？

		defer和async、动态创建DOM方式（用得最多）、按需异步载入js


-  Ajax 是什么? 如何创建一个Ajax？

		ajax的全称：Asynchronous Javascript And XML。
		异步传输+js+xml。
		所谓异步，在这里简单地解释就是：向服务器发送请求的时候，我们不必等待结果，而是可以同时做其他的事情，等到有了结果它自己会根据设定进行后续操作，与此同时，页面是不会发生整页刷新的，提高了用户体验。

		(1)创建XMLHttpRequest对象,也就是创建一个异步调用对象
		(2)创建一个新的HTTP请求,并指定该HTTP请求的方法、URL及验证信息
		(3)设置响应HTTP请求状态变化的函数
		(4)发送HTTP请求
		(5)获取异步调用返回的数据
		(6)使用JavaScript和DOM实现局部刷新

-  同步和异步的区别?

	同步的概念应该是来自于OS中关于同步的概念:不同进程为协同完成某项工作而在先后次序上调整(通过阻塞,唤醒等方式).同步强调的是顺序性.谁先谁后.异步则不存在这种顺序性.



	同步：浏览器访问服务器请求，用户看得到页面刷新，重新发请求,等请求完，页面刷新，新内容出现，用户看到新内容,进行下一步操作。

	异步：浏览器访问服务器请求，用户正常操作，浏览器后端进行请求。等请求完，页面不刷新，新内容也会出现，用户看到新内容。



	（待完善）

-  如何解决跨域问题?

		jsonp、 iframe、window.name、window.postMessage、服务器上设置代理页面

-  页面编码和被请求的资源编码如果不一致如何处理？

-  模块化开发怎么做？

	 [ 立即执行函数](http://benalman.com/news/2010/11/immediately-invoked-function-expression/),不暴露私有成员

		    var module1 = (function(){
		    　　　　var _count = 0;
		    　　　　var m1 = function(){
		    　　　　　　//...
		    　　　　};
		    　　　　var m2 = function(){
		    　　　　　　//...
		    　　　　};
		    　　　　return {
		    　　　　　　m1 : m1,
		    　　　　　　m2 : m2
		    　　　　};
		    　　})();

	（待完善）

-  AMD（Modules/Asynchronous-Definition）、CMD（Common Module Definition）规范区别？

	> AMD 规范在这里：https://github.com/amdjs/amdjs-api/wiki/AMD

	> CMD 规范在这里：https://github.com/seajs/seajs/issues/242

		Asynchronous Module Definition，异步模块定义，所有的模块将被异步加载，模块加载不影响后面语句运行。所有依赖某些模块的语句均放置在回调函数中。

		 区别：

		    1. 对于依赖的模块，AMD 是提前执行，CMD 是延迟执行。不过 RequireJS 从 2.0 开始，也改成可以延迟执行（根据写法不同，处理方式不同）。CMD 推崇 as lazy as possible.
		    2. CMD 推崇依赖就近，AMD 推崇依赖前置。看代码：

		// CMD
		define(function(require, exports, module) {
		    var a = require('./a')
		    a.doSomething()
		    // 此处略去 100 行
		    var b = require('./b') // 依赖可以就近书写
		    b.doSomething()
		    // ...
		})

		// AMD 默认推荐
		define(['./a', './b'], function(a, b) { // 依赖必须一开始就写好
		    a.doSomething()
		    // 此处略去 100 行
		    b.doSomething()
		    // ...
		})


-  requireJS的核心原理是什么？（如何动态加载的？如何避免多次加载的？如何
缓存的？）

		参考：http://annn.me/how-to-realize-cmd-loader/

-  JS模块加载器的轮子怎么造，也就是如何实现一个模块加载器？

-  谈一谈你对ECMAScript6的了解？

-  ECMAScript6 怎么写class么，为什么会出现class这种东西?

-  异步加载JS的方式有哪些？

	      (1) defer，只支持IE

	      (2) async：

	      (3) 创建script，插入到DOM中，加载完毕后callBack

- documen.write和 innerHTML的区别

		document.write只能重绘整个页面

		innerHTML可以重绘页面的一部分

- DOM操作——怎样添加、移除、移动、复制、创建和查找节点?

		（1）创建新节点
		  createDocumentFragment()    //创建一个DOM片段
		  createElement()   //创建一个具体的元素
		  createTextNode()   //创建一个文本节点
		（2）添加、移除、替换、插入
		  appendChild()
		  removeChild()
		  replaceChild()
		  insertBefore() //在已有的子节点前插入一个新的子节点
		（3）查找
		  getElementsByTagName()    //通过标签名称
		  getElementsByName()    //通过元素的Name属性的值(IE容错能力较强，会得到一个数组，其中包括id等于name值的)
		  getElementById()    //通过元素Id，唯一性

-  .call() 和 .apply() 的区别？


		  例子中用 add 来替换 sub，add.call(sub,3,1) == add(3,1) ，所以运行结果为：alert(4);

		  注意：js 中的函数其实是对象，函数名是对 Function 对象的引用。

			function add(a,b)
			{
			    alert(a+b);
			}

			function sub(a,b)
			{
			    alert(a-b);
			}

			add.call(sub,3,1);



-  数组和对象有哪些原生方法，列举一下？

-  JS 怎么实现一个类。怎么实例化这个类

-  JavaScript中的作用域与变量声明提升？

-  如何编写高性能的Javascript？

-  那些操作会造成内存泄漏？

-  JQuery的源码看过吗？能不能简单概况一下它的实现原理？

-  jQuery.fn的init方法返回的this指的是什么对象？为什么要返回this？

-  jquery中如何将数组转化为json字符串，然后再转化回来？

-  jQuery 的属性拷贝(extend)的实现原理是什么，如何实现深拷贝？

-  jquery.extend 与 jquery.fn.extend的区别？

-  jQuery 的队列是如何实现的？队列可以用在哪些地方？

-  谈一下Jquery中的bind(),live(),delegate(),on()的区别？

-  JQuery一个对象可以同时绑定多个事件，这是如何实现的？

-  是否知道自定义事件。jQuery里的fire函数是什么意思，什么时候用？

-  jQuery 是通过哪个方法和 Sizzle 选择器结合的？（jQuery.fn.find()进入Sizzle）

-  针对 jQuery性能的优化方法？

-  Jquery与jQuery UI 有啥区别？


		*jQuery是一个js库，主要提供的功能是选择器，属性修改和事件绑定等等。

		*jQuery UI则是在jQuery的基础上，利用jQuery的扩展性，设计的插件。
         提供了一些常用的界面元素，诸如对话框、拖动行为、改变大小行为等等


-  JQuery的源码看过吗？能不能简单说一下它的实现原理？

-  jquery 中如何将数组转化为json字符串，然后再转化回来？

jQuery中没有提供这个功能，所以你需要先编写两个jQuery的扩展：

		$.fn.stringifyArray = function(array) {
		    return JSON.stringify(array)
		}

		$.fn.parseArray = function(array) {
		    return JSON.parse(array)
		}

		然后调用：
		$("").stringifyArray(array)

-  jQuery和Zepto的区别？各自的使用场景？

-  针对 jQuery 的优化方法？

		*基于Class的选择性的性能相对于Id选择器开销很大，因为需遍历所有DOM元素。

		*频繁操作的DOM，先缓存起来再操作。用Jquery的链式调用更好。
         比如：var str=$("a").attr("href");

		*for (var i = size; i < arr.length; i++) {}
         for 循环每一次循环都查找了数组 (arr) 的.length 属性，在开始循环的时候设置一个变量来存储这个数字，可以让循环跑得更快：
         for (var i = size, length = arr.length; i < length; i++) {}



-  Zepto的点透问题如何解决？

-  jQueryUI如何自定义组件?

-  需求：实现一个页面操作不会整页刷新的网站，并且能在浏览器前进、后退时正确响应。给出你的技术实现方案？

- 如何判断当前脚本运行在浏览器还是node环境中？（阿里）

		通过判断Global对象是否为window，如果不为window，当前脚本没有运行在浏览器中

-  移动端最小触控区域是多大？

-  jQuery 的 slideUp动画 ，如果目标元素是被外部事件驱动, 当鼠标快速地连续触发外部元素事件, 动画会滞后的反复执行，该如何处理呢?

-  把 Script 标签 放在页面的最底部的body封闭之前 和封闭之后有什么区别？浏览器会如何解析它们？

-  移动端的点击事件的有延迟，时间是多久，为什么会有？ 怎么解决这个延时？（click 有 300ms 延迟,为了实现safari的双击事件的设计，浏览器要知道你是不是要双击操作。）

-  知道各种JS框架(Angular, Backbone, Ember, React, Meteor, Knockout...)么? 能讲出他们各自的优点和缺点么?

-  Underscore 对哪些 JS 原生对象进行了扩展以及提供了哪些好用的函数方法？

-  解释JavaScript中的作用域与变量声明提升？

-  那些操作会造成内存泄漏？

	    内存泄漏指任何对象在您不再拥有或需要它之后仍然存在。
        垃圾回收器定期扫描对象，并计算引用了每个对象的其他对象的数量。如果一个对象的引用数量为 0（没有其他对象引用过该对象），或对该对象的惟一引用是循环的，那么该对象的内存即可回收。

        setTimeout 的第一个参数使用字符串而非函数的话，会引发内存泄漏。
		闭包、控制台日志、循环（在两个对象彼此引用且彼此保留时，就会产生一个循环）

-  JQuery一个对象可以同时绑定多个事件，这是如何实现的？

-  Node.js的适用场景？

-  (如果会用node)知道route, middleware, cluster, nodemon, pm2, server-side rendering么?

-  解释一下 Backbone 的 MVC 实现方式？

- 什么是“前端路由”?什么时候适合使用“前端路由”? “前端路由”有哪些优点和缺点?

- 知道什么是webkit么? 知道怎么用浏览器的各种工具来调试和debug代码么?

- 如何测试前端代码么? 知道BDD, TDD, Unit Test么? 知道怎么测试你的前端工程么(mocha, sinon, jasmin, qUnit..)?

- 前端templating(Mustache, underscore, handlebars)是干嘛的, 怎么用?

- 简述一下 Handlebars 的基本用法？

- 简述一下 Handlerbars 的对模板的基本处理流程， 如何编译的？如何缓存的？

- 用js实现千位分隔符?(来源：[前端农民工](http://div.io/topic/744)，提示：正则+replace)


		参考：http://www.tuicool.com/articles/ArQZfui
		function commafy(num) {
		    return num && num
		        .toString()
		        .replace(/(\d)(?=(\d{3})+\.)/g, function($0, $1) {
		            return $1 + ",";
		        });
		}
		console.log(commafy(1234567.90)); //1,234,567.90



- 检测浏览器版本版本有哪些方式？

		功能检测、userAgent特征检测

		比如：navigator.userAgent
		//"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36
		  (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36"


- What is a Polyfill?

		polyfill 是“在旧版浏览器上复制标准 API 的 JavaScript 补充”,可以动态地加载 JavaScript 代码或库，在不支持这些标准 API 的浏览器中模拟它们。
		例如，geolocation（地理位置）polyfill 可以在 navigator 对象上添加全局的 geolocation 对象，还能添加 getCurrentPosition 函数以及“坐标”回调对象，
		所有这些都是 W3C 地理位置 API 定义的对象和函数。因为 polyfill 模拟标准 API，所以能够以一种面向所有浏览器未来的方式针对这些 API 进行开发，
		一旦对这些 API 的支持变成绝对大多数，则可以方便地去掉 polyfill，无需做任何额外工作。

- 做的项目中，有没有用过或自己实现一些 polyfill 方案（兼容性处理方案）？

		比如： html5shiv、Geolocation、Placeholder

- 我们给一个dom同时绑定两个点击事件，一个用捕获，一个用冒泡。会执行几次事件，会先执行冒泡还是捕获？


- 使用JS实现获取文件扩展名？

		function getFileExtension(filename) {
		  return filename.slice((filename.lastIndexOf(".") - 1 >>> 0) + 2);
		}

		String.lastIndexOf() 方法返回指定值（本例中的'.'）在调用该方法的字符串中最后出现的位置，如果没找到则返回 -1。
		对于'filename'和'.hiddenfile'，lastIndexOf的返回值分别为0和-1无符号右移操作符(»>) 将-1转换为4294967295，将-2转换为4294967294，这个方法可以保证边缘情况时文件名不变。
		String.prototype.slice() 从上面计算的索引处提取文件的扩展名。如果索引比文件名的长度大，结果为""。


#### <a name='other'>ECMAScript6 相关</a>

- Object.is() 与原来的比较操作符“ ===”、“ ==”的区别？

		两等号判等，会在比较时进行类型转换；
		三等号判等(判断严格)，比较时不进行隐式类型转换,（类型不同则会返回false）；

		Object.is 在三等号判等的基础上特别处理了 NaN 、-0 和 +0 ，保证 -0 和 +0 不再相同，
		但 Object.is(NaN, NaN) 会返回 true.

 		Object.is 应被认为有其特殊的用途，而不能用它认为它比其它的相等对比更宽松或严格。




#### <a name='other'>前端框架相关</a>

- react-router 路由系统的实现原理？

- React中如何解决第三方类库的问题?


## <a name='other'>其他问题</a>

- 原来公司工作流程是怎么样的，如何与其他人协作的？如何夸部门合作的？

- 你遇到过比较难的技术问题是？你是如何解决的？

- 设计模式 知道什么是singleton, factory, strategy, decrator么?

- 常使用的库有哪些？常用的前端开发工具？开发过什么应用或组件？

- 页面重构怎么操作？

		网站重构：在不改变外部行为的前提下，简化结构、添加可读性，而在网站前端保持一致的行为。
		也就是说是在不改变UI的情况下，对网站进行优化，在扩展的同时保持一致的UI。

		对于传统的网站来说重构通常是：

		表格(table)布局改为DIV+CSS
		使网站前端兼容于现代浏览器(针对于不合规范的CSS、如对IE6有效的)
		对于移动平台的优化
		针对于SEO进行优化
		深层次的网站重构应该考虑的方面

		减少代码间的耦合
		让代码保持弹性
		严格按规范编写代码
		设计可扩展的API
		代替旧有的框架、语言(如VB)
		增强用户体验
		通常来说对于速度的优化也包含在重构中

		压缩JS、CSS、image等前端资源(通常是由服务器来解决)
		程序的性能优化(如数据读写)
		采用CDN来加速资源加载
		对于JS DOM的优化
		HTTP服务器的文件缓存

- 列举IE与其他浏览器不一样的特性？


		1、事件不同之处：

		   	触发事件的元素被认为是目标（target）。而在 IE 中，目标包含在 event 对象的 srcElement 属性；

			获取字符代码、如果按键代表一个字符（shift、ctrl、alt除外），IE 的 keyCode 会返回字符代码（Unicode），DOM 中按键的代码和字符是分离的，要获取字符代码，需要使用 charCode 属性；

			阻止某个事件的默认行为，IE 中阻止某个事件的默认行为，必须将 returnValue 属性设置为 false，Mozilla 中，需要调用 preventDefault() 方法；

			停止事件冒泡，IE 中阻止事件进一步冒泡，需要设置 cancelBubble 为 true，Mozzilla 中，需要调用 stopPropagation()；


- 99%的网站都需要被重构是那本书上写的？

		网站重构：应用web标准进行设计（第2版）

- 什么叫优雅降级和渐进增强？

		优雅降级：Web站点在所有新式浏览器中都能正常工作，如果用户使用的是老式浏览器，则代码会针对旧版本的IE进行降级处理了,使之在旧式浏览器上以某种形式降级体验却不至于完全不能用。
		如：border-shadow

		渐进增强：从被所有浏览器支持的基本功能开始，逐步地添加那些只有新版本浏览器才支持的功能,向页面增加不影响基础浏览器的额外样式和功能的。当浏览器支持时，它们会自动地呈现出来并发挥作用。
		如：默认使用flash上传，但如果浏览器支持 HTML5 的文件上传功能，则使用HTML5实现更好的体验；

- 是否了解公钥加密和私钥加密。

		一般情况下是指私钥用于对数据进行签名，公钥用于对签名进行验证;
		HTTP网站在浏览器端用公钥加密敏感数据，然后在服务器端再用私钥解密。


- WEB应用从服务器主动推送Data到客户端有那些方式？

		html5提供的Websocket
		不可见的iframe
	    WebSocket通过Flash
	    XHR长时间连接
	    XHR Multipart Streaming
	    <script>标签的长时间连接(可跨域)

- 对Node的优点和缺点提出了自己的看法？


		*（优点）因为Node是基于事件驱动和无阻塞的，所以非常适合处理并发请求，
          因此构建在Node上的代理服务器相比其他技术实现（如Ruby）的服务器表现要好得多。
		  此外，与Node代理服务器交互的客户端代码是由javascript语言编写的，
	      因此客户端和服务器端都用同一种语言编写，这是非常美妙的事情。

		*（缺点）Node是一个相对新的开源项目，所以不太稳定，它总是一直在变，
          而且缺少足够多的第三方库支持。看起来，就像是Ruby/Rails当年的样子。


- 你有用过哪些前端性能优化的方法？

		  （1） 减少http请求次数：CSS Sprites, JS、CSS源码压缩、图片大小控制合适；网页Gzip，CDN托管，data缓存 ，图片服务器。

		  （2） 前端模板 JS+数据，减少由于HTML标签导致的带宽浪费，前端用变量保存AJAX请求结果，每次操作本地变量，不用请求，减少请求次数

		  （3） 用innerHTML代替DOM操作，减少DOM操作次数，优化javascript性能。

		  （4） 当需要设置的样式很多时设置className而不是直接操作style。

		  （5） 少用全局变量、缓存DOM节点查找的结果。减少IO读取操作。

		  （6） 避免使用CSS Expression（css表达式)又称Dynamic properties(动态属性)。

		  （7） 图片预加载，将样式表放在顶部，将脚本放在底部  加上时间戳。

		  （8） 避免在页面的主体布局中使用table，table要等其中的内容完全下载之后才会显示出来，显示比div+css布局慢。
		  对普通的网站有一个统一的思路，就是尽量向前端优化、减少数据库操作、减少磁盘IO。向前端优化指的是，在不影响功能和体验的情况下，能在浏览器执行的不要在服务端执行，能在缓存服务器上直接返回的不要到应用服务器，程序能直接取得的结果不要到外部取得，本机内能取得的数据不要到远程取，内存能取到的不要到磁盘取，缓存中有的不要去数据库查询。减少数据库操作指减少更新次数、缓存结果减少查询次数、将数据库执行的操作尽可能的让你的程序完成（例如join查询），减少磁盘IO指尽量不使用文件系统作为缓存、减少读写文件次数等。程序优化永远要优化慢的部分，换语言是无法“优化”的。

- http状态码有那些？分别代表是什么意思？

			简单版
			[
				100  Continue	继续，一般在发送post请求时，已发送了http header之后服务端将返回此信息，表示确认，之后发送具体参数信息
				200  OK 		正常返回信息
				201  Created  	请求成功并且服务器创建了新的资源
				202  Accepted 	服务器已接受请求，但尚未处理
				301  Moved Permanently  请求的网页已永久移动到新位置。
				302 Found  		临时性重定向。
				303 See Other  	临时性重定向，且总是使用 GET 请求新的 URI。
				304  Not Modified 自从上次请求后，请求的网页未修改过。

				400 Bad Request  服务器无法理解请求的格式，客户端不应当尝试再次使用相同的内容发起请求。
				401 Unauthorized 请求未授权。
				403 Forbidden  	禁止访问。
				404 Not Found  	找不到如何与 URI 相匹配的资源。

				500 Internal Server Error  最常见的服务器端错误。
				503 Service Unavailable 服务器端暂时无法处理请求（可能是过载或维护）。
			]

		  完整版
		  1**(信息类)：表示接收到请求并且继续处理
			100——客户必须继续发出请求
			101——客户要求服务器根据请求转换HTTP协议版本

		  2**(响应成功)：表示动作被成功接收、理解和接受
			200——表明该请求被成功地完成，所请求的资源发送回客户端
			201——提示知道新文件的URL
			202——接受和处理、但处理未完成
			203——返回信息不确定或不完整
			204——请求收到，但返回信息为空
			205——服务器完成了请求，用户代理必须复位当前已经浏览过的文件
			206——服务器已经完成了部分用户的GET请求

		  3**(重定向类)：为了完成指定的动作，必须接受进一步处理
			300——请求的资源可在多处得到
			301——本网页被永久性转移到另一个URL
			302——请求的网页被转移到一个新的地址，但客户访问仍继续通过原始URL地址，重定向，新的URL会在response中的Location中返回，浏览器将会使用新的URL发出新的Request。
			303——建议客户访问其他URL或访问方式
			304——自从上次请求后，请求的网页未修改过，服务器返回此响应时，不会返回网页内容，代表上次的文档已经被缓存了，还可以继续使用
			305——请求的资源必须从服务器指定的地址得到
			306——前一版本HTTP中使用的代码，现行版本中不再使用
			307——申明请求的资源临时性删除

		  4**(客户端错误类)：请求包含错误语法或不能正确执行
			400——客户端请求有语法错误，不能被服务器所理解
			401——请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用
			HTTP 401.1 - 未授权：登录失败
			　　HTTP 401.2 - 未授权：服务器配置问题导致登录失败
			　　HTTP 401.3 - ACL 禁止访问资源
			　　HTTP 401.4 - 未授权：授权被筛选器拒绝
			HTTP 401.5 - 未授权：ISAPI 或 CGI 授权失败
			402——保留有效ChargeTo头响应
			403——禁止访问，服务器收到请求，但是拒绝提供服务
			HTTP 403.1 禁止访问：禁止可执行访问
			　　HTTP 403.2 - 禁止访问：禁止读访问
			　　HTTP 403.3 - 禁止访问：禁止写访问
			　　HTTP 403.4 - 禁止访问：要求 SSL
			　　HTTP 403.5 - 禁止访问：要求 SSL 128
			　　HTTP 403.6 - 禁止访问：IP 地址被拒绝
			　　HTTP 403.7 - 禁止访问：要求客户证书
			　　HTTP 403.8 - 禁止访问：禁止站点访问
			　　HTTP 403.9 - 禁止访问：连接的用户过多
			　　HTTP 403.10 - 禁止访问：配置无效
			　　HTTP 403.11 - 禁止访问：密码更改
			　　HTTP 403.12 - 禁止访问：映射器拒绝访问
			　　HTTP 403.13 - 禁止访问：客户证书已被吊销
			　　HTTP 403.15 - 禁止访问：客户访问许可过多
			　　HTTP 403.16 - 禁止访问：客户证书不可信或者无效
			HTTP 403.17 - 禁止访问：客户证书已经到期或者尚未生效
			404——一个404错误表明可连接服务器，但服务器无法取得所请求的网页，请求资源不存在。eg：输入了错误的URL
			405——用户在Request-Line字段定义的方法不允许
			406——根据用户发送的Accept拖，请求资源不可访问
			407——类似401，用户必须首先在代理服务器上得到授权
			408——客户端没有在用户指定的饿时间内完成请求
			409——对当前资源状态，请求不能完成
			410——服务器上不再有此资源且无进一步的参考地址
			411——服务器拒绝用户定义的Content-Length属性请求
			412——一个或多个请求头字段在当前请求中错误
			413——请求的资源大于服务器允许的大小
			414——请求的资源URL长于服务器允许的长度
			415——请求资源不支持请求项目格式
			416——请求中包含Range请求头字段，在当前请求资源范围内没有range指示值，请求也不包含If-Range请求头字段
			417——服务器不满足请求Expect头字段指定的期望值，如果是代理服务器，可能是下一级服务器不能满足请求长。

		  5**(服务端错误类)：服务器不能正确执行一个正确的请求
			HTTP 500 - 服务器遇到错误，无法完成请求
			　　HTTP 500.100 - 内部服务器错误 - ASP 错误
			　　HTTP 500-11 服务器关闭
			　　HTTP 500-12 应用程序重新启动
			　　HTTP 500-13 - 服务器太忙
			　　HTTP 500-14 - 应用程序无效
			　　HTTP 500-15 - 不允许请求 global.asa
			　　Error 501 - 未实现
		  HTTP 502 - 网关错误
		  HTTP 503：由于超载或停机维护，服务器目前无法使用，一段时间后可能恢复正常

- 一个页面从输入 URL 到页面加载显示完成，这个过程中都发生了什么？（流程说的越详细越好）

		  注：这题胜在区分度高，知识点覆盖广，再不懂的人，也能答出几句，
		  而高手可以根据自己擅长的领域自由发挥，从URL规范、HTTP协议、DNS、CDN、数据库查询、
		  到浏览器流式解析、CSS规则构建、layout、paint、onload/domready、JS执行、JS API绑定等等；

		  详细版：
			1、浏览器会开启一个线程来处理这个请求，对 URL 分析判断如果是 http 协议就按照 Web 方式来处理;
			2、调用浏览器内核中的对应方法，比如 WebView 中的 loadUrl 方法;
		    3、通过DNS解析获取网址的IP地址，设置 UA 等信息发出第二个GET请求;
			4、进行HTTP协议会话，客户端发送报头(请求报头);
		    5、进入到web服务器上的 Web Server，如 Apache、Tomcat、Node.JS 等服务器;
		    6、进入部署好的后端应用，如 PHP、Java、JavaScript、Python 等，找到对应的请求处理;
			7、处理结束回馈报头，此处如果浏览器访问过，缓存上有对应资源，会与服务器最后修改时间对比，一致则返回304;
		    8、浏览器开始下载html文档(响应报头，状态码200)，同时使用缓存;
		    9、文档树建立，根据标记请求所需指定MIME类型的文件（比如css、js）,同时设置了cookie;
		    10、页面开始渲染DOM，JS根据DOM API操作DOM,执行事件绑定等，页面显示完成。

		  简洁版：
			浏览器根据请求的URL交给DNS域名解析，找到真实IP，向服务器发起请求；
			服务器交给后台处理完成后返回数据，浏览器接收文件（HTML、JS、CSS、图象等）；
			浏览器对加载到的资源（HTML、JS、CSS等）进行语法解析，建立相应的内部数据结构（如HTML的DOM）；
			载入解析到的资源文件，渲染页面，完成。

- 部分地区用户反应网站很卡，请问有哪些可能性的原因，以及解决方法？

- 从打开app到刷新出内容，整个过程中都发生了什么，如果感觉慢，怎么定位问题，怎么解决?

- 除了前端以外还了解什么其它技术么？你最最厉害的技能是什么？

- 你用的得心应手用的熟练地编辑器&开发环境是什么样子？

		Sublime Text 3 + 相关插件编写前端代码
		Google chrome 、Mozilla Firefox浏览器 +firebug 兼容测试和预览页面UI、动画效果和交互功能
		Node.js+Gulp
		git 用于版本控制和Code Review

- 对前端工程师这个职位是怎么样理解的？它的前景会怎么样？

	    前端是最贴近用户的程序员，比后端、数据库、产品经理、运营、安全都近。
		1、实现界面交互
		2、提升用户体验
		3、有了Node.js，前端可以实现服务端的一些事情


		前端是最贴近用户的程序员，前端的能力就是能让产品从 90分进化到 100 分，甚至更好，

		参与项目，快速高质量完成实现效果图，精确到1px；

		与团队成员，UI设计，产品经理的沟通；

		做好的页面结构，页面重构和用户体验；

		处理hack，兼容、写出优美的代码格式；

		针对服务器的优化、拥抱最新前端技术。

- 你怎么看待Web App 、hybrid App、Native App？

- 你移动端前端开发的理解？（和 Web 前端开发的主要区别是什么？）

- 你对加班的看法？


   		加班就像借钱，原则应当是------救急不救穷



- 平时如何管理你的项目？

		先期团队必须确定好全局样式（globe.css），编码模式(utf-8) 等；

		编写习惯必须一致（例如都是采用继承式的写法，单样式都写成一行）；

		标注样式编写人，各模块都及时标注（标注关键样式调用的地方）；

		页面进行标注（例如 页面 模块 开始和结束）；

		CSS跟HTML 分文件夹并行存放，命名都得统一（例如style.css）；

		JS 分文件夹存放 命名以该JS功能为准的英文翻译。

		图片采用整合的 images.png png8 格式文件使用 尽量整合在一起使用方便将来的管理

- 如何设计突发大规模并发架构？


- 当团队人手不足，把功能代码写完已经需要加班的情况下，你会做前端代码的测试吗？

- 说说最近最流行的一些东西吧？常去哪些网站？

			ES6\WebAssembly\Node\MVVM\Web Components\React\React Native\Webpack 组件化

- 知道什么是SEO并且怎么优化么? 知道各种meta data的含义么?


- 移动端（Android IOS）怎么做好用户体验?

		清晰的视觉纵线、
		信息的分组、极致的减法、
		利用选择代替输入、
		标签及文字的排布方式、
		依靠明文确认密码、
		合理的键盘利用、

- 简单描述一下你做过的移动APP项目研发流程？

- 你在现在的团队处于什么样的角色，起到了什么明显的作用？

- 你认为怎样才是全端工程师（Full Stack developer）？

- 介绍一个你最得意的作品吧？

- 你有自己的技术博客吗，用了哪些技术？

- 对前端安全有什么看法？

- 是否了解Web注入攻击，说下原理，最常见的两种攻击（XSS 和 CSRF）了解到什么程度？

- 项目中遇到国哪些印象深刻的技术难题，具体是什么问题，怎么解决？。

- 最近在学什么东西？

- 你的优点是什么？缺点是什么？

- 如何管理前端团队?

- 最近在学什么？能谈谈你未来3，5年给自己的规划吗？


## <a name='web'>前端学习网站推荐</a>

	1. 极客标签：     http://www.gbtags.com/

	2. 码农周刊：     http://weekly.manong.io/issues/

	3. 前端周刊：     http://www.feweekly.com/issues

	4. 慕课网：       http://www.imooc.com/

	5. div.io：		 http://div.io

	6. Hacker News： https://news.ycombinator.com/news

	7. InfoQ：       http://www.infoq.com/

	8. w3cplus：     http://www.w3cplus.com/

	9. Stack Overflow： http://stackoverflow.com/

	10.w3school：    http://www.w3school.com.cn/

	11.mozilla：     https://developer.mozilla.org/zh-CN/docs/Web/JavaScript



## <a name='web'>文档推荐</a>


1. [jQuery 基本原理](http://docs.huihoo.com/jquery/jquery-fundamentals/zh-cn/index.html "jQuery 基本原理")

2. [JavaScript 秘密花园](http://bonsaiden.github.io/JavaScript-Garden/zh/)

3. [CSS参考手册](http://css.doyoe.com/)

4. [JavaScript 标准参考教程](http://javascript.ruanyifeng.com/)

5. [ECMAScript 6入门](http://es6.ruanyifeng.com/)





**备注：**

	根据自己需要选择性阅读，面试题是对理论知识的总结，让自己学会应该如何表达。

	资料答案不够正确和全面，欢迎欢迎Star和提交issues。

	格式不断修改更新中。

	在 github 项目的右上角，有三个按钮,分别是 watch、star、fork，新来的同学注意不要用错了，无休止的邮件提醒会给你造成不必要的信息干扰。

	当你选择Watching，表示你以后会关注这个项目的全部动态，以后只要这个项目发生变动，被别人提交了pull request、被发起了issue等情况你都会收到邮件通知。

	star相当于是点赞或收藏，方便以后查找。

	fork表示你想要补充完善这个项目的内容。

	更新记录：

		2016年10月20日:更新一些已被发现的问题。

		2016年3月25日：新增ECMAScript6 相关问题


###更新时间:  2016年10月20日

	爱机车、爱骑行、爱旅行、爱摄影、爱阅读的前端开发攻城师。

	我的微博：http://weibo.com/920802999
'''

blog6_content = '''
# clean-code-javascript
[clean-code-javascript](https://github.com/ryanmcdermott/clean-code-javascript)
## Table of Contents
  1. [Introduction](#introduction)
  2. [Variables](#variables)
  3. [Functions](#functions)
  4. [Objects and Data Structures](#objects-and-data-structures)
  5. [Classes](#classes)
  6. [SOLID](#solid)
  7. [Testing](#testing)
  8. [Concurrency](#concurrency)
  9. [Error Handling](#error-handling)
  10. [Formatting](#formatting)
  11. [Comments](#comments)
  12. [Translation](#translation)

## Introduction
![Humorous image of software quality estimation as a count of how many expletives
you shout when reading code](http://www.osnews.com/images/comics/wtfm.jpg)

Software engineering principles, from Robert C. Martin's book
[*Clean Code*](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882),
adapted for JavaScript. This is not a style guide. It's a guide to producing
readable, reusable, and refactorable software in JavaScript.

Not every principle herein has to be strictly followed, and even fewer will be
universally agreed upon. These are guidelines and nothing more, but they are
ones codified over many years of collective experience by the authors of
*Clean Code*.

Our craft of software engineering is just a bit over 50 years old, and we are
still learning a lot. When software architecture is as old as architecture
itself, maybe then we will have harder rules to follow. For now, let these
guidelines serve as a touchstone by which to assess the quality of the
JavaScript code that you and your team produce.

One more thing: knowing these won't immediately make you a better software
developer, and working with them for many years doesn't mean you won't make
mistakes. Every piece of code starts as a first draft, like wet clay getting
shaped into its final form. Finally, we chisel away the imperfections when
we review it with our peers. Don't beat yourself up for first drafts that need
improvement. Beat up the code instead!

## **Variables**
### Use meaningful and pronounceable variable names

**Bad:**
```javascript
const yyyymmdstr = moment().format('YYYY/MM/DD');
```

**Good:**
```javascript
const currentDate = moment().format('YYYY/MM/DD');
```
**[⬆ back to top](#table-of-contents)**

### Use the same vocabulary for the same type of variable

**Bad:**
```javascript
getUserInfo();
getClientData();
getCustomerRecord();
```

**Good:**
```javascript
getUser();
```
**[⬆ back to top](#table-of-contents)**

### Use searchable names
We will read more code than we will ever write. It's important that the code we
do write is readable and searchable. By *not* naming variables that end up
being meaningful for understanding our program, we hurt our readers.
Make your names searchable. Tools like
[buddy.js](https://github.com/danielstjules/buddy.js) and
[ESLint](https://github.com/eslint/eslint/blob/660e0918933e6e7fede26bc675a0763a6b357c94/docs/rules/no-magic-numbers.md)
can help identify unnamed constants.

**Bad:**
```javascript
// What the heck is 86400000 for?
setTimeout(blastOff, 86400000);

```

**Good:**
```javascript
// Declare them as capitalized `const` globals.
const MILLISECONDS_IN_A_DAY = 86400000;

setTimeout(blastOff, MILLISECONDS_IN_A_DAY);

```
**[⬆ back to top](#table-of-contents)**

### Use explanatory variables
**Bad:**
```javascript
const address = 'One Infinite Loop, Cupertino 95014';
const cityZipCodeRegex = /^[^,\\]+[,\\\s]+(.+?)\s*(\d{5})?$/;
saveCityZipCode(address.match(cityZipCodeRegex)[1], address.match(cityZipCodeRegex)[2]);
```

**Good:**
```javascript
const address = 'One Infinite Loop, Cupertino 95014';
const cityZipCodeRegex = /^[^,\\]+[,\\\s]+(.+?)\s*(\d{5})?$/;
const [, city, zipCode] = address.match(cityZipCodeRegex) || [];
saveCityZipCode(city, zipCode);
```
**[⬆ back to top](#table-of-contents)**

### Avoid Mental Mapping
Explicit is better than implicit.

**Bad:**
```javascript
const locations = ['Austin', 'New York', 'San Francisco'];
locations.forEach((l) => {
  doStuff();
  doSomeOtherStuff();
  // ...
  // ...
  // ...
  // Wait, what is `l` for again?
  dispatch(l);
});
```

**Good:**
```javascript
const locations = ['Austin', 'New York', 'San Francisco'];
locations.forEach((location) => {
  doStuff();
  doSomeOtherStuff();
  // ...
  // ...
  // ...
  dispatch(location);
});
```
**[⬆ back to top](#table-of-contents)**

### Don't add unneeded context
If your class/object name tells you something, don't repeat that in your
variable name.

**Bad:**
```javascript
const Car = {
  carMake: 'Honda',
  carModel: 'Accord',
  carColor: 'Blue'
};

function paintCar(car) {
  car.carColor = 'Red';
}
```

**Good:**
```javascript
const Car = {
  make: 'Honda',
  model: 'Accord',
  color: 'Blue'
};

function paintCar(car) {
  car.color = 'Red';
}
```
**[⬆ back to top](#table-of-contents)**

### Use default arguments instead of short circuiting or conditionals
Default arguments are often cleaner than short circuiting. Be aware that if you
use them, your function will only provide default values for `undefined`
arguments. Other "falsy" values such as `''`, `""`, `false`, `null`, `0`, and
`NaN`, will not be replaced by a default value.

**Bad:**
```javascript
function createMicrobrewery(name) {
  const breweryName = name || 'Hipster Brew Co.';
  // ...
}

```

**Good:**
```javascript
function createMicrobrewery(breweryName = 'Hipster Brew Co.') {
  // ...
}

```
**[⬆ back to top](#table-of-contents)**

## **Functions**
### Function arguments (2 or fewer ideally)
Limiting the amount of function parameters is incredibly important because it
makes testing your function easier. Having more than three leads to a
combinatorial explosion where you have to test tons of different cases with
each separate argument.

One or two arguments is the ideal case, and three should be avoided if possible.
Anything more than that should be consolidated. Usually, if you have
more than two arguments then your function is trying to do too much. In cases
where it's not, most of the time a higher-level object will suffice as an
argument.

Since JavaScript allows you to make objects on the fly, without a lot of class
boilerplate, you can use an object if you are finding yourself needing a
lot of arguments.

To make it obvious what properties the function expects, you can use the ES2015/ES6
destructuring syntax. This has a few advantages:

1. When someone looks at the function signature, it's immediately clear what
properties are being used.
2. Destructuring also clones the specified primitive values of the argument
object passed into the function. This can help prevent side effects. Note:
objects and arrays that are destructured from the argument object are NOT
cloned.
3. Linters can warn you about unused properties, which would be impossible
without destructuring.

**Bad:**
```javascript
function createMenu(title, body, buttonText, cancellable) {
  // ...
}
```

**Good:**
```javascript
function createMenu({ title, body, buttonText, cancellable }) {
  // ...
}

createMenu({
  title: 'Foo',
  body: 'Bar',
  buttonText: 'Baz',
  cancellable: true
});
```
**[⬆ back to top](#table-of-contents)**


### Functions should do one thing
This is by far the most important rule in software engineering. When functions
do more than one thing, they are harder to compose, test, and reason about.
When you can isolate a function to just one action, they can be refactored
easily and your code will read much cleaner. If you take nothing else away from
this guide other than this, you'll be ahead of many developers.

**Bad:**
```javascript
function emailClients(clients) {
  clients.forEach((client) => {
    const clientRecord = database.lookup(client);
    if (clientRecord.isActive()) {
      email(client);
    }
  });
}
```

**Good:**
```javascript
function emailClients(clients) {
  clients
    .filter(isClientActive)
    .forEach(email);
}

function isClientActive(client) {
  const clientRecord = database.lookup(client);
  return clientRecord.isActive();
}
```
**[⬆ back to top](#table-of-contents)**

### Function names should say what they do

**Bad:**
```javascript
function addToDate(date, month) {
  // ...
}

const date = new Date();

// It's hard to to tell from the function name what is added
addToDate(date, 1);
```

**Good:**
```javascript
function addMonthToDate(month, date) {
  // ...
}

const date = new Date();
addMonthToDate(1, date);
```
**[⬆ back to top](#table-of-contents)**

### Functions should only be one level of abstraction
When you have more than one level of abstraction your function is usually
doing too much. Splitting up functions leads to reusability and easier
testing.

**Bad:**
```javascript
function parseBetterJSAlternative(code) {
  const REGEXES = [
    // ...
  ];

  const statements = code.split(' ');
  const tokens = [];
  REGEXES.forEach((REGEX) => {
    statements.forEach((statement) => {
      // ...
    });
  });

  const ast = [];
  tokens.forEach((token) => {
    // lex...
  });

  ast.forEach((node) => {
    // parse...
  });
}
```

**Good:**
```javascript
function tokenize(code) {
  const REGEXES = [
    // ...
  ];

  const statements = code.split(' ');
  const tokens = [];
  REGEXES.forEach((REGEX) => {
    statements.forEach((statement) => {
      tokens.push( /* ... */ );
    });
  });

  return tokens;
}

function lexer(tokens) {
  const ast = [];
  tokens.forEach((token) => {
    ast.push( /* ... */ );
  });

  return ast;
}

function parseBetterJSAlternative(code) {
  const tokens = tokenize(code);
  const ast = lexer(tokens);
  ast.forEach((node) => {
    // parse...
  });
}
```
**[⬆ back to top](#table-of-contents)**

### Remove duplicate code
Do your absolute best to avoid duplicate code. Duplicate code is bad because it
means that there's more than one place to alter something if you need to change
some logic.

Imagine if you run a restaurant and you keep track of your inventory: all your
tomatoes, onions, garlic, spices, etc. If you have multiple lists that
you keep this on, then all have to be updated when you serve a dish with
tomatoes in them. If you only have one list, there's only one place to update!

Oftentimes you have duplicate code because you have two or more slightly
different things, that share a lot in common, but their differences force you
to have two or more separate functions that do much of the same things. Removing
duplicate code means creating an abstraction that can handle this set of
different things with just one function/module/class.

Getting the abstraction right is critical, that's why you should follow the
SOLID principles laid out in the *Classes* section. Bad abstractions can be
worse than duplicate code, so be careful! Having said this, if you can make
a good abstraction, do it! Don't repeat yourself, otherwise you'll find yourself
updating multiple places anytime you want to change one thing.

**Bad:**
```javascript
function showDeveloperList(developers) {
  developers.forEach((developer) => {
    const expectedSalary = developer.calculateExpectedSalary();
    const experience = developer.getExperience();
    const githubLink = developer.getGithubLink();
    const data = {
      expectedSalary,
      experience,
      githubLink
    };

    render(data);
  });
}

function showManagerList(managers) {
  managers.forEach((manager) => {
    const expectedSalary = manager.calculateExpectedSalary();
    const experience = manager.getExperience();
    const portfolio = manager.getMBAProjects();
    const data = {
      expectedSalary,
      experience,
      portfolio
    };

    render(data);
  });
}
```

**Good:**
```javascript
function showEmployeeList(employees) {
  employees.forEach((employee) => {
    const expectedSalary = employee.calculateExpectedSalary();
    const experience = employee.getExperience();

    let portfolio = employee.getGithubLink();

    if (employee.type === 'manager') {
      portfolio = employee.getMBAProjects();
    }

    const data = {
      expectedSalary,
      experience,
      portfolio
    };

    render(data);
  });
}
```
**[⬆ back to top](#table-of-contents)**

### Set default objects with Object.assign

**Bad:**
```javascript
const menuConfig = {
  title: null,
  body: 'Bar',
  buttonText: null,
  cancellable: true
};

function createMenu(config) {
  config.title = config.title || 'Foo';
  config.body = config.body || 'Bar';
  config.buttonText = config.buttonText || 'Baz';
  config.cancellable = config.cancellable === undefined ? config.cancellable : true;
}

createMenu(menuConfig);
```

**Good:**
```javascript
const menuConfig = {
  title: 'Order',
  // User did not include 'body' key
  buttonText: 'Send',
  cancellable: true
};

function createMenu(config) {
  config = Object.assign({
    title: 'Foo',
    body: 'Bar',
    buttonText: 'Baz',
    cancellable: true
  }, config);

  // config now equals: {title: "Order", body: "Bar", buttonText: "Send", cancellable: true}
  // ...
}

createMenu(menuConfig);
```
**[⬆ back to top](#table-of-contents)**


### Don't use flags as function parameters
Flags tell your user that this function does more than one thing. Functions should do one thing. Split out your functions if they are following different code paths based on a boolean.

**Bad:**
```javascript
function createFile(name, temp) {
  if (temp) {
    fs.create(`./temp/${name}`);
  } else {
    fs.create(name);
  }
}
```

**Good:**
```javascript
function createFile(name) {
  fs.create(name);
}

function createTempFile(name) {
  createFile(`./temp/${name}`);
}
```
**[⬆ back to top](#table-of-contents)**

### Avoid Side Effects (part 1)
A function produces a side effect if it does anything other than take a value in
and return another value or values. A side effect could be writing to a file,
modifying some global variable, or accidentally wiring all your money to a
stranger.

Now, you do need to have side effects in a program on occasion. Like the previous
example, you might need to write to a file. What you want to do is to
centralize where you are doing this. Don't have several functions and classes
that write to a particular file. Have one service that does it. One and only one.

The main point is to avoid common pitfalls like sharing state between objects
without any structure, using mutable data types that can be written to by anything,
and not centralizing where your side effects occur. If you can do this, you will
be happier than the vast majority of other programmers.

**Bad:**
```javascript
// Global variable referenced by following function.
// If we had another function that used this name, now it'd be an array and it could break it.
let name = 'Ryan McDermott';

function splitIntoFirstAndLastName() {
  name = name.split(' ');
}

splitIntoFirstAndLastName();

console.log(name); // ['Ryan', 'McDermott'];
```

**Good:**
```javascript
function splitIntoFirstAndLastName(name) {
  return name.split(' ');
}

const name = 'Ryan McDermott';
const newName = splitIntoFirstAndLastName(name);

console.log(name); // 'Ryan McDermott';
console.log(newName); // ['Ryan', 'McDermott'];
```
**[⬆ back to top](#table-of-contents)**

### Avoid Side Effects (part 2)
In JavaScript, primitives are passed by value and objects/arrays are passed by
reference. In the case of objects and arrays, if your function makes a change
in a shopping cart array, for example, by adding an item to purchase,
then any other function that uses that `cart` array will be affected by this
addition. That may be great, however it can be bad too. Let's imagine a bad
situation:

The user clicks the "Purchase", button which calls a `purchase` function that
spawns a network request and sends the `cart` array to the server. Because
of a bad network connection, the `purchase` function has to keep retrying the
request. Now, what if in the meantime the user accidentally clicks "Add to Cart"
button on an item they don't actually want before the network request begins?
If that happens and the network request begins, then that purchase function
will send the accidentally added item because it has a reference to a shopping
cart array that the `addItemToCart` function modified by adding an unwanted
item.

A great solution would be for the `addItemToCart` to always clone the `cart`,
edit it, and return the clone. This ensures that no other functions that are
holding onto a reference of the shopping cart will be affected by any changes.

Two caveats to mention to this approach:
  1. There might be cases where you actually want to modify the input object,
but when you adopt this programming practice you will find that those case
are pretty rare. Most things can be refactored to have no side effects!

  2. Cloning big objects can be very expensive in terms of performance. Luckily,
this isn't a big issue in practice because there are
[great libraries](https://facebook.github.io/immutable-js/) that allow
this kind of programming approach to be fast and not as memory intensive as
it would be for you to manually clone objects and arrays.

**Bad:**
```javascript
const addItemToCart = (cart, item) => {
  cart.push({ item, date: Date.now() });
};
```

**Good:**
```javascript
const addItemToCart = (cart, item) => {
  return [...cart, { item, date : Date.now() }];
};
```

**[⬆ back to top](#table-of-contents)**

### Don't write to global functions
Polluting globals is a bad practice in JavaScript because you could clash with another
library and the user of your API would be none-the-wiser until they get an
exception in production. Let's think about an example: what if you wanted to
extend JavaScript's native Array method to have a `diff` method that could
show the difference between two arrays? You could write your new function
to the `Array.prototype`, but it could clash with another library that tried
to do the same thing. What if that other library was just using `diff` to find
the difference between the first and last elements of an array? This is why it
would be much better to just use ES2015/ES6 classes and simply extend the `Array` global.

**Bad:**
```javascript
Array.prototype.diff = function diff(comparisonArray) {
  const hash = new Set(comparisonArray);
  return this.filter(elem => !hash.has(elem));
};
```

**Good:**
```javascript
class SuperArray extends Array {
  diff(comparisonArray) {
    const hash = new Set(comparisonArray);
    return this.filter(elem => !hash.has(elem));
  }
}
```
**[⬆ back to top](#table-of-contents)**

### Favor functional programming over imperative programming
JavaScript isn't a functional language in the way that Haskell is, but it has
a functional flavor to it. Functional languages are cleaner and easier to test.
Favor this style of programming when you can.

**Bad:**
```javascript
const programmerOutput = [
  {
    name: 'Uncle Bobby',
    linesOfCode: 500
  }, {
    name: 'Suzie Q',
    linesOfCode: 1500
  }, {
    name: 'Jimmy Gosling',
    linesOfCode: 150
  }, {
    name: 'Gracie Hopper',
    linesOfCode: 1000
  }
];

let totalOutput = 0;

for (let i = 0; i < programmerOutput.length; i++) {
  totalOutput += programmerOutput[i].linesOfCode;
}
```

**Good:**
```javascript
const programmerOutput = [
  {
    name: 'Uncle Bobby',
    linesOfCode: 500
  }, {
    name: 'Suzie Q',
    linesOfCode: 1500
  }, {
    name: 'Jimmy Gosling',
    linesOfCode: 150
  }, {
    name: 'Gracie Hopper',
    linesOfCode: 1000
  }
];

const INITIAL_VALUE = 0;

const totalOutput = programmerOutput
  .map((programmer) => programmer.linesOfCode)
  .reduce((acc, linesOfCode) => acc + linesOfCode, INITIAL_VALUE);
```
**[⬆ back to top](#table-of-contents)**

### Encapsulate conditionals

**Bad:**
```javascript
if (fsm.state === 'fetching' && isEmpty(listNode)) {
  // ...
}
```

**Good:**
```javascript
function shouldShowSpinner(fsm, listNode) {
  return fsm.state === 'fetching' && isEmpty(listNode);
}

if (shouldShowSpinner(fsmInstance, listNodeInstance)) {
  // ...
}
```
**[⬆ back to top](#table-of-contents)**

### Avoid negative conditionals

**Bad:**
```javascript
function isDOMNodeNotPresent(node) {
  // ...
}

if (!isDOMNodeNotPresent(node)) {
  // ...
}
```

**Good:**
```javascript
function isDOMNodePresent(node) {
  // ...
}

if (isDOMNodePresent(node)) {
  // ...
}
```
**[⬆ back to top](#table-of-contents)**

### Avoid conditionals
This seems like an impossible task. Upon first hearing this, most people say,
"how am I supposed to do anything without an `if` statement?" The answer is that
you can use polymorphism to achieve the same task in many cases. The second
question is usually, "well that's great but why would I want to do that?" The
answer is a previous clean code concept we learned: a function should only do
one thing. When you have classes and functions that have `if` statements, you
are telling your user that your function does more than one thing. Remember,
just do one thing.

**Bad:**
```javascript
class Airplane {
  // ...
  getCruisingAltitude() {
    switch (this.type) {
      case '777':
        return this.getMaxAltitude() - this.getPassengerCount();
      case 'Air Force One':
        return this.getMaxAltitude();
      case 'Cessna':
        return this.getMaxAltitude() - this.getFuelExpenditure();
    }
  }
}
```

**Good:**
```javascript
class Airplane {
  // ...
}

class Boeing777 extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude() - this.getPassengerCount();
  }
}

class AirForceOne extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude();
  }
}

class Cessna extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude() - this.getFuelExpenditure();
  }
}
```
**[⬆ back to top](#table-of-contents)**

### Avoid type-checking (part 1)
JavaScript is untyped, which means your functions can take any type of argument.
Sometimes you are bitten by this freedom and it becomes tempting to do
type-checking in your functions. There are many ways to avoid having to do this.
The first thing to consider is consistent APIs.

**Bad:**
```javascript
function travelToTexas(vehicle) {
  if (vehicle instanceof Bicycle) {
    vehicle.pedal(this.currentLocation, new Location('texas'));
  } else if (vehicle instanceof Car) {
    vehicle.drive(this.currentLocation, new Location('texas'));
  }
}
```

**Good:**
```javascript
function travelToTexas(vehicle) {
  vehicle.move(this.currentLocation, new Location('texas'));
}
```
**[⬆ back to top](#table-of-contents)**

### Avoid type-checking (part 2)
If you are working with basic primitive values like strings, integers, and arrays,
and you can't use polymorphism but you still feel the need to type-check,
you should consider using TypeScript. It is an excellent alternative to normal
JavaScript, as it provides you with static typing on top of standard JavaScript
syntax. The problem with manually type-checking normal JavaScript is that
doing it well requires so much extra verbiage that the faux "type-safety" you get
doesn't make up for the lost readability. Keep your JavaScript clean, write
good tests, and have good code reviews. Otherwise, do all of that but with
TypeScript (which, like I said, is a great alternative!).

**Bad:**
```javascript
function combine(val1, val2) {
  if (typeof val1 === 'number' && typeof val2 === 'number' ||
      typeof val1 === 'string' && typeof val2 === 'string') {
    return val1 + val2;
  }

  throw new Error('Must be of type String or Number');
}
```

**Good:**
```javascript
function combine(val1, val2) {
  return val1 + val2;
}
```
**[⬆ back to top](#table-of-contents)**

### Don't over-optimize
Modern browsers do a lot of optimization under-the-hood at runtime. A lot of
times, if you are optimizing then you are just wasting your time. [There are good
resources](https://github.com/petkaantonov/bluebird/wiki/Optimization-killers)
for seeing where optimization is lacking. Target those in the meantime, until
they are fixed if they can be.

**Bad:**
```javascript

// On old browsers, each iteration with uncached `list.length` would be costly
// because of `list.length` recomputation. In modern browsers, this is optimized.
for (let i = 0, len = list.length; i < len; i++) {
  // ...
}
```

**Good:**
```javascript
for (let i = 0; i < list.length; i++) {
  // ...
}
```
**[⬆ back to top](#table-of-contents)**

### Remove dead code
Dead code is just as bad as duplicate code. There's no reason to keep it in
your codebase. If it's not being called, get rid of it! It will still be safe
in your version history if you still need it.

**Bad:**
```javascript
function oldRequestModule(url) {
  // ...
}

function newRequestModule(url) {
  // ...
}

const req = newRequestModule;
inventoryTracker('apples', req, 'www.inventory-awesome.io');

```

**Good:**
```javascript
function newRequestModule(url) {
  // ...
}

const req = newRequestModule;
inventoryTracker('apples', req, 'www.inventory-awesome.io');
```
**[⬆ back to top](#table-of-contents)**

## **Objects and Data Structures**
### Use getters and setters
Using getters and setters to access data on objects could be better than simply
looking for a property on an object. "Why?" you might ask. Well, here's an
unorganized list of reasons why:

* When you want to do more beyond getting an object property, you don't have
to look up and change every accessor in your codebase.
* Makes adding validation simple when doing a `set`.
* Encapsulates the internal representation.
* Easy to add logging and error handling when getting and setting.
* You can lazy load your object's properties, let's say getting it from a
server.


**Bad:**
```javascript
function makeBankAccount() {
  // ...

  return {
    balance: 0,
    // ...
  };
}

const account = makeBankAccount();
account.balance = 100;
```

**Good:**
```javascript
function makeBankAccount() {
  // this one is private
  let balance = 0;

  // a "getter", made public via the returned object below
  function getBalance() {
    return balance;
  }

  // a "setter", made public via the returned object below
  function setBalance(amount) {
    // ... validate before updating the balance
    balance = amount;
  }

  return {
    // ...
    getBalance,
    setBalance,
  };
}

const account = makeBankAccount();
account.setBalance(100);
```
**[⬆ back to top](#table-of-contents)**


### Make objects have private members
This can be accomplished through closures (for ES5 and below).

**Bad:**
```javascript

const Employee = function(name) {
  this.name = name;
};

Employee.prototype.getName = function getName() {
  return this.name;
};

const employee = new Employee('John Doe');
console.log(`Employee name: ${employee.getName()}`); // Employee name: John Doe
delete employee.name;
console.log(`Employee name: ${employee.getName()}`); // Employee name: undefined
```

**Good:**
```javascript
function makeEmployee(name) {
  return {
    getName() {
      return name;
    },
  };
}

const employee = makeEmployee('John Doe');
console.log(`Employee name: ${employee.getName()}`); // Employee name: John Doe
delete employee.name;
console.log(`Employee name: ${employee.getName()}`); // Employee name: John Doe
```
**[⬆ back to top](#table-of-contents)**


## **Classes**
### Prefer ES2015/ES6 classes over ES5 plain functions
It's very difficult to get readable class inheritance, construction, and method
definitions for classical ES5 classes. If you need inheritance (and be aware
that you might not), then prefer ES2015/ES6 classes. However, prefer small functions over
classes until you find yourself needing larger and more complex objects.

**Bad:**
```javascript
const Animal = function(age) {
  if (!(this instanceof Animal)) {
    throw new Error('Instantiate Animal with `new`');
  }

  this.age = age;
};

Animal.prototype.move = function move() {};

const Mammal = function(age, furColor) {
  if (!(this instanceof Mammal)) {
    throw new Error('Instantiate Mammal with `new`');
  }

  Animal.call(this, age);
  this.furColor = furColor;
};

Mammal.prototype = Object.create(Animal.prototype);
Mammal.prototype.constructor = Mammal;
Mammal.prototype.liveBirth = function liveBirth() {};

const Human = function(age, furColor, languageSpoken) {
  if (!(this instanceof Human)) {
    throw new Error('Instantiate Human with `new`');
  }

  Mammal.call(this, age, furColor);
  this.languageSpoken = languageSpoken;
};

Human.prototype = Object.create(Mammal.prototype);
Human.prototype.constructor = Human;
Human.prototype.speak = function speak() {};
```

**Good:**
```javascript
class Animal {
  constructor(age) {
    this.age = age;
  }

  move() { /* ... */ }
}

class Mammal extends Animal {
  constructor(age, furColor) {
    super(age);
    this.furColor = furColor;
  }

  liveBirth() { /* ... */ }
}

class Human extends Mammal {
  constructor(age, furColor, languageSpoken) {
    super(age, furColor);
    this.languageSpoken = languageSpoken;
  }

  speak() { /* ... */ }
}
```
**[⬆ back to top](#table-of-contents)**


### Use method chaining
This pattern is very useful in JavaScript and you see it in many libraries such
as jQuery and Lodash. It allows your code to be expressive, and less verbose.
For that reason, I say, use method chaining and take a look at how clean your code
will be. In your class functions, simply return `this` at the end of every function,
and you can chain further class methods onto it.

**Bad:**
```javascript
class Car {
  constructor() {
    this.make = 'Honda';
    this.model = 'Accord';
    this.color = 'white';
  }

  setMake(make) {
    this.make = make;
  }

  setModel(model) {
    this.model = model;
  }

  setColor(color) {
    this.color = color;
  }

  save() {
    console.log(this.make, this.model, this.color);
  }
}

const car = new Car();
car.setColor('pink');
car.setMake('Ford');
car.setModel('F-150');
car.save();
```

**Good:**
```javascript
class Car {
  constructor() {
    this.make = 'Honda';
    this.model = 'Accord';
    this.color = 'white';
  }

  setMake(make) {
    this.make = make;
    // NOTE: Returning this for chaining
    return this;
  }

  setModel(model) {
    this.model = model;
    // NOTE: Returning this for chaining
    return this;
  }

  setColor(color) {
    this.color = color;
    // NOTE: Returning this for chaining
    return this;
  }

  save() {
    console.log(this.make, this.model, this.color);
    // NOTE: Returning this for chaining
    return this;
  }
}

const car = new Car()
  .setColor('pink')
  .setMake('Ford')
  .setModel('F-150')
  .save();
```
**[⬆ back to top](#table-of-contents)**

### Prefer composition over inheritance
As stated famously in [*Design Patterns*](https://en.wikipedia.org/wiki/Design_Patterns) by the Gang of Four,
you should prefer composition over inheritance where you can. There are lots of
good reasons to use inheritance and lots of good reasons to use composition.
The main point for this maxim is that if your mind instinctively goes for
inheritance, try to think if composition could model your problem better. In some
cases it can.

You might be wondering then, "when should I use inheritance?" It
depends on your problem at hand, but this is a decent list of when inheritance
makes more sense than composition:

1. Your inheritance represents an "is-a" relationship and not a "has-a"
relationship (Human->Animal vs. User->UserDetails).
2. You can reuse code from the base classes (Humans can move like all animals).
3. You want to make global changes to derived classes by changing a base class.
(Change the caloric expenditure of all animals when they move).

**Bad:**
```javascript
class Employee {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  // ...
}

// Bad because Employees "have" tax data. EmployeeTaxData is not a type of Employee
class EmployeeTaxData extends Employee {
  constructor(ssn, salary) {
    super();
    this.ssn = ssn;
    this.salary = salary;
  }

  // ...
}
```

**Good:**
```javascript
class EmployeeTaxData {
  constructor(ssn, salary) {
    this.ssn = ssn;
    this.salary = salary;
  }

  // ...
}

class Employee {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  setTaxData(ssn, salary) {
    this.taxData = new EmployeeTaxData(ssn, salary);
  }
  // ...
}
```
**[⬆ back to top](#table-of-contents)**

## **SOLID**
### Single Responsibility Principle (SRP)
As stated in Clean Code, "There should never be more than one reason for a class
to change". It's tempting to jam-pack a class with a lot of functionality, like
when you can only take one suitcase on your flight. The issue with this is
that your class won't be conceptually cohesive and it will give it many reasons
to change. Minimizing the amount of times you need to change a class is important.
It's important because if too much functionality is in one class and you modify
a piece of it, it can be difficult to understand how that will affect other
dependent modules in your codebase.

**Bad:**
```javascript
class UserSettings {
  constructor(user) {
    this.user = user;
  }

  changeSettings(settings) {
    if (this.verifyCredentials()) {
      // ...
    }
  }

  verifyCredentials() {
    // ...
  }
}
```

**Good:**
```javascript
class UserAuth {
  constructor(user) {
    this.user = user;
  }

  verifyCredentials() {
    // ...
  }
}


class UserSettings {
  constructor(user) {
    this.user = user;
    this.auth = new UserAuth(user);
  }

  changeSettings(settings) {
    if (this.auth.verifyCredentials()) {
      // ...
    }
  }
}
```
**[⬆ back to top](#table-of-contents)**

### Open/Closed Principle (OCP)
As stated by Bertrand Meyer, "software entities (classes, modules, functions,
etc.) should be open for extension, but closed for modification." What does that
mean though? This principle basically states that you should allow users to
add new functionalities without changing existing code.

**Bad:**
```javascript
class AjaxAdapter extends Adapter {
  constructor() {
    super();
    this.name = 'ajaxAdapter';
  }
}

class NodeAdapter extends Adapter {
  constructor() {
    super();
    this.name = 'nodeAdapter';
  }
}

class HttpRequester {
  constructor(adapter) {
    this.adapter = adapter;
  }

  fetch(url) {
    if (this.adapter.name === 'ajaxAdapter') {
      return makeAjaxCall(url).then((response) => {
        // transform response and return
      });
    } else if (this.adapter.name === 'httpNodeAdapter') {
      return makeHttpCall(url).then((response) => {
        // transform response and return
      });
    }
  }
}

function makeAjaxCall(url) {
  // request and return promise
}

function makeHttpCall(url) {
  // request and return promise
}
```

**Good:**
```javascript
class AjaxAdapter extends Adapter {
  constructor() {
    super();
    this.name = 'ajaxAdapter';
  }

  request(url) {
    // request and return promise
  }
}

class NodeAdapter extends Adapter {
  constructor() {
    super();
    this.name = 'nodeAdapter';
  }

  request(url) {
    // request and return promise
  }
}

class HttpRequester {
  constructor(adapter) {
    this.adapter = adapter;
  }

  fetch(url) {
    return this.adapter.request(url).then((response) => {
      // transform response and return
    });
  }
}
```
**[⬆ back to top](#table-of-contents)**

### Liskov Substitution Principle (LSP)
This is a scary term for a very simple concept. It's formally defined as "If S
is a subtype of T, then objects of type T may be replaced with objects of type S
(i.e., objects of type S may substitute objects of type T) without altering any
of the desirable properties of that program (correctness, task performed,
etc.)." That's an even scarier definition.

The best explanation for this is if you have a parent class and a child class,
then the base class and child class can be used interchangeably without getting
incorrect results. This might still be confusing, so let's take a look at the
classic Square-Rectangle example. Mathematically, a square is a rectangle, but
if you model it using the "is-a" relationship via inheritance, you quickly
get into trouble.

**Bad:**
```javascript
class Rectangle {
  constructor() {
    this.width = 0;
    this.height = 0;
  }

  setColor(color) {
    // ...
  }

  render(area) {
    // ...
  }

  setWidth(width) {
    this.width = width;
  }

  setHeight(height) {
    this.height = height;
  }

  getArea() {
    return this.width * this.height;
  }
}

class Square extends Rectangle {
  setWidth(width) {
    this.width = width;
    this.height = width;
  }

  setHeight(height) {
    this.width = height;
    this.height = height;
  }
}

function renderLargeRectangles(rectangles) {
  rectangles.forEach((rectangle) => {
    rectangle.setWidth(4);
    rectangle.setHeight(5);
    const area = rectangle.getArea(); // BAD: Returns 25 for Square. Should be 20.
    rectangle.render(area);
  });
}

const rectangles = [new Rectangle(), new Rectangle(), new Square()];
renderLargeRectangles(rectangles);
```

**Good:**
```javascript
class Shape {
  setColor(color) {
    // ...
  }

  render(area) {
    // ...
  }
}

class Rectangle extends Shape {
  constructor(width, height) {
    super();
    this.width = width;
    this.height = height;
  }

  getArea() {
    return this.width * this.height;
  }
}

class Square extends Shape {
  constructor(length) {
    super();
    this.length = length;
  }

  getArea() {
    return this.length * this.length;
  }
}

function renderLargeShapes(shapes) {
  shapes.forEach((shape) => {
    const area = shape.getArea();
    shape.render(area);
  });
}

const shapes = [new Rectangle(4, 5), new Rectangle(4, 5), new Square(5)];
renderLargeShapes(shapes);
```
**[⬆ back to top](#table-of-contents)**

### Interface Segregation Principle (ISP)
JavaScript doesn't have interfaces so this principle doesn't apply as strictly
as others. However, it's important and relevant even with JavaScript's lack of
type system.

ISP states that "Clients should not be forced to depend upon interfaces that
they do not use." Interfaces are implicit contracts in JavaScript because of
duck typing.

A good example to look at that demonstrates this principle in JavaScript is for
classes that require large settings objects. Not requiring clients to setup
huge amounts of options is beneficial, because most of the time they won't need
all of the settings. Making them optional helps prevent having a
"fat interface".

**Bad:**
```javascript
class DOMTraverser {
  constructor(settings) {
    this.settings = settings;
    this.setup();
  }

  setup() {
    this.rootNode = this.settings.rootNode;
    this.animationModule.setup();
  }

  traverse() {
    // ...
  }
}

const $ = new DOMTraverser({
  rootNode: document.getElementsByTagName('body'),
  animationModule() {} // Most of the time, we won't need to animate when traversing.
  // ...
});

```

**Good:**
```javascript
class DOMTraverser {
  constructor(settings) {
    this.settings = settings;
    this.options = settings.options;
    this.setup();
  }

  setup() {
    this.rootNode = this.settings.rootNode;
    this.setupOptions();
  }

  setupOptions() {
    if (this.options.animationModule) {
      // ...
    }
  }

  traverse() {
    // ...
  }
}

const $ = new DOMTraverser({
  rootNode: document.getElementsByTagName('body'),
  options: {
    animationModule() {}
  }
});
```
**[⬆ back to top](#table-of-contents)**

### Dependency Inversion Principle (DIP)
This principle states two essential things:
1. High-level modules should not depend on low-level modules. Both should
depend on abstractions.
2. Abstractions should not depend upon details. Details should depend on
abstractions.

This can be hard to understand at first, but if you've worked with AngularJS,
you've seen an implementation of this principle in the form of Dependency
Injection (DI). While they are not identical concepts, DIP keeps high-level
modules from knowing the details of its low-level modules and setting them up.
It can accomplish this through DI. A huge benefit of this is that it reduces
the coupling between modules. Coupling is a very bad development pattern because
it makes your code hard to refactor.

As stated previously, JavaScript doesn't have interfaces so the abstractions
that are depended upon are implicit contracts. That is to say, the methods
and properties that an object/class exposes to another object/class. In the
example below, the implicit contract is that any Request module for an
`InventoryTracker` will have a `requestItems` method.

**Bad:**
```javascript
class InventoryRequester {
  constructor() {
    this.REQ_METHODS = ['HTTP'];
  }

  requestItem(item) {
    // ...
  }
}

class InventoryTracker {
  constructor(items) {
    this.items = items;

    // BAD: We have created a dependency on a specific request implementation.
    // We should just have requestItems depend on a request method: `request`
    this.requester = new InventoryRequester();
  }

  requestItems() {
    this.items.forEach((item) => {
      this.requester.requestItem(item);
    });
  }
}

const inventoryTracker = new InventoryTracker(['apples', 'bananas']);
inventoryTracker.requestItems();
```

**Good:**
```javascript
class InventoryTracker {
  constructor(items, requester) {
    this.items = items;
    this.requester = requester;
  }

  requestItems() {
    this.items.forEach((item) => {
      this.requester.requestItem(item);
    });
  }
}

class InventoryRequesterV1 {
  constructor() {
    this.REQ_METHODS = ['HTTP'];
  }

  requestItem(item) {
    // ...
  }
}

class InventoryRequesterV2 {
  constructor() {
    this.REQ_METHODS = ['WS'];
  }

  requestItem(item) {
    // ...
  }
}

// By constructing our dependencies externally and injecting them, we can easily
// substitute our request module for a fancy new one that uses WebSockets.
const inventoryTracker = new InventoryTracker(['apples', 'bananas'], new InventoryRequesterV2());
inventoryTracker.requestItems();
```
**[⬆ back to top](#table-of-contents)**

## **Testing**
Testing is more important than shipping. If you have no tests or an
inadequate amount, then every time you ship code you won't be sure that you
didn't break anything. Deciding on what constitutes an adequate amount is up
to your team, but having 100% coverage (all statements and branches) is how
you achieve very high confidence and developer peace of mind. This means that
in addition to having a great testing framework, you also need to use a
[good coverage tool](http://gotwarlost.github.io/istanbul/).

There's no excuse to not write tests. There's [plenty of good JS test frameworks](http://jstherightway.org/#testing-tools), so find one that your team prefers.
When you find one that works for your team, then aim to always write tests
for every new feature/module you introduce. If your preferred method is
Test Driven Development (TDD), that is great, but the main point is to just
make sure you are reaching your coverage goals before launching any feature,
or refactoring an existing one.

### Single concept per test

**Bad:**
```javascript
import assert from 'assert';

describe('MakeMomentJSGreatAgain', () => {
  it('handles date boundaries', () => {
    let date;

    date = new MakeMomentJSGreatAgain('1/1/2015');
    date.addDays(30);
    assert.equal('1/31/2015', date);

    date = new MakeMomentJSGreatAgain('2/1/2016');
    date.addDays(28);
    assert.equal('02/29/2016', date);

    date = new MakeMomentJSGreatAgain('2/1/2015');
    date.addDays(28);
    assert.equal('03/01/2015', date);
  });
});
```

**Good:**
```javascript
import assert from 'assert';

describe('MakeMomentJSGreatAgain', () => {
  it('handles 30-day months', () => {
    const date = new MakeMomentJSGreatAgain('1/1/2015');
    date.addDays(30);
    assert.equal('1/31/2015', date);
  });

  it('handles leap year', () => {
    const date = new MakeMomentJSGreatAgain('2/1/2016');
    date.addDays(28);
    assert.equal('02/29/2016', date);
  });

  it('handles non-leap year', () => {
    const date = new MakeMomentJSGreatAgain('2/1/2015');
    date.addDays(28);
    assert.equal('03/01/2015', date);
  });
});
```
**[⬆ back to top](#table-of-contents)**

## **Concurrency**
### Use Promises, not callbacks
Callbacks aren't clean, and they cause excessive amounts of nesting. With ES2015/ES6,
Promises are a built-in global type. Use them!

**Bad:**
```javascript
import { get } from 'request';
import { writeFile } from 'fs';

get('https://en.wikipedia.org/wiki/Robert_Cecil_Martin', (requestErr, response) => {
  if (requestErr) {
    console.error(requestErr);
  } else {
    writeFile('article.html', response.body, (writeErr) => {
      if (writeErr) {
        console.error(writeErr);
      } else {
        console.log('File written');
      }
    });
  }
});

```

**Good:**
```javascript
import { get } from 'request';
import { writeFile } from 'fs';

get('https://en.wikipedia.org/wiki/Robert_Cecil_Martin')
  .then((response) => {
    return writeFile('article.html', response);
  })
  .then(() => {
    console.log('File written');
  })
  .catch((err) => {
    console.error(err);
  });

```
**[⬆ back to top](#table-of-contents)**

### Async/Await are even cleaner than Promises
Promises are a very clean alternative to callbacks, but ES2017/ES8 brings async and await
which offer an even cleaner solution. All you need is a function that is prefixed
in an `async` keyword, and then you can write your logic imperatively without
a `then` chain of functions. Use this if you can take advantage of ES2017/ES8 features
today!

**Bad:**
```javascript
import { get } from 'request-promise';
import { writeFile } from 'fs-promise';

get('https://en.wikipedia.org/wiki/Robert_Cecil_Martin')
  .then((response) => {
    return writeFile('article.html', response);
  })
  .then(() => {
    console.log('File written');
  })
  .catch((err) => {
    console.error(err);
  });

```

**Good:**
```javascript
import { get } from 'request-promise';
import { writeFile } from 'fs-promise';

async function getCleanCodeArticle() {
  try {
    const response = await get('https://en.wikipedia.org/wiki/Robert_Cecil_Martin');
    await writeFile('article.html', response);
    console.log('File written');
  } catch(err) {
    console.error(err);
  }
}
```
**[⬆ back to top](#table-of-contents)**


## **Error Handling**
Thrown errors are a good thing! They mean the runtime has successfully
identified when something in your program has gone wrong and it's letting
you know by stopping function execution on the current stack, killing the
process (in Node), and notifying you in the console with a stack trace.

### Don't ignore caught errors
Doing nothing with a caught error doesn't give you the ability to ever fix
or react to said error. Logging the error to the console (`console.log`)
isn't much better as often times it can get lost in a sea of things printed
to the console. If you wrap any bit of code in a `try/catch` it means you
think an error may occur there and therefore you should have a plan,
or create a code path, for when it occurs.

**Bad:**
```javascript
try {
  functionThatMightThrow();
} catch (error) {
  console.log(error);
}
```

**Good:**
```javascript
try {
  functionThatMightThrow();
} catch (error) {
  // One option (more noisy than console.log):
  console.error(error);
  // Another option:
  notifyUserOfError(error);
  // Another option:
  reportErrorToService(error);
  // OR do all three!
}
```

### Don't ignore rejected promises
For the same reason you shouldn't ignore caught errors
from `try/catch`.

**Bad:**
```javascript
getdata()
  .then((data) => {
    functionThatMightThrow(data);
  })
  .catch((error) => {
    console.log(error);
  });
```

**Good:**
```javascript
getdata()
  .then((data) => {
    functionThatMightThrow(data);
  })
  .catch((error) => {
    // One option (more noisy than console.log):
    console.error(error);
    // Another option:
    notifyUserOfError(error);
    // Another option:
    reportErrorToService(error);
    // OR do all three!
  });
```

**[⬆ back to top](#table-of-contents)**


## **Formatting**
Formatting is subjective. Like many rules herein, there is no hard and fast
rule that you must follow. The main point is DO NOT ARGUE over formatting.
There are [tons of tools](http://standardjs.com/rules.html) to automate this.
Use one! It's a waste of time and money for engineers to argue over formatting.

For things that don't fall under the purview of automatic formatting
(indentation, tabs vs. spaces, double vs. single quotes, etc.) look here
for some guidance.

### Use consistent capitalization
JavaScript is untyped, so capitalization tells you a lot about your variables,
functions, etc. These rules are subjective, so your team can choose whatever
they want. The point is, no matter what you all choose, just be consistent.

**Bad:**
```javascript
const DAYS_IN_WEEK = 7;
const daysInMonth = 30;

const songs = ['Back In Black', 'Stairway to Heaven', 'Hey Jude'];
const Artists = ['ACDC', 'Led Zeppelin', 'The Beatles'];

function eraseDatabase() {}
function restore_database() {}

class animal {}
class Alpaca {}
```

**Good:**
```javascript
const DAYS_IN_WEEK = 7;
const DAYS_IN_MONTH = 30;

const songs = ['Back In Black', 'Stairway to Heaven', 'Hey Jude'];
const artists = ['ACDC', 'Led Zeppelin', 'The Beatles'];

function eraseDatabase() {}
function restoreDatabase() {}

class Animal {}
class Alpaca {}
```
**[⬆ back to top](#table-of-contents)**


### Function callers and callees should be close
If a function calls another, keep those functions vertically close in the source
file. Ideally, keep the caller right above the callee. We tend to read code from
top-to-bottom, like a newspaper. Because of this, make your code read that way.

**Bad:**
```javascript
class PerformanceReview {
  constructor(employee) {
    this.employee = employee;
  }

  lookupPeers() {
    return db.lookup(this.employee, 'peers');
  }

  lookupManager() {
    return db.lookup(this.employee, 'manager');
  }

  getPeerReviews() {
    const peers = this.lookupPeers();
    // ...
  }

  perfReview() {
    this.getPeerReviews();
    this.getManagerReview();
    this.getSelfReview();
  }

  getManagerReview() {
    const manager = this.lookupManager();
  }

  getSelfReview() {
    // ...
  }
}

const review = new PerformanceReview(employee);
review.perfReview();
```

**Good:**
```javascript
class PerformanceReview {
  constructor(employee) {
    this.employee = employee;
  }

  perfReview() {
    this.getPeerReviews();
    this.getManagerReview();
    this.getSelfReview();
  }

  getPeerReviews() {
    const peers = this.lookupPeers();
    // ...
  }

  lookupPeers() {
    return db.lookup(this.employee, 'peers');
  }

  getManagerReview() {
    const manager = this.lookupManager();
  }

  lookupManager() {
    return db.lookup(this.employee, 'manager');
  }

  getSelfReview() {
    // ...
  }
}

const review = new PerformanceReview(employee);
review.perfReview();
```

**[⬆ back to top](#table-of-contents)**

## **Comments**
### Only comment things that have business logic complexity.
Comments are an apology, not a requirement. Good code *mostly* documents itself.

**Bad:**
```javascript
function hashIt(data) {
  // The hash
  let hash = 0;

  // Length of string
  const length = data.length;

  // Loop through every character in data
  for (let i = 0; i < length; i++) {
    // Get character code.
    const char = data.charCodeAt(i);
    // Make the hash
    hash = ((hash << 5) - hash) + char;
    // Convert to 32-bit integer
    hash &= hash;
  }
}
```

**Good:**
```javascript

function hashIt(data) {
  let hash = 0;
  const length = data.length;

  for (let i = 0; i < length; i++) {
    const char = data.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;

    // Convert to 32-bit integer
    hash &= hash;
  }
}

```
**[⬆ back to top](#table-of-contents)**

### Don't leave commented out code in your codebase
Version control exists for a reason. Leave old code in your history.

**Bad:**
```javascript
doStuff();
// doOtherStuff();
// doSomeMoreStuff();
// doSoMuchStuff();
```

**Good:**
```javascript
doStuff();
```
**[⬆ back to top](#table-of-contents)**

### Don't have journal comments
Remember, use version control! There's no need for dead code, commented code,
and especially journal comments. Use `git log` to get history!

**Bad:**
```javascript
/**
 * 2016-12-20: Removed monads, didn't understand them (RM)
 * 2016-10-01: Improved using special monads (JP)
 * 2016-02-03: Removed type-checking (LI)
 * 2015-03-14: Added combine with type-checking (JR)
 */
function combine(a, b) {
  return a + b;
}
```

**Good:**
```javascript
function combine(a, b) {
  return a + b;
}
```
**[⬆ back to top](#table-of-contents)**

### Avoid positional markers
They usually just add noise. Let the functions and variable names along with the
proper indentation and formatting give the visual structure to your code.

**Bad:**
```javascript
////////////////////////////////////////////////////////////////////////////////
// Scope Model Instantiation
////////////////////////////////////////////////////////////////////////////////
$scope.model = {
  menu: 'foo',
  nav: 'bar'
};

////////////////////////////////////////////////////////////////////////////////
// Action setup
////////////////////////////////////////////////////////////////////////////////
const actions = function() {
  // ...
};
```

**Good:**
```javascript
$scope.model = {
  menu: 'foo',
  nav: 'bar'
};

const actions = function() {
  // ...
};
```
**[⬆ back to top](#table-of-contents)**

## Translation

This is also available in other languages:

  - ![br](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Brazil.png) **Brazilian Portuguese**: [fesnt/clean-code-javascript](https://github.com/fesnt/clean-code-javascript)
  - ![es](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Uruguay.png) **Spanish**: [andersontr15/clean-code-javascript](https://github.com/andersontr15/clean-code-javascript-es)
  - ![cn](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/China.png) **Chinese**:
    - [alivebao/clean-code-js](https://github.com/alivebao/clean-code-js)
    - [beginor/clean-code-javascript](https://github.com/beginor/clean-code-javascript)
  - ![de](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Germany.png) **German**: [marcbruederlin/clean-code-javascript](https://github.com/marcbruederlin/clean-code-javascript)
  - ![kr](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/South-Korea.png) **Korean**: [qkraudghgh/clean-code-javascript-ko](https://github.com/qkraudghgh/clean-code-javascript-ko)
  - ![ru](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Russia.png) **Russian**:
    - [BoryaMogila/clean-code-javascript-ru/](https://github.com/BoryaMogila/clean-code-javascript-ru/)
    - [maksugr/clean-code-javascript](https://github.com/maksugr/clean-code-javascript)
  - ![vi](https://raw.githubusercontent.com/gosquared/flags/master/flags/flags/shiny/24/Vietnam.png) **Vietnamese**: [hienvd/clean-code-javascript/](https://github.com/hienvd/clean-code-javascript/)

**[⬆ back to top](#table-of-contents)**
'''