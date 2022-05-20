-- phpMyAdmin SQL Dump
-- version 2.9.1.1
-- http://www.phpmyadmin.net
-- 
-- Host: localhost
-- Generation Time: Apr 25, 2022 at 03:03 PM
-- Server version: 5.0.27
-- PHP Version: 5.2.0
-- 
-- Database: `bac2021`
-- 

-- --------------------------------------------------------

-- 
-- Table structure for table `mesure`
-- 

CREATE TABLE `mesure` (
  `Idstation` int(11) NOT NULL,
  `Annee` int(11) NOT NULL,
  `Saison` varchar(9) NOT NULL,
  `Temperature` decimal(5,2) NOT NULL,
  `Pluie` int(11) NOT NULL,
  PRIMARY KEY  (`Idstation`,`Annee`,`Saison`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `mesure`
-- 

INSERT INTO `mesure` (`Idstation`, `Annee`, `Saison`, `Temperature`, `Pluie`) VALUES 
(60715, 2018, 'Ete', 30.60, 24),
(60715, 2018, 'Hiver', 13.50, 150),
(60715, 2019, 'Printemps', 25.60, 80),
(60731, 2018, 'Ete', 33.60, 10),
(60731, 2018, 'Hiver', 17.60, 100),
(60731, 2019, 'Automne', 30.00, 11),
(60780, 2019, 'Ete', 42.30, 0),
(60780, 2019, 'Hiver', 16.60, 10);

-- --------------------------------------------------------

-- 
-- Table structure for table `station`
-- 

CREATE TABLE `station` (
  `Idstation` int(11) NOT NULL,
  `Nom` varchar(30) NOT NULL,
  `Ville` varchar(30) NOT NULL,
  PRIMARY KEY  (`Idstation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `station`
-- 

INSERT INTO `station` (`Idstation`, `Nom`, `Ville`) VALUES 
(60715, 'Carthage', 'Tunis'),
(60731, 'Enfidha-Aeropot', 'Sousse'),
(60780, 'El-Borma', 'Tataouine');
