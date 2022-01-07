-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 07, 2022 at 08:53 AM
-- Server version: 5.7.17
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `eleve`
--

-- --------------------------------------------------------

--
-- Table structure for table `classes`
--

CREATE TABLE `classes` (
  `ID` int(11) NOT NULL,
  `class` varchar(300) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `classes`
--

INSERT INTO `classes` (`ID`, `class`) VALUES
(1, '1ERE'),
(2, '2eme Lettre'),
(3, '2eme Science'),
(4, '2eme Info'),
(5, '2eme Eco'),
(6, '3eme Lettre'),
(7, '3eme Science'),
(8, '3eme Info'),
(9, '3eme Eco'),
(10, '3eme Math'),
(11, '3eme Technique'),
(12, '4eme Lettre'),
(13, '4eme Science'),
(14, '4eme Info'),
(15, '4eme Eco'),
(16, '4eme Technique'),
(17, '4eme Math');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ID` int(11) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `cin` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `password` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `adress` varchar(600) NOT NULL,
  `hobb` varchar(3) NOT NULL,
  `image` varchar(300) DEFAULT NULL,
  `creationdate` varchar(200) DEFAULT NULL,
  `class` varchar(200) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `fullname`, `cin`, `date`, `password`, `gender`, `email`, `phone`, `adress`, `hobb`, `image`, `creationdate`, `class`) VALUES
(8, 'Alaa Barka', '14524725', '2002-07-04', 'azerty', 'male', 'tmakaveli643@gmail.com', '54324884', '24 wadhraf', '000', 'assets/uploads/pizzargl.png', '2021.10.01', '4eme Info'),
(7, 'Oussema Boukeri', '112233', '2021-10-07', 'azerty', 'female', 'tmakaveli643@gmail.com', '911', '24 wadhraf', '000', 'assets/uploads/pizzargl.png', '2021.10.01', '4eme Info');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `classes`
--
ALTER TABLE `classes`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `class` (`class`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `classes`
--
ALTER TABLE `classes`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
