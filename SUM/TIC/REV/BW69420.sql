-- phpMyAdmin SQL Dump
-- version 2.9.1.1
-- http://www.phpmyadmin.net
-- 
-- Host: localhost
-- Generation Time: Apr 29, 2022 at 12:08 AM
-- Server version: 5.0.27
-- PHP Version: 5.2.0
-- 
-- Database: `BW69420`
-- 

-- --------------------------------------------------------

-- 
-- Table structure for table `client`
-- 

CREATE TABLE `client` (
  `tel` varchar(8) NOT NULL,
  `nom` varchar(25) NOT NULL,
  `prenom` varchar(25) NOT NULL,
  `adresse` varchar(100) NOT NULL,
  `motpass` varchar(6) NOT NULL,
  PRIMARY KEY  (`tel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `client`
-- 


-- --------------------------------------------------------

-- 
-- Table structure for table `commande`
-- 

CREATE TABLE `commande` (
  `idpizza` varchar(3) NOT NULL,
  `tel` varchar(8) NOT NULL,
  `datecmd` datetime NOT NULL,
  `qtecmd` int(11) NOT NULL,
  PRIMARY KEY  (`idpizza`,`tel`,`datecmd`),
  KEY `tel` (`tel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `commande`
-- 


-- --------------------------------------------------------

-- 
-- Table structure for table `pizza`
-- 

CREATE TABLE `pizza` (
  `idpizza` varchar(3) NOT NULL,
  `nompizza` varchar(30) NOT NULL,
  `details` varchar(200) NOT NULL,
  `prix` decimal(6,3) NOT NULL,
  PRIMARY KEY  (`idpizza`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `pizza`
-- 

INSERT INTO `pizza` (`idpizza`, `nompizza`, `details`, `prix`) VALUES 
('Fmr', 'Fruit de mer', 'Tomate,Mozzarella,Fruits de mer', 18.500),
('Mgh', 'Margherita', 'Tomate,Mozzarella,Basilic', 8.000),
('Nap', 'Napolitaine', 'Tomate,Mozzarella,Thon,Anchois', 12.000),
('Nep', 'Neptune', 'Tomate,Mozzarella,Thon', 10.500),
('Roy', 'Royale', 'Tomate,Mozzarella,Jambon,Champignon', 14.500);

-- 
-- Constraints for dumped tables
-- 

-- 
-- Constraints for table `commande`
-- 
ALTER TABLE `commande`
  ADD CONSTRAINT `commande_ibfk_2` FOREIGN KEY (`tel`) REFERENCES `client` (`tel`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `commande_ibfk_1` FOREIGN KEY (`idpizza`) REFERENCES `pizza` (`idpizza`) ON DELETE CASCADE ON UPDATE CASCADE;
