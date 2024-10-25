-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Oct 21, 2024 at 10:22 AM
-- Server version: 5.7.34
-- PHP Version: 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Курсовой_проект`
--

-- --------------------------------------------------------

--
-- Table structure for table `Activities`
--

CREATE TABLE `Activities` (
  `id_activity` int(70) NOT NULL,
  `Activity_name` varchar(50) NOT NULL,
  `Duration` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Holidays`
--

CREATE TABLE `Holidays` (
  `id_holiday` int(70) NOT NULL,
  `Holiday` varchar(255) NOT NULL,
  `Date_start` date NOT NULL,
  `Date_end` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Roles`
--

CREATE TABLE `Roles` (
  `id_role` int(70) NOT NULL,
  `Role_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `id_user` int(70) NOT NULL,
  `Furst_name` varchar(40) NOT NULL,
  `Last_name` varchar(40) NOT NULL,
  `Surname` varchar(40) DEFAULT NULL,
  `Login` varchar(50) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `id_role` int(70) NOT NULL,
  `id_vacation` int(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Weekends`
--

CREATE TABLE `Weekends` (
  `id_weekend` int(70) NOT NULL,
  `Weekend_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Work_time`
--

CREATE TABLE `Work_time` (
  `id_work_time` int(70) NOT NULL,
  `id_user` int(70) NOT NULL,
  `id_activity` int(70) NOT NULL,
  `date` date NOT NULL,
  `time_spent` int(70) NOT NULL,
  `id_holiday` int(70) NOT NULL,
  `id_weekend` int(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Activities`
--
ALTER TABLE `Activities`
  ADD PRIMARY KEY (`id_activity`),
  ADD UNIQUE KEY `id_activity` (`id_activity`);

--
-- Indexes for table `Holidays`
--
ALTER TABLE `Holidays`
  ADD PRIMARY KEY (`id_holiday`),
  ADD UNIQUE KEY `id_holiday` (`id_holiday`);

--
-- Indexes for table `Roles`
--
ALTER TABLE `Roles`
  ADD PRIMARY KEY (`id_role`),
  ADD UNIQUE KEY `id_role` (`id_role`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`id_user`),
  ADD UNIQUE KEY `id_user` (`id_user`),
  ADD UNIQUE KEY `id_vacation` (`id_vacation`),
  ADD KEY `Users_fk6` (`id_role`);

--
-- Indexes for table `Weekends`
--
ALTER TABLE `Weekends`
  ADD PRIMARY KEY (`id_weekend`),
  ADD UNIQUE KEY `id_weekend` (`id_weekend`);

--
-- Indexes for table `Work_time`
--
ALTER TABLE `Work_time`
  ADD PRIMARY KEY (`id_work_time`),
  ADD UNIQUE KEY `id_work_time` (`id_work_time`),
  ADD KEY `Work_time_fk1` (`id_user`),
  ADD KEY `Work_time_fk2` (`id_activity`),
  ADD KEY `Work_time_fk5` (`id_holiday`),
  ADD KEY `Work_time_fk6` (`id_weekend`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Activities`
--
ALTER TABLE `Activities`
  MODIFY `id_activity` int(70) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Holidays`
--
ALTER TABLE `Holidays`
  MODIFY `id_holiday` int(70) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Roles`
--
ALTER TABLE `Roles`
  MODIFY `id_role` int(70) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `id_user` int(70) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Weekends`
--
ALTER TABLE `Weekends`
  MODIFY `id_weekend` int(70) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Work_time`
--
ALTER TABLE `Work_time`
  MODIFY `id_work_time` int(70) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Users`
--
ALTER TABLE `Users`
  ADD CONSTRAINT `Users_fk6` FOREIGN KEY (`id_role`) REFERENCES `Roles` (`id_role`);

--
-- Constraints for table `Work_time`
--
ALTER TABLE `Work_time`
  ADD CONSTRAINT `Work_time_fk1` FOREIGN KEY (`id_user`) REFERENCES `Users` (`id_user`),
  ADD CONSTRAINT `Work_time_fk2` FOREIGN KEY (`id_activity`) REFERENCES `Activities` (`id_activity`),
  ADD CONSTRAINT `Work_time_fk5` FOREIGN KEY (`id_holiday`) REFERENCES `Holidays` (`id_holiday`),
  ADD CONSTRAINT `Work_time_fk6` FOREIGN KEY (`id_weekend`) REFERENCES `Weekends` (`id_weekend`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
