-- phpMyAdmin SQL Dump
-- version 2.9.1.1
-- http://www.phpmyadmin.net
-- 
-- Host: localhost
-- Generation Time: Jan 21, 2022 at 10:58 AM
-- Server version: 5.0.27
-- PHP Version: 5.2.0
-- 
-- Database: `bdsialaabarka`
-- 

-- --------------------------------------------------------

-- 
-- Table structure for table `abonne`
-- 

CREATE TABLE `abonne` (
  `codeabonne` varchar(4) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(20) NOT NULL,
  `adresse` varchar(50) NOT NULL,
  `codepostale` int(4) NOT NULL,
  `age` int(2) NOT NULL,
  `genre` enum('M','F') NOT NULL default 'M',
  PRIMARY KEY  (`codeabonne`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `abonne`
-- 

INSERT INTO `abonne` (`codeabonne`, `nom`, `prenom`, `adresse`, `codepostale`, `age`, `genre`) VALUES 
('A001', 'Saleh', 'Ali', 'Gafsa', 2100, 0, 'M'),
('A002', 'Mahmoudi', 'Jamel', 'Touzir', 2123, 0, 'M'),
('A003', 'Brahim', 'Hela', 'Sousse', 3112, 0, 'F');

-- --------------------------------------------------------

-- 
-- Table structure for table `livre`
-- 

CREATE TABLE `livre` (
  `codelivre` int(4) NOT NULL,
  `titre` varchar(100) NOT NULL,
  `auteur` enum('claude duigo','eric sarrion','christine berhardt') NOT NULL,
  `annee` varchar(4) NOT NULL,
  `nbrpage` int(3) NOT NULL,
  PRIMARY KEY  (`codelivre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `livre`
-- 

INSERT INTO `livre` (`codelivre`, `titre`, `auteur`, `annee`, `nbrpage`) VALUES 
(1000, 'Travaux pratique World', 'christine berhardt', '2022', 128),
(1001, 'Travaux pratiqure PowerPoint', 'christine berhardt', '2020', 128),
(1002, 'VBA pour Excel', 'claude duigo', '2021', 406),
(1003, 'Excel 2016', 'claude duigo', '2016', 765),
(1004, 'React.js', 'eric sarrion', '2019', 348);

-- --------------------------------------------------------

-- 
-- Table structure for table `prets`
-- 

CREATE TABLE `prets` (
  `numpret` int(3) NOT NULL auto_increment,
  `datepret` date NOT NULL,
  `duree` int(3) NOT NULL default '1',
  `codelivre` int(4) NOT NULL,
  `codeabonne` varchar(4) NOT NULL,
  PRIMARY KEY  (`numpret`),
  KEY `codeabonne` (`codeabonne`),
  KEY `codelivre` (`codelivre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

-- 
-- Dumping data for table `prets`
-- 

INSERT INTO `prets` (`numpret`, `datepret`, `duree`, `codelivre`, `codeabonne`) VALUES 
(1, '2021-02-06', 1, 1002, 'A003'),
(2, '2021-03-15', 5, 1004, 'A003'),
(3, '0000-00-00', 4, 1000, 'A001'),
(4, '2021-03-01', 9, 1002, 'A002');

-- 
-- Constraints for dumped tables
-- 

-- 
-- Constraints for table `prets`
-- 
ALTER TABLE `prets`
  ADD CONSTRAINT `prets_ibfk_2` FOREIGN KEY (`codeabonne`) REFERENCES `abonne` (`codeabonne`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `prets_ibfk_1` FOREIGN KEY (`codelivre`) REFERENCES `livre` (`codelivre`) ON DELETE CASCADE ON UPDATE CASCADE;
