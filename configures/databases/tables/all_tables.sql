
--用户表
CREATE TABLE IF NOT EXISTS `customers` (
    `id` INT NOT NULL AUTO_INCREMENT ,
    `email` VARCHAR(255),
    `pwd` VARCHAR(255) ,
    `last_login_time` VARCHAR(255),
    `register_time` VARCHAR(255),
    `sex` char,
    `birth` VARCHAR,
	`register_platform` VARCHAR,
	`phone` VARCHAR,
   
)  ENGINE=INNODB ;


--分类表
CREATE TABLE IF NOT EXISTS `category` (
	`id` int(10) NOT NULL,
  	`createtime` varchar(50) NOT NULL,
	`name` varchar(100) NOT NULL,
	`creatorname` varchar(200) NOT NULL,
	`parent` varchar
) ENGINE=InnoDB ;

--新闻表
CREATE TABLE IF NOT EXISTS `articals` (
	`id` int(10) NOT NULL,
	`datetime` varchar(50) NOT NULL,
	`title` varchar(200) NOT NULL,
	`url` varchar(200),
	`category` varchar(100) NOT NULL,
	`author` varchar(100) NOT NULL,
	`image` varchar(200) NOT NULL,
	`contents` varchar(10000) NOT NULL,
  	`rank` INT ,
    `description` VARCHAR(255),
	`originlink` VARCHAR(255),
	`postTime` VARCHAR(255),
	`pubDate` VARCHAR(255),
	`source` VARCHAR(255),
	`title` VARCHAR(255),
	`keyword` VARCHAR(255),
) ENGINE=InnoDB ;

--评论表
CREATE TABLE IF NOT EXISTS `comments` (
    `id` INT NOT NULL AUTO_INCREMENT ,
    `customers_id` INT,
    `contents` VARCHAR(255) ,
    `artical_id` INT,
	`pubDate` VARCHAR(255),
	`status` char,
    FOREIGN KEY (`customers_id`) REFERENCES customers(`id`),
)  ENGINE=INNODB ;

--评论和回复者关系
CREATE TABLE IF NOT EXISTS `comments_reply` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `comment_id` INT ,
    `reply_id` INT ,
    FOREIGN KEY (`comment_id`) REFERENCES comments(`id`),
    FOREIGN KEY (`reply_id`) REFERENCES comments(`id`)
)  ENGINE=INNODB ;
#ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
#AUTO_INCREMENT=53 DEFAULT CHARSET=latin1
