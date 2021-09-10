DROP TABLE IF EXISTS `cars`;
CREATE TABLE IF NOT EXISTS `cars` (
  `car_id` int(7) DEFAULT NULL,
  `maker` varchar(13) DEFAULT NULL,
  `model` varchar(18) DEFAULT NULL,
  `mileage` decimal(8,1) DEFAULT NULL,
  `manufacture_year` decimal(5,1) DEFAULT NULL,
  `engine_displacement` decimal(5,1) DEFAULT NULL,
  `engine_power` decimal(4,1) DEFAULT NULL,
  `color_slug` varchar(6) DEFAULT NULL,
  `transmission` varchar(4) DEFAULT NULL,
  `door_count` decimal(2,1) DEFAULT NULL,
  `seat_count` decimal(2,1) DEFAULT NULL,
  `fuel_type` varchar(8) DEFAULT NULL,
  `price_eur` decimal(7,0) DEFAULT NULL
);
