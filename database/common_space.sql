-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: common_space
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(50) DEFAULT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `image_file` varchar(200) NOT NULL,
  `created_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES (1,'Simran','Kathuria','kathuriasimran','kathuriasimran7243@gmail.com','test','default-image.jpg','2021-11-25 12:32:35'),(2,'Ishita','Saxena','Ishita','ishitasaxena@gmail.com','test','dp.png','2021-11-25 14:33:59'),(3,'Hemang','Sharma','Hemang','sharmahemang@gmail.com','test','dp.png','2021-11-25 14:42:44'),(4,'Anushka','Pandey','Anushka','anushka@gmail.com','test','dp.png','2021-11-26 00:45:27');
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` text NOT NULL,
  `date_posted` datetime NOT NULL,
  `post_id` int NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `post_id` (`post_id`),
  CONSTRAINT `answer_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `query` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
INSERT INTO `answer` VALUES (8,'First of all you need to start thinking what\'s/are the Web Application Frameworks for Java that fits your needs. You have plenty of them:\r\n\r\nApache Struts\r\nAppFuse\r\nFlexive\r\nGWT\r\nGrails\r\nVaadin\r\nItsNat\r\nJavaServer Faces\r\nMakumba\r\nOpenXava\r\nEclipse RAP\r\nReasonable Server Faces\r\nRIFE\r\nRestlet\r\nSeam\r\nSpring\r\nStripes\r\nTapestry\r\nWebWork\r\nWicket\r\nZK\r\nSecond: What will be the web server where the web app will run?\r\n\r\nApache Tomcat\r\nResin Server\r\nCaudium\r\nGlassFish\r\nIBM Lotus Domino service\r\nJetty\r\nJRun\r\nlighttpd\r\nand many others\r\nAbout the database, use Hibernate, will allow you to use all SQL databases (Oracle, MySQL, etc....)\r\n\r\nThen the next step should be a simple \"hello world\" tutorial according the frameworks you are using and start from there to fallowing the Hibernate tutorials.','2021-11-25 14:27:08',4,'Hemang'),(10,'There is already a very comprehensive community wiki on What should a developer know before building a public web site? From that question you should be able to find most of the \"best practices\" to follow. As for specifics to J2EE, check out the following: Java Application Architecture Guide.\r\n\r\nFor reference: both of the above were found by searching the site for \"web site\" and \"j2ee\"','2021-11-25 14:27:08',4,'kathuriasimran'),(11,'demo-answer','2021-11-25 14:27:08',4,'kathuriasimran'),(12,'Try this markdown:\r\n\r\n![alt text](http://url/to/img.png)','2021-11-26 00:37:02',5,'kathuriasimran'),(14,'In computer networking, localhost (meaning \"this computer\") is the standard hostname given to the address of the loopback network interface.\r\n\r\nLocalhost always translates to the loopback IP address 127.0.0.1 in IPv4.\r\n\r\nIt is also used instead of the hostname of a computer. For example, directing a web browser installed on a system running an HTTP server to http://localhost will display the home page of the local web site.','2021-11-26 00:37:02',8,'Ishita'),(15,'python3 -m venv <myenvname>','2021-11-26 00:37:02',7,'Ishita'),(16,'Port: In simple language, \"Port\" is a number used by a particular software to identify its data coming from internet.\r\n\r\nEach software, like Skype, Chrome, Youtube has its own port number and that\'s how they know which internet data is for itself.\r\n\r\nSocket: \"IP address and Port \" together is called \"Socket\". It is used by another computer to send data to one particular computer\'s particular software.\r\n\r\nIP address is used to identify the computer and Port is to identify the software such as IE, Chrome, Skype etc.','2021-11-26 00:37:02',8,'Hemang'),(17,'virtualenv -p python3 venv_name \r\nThis will create new python executable in baseDirectory/bin/python3\r\n\r\n','2021-11-26 00:37:02',7,'Anushka'),(18,'>>> import os\r\n                                 >>> os.urandom(12)','2021-11-26 00:37:02',10,'kathuriasimran');
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blogposts`
--

DROP TABLE IF EXISTS `blogposts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blogposts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(500) DEFAULT NULL,
  `subtitle` varchar(500) DEFAULT NULL,
  `date_posted` datetime DEFAULT NULL,
  `content` text,
  `image_file` varchar(200) NOT NULL,
  `author` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogposts`
--

LOCK TABLES `blogposts` WRITE;
/*!40000 ALTER TABLE `blogposts` DISABLE KEYS */;
INSERT INTO `blogposts` VALUES (2,'US restricts trade with a dozen more Chinese technology firms','','2021-11-25 14:37:00','The US government has added a dozen more Chinese companies to its restricted trade list, citing national security and foreign policy concerns.\r\n\r\nWashington says that some of the firms are helping develop the Chinese military\'s quantum computing programme.\r\n\r\nThis latest move comes as tensions grow between the US and China over the status of Taiwan and other issues.\r\n\r\nTrade was among the items discussed at a virtual summit between the leaders of both countries earlier this month.\r\n\r\nBiden strike force to target \'unfair\' trade\r\nUS and China hold first trade talks of Biden era\r\nEight Chinese-based technology firms were added to the so-called \"Entity List\" for their alleged role in assisting the Chinese military\'s quantum computing efforts and acquiring or attempting \"to acquire US origin-items in support of military applications\".\r\n\r\nThis entity list has increasingly been used for national security reasons since the previous Trump administration.\r\n\r\nThe US Commerce Department also said 16 individuals and entities operating in China and Pakistan were added to the list due to their involvement in \"Pakistan\'s unsafeguarded nuclear activities or ballistic missile program.\"\r\n\r\nA total of 27 new entities were added to the list from China, Japan, Pakistan, and Singapore.\r\n\r\nSeparately, the Moscow Institute of Physics and Technology was added to the department\'s military end user list, although the listing gave no more details other than it had produced military equipment.\r\n\r\nThe new listings will help prevent American technology from supporting the development of Chinese and Russian \"military advancement and activities of non-proliferation concern like Pakistan\'s unsafeguarded nuclear activities or ballistic missile program,\" Commerce Secretary Gina Raimondo said in a statement.\r\n\r\nPotential suppliers to firms on the list will now need to apply for a licence before they can sell to them, with applications likely to be denied.\r\n\r\nChinese telecoms giant Huawei was added to the list in 2019 over claims that it posed a risk US national security.\r\n\r\nThe move cut it off from some of its key suppliers and made it difficult for the company to produce mobile phones.\r\n\r\nThe Chinese government has previously denied that it takes part in industrial espionage.','_121788351_gettyimages-1201441387.jpg','Ishita'),(3,'Indian government set to ban cryptocurrencies','India is set to go ahead with its plan to ban most cryptocurrencies in the country under a long-awaited bill.','2021-11-25 14:49:15','Expectations had grown in recent months that the government may soften its view on digital currencies.\r\n\r\nThe ban would relate to all private cryptocurrencies with certain exceptions to allow the promotion of the underlying technology and its uses.\r\n\r\nCryptocurrency prices dropped on Indian exchanges after the decision on the bill\'s future was announced.\r\n\r\nCrypto-focused bill\r\nAccording to a government bulletin, the ban is part of the proposed Cryptocurrency and Regulation of Official Digital Currency Bill that will be introduced in its winter session.\r\n\r\nThe planned legislation aims \"to create a facilitative framework for the creation of the official digital currency to be issued by the Reserve Bank of India (RBI)\".\r\n\r\nThe plan to prohibit all private cryptocurrencies appeared to be essentially the same as an earlier draft of the bill submitted in January.','_119367107_hi068000734.jpg','Hemang'),(7,'World Esports Cup (WEC) 2021 registration window expanded; tournament starts today','India Today Gaming, the gaming and esports division of India Today Group, has extended the registration window for World Esports Cup (WEC) 2021.','2021-11-26 00:44:35','India Today Gaming, the gaming, and esports division of India Today Group has extended the registration window for World Esports Cup (WEC) 2021. The registrations for the India leg of the tournament will go on till November 27, 2021. Beyond this, the registrations for the Pakistan and Nepal leg will continue as of now. As previously announced, World Esports Cup is the second tournament this year from India Today Gaming. India Today Gaming organized Esports Premier League (ESPL) 2021 in the first half of the year. WEC is one of the most anticipated Free Fire tournaments for Free Fire fans in the South Asian hemisphere. The tournament offers the top teams from India, Pakistan, and Nepal to represent their country and then compete for the top spot.\r\n\r\nWorld Esports Cup (WEC) 2021 tournament details and more\r\nWEC will follow a league format, and it has been divided into multiple rounds. The first round is known as the country invitational qualifiers where invited teams will compete for the top spots across several groups. In addition to this, WEC will also include qualifiers for the teams that have signed up for the tournament in the background. The top teams from both these segments will compete to reach the country finals. Once in the country finals, these teams will need to compete for the final four slots to compete in the WEC grand-finals.\r\n\r\nIn addition to the opportunity to represent ones country on the international stage, WEC will also feature a prize pool worth Rs. 75 lakhs. India Today Gaming has also signed up Bollywood star, Tiger Shroff as the ambassador for the first edition of WEC. Infinix Mobile makes a return as the title sponsor for WEC 2021 after ESPL 2021. It is worth nothing that it is the first international tournament from India Today Gaming. The tournament will span over a period of three months and players can head to the Instagram handle, Facebook, or Discord server of India Today Gaming to find all the latest updates. The tournament live stream will be available on official YouTube, and Facebook accounts of the organizer.\r\n\r\nLooking back, ESPL 2021 was the first franchise-based tournament for Free Fire in the world. As part of the tournament, the top Free Fire teams from across the country competed against each other to represent one of the eight franchise teams.','2018-06-26-esports-thumbnail-03.jpg','kathuriasimran'),(8,'Tech companies don’t get science fiction – and that\'s deeply troubling','','2021-11-26 00:49:19','SURREAL news from Silicon Valley: Facebook has rebranded itself as Meta. This is because the company’s boss, Mark Zuckerberg, wants to launch a product called the metaverse, a shared virtual reality world. Let’s leave aside the fact that the metaverse is, for the moment, still a fictional idea. This is also an insanely bad episode in branding that would be hilarious if it weren’t so depressing.\r\n\r\nImagine you are Zuckerberg meeting your crack team of brand experts. A few years ago, you bought a company called Oculus that makes virtual reality headsets and now you have figured out …','PRI_211043676.jpg','Anushka');
/*!40000 ALTER TABLE `blogposts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `query`
--

DROP TABLE IF EXISTS `query`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `query` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` text,
  `body` text,
  `date_posted` datetime DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `query`
--

LOCK TABLES `query` WRITE;
/*!40000 ALTER TABLE `query` DISABLE KEYS */;
INSERT INTO `query` VALUES (4,'Steps to develop a website','What are the aspects to be considered when I want to develop a website using J2EE application server and a database for back end, I am looking for an answer that can guide me through the steps required to get the site set up-','2021-11-25 14:41:32','Ishita'),(5,'How to add images to README.md on GitHub?','Recently I joined GitHub. I hosted some projects there.\r\n\r\nI need to include some images in my README File. I don\'t know how to do that.\r\n\r\nI searched about this, but all I got was some links which tell me to \"host images on web and specify the image path in README.md file\".\r\n\r\nIs there any way to do this without hosting the images on any third-party web hosting services?','2021-11-26 00:50:37','Anushka'),(7,'How to create virtual env with python3','I am using python 2.7 + virtualenv version 1.10.1 for running myproject projects. Due to some other projects requirement I have to work with other version of python(Python 3.5) and Django 1.9. For this I have installed python in my user directory. Also I have dowloaded and installed virtualenv( version - 15.1.0) into my user directory. But whenever I am trying to create virtual env I am getting the below error','2021-11-26 00:54:02','kathuriasimran'),(8,'What\'s the whole point of \"localhost\", hosts and ports at all?','I\'m totally new to this web development stuff. So I see things like \"localhost\" all the time and ask myself: What\'s that?\r\n\r\nI feel to know what a \"host\" actually is. Something that executes something. So my mac is the host for everything that runs on it. So \"localhost\" is actually just my mac? Can I have also other hosts? like \"otherhost\" or \"betterhost\"?\r\n\r\nSo when I write in my browser: http://localhost:80/mysite/index.php, this \"localhost\" thing tells the browser to look on my machine for that stuff rather than online?\r\n\r\nMaybe someone can clear this up a little bit :-)','2021-11-26 00:55:44','kathuriasimran'),(10,'Where do I get a SECRET_KEY for Flask?','I am trying to set up Flask-Debugtoolbar, but I get the message \"DebugToolBar requires a SECRET_KEY\". Where do I get the secret key?','2021-11-26 01:05:32','Anushka');
/*!40000 ALTER TABLE `query` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-27 13:24:26
