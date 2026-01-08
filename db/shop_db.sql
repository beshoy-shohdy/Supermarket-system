-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: shop
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(10) DEFAULT NULL,
  `cash_back` float unsigned DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `user_name` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (11,'Ahmed',25.5,'01012345678'),(12,'Sara',10,'01123456789'),(13,'Omar',2,'01234567890'),(14,'Mona',0,'01598765432'),(15,'Youssef',18.25,'01087654321'),(17,'Tony',0,'01234567891'),(18,'Beshoy',0,'01234567899'),(19,'shosho',0,'0112345678'),(20,'Pop',0,'01234567897');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(10) NOT NULL,
  `hire_date` date NOT NULL,
  `salary` int NOT NULL,
  `phone` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`employee_id`),
  UNIQUE KEY `user_name` (`user_name`),
  UNIQUE KEY `phone_UNIQUE` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'John','2021-03-15',5000,'01234567890'),(2,'Sarah','2020-07-01',6200,'01234567882'),(3,'Michael','2022-01-10',4800,'01234567883'),(4,'Emily','2019-11-25',7100,'01234567803'),(5,'David','2023-05-05',4500,'01234557803');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `goods` (
  `good_id` int NOT NULL AUTO_INCREMENT,
  `good_name` varchar(50) NOT NULL,
  `count` int NOT NULL,
  `price` float NOT NULL,
  `net_profit` float NOT NULL,
  `discount` float unsigned DEFAULT NULL,
  PRIMARY KEY (`good_id`),
  UNIQUE KEY `good_name_UNIQUE` (`good_name`),
  CONSTRAINT `np_c` CHECK ((`net_profit` >= `discount`)),
  CONSTRAINT `p_c` CHECK ((`price` > (`net_profit` + `discount`)))
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods`
--

LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
INSERT INTO `goods` VALUES (1,'Milk',13,40,5,1),(2,'Bread',8,20,3,1),(3,'Eggs',4,90,6,5),(4,'Rice',3,120,7,4),(5,'Sugar',8,30,2,1),(6,'Cooking Oil',6,75,6,3),(7,'Pasta',9,25,3,1),(8,'Tomato Sauce',12,18,2,1),(9,'Chicken',2,160,8,6),(10,'Cheese',4,85,5,3),(11,'Yogurt',15,12,2,1),(12,'Butter',3,60,5,2),(13,'Apples',8,30,2,1),(14,'Bananas',10,28,2,1),(15,'Oranges',10,22,2,0),(16,'Potatoes',18,12,1,0),(17,'Onions',15,10,1,0),(18,'Tomatoes',10,14,2,1),(19,'Cereal',6,55,5,3),(20,'Chocolate',8,12,2,1),(21,'Tea',5,45,4,2),(22,'Coffee',3,75,5,3),(23,'Salt',20,5,1,0),(24,'Pepper',5,20,3,1),(25,'Tuna',6,35,4,2),(26,'Sardines',5,28,3,1),(27,'Biscuits',10,10,2,1),(28,'Noodles',15,8,1,0),(29,'Soft Drink',12,18,2,1),(30,'Water',20,6,1,0),(31,'Orange Juice',8,25,2,1),(32,'Apple Juice',7,27,2,1),(33,'Energy Drink',5,30,2,1),(34,'Ice Cream',3,65,5,3),(35,'Frozen Pizza',2,90,6,5),(36,'Chicken Nuggets',4,85,5,3),(37,'French Fries',6,40,4,2),(38,'Veg Mix',5,35,2,1),(39,'Detergent',3,120,7,5),(40,'Dish Soap',6,45,4,2),(41,'Hand Soap',10,15,2,1),(42,'Shampoo',3,85,5,3),(43,'Toothpaste',5,30,3,1),(44,'Toilet Paper',4,70,5,3),(45,'Paper Towels',6,40,4,2),(46,'Trash Bags',8,25,2,1),(47,'Air Freshener',3,55,4,2),(48,'Cleaning Spray',4,60,5,2),(49,'Diapers',3,180,8,2),(50,'Wipes',6,35,2,1),(51,'Baby Formula',2,320,10,5),(52,'Pet Food',4,140,6,5),(53,'Cat Litter',3,90,5,3),(54,'Dog Treats',5,50,2,1),(55,'Honey',3,95,5,4),(56,'Jam',5,30,2,1),(57,'Peanut Butter',3,65,5,3),(58,'Olive Oil',2,180,8,2),(59,'Vinegar',6,18,2,1),(60,'Ketchup',5,22,2,1),(61,'Mayonnaise',4,28,2,1),(62,'Mustard',5,24,2,1),(63,'Flour',7,18,2,1),(64,'Baking Powder',6,12,1,1),(65,'Vanilla',5,15,2,1),(66,'Yeast',8,8,1,0),(67,'Corn Oil',3,75,5,2),(68,'Frozen Peas',4,30,2,1),(69,'Frozen Spinach',4,28,2,1),(70,'Frozen Okra',3,32,2,1),(71,'Frozen Strawberries',2,45,2,1),(72,'Frozen Mango',2,50,2,1),(73,'Canned Beans',6,20,2,1),(74,'Canned Corn',5,18,2,1),(75,'Canned Peas',5,19,2,1),(76,'Canned Mushrooms',3,30,2,1),(77,'Canned Soup',3,35,2,1),(78,'Instant Coffee',2,110,4,0),(79,'Green Tea',4,40,2,1),(80,'Herbal Tea',3,38,2,1),(81,'Sugar Free Biscuits',5,25,2,1),(82,'Protein Bar',3,45,2,1),(83,'Oats',3,55,3,2),(84,'Granola',2,70,3,2),(85,'Almond Milk',3,45,2,1),(86,'Soy Milk',3,40,2,1),(87,'Coconut Milk',2,48,3,2),(88,'Spaghetti',6,20,2,1),(89,'Lasagna Sheets',3,35,2,1),(90,'Macaroni',5,18,2,1),(91,'Instant Soup',7,12,1,0),(92,'Chips Potato',10,10,1,0),(93,'Popcorn',6,15,2,1),(94,'Ice Tea',5,18,2,1),(95,'Sports Drink',4,25,2,1),(96,'Sparkling Water',7,12,1,0),(97,'Chocolate Spread',2,85,4,3),(98,'Milk Chocolate',3,30,2,1),(99,'Cookies',5,25,2,1),(100,'Cereal Bar',6,20,2,1),(101,'cola',20,18,5,0),(102,'Pepsi',5,18,3,0);
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trans`
--

DROP TABLE IF EXISTS `trans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trans` (
  `trans_id` int NOT NULL AUTO_INCREMENT,
  `c_id` int NOT NULL,
  `t_price` float NOT NULL,
  `t_net_profit` float NOT NULL,
  `discount` float DEFAULT NULL,
  PRIMARY KEY (`trans_id`),
  KEY `t_c_id_fk` (`c_id`),
  CONSTRAINT `t_c_id_fk` FOREIGN KEY (`c_id`) REFERENCES `customer` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trans`
--

LOCK TABLES `trans` WRITE;
/*!40000 ALTER TABLE `trans` DISABLE KEYS */;
INSERT INTO `trans` VALUES (2,14,52,4,2),(3,13,40,4,2),(4,14,34,3,0);
/*!40000 ALTER TABLE `trans` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-03 22:59:46
