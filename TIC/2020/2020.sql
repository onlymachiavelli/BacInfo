-- phpMyAdmin SQL Dump
-- version 2.9.1.1
-- http://www.phpmyadmin.net
-- 
-- Host: localhost
-- Generation Time: May 22, 2022 at 03:14 PM
-- Server version: 5.0.27
-- PHP Version: 5.2.0
-- 
-- Database: `2020`
-- 

-- --------------------------------------------------------

-- 
-- Table structure for table `client`
-- 

CREATE TABLE `client` (
  `Tel` varchar(8) NOT NULL,
  `Nom` varchar(25) NOT NULL,
  `Prenom` varchar(25) NOT NULL,
  `Adresse` varchar(100) NOT NULL,
  `MotPass` varchar(6) NOT NULL,
  PRIMARY KEY  (`Tel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `client`
-- 


-- --------------------------------------------------------

-- 
-- Table structure for table `commande`
-- 

CREATE TABLE `commande` (
  `IdPizza` varchar(3) NOT NULL,
  `Tel` varchar(8) NOT NULL,
  `DateCmd` datetime NOT NULL,
  `QteCmd` int(11) NOT NULL,
  PRIMARY KEY  (`IdPizza`,`Tel`,`DateCmd`),
  KEY `Tel` (`Tel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `commande`
-- 


-- --------------------------------------------------------

-- 
-- Table structure for table `pizza`
-- 

CREATE TABLE `pizza` (
  `IdPizza` varchar(3) NOT NULL,
  `NomPizza` varchar(30) NOT NULL,
  `Details` varchar(200) NOT NULL,
  `Prix` decimal(6,3) NOT NULL,
  PRIMARY KEY  (`IdPizza`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `pizza`
-- 

INSERT INTO `pizza` (`IdPizza`, `NomPizza`, `Details`, `Prix`) VALUES 
('Fmr', 'Fruit de me Mer', 'Tomate, Mozarella, Fruit de mer', 18.500),
('Mgh', 'Margherita', 'Tomate, Mozarella, Basilic', 8.000),
('Nap', 'Napolitaine', 'Tomate, Mozarella, Thon , Anchois', 12.000),
('Nep', 'Neptune', 'Tomate, Mozarella , Thon', 10.500),
('Roy', 'Royale', 'Tomate, Mozarella, Jambon, Champignon', 14.500);

-- 
-- Constraints for dumped tables
-- 

-- 
-- Constraints for table `commande`
-- 
ALTER TABLE `commande`
  ADD CONSTRAINT `commande_ibfk_2` FOREIGN KEY (`Tel`) REFERENCES `client` (`Tel`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `commande_ibfk_1` FOREIGN KEY (`IdPizza`) REFERENCES `pizza` (`IdPizza`) ON DELETE CASCADE ON UPDATE CASCADE;
