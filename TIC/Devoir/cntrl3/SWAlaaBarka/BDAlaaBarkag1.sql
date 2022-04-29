-- phpMyAdmin SQL Dump
-- version 2.9.1.1
-- http://www.phpmyadmin.net
-- 
-- Host: localhost
-- Generation Time: Apr 29, 2022 at 10:58 AM
-- Server version: 5.0.27
-- PHP Version: 5.2.0
-- 
-- Database: `BDAlaaBarkag1`
-- 

-- --------------------------------------------------------

-- 
-- Table structure for table `musicien`
-- 

CREATE TABLE `musicien` (
  `id_musicien` varchar(5) NOT NULL,
  `nom` varchar(30) NOT NULL,
  `prenom` varchar(30) NOT NULL,
  `age` int(2) NOT NULL,
  `instrument` varchar(20) NOT NULL,
  PRIMARY KEY  (`id_musicien`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Dumping data for table `musicien`
-- 

INSERT INTO `musicien` (`id_musicien`, `nom`, `prenom`, `age`, `instrument`) VALUES 
('M1111', 'Ben Salem', 'Salah', 43, 'Violon'),
('M2222', 'Rhouma', 'Intissar', 15, 'Piano'),
('M3333', 'Ahmadi', 'Hela', 32, 'Accordeon');
