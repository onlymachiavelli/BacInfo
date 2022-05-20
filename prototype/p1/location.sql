-- phpMyAdmin SQL Dump
-- version 2.9.1.1
-- http://www.phpmyadmin.net
-- 
-- Host: localhost
-- Generation Time: May 18, 2022 at 05:45 PM
-- Server version: 5.0.27
-- PHP Version: 5.2.0
-- 
-- Database: `location`
-- 

-- --------------------------------------------------------

-- 
-- Table structure for table `client`
-- 

CREATE TABLE `client` (
  `Ncin` varchar(8) NOT NULL,
  `Nom` varchar(30) NOT NULL,
  `Prenom` varchar(30) NOT NULL,
  `Tel` varchar(8) NOT NULL,
  PRIMARY KEY  (`Ncin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `client`
-- 

INSERT INTO `client` (`Ncin`, `Nom`, `Prenom`, `Tel`) VALUES 
('11111111', 'Abidi', 'Anis', '99999999'),
('11111122', 'Louiz', 'Radhia', '88888888');

-- --------------------------------------------------------

-- 
-- Table structure for table `louer`
-- 

CREATE TABLE `louer` (
  `Ncin` varchar(8) NOT NULL,
  `Imat` varchar(9) NOT NULL,
  `DateLoc` datetime NOT NULL,
  `DateRet` datetime NOT NULL default '2000-01-01 00:00:00',
  PRIMARY KEY  (`Ncin`,`Imat`,`DateLoc`),
  KEY `Imat` (`Imat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `louer`
-- 

INSERT INTO `louer` (`Ncin`, `Imat`, `DateLoc`, `DateRet`) VALUES 
('11111111', '250TU3998', '2021-05-01 00:00:00', '2021-05-04 00:00:00'),
('11111111', '251TU8721', '2022-01-31 00:00:00', '2000-01-01 00:00:00'),
('11111122', '254TU352', '2022-01-14 00:00:00', '2000-01-01 00:00:00');

-- --------------------------------------------------------

-- 
-- Table structure for table `voiture`
-- 

CREATE TABLE `voiture` (
  `Imat` varchar(9) NOT NULL,
  `Model` varchar(20) NOT NULL,
  `PrixLoc` int(11) NOT NULL,
  `Disponible` varchar(1) NOT NULL,
  PRIMARY KEY  (`Imat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `voiture`
-- 

INSERT INTO `voiture` (`Imat`, `Model`, `PrixLoc`, `Disponible`) VALUES 
('250TU3998', 'CLIO', 90, 'D'),
('251TU8721', 'Q8', 300, 'N'),
('254TU352', 'RIO', 100, 'N');

-- 
-- Constraints for dumped tables
-- 

-- 
-- Constraints for table `louer`
-- 
ALTER TABLE `louer`
  ADD CONSTRAINT `louer_ibfk_2` FOREIGN KEY (`Imat`) REFERENCES `voiture` (`Imat`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `louer_ibfk_1` FOREIGN KEY (`Ncin`) REFERENCES `client` (`Ncin`) ON DELETE CASCADE ON UPDATE CASCADE;
