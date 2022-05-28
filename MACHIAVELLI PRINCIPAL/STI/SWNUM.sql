-- phpMyAdmin SQL Dump
-- version 2.9.1.1
-- http://www.phpmyadmin.net
-- 
-- Host: localhost
-- Generation Time: May 28, 2022 at 12:02 PM
-- Server version: 5.0.27
-- PHP Version: 5.2.0
-- 
-- Database: `SWNUM`
-- 

-- --------------------------------------------------------

-- 
-- Table structure for table `evaluation`
-- 

CREATE TABLE `evaluation` (
  `numPermis` varchar(8) NOT NULL,
  `idModele` int(11) NOT NULL,
  `dateTest` datetime NOT NULL,
  `seurite` int(11) NOT NULL,
  `conduite` int(11) NOT NULL,
  `confort` int(11) NOT NULL,
  PRIMARY KEY  (`numPermis`,`idModele`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `evaluation`
-- 


-- --------------------------------------------------------

-- 
-- Table structure for table `modelevoiture`
-- 

CREATE TABLE `modelevoiture` (
  `idModele` int(11) NOT NULL,
  `libelle` varchar(20) NOT NULL,
  PRIMARY KEY  (`idModele`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `modelevoiture`
-- 

INSERT INTO `modelevoiture` (`idModele`, `libelle`) VALUES 
(15, 'WALLYS IRIS'),
(26, 'WALLYS 619'),
(38, 'WALLYS 216');

-- --------------------------------------------------------

-- 
-- Table structure for table `testeur`
-- 

CREATE TABLE `testeur` (
  `numPermis` varchar(8) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `prenom` char(20) NOT NULL,
  `genre` varchar(1) NOT NULL,
  PRIMARY KEY  (`numPermis`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `testeur`
-- 

INSERT INTO `testeur` (`numPermis`, `nom`, `prenom`, `genre`) VALUES 
('21/12345', 'Brini', 'Samir', 'M'),
('33/44444', 'Zaghdane', 'Olfa', 'F'),
('58/98765', 'Krimi', 'Fethi', 'M');
