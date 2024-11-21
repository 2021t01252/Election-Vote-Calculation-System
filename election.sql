-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 14, 2023 at 06:24 PM
-- Server version: 10.1.35-MariaDB
-- PHP Version: 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `election`
--

-- --------------------------------------------------------

--
-- Table structure for table `candidate`
--

CREATE TABLE `candidate` (
  `can_id` int(50) NOT NULL,
  `nic` varchar(100) NOT NULL,
  `name` varchar(200) NOT NULL,
  `age` int(5) NOT NULL,
  `education` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `poli_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `candidate`
--

INSERT INTO `candidate` (`can_id`, `nic`, `name`, `age`, `education`, `state`, `poli_id`) VALUES
(7, '696072325', 'Jinendrika Wijekoon', 55, 'GCE A/L', 'Kurunegala', '5'),
(8, '200126903651', 'Bawantha', 22, 'BSC', 'Kandy', '5');

-- --------------------------------------------------------

--
-- Table structure for table `citizen`
--

CREATE TABLE `citizen` (
  `nic` varchar(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `age` int(5) NOT NULL,
  `state` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `citizen`
--

INSERT INTO `citizen` (`nic`, `name`, `age`, `state`) VALUES
('200126903651', 'Bawantha', 22, 'Kandy'),
('196530510049', 'Namal Wijekoon', 26, 'Kandy'),
('696072325v', 'Jinendrika Wijekoon', 55, 'Kurunegala');

-- --------------------------------------------------------

--
-- Table structure for table `poli_party`
--

CREATE TABLE `poli_party` (
  `poli_id` int(20) NOT NULL,
  `poli_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `poli_party`
--

INSERT INTO `poli_party` (`poli_id`, `poli_name`) VALUES
(5, 'JVP');

-- --------------------------------------------------------

--
-- Table structure for table `voting`
--

CREATE TABLE `voting` (
  `nic` varchar(50) NOT NULL,
  `vote1` int(20) NOT NULL,
  `vote2` int(20) NOT NULL,
  `vote3` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `voting`
--

INSERT INTO `voting` (`nic`, `vote1`, `vote2`, `vote3`) VALUES
('200126903651', 7, 8, 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `candidate`
--
ALTER TABLE `candidate`
  ADD PRIMARY KEY (`can_id`);

--
-- Indexes for table `poli_party`
--
ALTER TABLE `poli_party`
  ADD PRIMARY KEY (`poli_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `candidate`
--
ALTER TABLE `candidate`
  MODIFY `can_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `poli_party`
--
ALTER TABLE `poli_party`
  MODIFY `poli_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
