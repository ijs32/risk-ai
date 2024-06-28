CREATE TABLE `continents` (
    `continent_id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `troop_bonus` int(11) NOT NULL,
    PRIMARY KEY (`continent_id`)
)

INSERT INTO `continents` (`name`, `troop_bonus`) VALUES
('Oceania', 2),
('Asia', 7),
('Africa', 3),
('Europe', 5),
('North America', 5),
('South America', 2)