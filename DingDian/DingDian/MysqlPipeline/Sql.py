DROP TABLE IF EXISTS `dd_name`;
CREATE TABLE `dd_name` (
  'id' int(11) NOT NULL AUTO_INCREMENT,
  'xs_name' varchar(255) DEFAULT NULL,
  'xs_author' varchar(255) DEFAULT NULL,
  'category' varchar(255) DEFAULT NULL,
  'name_id' varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4;
