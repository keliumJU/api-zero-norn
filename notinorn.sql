-- MariaDB dump 10.18  Distrib 10.4.17-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: notinorn
-- ------------------------------------------------------
-- Server version	10.4.17-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8_general_ci */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `heroku_d16712f7edb2a95`
--

DROP TABLE IF EXISTS `heroku_d16712f7edb2a95`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `heroku_d16712f7edb2a95` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heroku_d16712f7edb2a95`
--

LOCK TABLES `heroku_d16712f7edb2a95` WRITE;
/*!40000 ALTER TABLE `heroku_d16712f7edb2a95` DISABLE KEYS */;
INSERT INTO `heroku_d16712f7edb2a95` VALUES ('916e41b3eae3');
/*!40000 ALTER TABLE `heroku_d16712f7edb2a95` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` text DEFAULT NULL,
  `email` varchar(100) DEFAULT 'example@gmail.com',
  `name` varchar(100) DEFAULT NULL,
  `img` text DEFAULT NULL,
  `roles` text DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 0,
  `token_fcm` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (7,'eliana','$pbkdf2-sha512$25000$CyHk/H9vrfWek5Ly/j/nPA$UsNwMX/JHIOY8KYQVBgfN70aRF8HkaM24fXiZ5pzyxd9MxwBemriTgGgsB4gQTT4IIvqa2niQ8I5iU6m10l8zA','elianita@gmail.com','Eliana Mazzurco','http://127.0.0.1:5000/static/uploads/alexandra-kosteniuk-child.jpg','admin',1,NULL),(8,'pedro','$pbkdf2-sha512$25000$jjFGqJWSkjKm1NpbC6H03g$XiiiKg/LzB9v60srbNcgone5bCxKkbYvwmJDnWkRkGOKkt4FBhXMV8C/SWXcZutNVTdrG/hlkySwk9gpHRuRDw','pedro@gmail.com','Pedro Elias Guerra','http://127.0.0.1:5000/static/uploads/bukowski.jpg','graduate',1,NULL),(9,'carlos','$pbkdf2-sha512$25000$IUSo9d77vxdiDMFYi1GKsQ$e7wZO4fn2ozlcWQXgmEIL2VMY8UEJ.MWNnvewFaMduhfMbsUQLcOjw5U4DXKBQG8JbLTQP1KyARUu.rq1VD1iQ','carlos@gmail.com','carlitos jurado','http://127.0.0.1:5000/static/uploads/gge.jpg','company',0,NULL),(10,'lucas','$pbkdf2-sha512$25000$vrcWYsxZa20tpRTiHCMEoA$Hd8Hzz8MEvq5IbbR8VLu.M81AaX7dbvHYMytjmbttPHKfnQ0IvT3eohPSvgTtd1588PEDBDjgyfcLYuMLFzCLw','lucas@gmail.com',NULL,NULL,'company',0,NULL),(11,'ramon','$pbkdf2-sha512$25000$KiVk7F2rdU4JIYRwDiGE0A$HnfR4paZ0dl8TvQ68iZLdczVVTXbIkzWl5hSxLwyYpsFAHuauMo7luVHnGiq4ocO4BvTDkmMavarljZnfU2xPw','ramon@gmail.com',NULL,NULL,'graduate',0,NULL),(12,'claudio','$pbkdf2-sha512$25000$BiBESGkNgXCOkVLq3bt3jg$8.eK6uRM9sOUwd9uq1JEkLAnwh.EccurofIoDgkyEDyLawLqPSvwDq.mxq7v/lmZhWv/Rq1Ifp3QthY8NDoTLQ','claudio@gmail.com',NULL,NULL,'graduate',0,NULL),(13,'rodolfo','$pbkdf2-sha512$25000$55yztpYyZszZWwuh9P4/Jw$mQkti1bFNIVbDv/mXtpJeutmOep.lbmLOJn4MbNNfgkXpgt01Syqp5GaFw/fIa1SbXxVdnettnFN1GqEeU0LZQ','pedro123@gmail.com',NULL,NULL,'graduate',1,NULL),(14,'charli','$pbkdf2-sha512$25000$gLA25vy/N8aYE.IcYwyh1A$qr609Fnm5pK7st1H92FSrSCMrnBDw/D5/HCMojaUNy6TZzSrQ439rEBX/LrYAhXhAQWF5CER.QVtEwY/FeMWVg','pedroLOpez@gmail.com',NULL,NULL,'graduate',1,NULL),(15,'vallejo','$pbkdf2-sha512$25000$Rsi5V4rReo8x5nzvvVdKyQ$GTyg22iNxjz0MqD1iPjHFguiVYkSYDfpC4W9YcCAQXwCzduVo8WCGvFANdS/sEy430OVw0due5kYrnSotBrAtw','pedroVallejo@gmail.com',NULL,NULL,'graduate',1,NULL),(17,'juan','$pbkdf2-sha512$25000$lxKi9N7b.5/zvrfWOgfgnA$bYL90Swtfoc0lVGZpFKV48KVs2EdU1ArZgmqy1.uPdOXMZc7kxk.t2hdAFqpUhU9npb4f7kTjdweKg4/2o8UFw','juanito@gmail.com',NULL,NULL,'graduate',1,NULL),(18,'teent','$pbkdf2-sha512$25000$kzLGGKOUEgJAKIUwxvhfSw$mEkpJRic.GoHXU3yickeRFS0H0vzQX0zTVrgUfFl/kb5NZYHWHDLABHure4.v5NIAmPOYXj8LkwzzbcHkQHEIA','teent@gmail.com','Alex Makliv ','http://127.0.0.1:5000/static/uploads/chs.png','admin',0,NULL),(19,'two','$pbkdf2-sha512$25000$NgaA0DoHQOhd6/2fMyZECA$.KT0nfEtK4Mn/lyMQXTVyRjTKdaQ87Xmpg.azHwYxn4Lj29ltwSD/tIOtrDaq045QkPjmgTrxTt1E0QlVql.vg','two@gmail.com',NULL,NULL,'graduate',1,NULL),(20,'nuevo','$pbkdf2-sha512$25000$vpeSktJ6750TQkgpJeScMw$mexsj9DBE1.FvLfTFGAhdv7LpBcr7em3oTLmxR5Mnl/OGaSFTikLxou7TMtwKab.uTxmtuvDGOPbNhBblseXdg','nuevo@gmail.com','juan calabaza','http://127.0.0.1:5000/static/uploads/ardilla_patineta.jpg','graduate',1,NULL),(21,'nuevo2','$pbkdf2-sha512$25000$956TMkYIISQkZCwlxJjzng$ROZaQiWguHXWMd4OabaAZh13GNRN5YbNgzDQTbWEMu2PsfE25wWyE1AHab5FBUg1FHV6kCVqFzyPg4GWpw42BQ','nuevo2@gmail.com',NULL,NULL,'graduate',1,NULL),(22,'nuevo3','$pbkdf2-sha512$25000$Ooewdi4FYCyFMKY0BsD4fw$BlZeBUWQV5op9/m9S0eTjbT9FWhZ48iU5WqmNRvlppLADCtOQShQAdBYQLK3yQ6GvMa.qIrioPzb6f6q.vbl0A','nuevo3@gmail.com',NULL,NULL,'graduate',0,NULL),(23,'nuevo4','$pbkdf2-sha512$25000$.n/P.Z.Tcu6d03ovZSwFYA$YO3j5FRTn1Xqvnl5grkdnwHNUi68I/VZTnm974/fyHGuuz/wj4sdwV3pagRMMNWVQO3pAkqOSFXKPERYRn7mkw','nuevo4@gmail.com',NULL,NULL,'graduate',0,NULL),(24,'nuevo5','$pbkdf2-sha512$25000$Xouxdo4RQiglxLjXuvdeiw$.XEzblDZ100f1fxg7Pl0BN6eeWCOTHlfqwiRL72KfVq9C538RfAmkrGBtAvrmbJcMfOSmLtcTeyH8cVw.b1eUA','nuevo5@gmail.com',NULL,NULL,'graduate',1,NULL),(27,'lucius','$pbkdf2-sha512$25000$LOW8l/K.V6p1rjUmRIhxzg$6ROVEXIa2acZHCtAd0uoxkjqPtRqamJOSM.JjiRXis0bF10r5fzQnY7AJi1PV4lqxkMd.B/Zy0Ws2lvr4puo9g','lucius@gmail.com','lucious glacius','http://127.0.0.1:5000/static/uploads/Cara_Delevingne_by_Gage_Skidmore.jpg','lucious glacius',0,NULL),(30,'jacinto','$pbkdf2-sha512$25000$q/W.1xpDiDGG0HpvDcEYIw$/rA9nVUU1oKrCTOOnBX6AegYEamswT2aIEeaSTIoVHIRWl6fptS5yuHnAV.853U30TbFmjmyysiZFNpB6psyfg','jacinto@gmail.com',NULL,NULL,'graduate',0,NULL),(31,'cartus','$pbkdf2-sha512$25000$ag3hvNd6b.2d07qXkrIWwg$QvMW59K.CiQlnErUe822ytqtCJQhK6KXRu.4qRVLjrCZWdhNDxQSihzPyl4VDngV9mREmT7mTAystinzsf5Cww','cartus@gmail.com',NULL,NULL,'graduate',1,'null'),(32,'testnoti','$pbkdf2-sha512$25000$SElJyZlTSokxxjiH0JozJg$83Mz.IYk9NZ4aSnM5fabYZRMFodcvsB7j9dID1VtBoTShqa/UAc3SWRO1KUtJ7kJipwCPvMbFTPGTsHKHGmxTw','testnoti@gmail.com',NULL,NULL,'graduate',0,'dExM_MuhSBMscgzvCI7NWW:APA91bFbjicTY5NFWILQbsaJ475EYspidioEan9WKveM3xPLLbWZWmruYWSnFAGnM1ncQ9IK7BaMB_lr7iiAqlPXGx0i7SLnzDGc99UV9vde3MtKUyQwkV9Wg5gOv9WMBL8pCp75DX0O'),(33,'otronn','$pbkdf2-sha512$25000$cE4pRQhhbG1t7d0b4xyjNA$0GyocQapchAwkjzB87Ny/0SyBHOQaS45CRGhxMgUssq/D9AgZnQzxo9cWrDiOsbLWlUxByoGemxmYMzJ13HjCg','otronn@gmail.com',NULL,NULL,'graduate',0,'dExM_MuhSBMscgzvCI7NWW:APA91bFbjicTY5NFWILQbsaJ475EYspidioEan9WKveM3xPLLbWZWmruYWSnFAGnM1ncQ9IK7BaMB_lr7iiAqlPXGx0i7SLnzDGc99UV9vde3MtKUyQwkV9Wg5gOv9WMBL8pCp75DX0O'),(34,'tres','$pbkdf2-sha512$25000$OCfEGAMghHBurZVy7n1vjQ$sK.slIJCtieF4afQ9ZCu239rJTMrXqMv6UL3VuHQ.SkduYaCP6GfDWQNCLwSDjK3nrzP1fHP9RyZT59x0UxfdA','tres@gmail.com',NULL,NULL,'graduate',0,'dExM_MuhSBMscgzvCI7NWW:APA91bFbjicTY5NFWILQbsaJ475EYspidioEan9WKveM3xPLLbWZWmruYWSnFAGnM1ncQ9IK7BaMB_lr7iiAqlPXGx0i7SLnzDGc99UV9vde3MtKUyQwkV9Wg5gOv9WMBL8pCp75DX0O');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-13  0:40:47
