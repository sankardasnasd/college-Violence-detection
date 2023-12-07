/*
SQLyog Community v13.2.0 (64 bit)
MySQL - 8.0.31 : Database - cvd
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`cvd` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `cvd`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add alert',7,'add_alert'),
(26,'Can change alert',7,'change_alert'),
(27,'Can delete alert',7,'delete_alert'),
(28,'Can view alert',7,'view_alert'),
(29,'Can add authority',8,'add_authority'),
(30,'Can change authority',8,'change_authority'),
(31,'Can delete authority',8,'delete_authority'),
(32,'Can view authority',8,'view_authority'),
(33,'Can add course',9,'add_course'),
(34,'Can change course',9,'change_course'),
(35,'Can delete course',9,'delete_course'),
(36,'Can view course',9,'view_course'),
(37,'Can add department',10,'add_department'),
(38,'Can change department',10,'change_department'),
(39,'Can delete department',10,'delete_department'),
(40,'Can view department',10,'view_department'),
(41,'Can add incident',11,'add_incident'),
(42,'Can change incident',11,'change_incident'),
(43,'Can delete incident',11,'delete_incident'),
(44,'Can view incident',11,'view_incident'),
(45,'Can add login',12,'add_login'),
(46,'Can change login',12,'change_login'),
(47,'Can delete login',12,'delete_login'),
(48,'Can view login',12,'view_login'),
(49,'Can add security_guard',13,'add_security_guard'),
(50,'Can change security_guard',13,'change_security_guard'),
(51,'Can delete security_guard',13,'delete_security_guard'),
(52,'Can view security_guard',13,'view_security_guard'),
(53,'Can add student',14,'add_student'),
(54,'Can change student',14,'change_student'),
(55,'Can delete student',14,'delete_student'),
(56,'Can view student',14,'view_student'),
(57,'Can add staff',15,'add_staff'),
(58,'Can change staff',15,'change_staff'),
(59,'Can delete staff',15,'delete_staff'),
(60,'Can view staff',15,'view_staff'),
(61,'Can add notification',16,'add_notification'),
(62,'Can change notification',16,'change_notification'),
(63,'Can delete notification',16,'delete_notification'),
(64,'Can view notification',16,'view_notification'),
(65,'Can add feedback',17,'add_feedback'),
(66,'Can change feedback',17,'change_feedback'),
(67,'Can delete feedback',17,'delete_feedback'),
(68,'Can view feedback',17,'view_feedback'),
(69,'Can add complaint',18,'add_complaint'),
(70,'Can change complaint',18,'change_complaint'),
(71,'Can delete complaint',18,'delete_complaint'),
(72,'Can view complaint',18,'view_complaint'),
(73,'Can add checkin_chechout',19,'add_checkin_chechout'),
(74,'Can change checkin_chechout',19,'change_checkin_chechout'),
(75,'Can delete checkin_chechout',19,'delete_checkin_chechout'),
(76,'Can view checkin_chechout',19,'view_checkin_chechout'),
(77,'Can add chat',20,'add_chat'),
(78,'Can change chat',20,'change_chat'),
(79,'Can delete chat',20,'delete_chat'),
(80,'Can view chat',20,'view_chat'),
(81,'Can add attendance',21,'add_attendance'),
(82,'Can change attendance',21,'change_attendance'),
(83,'Can delete attendance',21,'delete_attendance'),
(84,'Can view attendance',21,'view_attendance'),
(85,'Can add action',22,'add_action'),
(86,'Can change action',22,'change_action'),
(87,'Can delete action',22,'delete_action'),
(88,'Can view action',22,'view_action'),
(89,'Can add message',23,'add_message'),
(90,'Can change message',23,'change_message'),
(91,'Can delete message',23,'delete_message'),
(92,'Can view message',23,'view_message'),
(93,'Can add violence',24,'add_violence'),
(94,'Can change violence',24,'change_violence'),
(95,'Can delete violence',24,'delete_violence'),
(96,'Can view violence',24,'view_violence'),
(97,'Can add violence_included_face',25,'add_violence_included_face'),
(98,'Can change violence_included_face',25,'change_violence_included_face'),
(99,'Can delete violence_included_face',25,'delete_violence_included_face'),
(100,'Can view violence_included_face',25,'view_violence_included_face');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(2,'auth','permission'),
(3,'auth','group'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(7,'myapp','alert'),
(8,'myapp','authority'),
(9,'myapp','course'),
(10,'myapp','department'),
(11,'myapp','incident'),
(12,'myapp','login'),
(13,'myapp','security_guard'),
(14,'myapp','student'),
(15,'myapp','staff'),
(16,'myapp','notification'),
(17,'myapp','feedback'),
(18,'myapp','complaint'),
(19,'myapp','checkin_chechout'),
(20,'myapp','chat'),
(21,'myapp','attendance'),
(22,'myapp','action'),
(23,'myapp','message'),
(24,'myapp','violence'),
(25,'myapp','violence_included_face');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-10-24 06:46:50.833656'),
(2,'auth','0001_initial','2023-10-24 06:46:51.387530'),
(3,'admin','0001_initial','2023-10-24 06:46:51.574032'),
(4,'admin','0002_logentry_remove_auto_add','2023-10-24 06:46:51.580607'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-10-24 06:46:51.586532'),
(6,'contenttypes','0002_remove_content_type_name','2023-10-24 06:46:51.656896'),
(7,'auth','0002_alter_permission_name_max_length','2023-10-24 06:46:51.695518'),
(8,'auth','0003_alter_user_email_max_length','2023-10-24 06:46:51.738820'),
(9,'auth','0004_alter_user_username_opts','2023-10-24 06:46:51.743172'),
(10,'auth','0005_alter_user_last_login_null','2023-10-24 06:46:51.788015'),
(11,'auth','0006_require_contenttypes_0002','2023-10-24 06:46:51.791783'),
(12,'auth','0007_alter_validators_add_error_messages','2023-10-24 06:46:51.797002'),
(13,'auth','0008_alter_user_username_max_length','2023-10-24 06:46:51.838008'),
(14,'auth','0009_alter_user_last_name_max_length','2023-10-24 06:46:51.879185'),
(15,'auth','0010_alter_group_name_max_length','2023-10-24 06:46:51.921966'),
(16,'auth','0011_update_proxy_permissions','2023-10-24 06:46:51.930317'),
(17,'auth','0012_alter_user_first_name_max_length','2023-10-24 06:46:51.974155'),
(18,'myapp','0001_initial','2023-10-24 06:46:53.034908'),
(19,'myapp','0002_rename_age_student_dob','2023-10-24 06:46:53.062419'),
(20,'myapp','0003_rename_age_staff_dob_remove_student_no_of_semester','2023-10-24 06:46:53.126644'),
(21,'myapp','0004_complaint_complaint_staff_qulification_and_more','2023-10-24 06:46:53.261616'),
(22,'myapp','0005_complaint_reply','2023-10-24 06:46:53.306079'),
(23,'myapp','0006_rename_gender_authority_gendre_and_more','2023-10-24 06:46:53.360184'),
(24,'myapp','0007_message','2023-10-24 06:46:53.436236'),
(25,'myapp','0008_violence_remove_complaint_complaint_replay_and_more','2023-10-24 06:46:53.825473'),
(26,'sessions','0001_initial','2023-10-24 06:46:53.871513'),
(27,'myapp','0009_attendance_photo','2023-10-26 09:24:40.347451');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('nntnhjg7aspbr2z72us83vx12ow94u0a','eyJsaWQiOjIsInVzZXJpZCI6IjQiLCJuZXciOiI0In0:1qvEws:4N1G2I1Vaa0LUbYlkjxEWinF91vY-Ue1IE4wpaCkhHg','2023-11-07 10:47:46.398069'),
('ybt54x14kq5uxj9qu3umdryro0h3yqw4','eyJsaWQiOjIsInVzZXJpZCI6IjUiLCJuZXciOiI1In0:1qvwds:IGPsP-1p4JGIIMfSNrCw5zO7-IxqyR57uBmc6_BI4eE','2023-11-09 09:27:04.960943');

/*Table structure for table `myapp_action` */

DROP TABLE IF EXISTS `myapp_action`;

CREATE TABLE `myapp_action` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `action` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `ALERT_id` bigint NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_action_ALERT_id_0ac71499` (`ALERT_id`),
  KEY `myapp_action_STUDENT_id_5e137ca6` (`STUDENT_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_action` */

/*Table structure for table `myapp_alert` */

DROP TABLE IF EXISTS `myapp_alert`;

CREATE TABLE `myapp_alert` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `alert` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_alert` */

/*Table structure for table `myapp_attendance` */

DROP TABLE IF EXISTS `myapp_attendance`;

CREATE TABLE `myapp_attendance` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `checkin_checkout` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  `time` varchar(100) NOT NULL,
  `photo` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_attendance_STUDENT_id_d2e99675` (`STUDENT_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_attendance` */

insert  into `myapp_attendance`(`id`,`checkin_checkout`,`date`,`STUDENT_id`,`time`,`photo`) values 
(1,'Check In','2023-10-26',1,'14:55:26','/media/attendance/20231026145526373102.jpg'),
(2,'Check Out','2023-10-26',1,'14:55:28','/media/attendance/20231026145528386044.jpg');

/*Table structure for table `myapp_authority` */

DROP TABLE IF EXISTS `myapp_authority`;

CREATE TABLE `myapp_authority` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `phone_number` bigint NOT NULL,
  `gendre` varchar(100) NOT NULL,
  `age` date NOT NULL,
  `image` varchar(350) NOT NULL,
  `e_mail` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_authority_LOGIN_id_edd5b446` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_authority` */

insert  into `myapp_authority`(`id`,`name`,`phone_number`,`gendre`,`age`,`image`,`e_mail`,`LOGIN_id`) values 
(1,'mallu',6578435678,'Female','2005-10-11','/media/Y1025-114551.jpg','Afra12@gmail.com',2),
(2,'mallu',6578435678,'Male','2005-10-05','/media/Y1025-114949.jpg','Afra12@gmail.com',3);

/*Table structure for table `myapp_chat` */

DROP TABLE IF EXISTS `myapp_chat`;

CREATE TABLE `myapp_chat` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `massege` varchar(100) NOT NULL,
  `FROMID_id` bigint NOT NULL,
  `TOID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_chat_FROMID_id_c34a39e8` (`FROMID_id`),
  KEY `myapp_chat_TOID_id_c3a45261` (`TOID_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_chat` */

insert  into `myapp_chat`(`id`,`date`,`massege`,`FROMID_id`,`TOID_id`) values 
(6,'2023-10-24','kjk',2,5),
(5,'2023-10-24','Hey',5,2),
(4,'2023-10-24','klk',2,5),
(7,'2023-10-24','fugjgj',5,2),
(8,'2023-10-26','ggdd',2,5),
(9,'2023-10-26','from parent',2,5),
(10,'2023-10-26','test',2,5),
(11,'2023-10-26','jjkkkko',5,2),
(12,'2023-10-26','jjkkkko',5,2),
(13,'2023-10-26','chckgih',5,2),
(14,'2023-10-26','p',2,5);

/*Table structure for table `myapp_checkin_chechout` */

DROP TABLE IF EXISTS `myapp_checkin_chechout`;

CREATE TABLE `myapp_checkin_chechout` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `checkin_checkout` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_checkin_chechout_STUDENT_id_edb311cb` (`STUDENT_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_checkin_chechout` */

/*Table structure for table `myapp_complaint` */

DROP TABLE IF EXISTS `myapp_complaint`;

CREATE TABLE `myapp_complaint` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `PARENT_id` bigint NOT NULL,
  `complaint` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_complaint_PARENT_id_22b50dc6` (`PARENT_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_complaint` */

insert  into `myapp_complaint`(`id`,`date`,`status`,`PARENT_id`,`complaint`,`reply`) values 
(1,'2023-10-25','pending',5,'cc','pending'),
(2,'2023-10-25','pending',5,'teddy utt DCR','pending'),
(3,'2023-10-25','pending',5,'Manju','pending'),
(4,'2023-10-25','pending',5,'Amit Anna','pending'),
(5,'2023-10-26','pending',5,'Bad','pending'),
(6,'2023-10-26','pending',9,'Tests','pending'),
(7,'2023-10-26','pending',9,'hehdjdjdf','pending'),
(8,'2023-10-26','pending',9,'glass','pending');

/*Table structure for table `myapp_course` */

DROP TABLE IF EXISTS `myapp_course`;

CREATE TABLE `myapp_course` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `course` varchar(100) NOT NULL,
  `no_of_semester` varchar(100) NOT NULL,
  `DEPARTMENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_course_DEPARTMENT_id_9a598a92` (`DEPARTMENT_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_course` */

insert  into `myapp_course`(`id`,`course`,`no_of_semester`,`DEPARTMENT_id`) values 
(1,'computerscience','4',2);

/*Table structure for table `myapp_department` */

DROP TABLE IF EXISTS `myapp_department`;

CREATE TABLE `myapp_department` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `department` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_department` */

insert  into `myapp_department`(`id`,`department`) values 
(1,'bsc'),
(2,'bsc');

/*Table structure for table `myapp_feedback` */

DROP TABLE IF EXISTS `myapp_feedback`;

CREATE TABLE `myapp_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `feedback` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_feedback_LOGIN_id_7243a689` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_feedback` */

insert  into `myapp_feedback`(`id`,`date`,`feedback`,`LOGIN_id`) values 
(1,'2023-10-26','gdhdhjdd',3),
(2,'2023-10-26','',3),
(3,'2023-10-26','nd Ann',3);

/*Table structure for table `myapp_incident` */

DROP TABLE IF EXISTS `myapp_incident`;

CREATE TABLE `myapp_incident` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `incident` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_incident` */

insert  into `myapp_incident`(`id`,`date`,`incident`,`description`) values 
(1,'2023-10-24','sdfghj','ertyu');

/*Table structure for table `myapp_login` */

DROP TABLE IF EXISTS `myapp_login`;

CREATE TABLE `myapp_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`type`) values 
(1,'admin@123','Ashnm098','admin'),
(2,'Afra12@gmail.com','Fv78','authority'),
(3,'Afra12@gmail.com','6578435678','authority'),
(4,'Asdf123z@gmail.com','1234','student'),
(5,'nhz123@gmail.com','1234','parent'),
(6,'Hasna51@gmail.com','7896543210','student'),
(7,'Adfg12@gmail.com','9098768989','parent'),
(8,'mrudula@gmail.com','1234','student'),
(9,'mrudula@gmail.com','parent','parent');

/*Table structure for table `myapp_message` */

DROP TABLE IF EXISTS `myapp_message`;

CREATE TABLE `myapp_message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `AUTHORITY_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_message_AUTHORITY_id_e2128075` (`AUTHORITY_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_message` */

insert  into `myapp_message`(`id`,`message`,`date`,`AUTHORITY_id`) values 
(1,'NBV','2023-10-24',1);

/*Table structure for table `myapp_notification` */

DROP TABLE IF EXISTS `myapp_notification`;

CREATE TABLE `myapp_notification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `notification` varchar(100) NOT NULL,
  `AUTHORITY_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_notification_AUTHORITY_id_88858d26` (`AUTHORITY_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_notification` */

insert  into `myapp_notification`(`id`,`date`,`notification`,`AUTHORITY_id`) values 
(1,'2023-10-24','098',1),
(2,'2023-10-24','1234',1);

/*Table structure for table `myapp_security_guard` */

DROP TABLE IF EXISTS `myapp_security_guard`;

CREATE TABLE `myapp_security_guard` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `phone_number` bigint NOT NULL,
  `e_mail` varchar(100) NOT NULL,
  `age` date NOT NULL,
  `gender` varchar(100) NOT NULL,
  `image` varchar(350) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_security_guard` */

/*Table structure for table `myapp_staff` */

DROP TABLE IF EXISTS `myapp_staff`;

CREATE TABLE `myapp_staff` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `phone_number` bigint NOT NULL,
  `gender` varchar(100) NOT NULL,
  `e_mail` varchar(100) NOT NULL,
  `image` varchar(350) NOT NULL,
  `dob` date NOT NULL,
  `DEPARTMENT_id` bigint NOT NULL,
  `qulification` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_staff_DEPARTMENT_id_1ae2ea1b` (`DEPARTMENT_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_staff` */

insert  into `myapp_staff`(`id`,`name`,`phone_number`,`gender`,`e_mail`,`image`,`dob`,`DEPARTMENT_id`,`qulification`) values 
(1,'xcvbn',7654567890,'Male','Adfg123@gmil.com','/media/Y1024-124005.jpg','2005-10-14',1,'degree');

/*Table structure for table `myapp_student` */

DROP TABLE IF EXISTS `myapp_student`;

CREATE TABLE `myapp_student` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `phone_number` bigint NOT NULL,
  `e_mail` varchar(100) NOT NULL,
  `image` varchar(350) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `pincode` int NOT NULL,
  `parent_name` varchar(100) NOT NULL,
  `parent_number` bigint NOT NULL,
  `parent_e_mail_id` varchar(100) NOT NULL,
  `COURSE_id` bigint NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_student_COURSE_id_5fe98c90` (`COURSE_id`),
  KEY `myapp_student_LOGIN_id_d3327a2f` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_student` */

insert  into `myapp_student`(`id`,`name`,`phone_number`,`e_mail`,`image`,`dob`,`gender`,`place`,`city`,`district`,`state`,`pincode`,`parent_name`,`parent_number`,`parent_e_mail_id`,`COURSE_id`,`LOGIN_id`) values 
(1,'afruu',7656765645,'Asdf123z@gmail.com','/media/Y1024-124301.jpg','2005-10-15','Female','cfh','fgh','sdf','dfg',567890,'nehluz',9876543219,'nhz123@gmail.com',1,4),
(2,'hasna',7896543210,'Hasna51@gmail.com','/media/Y1025-114551.jpg','2005-10-13','Female','bnmk','bnmk','kjh','asd',98765,'sdfgh',9098768989,'Adfg12@gmail.com',1,6),
(3,'mrudula',8848794800,'mrudula@gmail.com','/media/Y1025-114949.jpg','2003-05-05','Female','ponnani','ponnani','malapuram','kerala',678905,'ythg',9656033567,'mrudula@gmail.com',1,8);

/*Table structure for table `myapp_violence` */

DROP TABLE IF EXISTS `myapp_violence`;

CREATE TABLE `myapp_violence` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` varchar(100) NOT NULL,
  `image` varchar(350) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_violence` */

insert  into `myapp_violence`(`id`,`date`,`time`,`image`) values 
(1,'2023-10-17','10:16','/media/Y1024-124301.jpg');

/*Table structure for table `myapp_violence_included_face` */

DROP TABLE IF EXISTS `myapp_violence_included_face`;

CREATE TABLE `myapp_violence_included_face` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `STUDENT_id` bigint NOT NULL,
  `VIOLENCE_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_violence_included_face_STUDENT_id_593d4ab5` (`STUDENT_id`),
  KEY `myapp_violence_included_face_VIOLENCE_id_059d4962` (`VIOLENCE_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_violence_included_face` */

insert  into `myapp_violence_included_face`(`id`,`STUDENT_id`,`VIOLENCE_id`) values 
(1,1,1),
(2,1,1),
(3,2,1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
