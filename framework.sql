-- MySQL dump 10.13  Distrib 5.6.24, for osx10.8 (x86_64)
--
-- Host: localhost    Database: framework
-- ------------------------------------------------------
-- Server version	5.5.50-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add projeto',6,'add_projeto'),(17,'Can change projeto',6,'change_projeto'),(18,'Can delete projeto',6,'delete_projeto'),(19,'Can add genero',7,'add_genero'),(20,'Can change genero',7,'change_genero'),(21,'Can delete genero',7,'delete_genero'),(22,'Can add logradouro',8,'add_logradouro'),(23,'Can change logradouro',8,'change_logradouro'),(24,'Can delete logradouro',8,'delete_logradouro'),(25,'Can add endereco',9,'add_endereco'),(26,'Can change endereco',9,'change_endereco'),(27,'Can delete endereco',9,'delete_endereco'),(28,'Can add tipo empresa',10,'add_tipoempresa'),(29,'Can change tipo empresa',10,'change_tipoempresa'),(30,'Can delete tipo empresa',10,'delete_tipoempresa'),(31,'Can add empresa',11,'add_empresa'),(32,'Can change empresa',11,'change_empresa'),(33,'Can delete empresa',11,'delete_empresa'),(34,'Can add tipo usuario',12,'add_tipousuario'),(35,'Can change tipo usuario',12,'change_tipousuario'),(36,'Can delete tipo usuario',12,'delete_tipousuario'),(37,'Can add tipo relacao',13,'add_tiporelacao'),(38,'Can change tipo relacao',13,'change_tiporelacao'),(39,'Can delete tipo relacao',13,'delete_tiporelacao'),(40,'Can add tipo relacao empresa',14,'add_tiporelacaoempresa'),(41,'Can change tipo relacao empresa',14,'change_tiporelacaoempresa'),(42,'Can delete tipo relacao empresa',14,'delete_tiporelacaoempresa'),(43,'Can add tipo documento',15,'add_tipodocumento'),(44,'Can change tipo documento',15,'change_tipodocumento'),(45,'Can delete tipo documento',15,'delete_tipodocumento'),(46,'Can add tipo telefone',16,'add_tipotelefone'),(47,'Can change tipo telefone',16,'change_tipotelefone'),(48,'Can delete tipo telefone',16,'delete_tipotelefone'),(49,'Can add usuario',17,'add_usuario'),(50,'Can change usuario',17,'change_usuario'),(51,'Can delete usuario',17,'delete_usuario'),(52,'Can add telefone usuario',18,'add_telefoneusuario'),(53,'Can change telefone usuario',18,'change_telefoneusuario'),(54,'Can delete telefone usuario',18,'delete_telefoneusuario'),(55,'Can add telefone empresa',19,'add_telefoneempresa'),(56,'Can change telefone empresa',19,'change_telefoneempresa'),(57,'Can delete telefone empresa',19,'delete_telefoneempresa'),(58,'Can add usuario empresa',20,'add_usuarioempresa'),(59,'Can change usuario empresa',20,'change_usuarioempresa'),(60,'Can delete usuario empresa',20,'delete_usuarioempresa'),(61,'Can add visao',21,'add_visao'),(62,'Can change visao',21,'change_visao'),(63,'Can delete visao',21,'delete_visao'),(64,'Can add relacao empresa',22,'add_relacaoempresa'),(65,'Can change relacao empresa',22,'change_relacaoempresa'),(66,'Can delete relacao empresa',22,'delete_relacaoempresa'),(67,'Can add relacao usuario',23,'add_relacaousuario'),(68,'Can change relacao usuario',23,'change_relacaousuario'),(69,'Can delete relacao usuario',23,'delete_relacaousuario'),(70,'Can add documento',24,'add_documento'),(71,'Can change documento',24,'change_documento'),(72,'Can delete documento',24,'delete_documento'),(73,'Can add startup',25,'add_startup'),(74,'Can change startup',25,'change_startup'),(75,'Can delete startup',25,'delete_startup'),(76,'Can add funcionario',26,'add_funcionario'),(77,'Can change funcionario',26,'change_funcionario'),(78,'Can delete funcionario',26,'delete_funcionario');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_documento`
--

DROP TABLE IF EXISTS `default_documento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_documento` (
  `id_documento` int(11) NOT NULL AUTO_INCREMENT,
  `anexo` varchar(100) NOT NULL,
  `datahora` datetime NOT NULL,
  `id_tipo_documento_id` int(11) NOT NULL,
  `id_usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id_documento`),
  KEY `default_documento_13cd52fd` (`id_tipo_documento_id`),
  KEY `default_documento_76a74f43` (`id_usuario_id`),
  CONSTRAINT `D51b612561fc499295817976b3c6ae31` FOREIGN KEY (`id_tipo_documento_id`) REFERENCES `default_tipodocumento` (`id_tipo_documento`),
  CONSTRAINT `default_doc_id_usuario_id_4a40639f_fk_default_usuario_id_usuario` FOREIGN KEY (`id_usuario_id`) REFERENCES `default_usuario` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_documento`
--

LOCK TABLES `default_documento` WRITE;
/*!40000 ALTER TABLE `default_documento` DISABLE KEYS */;
/*!40000 ALTER TABLE `default_documento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_empresa`
--

DROP TABLE IF EXISTS `default_empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_empresa` (
  `id_empresa` int(11) NOT NULL AUTO_INCREMENT,
  `razaosocial` varchar(100) NOT NULL,
  `nomefantasia` varchar(100) NOT NULL,
  `cnpj` varchar(20) NOT NULL,
  `verificada` tinyint(1) NOT NULL,
  `ie` varchar(45) NOT NULL,
  `id_endereco_id` int(11) NOT NULL,
  `id_tipo_empresa_id` int(11) NOT NULL,
  PRIMARY KEY (`id_empresa`),
  KEY `default_empresa_f5c1a11c` (`id_endereco_id`),
  KEY `default_empresa_901cc6c7` (`id_tipo_empresa_id`),
  CONSTRAINT `a6a0282ea2f63a1d9c75cdbb9f396619` FOREIGN KEY (`id_tipo_empresa_id`) REFERENCES `default_tipoempresa` (`id_tipo_empresa`),
  CONSTRAINT `default__id_endereco_id_dc9a6a4a_fk_default_endereco_id_endereco` FOREIGN KEY (`id_endereco_id`) REFERENCES `default_endereco` (`id_endereco`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_empresa`
--

LOCK TABLES `default_empresa` WRITE;
/*!40000 ALTER TABLE `default_empresa` DISABLE KEYS */;
/*!40000 ALTER TABLE `default_empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_endereco`
--

DROP TABLE IF EXISTS `default_endereco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_endereco` (
  `id_endereco` int(11) NOT NULL AUTO_INCREMENT,
  `numero` int(11) NOT NULL,
  `complemento` varchar(45) NOT NULL,
  `pontoreferencia` varchar(45) NOT NULL,
  `id_logradouro_id` int(11) NOT NULL,
  PRIMARY KEY (`id_endereco`),
  KEY `default_endereco_9646dd94` (`id_logradouro_id`),
  CONSTRAINT `de_id_logradouro_id_8b4dc3bd_fk_default_logradouro_id_logradouro` FOREIGN KEY (`id_logradouro_id`) REFERENCES `default_logradouro` (`id_logradouro`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_endereco`
--

LOCK TABLES `default_endereco` WRITE;
/*!40000 ALTER TABLE `default_endereco` DISABLE KEYS */;
INSERT INTO `default_endereco` VALUES (1,125,'casa 03','Restaurante Gota serena',1);
/*!40000 ALTER TABLE `default_endereco` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_genero`
--

DROP TABLE IF EXISTS `default_genero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_genero` (
  `id_genero` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(45) NOT NULL,
  `abreviacao` varchar(1) NOT NULL,
  PRIMARY KEY (`id_genero`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_genero`
--

LOCK TABLES `default_genero` WRITE;
/*!40000 ALTER TABLE `default_genero` DISABLE KEYS */;
INSERT INTO `default_genero` VALUES (1,'Feminino','F'),(2,'Masculino','M'),(3,'Outros','O');
/*!40000 ALTER TABLE `default_genero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_logradouro`
--

DROP TABLE IF EXISTS `default_logradouro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_logradouro` (
  `id_logradouro` int(11) NOT NULL AUTO_INCREMENT,
  `cep` varchar(10) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `bairro` varchar(45) NOT NULL,
  `cidade` varchar(20) NOT NULL,
  `estado` varchar(2) NOT NULL,
  `pais` varchar(45) NOT NULL,
  PRIMARY KEY (`id_logradouro`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_logradouro`
--

LOCK TABLES `default_logradouro` WRITE;
/*!40000 ALTER TABLE `default_logradouro` DISABLE KEYS */;
INSERT INTO `default_logradouro` VALUES (1,'50.670-400','Ytalo','Iputinga','Recife','PE','Brazil');
/*!40000 ALTER TABLE `default_logradouro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_projeto`
--

DROP TABLE IF EXISTS `default_projeto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_projeto` (
  `id_projeto` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `logo` varchar(100) DEFAULT NULL,
  `website` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_projeto`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_projeto`
--

LOCK TABLES `default_projeto` WRITE;
/*!40000 ALTER TABLE `default_projeto` DISABLE KEYS */;
INSERT INTO `default_projeto` VALUES (1,'Manual do Proprietário','default/project/logo.png','http://www.portoengenharia.com.br');
/*!40000 ALTER TABLE `default_projeto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_relacaoempresa`
--

DROP TABLE IF EXISTS `default_relacaoempresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_relacaoempresa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data_criacao` datetime NOT NULL,
  `id_empresa_1_id` int(11) NOT NULL,
  `id_relacao_empresa_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `default_relacaoempresa_0a47fdd4` (`id_empresa_1_id`),
  KEY `default_relacaoempresa_9e8d65bd` (`id_relacao_empresa_id`),
  CONSTRAINT `cc7499ff4bc12c1cfcde89deff94e7c3` FOREIGN KEY (`id_relacao_empresa_id`) REFERENCES `default_tiporelacaoempresa` (`id_tipo_relacao_empresa`),
  CONSTRAINT `id_empresa_1_id_7df44c83_fk_default_tipoempresa_id_tipo_empresa` FOREIGN KEY (`id_empresa_1_id`) REFERENCES `default_tipoempresa` (`id_tipo_empresa`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_relacaoempresa`
--

LOCK TABLES `default_relacaoempresa` WRITE;
/*!40000 ALTER TABLE `default_relacaoempresa` DISABLE KEYS */;
/*!40000 ALTER TABLE `default_relacaoempresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_relacaousuario`
--

DROP TABLE IF EXISTS `default_relacaousuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_relacaousuario` (
  `id_relacao_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `data_criacao` datetime NOT NULL,
  `id_tipo_relacao_empresa_id` int(11) NOT NULL,
  `id_usuario_1_id` int(11) NOT NULL,
  PRIMARY KEY (`id_relacao_usuario`),
  KEY `default_relacaousuario_f094d499` (`id_tipo_relacao_empresa_id`),
  KEY `default_relacaousuario_666c6143` (`id_usuario_1_id`),
  CONSTRAINT `D34d9c4beda37846ebc322ec60133f15` FOREIGN KEY (`id_tipo_relacao_empresa_id`) REFERENCES `default_tiporelacaoempresa` (`id_tipo_relacao_empresa`),
  CONSTRAINT `id_usuario_1_id_4d1c3ff4_fk_default_tipousuario_id_tipo_usuario` FOREIGN KEY (`id_usuario_1_id`) REFERENCES `default_tipousuario` (`id_tipo_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_relacaousuario`
--

LOCK TABLES `default_relacaousuario` WRITE;
/*!40000 ALTER TABLE `default_relacaousuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `default_relacaousuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_telefoneempresa`
--

DROP TABLE IF EXISTS `default_telefoneempresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_telefoneempresa` (
  `id_telefone_empresa` int(11) NOT NULL AUTO_INCREMENT,
  `numero` varchar(11) NOT NULL,
  `ramal` varchar(4) NOT NULL,
  `nome_contato` varchar(45) NOT NULL,
  `id_empresa_id` int(11) NOT NULL,
  `id_tipo_telefone_id` int(11) NOT NULL,
  PRIMARY KEY (`id_telefone_empresa`),
  KEY `default_telefoneempresa_87cc7c3c` (`id_tipo_telefone_id`),
  KEY `default_tel_id_empresa_id_115e1814_fk_default_empresa_id_empresa` (`id_empresa_id`),
  CONSTRAINT `default_tel_id_empresa_id_115e1814_fk_default_empresa_id_empresa` FOREIGN KEY (`id_empresa_id`) REFERENCES `default_empresa` (`id_empresa`),
  CONSTRAINT `e57c3026a5a8b92739169aba879b8b92` FOREIGN KEY (`id_tipo_telefone_id`) REFERENCES `default_tipotelefone` (`id_tipo_Telefone`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_telefoneempresa`
--

LOCK TABLES `default_telefoneempresa` WRITE;
/*!40000 ALTER TABLE `default_telefoneempresa` DISABLE KEYS */;
/*!40000 ALTER TABLE `default_telefoneempresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_telefoneusuario`
--

DROP TABLE IF EXISTS `default_telefoneusuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_telefoneusuario` (
  `id_telefone_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `numero` varchar(11) NOT NULL,
  `id_tipo_telefone_id` int(11) NOT NULL,
  `id_usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id_telefone_usuario`),
  KEY `default_telefoneusuario_87cc7c3c` (`id_tipo_telefone_id`),
  KEY `default_telefoneusuario_76a74f43` (`id_usuario_id`),
  CONSTRAINT `D3652c27d890da756e3d185fd6e56151` FOREIGN KEY (`id_tipo_telefone_id`) REFERENCES `default_tipotelefone` (`id_tipo_Telefone`),
  CONSTRAINT `default_tel_id_usuario_id_1cb5cf33_fk_default_usuario_id_usuario` FOREIGN KEY (`id_usuario_id`) REFERENCES `default_usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_telefoneusuario`
--

LOCK TABLES `default_telefoneusuario` WRITE;
/*!40000 ALTER TABLE `default_telefoneusuario` DISABLE KEYS */;
INSERT INTO `default_telefoneusuario` VALUES (1,'81987666730',1,3);
/*!40000 ALTER TABLE `default_telefoneusuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_tipodocumento`
--

DROP TABLE IF EXISTS `default_tipodocumento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_tipodocumento` (
  `id_tipo_documento` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(45) NOT NULL,
  PRIMARY KEY (`id_tipo_documento`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_tipodocumento`
--

LOCK TABLES `default_tipodocumento` WRITE;
/*!40000 ALTER TABLE `default_tipodocumento` DISABLE KEYS */;
/*!40000 ALTER TABLE `default_tipodocumento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_tipoempresa`
--

DROP TABLE IF EXISTS `default_tipoempresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_tipoempresa` (
  `id_tipo_empresa` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(45) NOT NULL,
  PRIMARY KEY (`id_tipo_empresa`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_tipoempresa`
--

LOCK TABLES `default_tipoempresa` WRITE;
/*!40000 ALTER TABLE `default_tipoempresa` DISABLE KEYS */;
INSERT INTO `default_tipoempresa` VALUES (1,'Incorporadora');
/*!40000 ALTER TABLE `default_tipoempresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_tiporelacao`
--

DROP TABLE IF EXISTS `default_tiporelacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_tiporelacao` (
  `id_tipo_relacao` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(45) NOT NULL,
  PRIMARY KEY (`id_tipo_relacao`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_tiporelacao`
--

LOCK TABLES `default_tiporelacao` WRITE;
/*!40000 ALTER TABLE `default_tiporelacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `default_tiporelacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_tiporelacaoempresa`
--

DROP TABLE IF EXISTS `default_tiporelacaoempresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_tiporelacaoempresa` (
  `id_tipo_relacao_empresa` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(45) NOT NULL,
  PRIMARY KEY (`id_tipo_relacao_empresa`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_tiporelacaoempresa`
--

LOCK TABLES `default_tiporelacaoempresa` WRITE;
/*!40000 ALTER TABLE `default_tiporelacaoempresa` DISABLE KEYS */;
/*!40000 ALTER TABLE `default_tiporelacaoempresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_tipotelefone`
--

DROP TABLE IF EXISTS `default_tipotelefone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_tipotelefone` (
  `id_tipo_Telefone` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(45) NOT NULL,
  PRIMARY KEY (`id_tipo_Telefone`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_tipotelefone`
--

LOCK TABLES `default_tipotelefone` WRITE;
/*!40000 ALTER TABLE `default_tipotelefone` DISABLE KEYS */;
INSERT INTO `default_tipotelefone` VALUES (1,'FAX'),(2,'Comercial'),(3,'Residencial'),(4,'Celular'),(5,'Whatsapp');
/*!40000 ALTER TABLE `default_tipotelefone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_tipousuario`
--

DROP TABLE IF EXISTS `default_tipousuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_tipousuario` (
  `id_tipo_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(45) NOT NULL,
  PRIMARY KEY (`id_tipo_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_tipousuario`
--

LOCK TABLES `default_tipousuario` WRITE;
/*!40000 ALTER TABLE `default_tipousuario` DISABLE KEYS */;
INSERT INTO `default_tipousuario` VALUES (1,'Engenheiro Técnico'),(2,'Diretor'),(3,'Administrador');
/*!40000 ALTER TABLE `default_tipousuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_usuario`
--

DROP TABLE IF EXISTS `default_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_usuario` (
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) DEFAULT NULL,
  `sobrenome` varchar(45) DEFAULT NULL,
  `nomecompleto` varchar(100) DEFAULT NULL,
  `email` varchar(75) NOT NULL,
  `cpf` varchar(14) DEFAULT NULL,
  `data_nascimento` datetime DEFAULT NULL,
  `rg` varchar(12) DEFAULT NULL,
  `orgaoemissor` varchar(45) DEFAULT NULL,
  `foto` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `id_endereco_id` int(11),
  `id_genero_id` int(11),
  `id_tipo_usuario_id` int(11),
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `email` (`email`),
  KEY `default_usuario_f5c1a11c` (`id_endereco_id`),
  KEY `default_usuario_969ce83a` (`id_genero_id`),
  KEY `default_usuario_f3e37a2b` (`id_tipo_usuario_id`),
  CONSTRAINT `D3e1b93df2c4eb0b0de877c6e15b0d77` FOREIGN KEY (`id_tipo_usuario_id`) REFERENCES `default_tipousuario` (`id_tipo_usuario`),
  CONSTRAINT `default_usuari_id_genero_id_d59b4611_fk_default_genero_id_genero` FOREIGN KEY (`id_genero_id`) REFERENCES `default_genero` (`id_genero`),
  CONSTRAINT `default__id_endereco_id_f2655603_fk_default_endereco_id_endereco` FOREIGN KEY (`id_endereco_id`) REFERENCES `default_endereco` (`id_endereco`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_usuario`
--

LOCK TABLES `default_usuario` WRITE;
/*!40000 ALTER TABLE `default_usuario` DISABLE KEYS */;
INSERT INTO `default_usuario` VALUES ('pbkdf2_sha256$24000$uxJUjKIrBNoD$or98VV8STxsLdGIWN+/5pL7e0clPMof21fZiEO3HLL0=',NULL,1,NULL,NULL,NULL,'teste@3ysoftwarehouse.com.br',NULL,NULL,NULL,NULL,'',1,1,NULL,NULL,NULL),('pbkdf2_sha256$24000$SKsFyXIlNMqP$65jKC/itnLQ/q7ShgxJRKmFdYigmb9lPF95akKovUWg=','2016-08-12 17:23:38',2,NULL,NULL,NULL,'teste@teste.com.br',NULL,NULL,NULL,NULL,'',1,1,NULL,NULL,NULL),('pbkdf2_sha256$24000$ddfWOENW728W$j8mb1KwVNnQfyCeJKtqhto1LGMexpICC/imny1HpMfU=',NULL,3,'Ytalo','Martins','Ytalo Martins','ytalomartins@outlook.com','016.190.024-00','2009-04-29 00:00:00','00.822.507-0','sds PE','',0,0,1,2,1);
/*!40000 ALTER TABLE `default_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_usuarioempresa`
--

DROP TABLE IF EXISTS `default_usuarioempresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_usuarioempresa` (
  `id_usuario_empresa` int(11) NOT NULL AUTO_INCREMENT,
  `ativo` tinyint(1) NOT NULL,
  `id_empresa_id` int(11) NOT NULL,
  `id_usuario_id` int(11) NOT NULL,
  `id_visao_id` int(11) NOT NULL,
  PRIMARY KEY (`id_usuario_empresa`),
  KEY `default_usu_id_empresa_id_3913a4e0_fk_default_empresa_id_empresa` (`id_empresa_id`),
  KEY `default_usu_id_usuario_id_4300c9b1_fk_default_usuario_id_usuario` (`id_usuario_id`),
  KEY `default_usuarioempresa_b952c8d6` (`id_visao_id`),
  CONSTRAINT `default_usuarioem_id_visao_id_0f5aa673_fk_default_visao_id_visao` FOREIGN KEY (`id_visao_id`) REFERENCES `default_visao` (`id_visao`),
  CONSTRAINT `default_usu_id_empresa_id_3913a4e0_fk_default_empresa_id_empresa` FOREIGN KEY (`id_empresa_id`) REFERENCES `default_empresa` (`id_empresa`),
  CONSTRAINT `default_usu_id_usuario_id_4300c9b1_fk_default_usuario_id_usuario` FOREIGN KEY (`id_usuario_id`) REFERENCES `default_usuario` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_usuarioempresa`
--

LOCK TABLES `default_usuarioempresa` WRITE;
/*!40000 ALTER TABLE `default_usuarioempresa` DISABLE KEYS */;
/*!40000 ALTER TABLE `default_usuarioempresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `default_visao`
--

DROP TABLE IF EXISTS `default_visao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `default_visao` (
  `id_visao` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(45) NOT NULL,
  PRIMARY KEY (`id_visao`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `default_visao`
--

LOCK TABLES `default_visao` WRITE;
/*!40000 ALTER TABLE `default_visao` DISABLE KEYS */;
/*!40000 ALTER TABLE `default_visao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_default_usuario_id_usuario` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_default_usuario_id_usuario` FOREIGN KEY (`user_id`) REFERENCES `default_usuario` (`id_usuario`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-08-12 17:25:21','1','Manual do Proprietário',1,'Adicionado.',6,2),(2,'2016-08-12 17:26:56','1','Manual do Proprietário',2,'Modificado logo.',6,2),(3,'2016-08-12 17:51:04','1','FAX',1,'Adicionado.',16,2),(4,'2016-08-12 17:51:11','2','Comercial',1,'Adicionado.',16,2),(5,'2016-08-12 17:51:20','3','Residencial',1,'Adicionado.',16,2),(6,'2016-08-12 17:51:30','4','Celular',1,'Adicionado.',16,2),(7,'2016-08-12 17:51:37','5','Whatsapp',1,'Adicionado.',16,2),(8,'2016-08-12 17:51:58','1','Feminino',1,'Adicionado.',7,2),(9,'2016-08-12 17:52:03','2','Masculino',1,'Adicionado.',7,2),(10,'2016-08-12 17:52:09','3','Outros',1,'Adicionado.',7,2),(11,'2016-08-12 17:52:36','1','Engenheiro Técnico',1,'Adicionado.',12,2),(12,'2016-08-12 17:52:41','2','Diretor',1,'Adicionado.',12,2),(13,'2016-08-12 17:52:54','3','Administrador',1,'Adicionado.',12,2),(14,'2016-08-12 17:53:11','1','Incorporadora',1,'Adicionado.',10,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(24,'default','documento'),(11,'default','empresa'),(9,'default','endereco'),(7,'default','genero'),(8,'default','logradouro'),(6,'default','projeto'),(22,'default','relacaoempresa'),(23,'default','relacaousuario'),(19,'default','telefoneempresa'),(18,'default','telefoneusuario'),(15,'default','tipodocumento'),(10,'default','tipoempresa'),(13,'default','tiporelacao'),(14,'default','tiporelacaoempresa'),(16,'default','tipotelefone'),(12,'default','tipousuario'),(17,'default','usuario'),(20,'default','usuarioempresa'),(21,'default','visao'),(25,'empresa','startup'),(5,'sessions','session'),(26,'usuario','funcionario');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'default','0001_initial','2016-08-08 20:46:37'),(2,'contenttypes','0001_initial','2016-08-08 20:46:37'),(3,'admin','0001_initial','2016-08-08 20:46:37'),(4,'admin','0002_logentry_remove_auto_add','2016-08-08 20:46:37'),(5,'contenttypes','0002_remove_content_type_name','2016-08-08 20:46:37'),(6,'auth','0001_initial','2016-08-08 20:46:38'),(7,'auth','0002_alter_permission_name_max_length','2016-08-08 20:46:38'),(8,'auth','0003_alter_user_email_max_length','2016-08-08 20:46:38'),(9,'auth','0004_alter_user_username_opts','2016-08-08 20:46:38'),(10,'auth','0005_alter_user_last_login_null','2016-08-08 20:46:38'),(11,'auth','0006_require_contenttypes_0002','2016-08-08 20:46:38'),(12,'auth','0007_alter_validators_add_error_messages','2016-08-08 20:46:38'),(13,'sessions','0001_initial','2016-08-08 20:46:38'),(14,'default','0002_auto_20160812_1717','2016-08-12 17:17:43'),(15,'empresa','0001_initial','2016-08-12 17:17:43'),(16,'usuario','0001_initial','2016-08-12 17:17:43');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('cp8n1tjutloxg19hksn8gjzouhs9c5zy','MzkyZmJlNWIzOGJjMjIzYWFjZWNlZTQwYTlkYWNiNTRjODQxZjRlNDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9oYXNoIjoiMDQ2ODU4MGRhM2I5ZWEyN2JlN2I0YWFlYzAzMGMxMDY1ZWYxY2ZmMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2016-08-26 17:23:38');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empresa_startup`
--

DROP TABLE IF EXISTS `empresa_startup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `empresa_startup` (
  `id_startup` int(11) NOT NULL AUTO_INCREMENT,
  `representante` varchar(150) DEFAULT NULL,
  `logo` varchar(100) DEFAULT NULL,
  `empresa_id` int(11) NOT NULL,
  PRIMARY KEY (`id_startup`),
  UNIQUE KEY `empresa_id` (`empresa_id`),
  CONSTRAINT `empresa_startu_empresa_id_5fe7cf15_fk_default_empresa_id_empresa` FOREIGN KEY (`empresa_id`) REFERENCES `default_empresa` (`id_empresa`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empresa_startup`
--

LOCK TABLES `empresa_startup` WRITE;
/*!40000 ALTER TABLE `empresa_startup` DISABLE KEYS */;
/*!40000 ALTER TABLE `empresa_startup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_funcionario`
--

DROP TABLE IF EXISTS `usuario_funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario_funcionario` (
  `id_funcionario` int(11) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(20) DEFAULT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id_funcionario`),
  UNIQUE KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `usuario_funcio_usuario_id_44a7e0b9_fk_default_usuario_id_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `default_usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_funcionario`
--

LOCK TABLES `usuario_funcionario` WRITE;
/*!40000 ALTER TABLE `usuario_funcionario` DISABLE KEYS */;
INSERT INTO `usuario_funcionario` VALUES (1,'8171827',3);
/*!40000 ALTER TABLE `usuario_funcionario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-08-12 15:19:28
