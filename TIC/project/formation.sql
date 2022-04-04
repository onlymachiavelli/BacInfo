-- phpMyAdmin SQL Dump
-- version 2.9.1.1
-- http://www.phpmyadmin.net
-- 
-- Host: localhost
-- Generation Time: Apr 01, 2022 at 11:20 AM
-- Server version: 5.0.27
-- PHP Version: 5.2.0
-- 
-- Database: `formation`
-- 

-- --------------------------------------------------------

-- 
-- Table structure for table `condidat`
-- 

CREATE TABLE `condidat` (
  `id` int(4) NOT NULL auto_increment,
  `nom` varchar(20) NOT NULL,
  `prenom` varchar(20) NOT NULL,
  `genre` enum('M','F') NOT NULL,
  `email` varchar(50) NOT NULL,
  `bac` varchar(10) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;
 
-- 
-- Dumping data for table `condidat`
-- 

INSERT INTO `condidat` (`id`, `nom`, `prenom`, `genre`, `email`, `bac`) VALUES 
(1, 'Benarab', 'Hedia', 'F', 'hediaben@gmail.com', '4si'),
(2, 'Ghannem', 'Tarek', 'M', 'T_GH@yahoo.fr', '4tech'),
(3, 'Salhi', 'Louay', 'M', 'LouayS@gmail.com', '4si');
