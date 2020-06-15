-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- 主機: 127.0.0.1
-- 產生時間： 2018 年 11 月 28 日 14:10
-- 伺服器版本: 10.1.36-MariaDB
-- PHP 版本： 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `pos`
--

-- --------------------------------------------------------

--
-- 資料表結構 `customer`
--

CREATE TABLE `customer` (
  `cr_ID` int(8) NOT NULL,
  `cr_firstName` varchar(30) COLLATE utf8_bin NOT NULL,
  `cr_lastName` varchar(30) COLLATE utf8_bin NOT NULL,
  `cr_Username` varchar(20) COLLATE utf8_bin NOT NULL,
  `cr_Password` varchar(20) COLLATE utf8_bin NOT NULL,
  `cr_Email` varchar(30) COLLATE utf8_bin NOT NULL,
  `cr_phoneNO` int(8) NOT NULL,
  `shopping_point` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 資料表的匯出資料 `customer`
--

INSERT INTO `customer` (`cr_ID`, `cr_firstName`, `cr_lastName`, `cr_Username`, `cr_Password`, `cr_Email`, `cr_phoneNO`, `shopping_point`) VALUES
(20180001, 'lam', 'tai man', 'hi123', '12345678', 'ok1@gmail.com', 12345678, 0),
(20180002, 'li', 'tai man', 'man123', '99999999', 'man123@kmail.com', 99999999, 0),
(20180003, 'yo', 'yo yo', 'tai123', '87778777', 'tai123@gg.com', 87778777, 3),
(20180004, 'ng', 'fun', 'fun111', '86868686', 'fun111@er.com', 86868686, 0),
(20180005, 'wong', 'tai sin', 'god', '66666666', 'god@god.com', 66666666, 2),
(20180006, 'chan', 'tom', 'tom123', '78912345', 'tom123@hello.com', 78912345, 0),
(20180007, 'li', 'vin', 'AppleINC', 't31285362', 'vincent@apple.com', 97218289, 6),
(20180008, 'm', 'mky', 'm.mky', 'iamrich', 'mmky@richclub.com', 69020826, 15),
(20180011, 'panda', 'eric', 'PandaEric', 'uhgu434', 'hi_im_eric@pandamail.com', 51105554, 0);

-- --------------------------------------------------------

--
-- 資料表結構 `products`
--

CREATE TABLE `products` (
  `pd_ID` varchar(4) COLLATE utf8_bin NOT NULL,
  `pd_Name` varchar(40) COLLATE utf8_bin NOT NULL,
  `pd_Brand` varchar(20) COLLATE utf8_bin NOT NULL,
  `pd_Type` varchar(15) COLLATE utf8_bin NOT NULL,
  `pd_Rom` int(3) NOT NULL,
  `pd_Price` int(6) NOT NULL,
  `pd_Stock` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 資料表的匯出資料 `products`
--

INSERT INTO `products` (`pd_ID`, `pd_Name`, `pd_Brand`, `pd_Type`, `pd_Rom`, `pd_Price`, `pd_Stock`) VALUES
('A01', 'iPhone 6s plus', 'Apple', 'Smartphone', 32, 4688, 5),
('A02', 'iPhone 6s plus', 'Apple', 'Smartphone', 128, 5588, 4),
('A03', 'iPhone 7', 'Sony', 'Smartphone', 32, 4688, 3),
('A04', 'iPhone 7', 'Apple', 'Smartphone', 128, 5588, 2),
('A05', 'iPhone 7 plus', 'Apple', 'Smartphone', 32, 5788, 2),
('A06', 'iPhone 7 plus', 'Apple', 'Smartphone', 128, 6688, 3),
('A07', 'iPhone 8', 'Apple', 'Smartphone', 64, 5988, 6),
('A08', 'iPhone 8', 'Apple', 'Smartphone', 256, 7288, 5),
('A09', 'iPhone 8 plus', 'Apple', 'Smartphone', 64, 6888, 6),
('A10', 'iPhone 8 plus', 'Apple', 'Smartphone', 256, 8188, 6),
('A11', 'iPhone X', 'Apple', 'Smartphone', 64, 8588, 10),
('A12', 'iPhone X', 'Apple', 'Smartphone', 256, 9888, 14),
('AS01', 'zenfone 4', 'ASUS', 'Smartphone', 128, 3798, 4),
('AS02', 'zenfone 4 Max Pro', 'ASUS', 'Smartphone', 64, 1798, 2),
('HT01', 'U Ultra ', 'HTC', 'Smartphone', 64, 4988, 4),
('HT02', 'U play', 'HTC', 'Smartphone', 32, 1798, 2),
('LG01', 'V30+', 'LG', 'Smartphone', 64, 5698, 4),
('NK01', '3310 4G', 'Nokia', 'Phone', 4, 598, 20),
('SA01', 'Galaxy S8', 'Samsung', 'Smartphone', 64, 5698, 3),
('SA02', 'Galaxy S8+', 'Samsung', 'Smartphone', 64, 6398, 4),
('SA03', 'Galaxy S8+', 'Samsung', 'Smartphone', 128, 6998, 3),
('SA04', 'Galaxy note 8', 'Samsung', 'Smartphone', 64, 6998, 2),
('SA05', 'Galaxy note 8', 'Samsung', 'Smartphone', 128, 7598, 5),
('SA06', 'Galaxy note 8', 'Samsung', 'Smartphone', 256, 8198, 8),
('SA07', 'Galaxy S9', 'Samsung', 'Smartphone', 64, 6398, 6),
('SA08', 'Galaxy S9+', 'Samsung', 'Smartphone', 128, 7298, 7),
('SA09', 'Galaxy S9+', 'Samsung', 'Smartphone', 256, 8398, 5),
('SA10', 'Galaxy A8+', 'Samsung', 'Smartphone', 64, 4398, 10),
('SN01', 'Xperia XZ Premium', 'Sony', 'Smartphone', 64, 4698, 4),
('SN02', 'Xperia XZ2   ', 'Sony', 'Smartphone', 128, 7898, 5);

-- --------------------------------------------------------

--
-- 資料表結構 `smartphone`
--

CREATE TABLE `smartphone` (
  `pd_Type` varchar(8) COLLATE utf8_bin NOT NULL,
  `pd_Color` varchar(20) COLLATE utf8_bin NOT NULL,
  `pd_Description` varchar(100) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- 資料表結構 `staff`
--

CREATE TABLE `staff` (
  `sf_ID` int(8) NOT NULL,
  `sf_firstName` varchar(30) COLLATE utf8_bin NOT NULL,
  `sf_lastName` varchar(30) COLLATE utf8_bin NOT NULL,
  `sf_Username` varchar(20) COLLATE utf8_bin NOT NULL,
  `sf_Birthday` date NOT NULL,
  `sf_Password` varchar(20) COLLATE utf8_bin NOT NULL,
  `sf_Email` varchar(50) COLLATE utf8_bin NOT NULL,
  `sf_Address` text COLLATE utf8_bin NOT NULL,
  `sf_phoneNO` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 資料表的匯出資料 `staff`
--

INSERT INTO `staff` (`sf_ID`, `sf_firstName`, `sf_lastName`, `sf_Username`, `sf_Birthday`, `sf_Password`, `sf_Email`, `sf_Address`, `sf_phoneNO`) VALUES
(12340001, 'Wong', 'Kenton', 'kenton', '1997-03-01', '12345678', 'kenton@gmail.com', '112road,Hong Kong', 98765432),
(12340002, 'Poon', 'Eric', 'eric', '1998-01-01', '87654321', 'eric@gmail.com', '1233 road, Hong Kong', 97654321),
(12340003, 'Tsui', 'Jason', 'jason', '1999-02-01', '11111111', 'jason@gmail.com', '111 road', 55555555),
(12340004, 'Yuen', 'Ambrose', 'ambrose', '1999-04-01', '22334455', 'ambrose@gmail.com', '2345 road', 66666666);

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`cr_ID`);

--
-- 資料表索引 `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`pd_ID`),
  ADD UNIQUE KEY `pd_ID` (`pd_ID`),
  ADD KEY `pd_Type` (`pd_Type`),
  ADD KEY `pd_ID_2` (`pd_ID`);

--
-- 資料表索引 `smartphone`
--
ALTER TABLE `smartphone`
  ADD KEY `pd_Type` (`pd_Type`);

--
-- 資料表索引 `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`sf_ID`);

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `customer`
--
ALTER TABLE `customer`
  MODIFY `cr_ID` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20180012;

--
-- 已匯出資料表的限制(Constraint)
--

--
-- 資料表的 Constraints `smartphone`
--
ALTER TABLE `smartphone`
  ADD CONSTRAINT `smartphone_ibfk_1` FOREIGN KEY (`pd_Type`) REFERENCES `products` (`pd_Type`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
