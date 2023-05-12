-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: localhost    Database: sbi_database
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account_balance`
--

DROP TABLE IF EXISTS `account_balance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `account_balance` (
  `transaction_id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `u_name` varchar(50) NOT NULL,
  `time_trans` datetime NOT NULL,
  `deposit` float NOT NULL,
  `withdraw` float NOT NULL,
  `balance` float NOT NULL,
  PRIMARY KEY (`transaction_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_balance`
--

LOCK TABLES `account_balance` WRITE;
/*!40000 ALTER TABLE `account_balance` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_balance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_deposits`
--

DROP TABLE IF EXISTS `account_deposits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `account_deposits` (
  `deposit_id` int(7) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `u_name` varchar(50) NOT NULL,
  `time_dep` datetime NOT NULL,
  `deposit_type` varchar(50) NOT NULL,
  `deposit_amount` float NOT NULL,
  `deposit_interest` float NOT NULL,
  `deposit_duration` float NOT NULL,
  `final_amount` float NOT NULL,
  PRIMARY KEY (`deposit_id`),
  KEY `u_name` (`u_name`),
  KEY `deposit_type` (`deposit_type`),
  CONSTRAINT `account_deposits_ibfk_1` FOREIGN KEY (`u_name`) REFERENCES `profile_details` (`u_name`),
  CONSTRAINT `account_deposits_ibfk_2` FOREIGN KEY (`deposit_type`) REFERENCES `deposit_types` (`deposit_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_deposits`
--

LOCK TABLES `account_deposits` WRITE;
/*!40000 ALTER TABLE `account_deposits` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_deposits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `branch_details`
--

DROP TABLE IF EXISTS `branch_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `branch_details` (
  `account_number` int(7) unsigned zerofill NOT NULL,
  `ifsc_code` char(11) DEFAULT NULL,
  `branch_name` varchar(50) NOT NULL,
  UNIQUE KEY `branch_name` (`branch_name`),
  KEY `account_number` (`account_number`),
  CONSTRAINT `branch_details_ibfk_1` FOREIGN KEY (`account_number`) REFERENCES `profile_details` (`account_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch_details`
--

LOCK TABLES `branch_details` WRITE;
/*!40000 ALTER TABLE `branch_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `branch_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deposit_types`
--

DROP TABLE IF EXISTS `deposit_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `deposit_types` (
  `deposit_type` varchar(50) NOT NULL,
  `deposit_interest` float NOT NULL,
  PRIMARY KEY (`deposit_type`),
  UNIQUE KEY `deposit_interest` (`deposit_interest`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deposit_types`
--

LOCK TABLES `deposit_types` WRITE;
/*!40000 ALTER TABLE `deposit_types` DISABLE KEYS */;
/*!40000 ALTER TABLE `deposit_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan_types`
--

DROP TABLE IF EXISTS `loan_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `loan_types` (
  `loan_type` varchar(50) NOT NULL,
  `loan_interest` float NOT NULL,
  PRIMARY KEY (`loan_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan_types`
--

LOCK TABLES `loan_types` WRITE;
/*!40000 ALTER TABLE `loan_types` DISABLE KEYS */;
/*!40000 ALTER TABLE `loan_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loans_hist`
--

DROP TABLE IF EXISTS `loans_hist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `loans_hist` (
  `loan_number` int(7) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `u_name` varchar(50) NOT NULL,
  `time_loan` datetime NOT NULL,
  `loan_type` varchar(50) NOT NULL,
  `loan_amount` float NOT NULL,
  `loan_interest` float NOT NULL,
  `loan_period` float NOT NULL,
  `emi` float NOT NULL,
  `final_amount` float NOT NULL,
  PRIMARY KEY (`loan_number`),
  KEY `u_name` (`u_name`),
  KEY `loan_type` (`loan_type`),
  CONSTRAINT `loans_hist_ibfk_1` FOREIGN KEY (`u_name`) REFERENCES `profile_details` (`u_name`),
  CONSTRAINT `loans_hist_ibfk_2` FOREIGN KEY (`loan_type`) REFERENCES `loan_types` (`loan_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loans_hist`
--

LOCK TABLES `loans_hist` WRITE;
/*!40000 ALTER TABLE `loans_hist` DISABLE KEYS */;
/*!40000 ALTER TABLE `loans_hist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_credentials`
--

DROP TABLE IF EXISTS `login_credentials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `login_credentials` (
  `u_name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `sec_ques1` varchar(250) NOT NULL,
  `sec_ans1` varchar(50) NOT NULL,
  `sec_ques2` varchar(250) NOT NULL,
  `sec_ans2` varchar(50) NOT NULL,
  `sec_ques3` varchar(250) NOT NULL,
  `sec_ans3` varchar(50) NOT NULL,
  PRIMARY KEY (`u_name`),
  CONSTRAINT `name_check` CHECK ((regexp_like(`u_name`,_utf8mb4'^[a-zA-Z0-9_!#]+$') and (char_length(`u_name`) >= 5))),
  CONSTRAINT `pass_check` CHECK ((regexp_like(`password`,_utf8mb4'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)') and (char_length(`password`) >= 8)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_credentials`
--

LOCK TABLES `login_credentials` WRITE;
/*!40000 ALTER TABLE `login_credentials` DISABLE KEYS */;
/*!40000 ALTER TABLE `login_credentials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profile_details`
--

DROP TABLE IF EXISTS `profile_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `profile_details` (
  `account_number` int(7) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `u_name` varchar(50) NOT NULL,
  `photo` longblob,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) NOT NULL,
  `email_address` varchar(50) NOT NULL,
  `contact` char(10) NOT NULL,
  `balance` float NOT NULL,
  PRIMARY KEY (`account_number`),
  UNIQUE KEY `u_name` (`u_name`),
  UNIQUE KEY `contact` (`contact`),
  CONSTRAINT `profile_details_ibfk_1` FOREIGN KEY (`u_name`) REFERENCES `login_credentials` (`u_name`),
  CONSTRAINT `contact_check` CHECK ((regexp_like(`contact`,_utf8mb4'^[0-9]+$') and (char_length(`contact`) = 10))),
  CONSTRAINT `email_check` CHECK (regexp_like(`email_address`,_utf8mb4'^[^s@]+@[^s@]+.[^s@]+$')),
  CONSTRAINT `name_check1` CHECK ((regexp_like(`first_name`,_utf8mb4'^[a-zA-Z]+$') and regexp_like(`middle_name`,_utf8mb4'^[a-zA-Z]+$') and regexp_like(`last_name`,_utf8mb4'^[a-zA-Z]+$')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profile_details`
--

LOCK TABLES `profile_details` WRITE;
/*!40000 ALTER TABLE `profile_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `profile_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-04 14:55:38
