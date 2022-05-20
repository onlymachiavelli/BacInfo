-- phpMyAdmin SQL Dump
-- version 2.9.1.1
-- http://www.phpmyadmin.net
-- 
-- Host: localhost
-- Generation Time: May 20, 2022 at 12:36 PM
-- Server version: 5.0.27
-- PHP Version: 5.2.0
-- 
-- Database: `bac2018`
-- 

-- --------------------------------------------------------

-- 
-- Table structure for table `evaluation`
-- 

CREATE TABLE `evaluation` (
  `DateEval` date NOT NULL,
  `IdHotel` int(11) NOT NULL,
  `NoteAcceuil` int(11) NOT NULL,
  `NoteRest` int(11) NOT NULL,
  `NoteExtra` int(11) NOT NULL,
  PRIMARY KEY  (`DateEval`,`IdHotel`),
  KEY `IdHotel` (`IdHotel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `evaluation`
-- 

INSERT INTO `evaluation` (`DateEval`, `IdHotel`, `NoteAcceuil`, `NoteRest`, `NoteExtra`) VALUES 
('2017-05-22', 10, 3, 1, 0),
('2017-06-15', 20, 3, 2, 2),
('2017-06-15', 30, 2, 1, 2),
('2018-02-20', 10, 2, 1, 1),
('2018-04-13', 30, 2, 2, 7);

-- --------------------------------------------------------

-- 
-- Table structure for table `hotel`
-- 

CREATE TABLE `hotel` (
  `IdHotel` int(11) NOT NULL,
  `NomHotel` varchar(50) NOT NULL,
  `TelHotel` varchar(8) NOT NULL,
  `VilleHotel` varchar(30) NOT NULL,
  PRIMARY KEY  (`IdHotel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `hotel`
-- 

INSERT INTO `hotel` (`IdHotel`, `NomHotel`, `TelHotel`, `VilleHotel`) VALUES 
(10, '5 Stars', '76333444', 'Tozeur'),
(20, 'Globe', '78111111', 'Tabarka'),
(30, 'The Sun', '73888888', 'Monastir');

-- 
-- Constraints for dumped tables
-- 

-- 
-- Constraints for table `evaluation`
-- 
ALTER TABLE `evaluation`
  ADD CONSTRAINT `evaluation_ibfk_1` FOREIGN KEY (`IdHotel`) REFERENCES `hotel` (`IdHotel`) ON DELETE CASCADE ON UPDATE CASCADE;
