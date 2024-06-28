CREATE TABLE `territories` (
    `territory_id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `continent_id` varchar(255) NOT NULL,
    PRIMARY KEY (`territory_id`),
    FOREIGN KEY (`continent_id`) REFERENCES `continents` (`continent_id`)
)

ALTER TABLE territories ADD continent_id int(11) NOT NULL FOREIGN KEY REFERENCES continents(continent_id)
INSERT INTO `territories` (`name`, `continent`) VALUES
-- Oceania
('Indonesia', 'Oceania'),
('New Guinea', 'Oceania'),
('Western Australia', 'Oceania'),
('Eastern Australia', 'Oceania'),
-- Asia
('China', 'Asia'),
('India', 'Asia'),
('Siam', 'Asia'),
('Mongolia', 'Asia'),
('Japan', 'Asia'),
('Irkutsk', 'Asia'),
('Kamchatka', 'Asia'),
('Siberia', 'Asia'),
('Afghanistan', 'Asia'),
('Ural', 'Asia'),
('Middle East', 'Asia'),
('Yakutsk', 'Asia'),
-- Africa
('North Africa', 'Africa'),
('Egypt', 'Africa'),
('Congo', 'Africa'),
('South Africa', 'Africa'),
('East Africa', 'Africa'),
('Madagascar', 'Africa'),
-- Europe
('Iceland', 'Europe'),
('Scandinavia', 'Europe'),
('Ukraine', 'Europe'),
('Western Europe', 'Europe'),
('Great Britain', 'Europe'),
('Northern Europe', 'Europe'),
('Southern Europe', 'Europe'),
-- North America
('Alaska', 'North America')
('Northwest Territory', 'North America')
('Greenland', 'North America')
('Alberta', 'North America')
('Ontario', 'North America')
('Quebec', 'North America')
('Western United States', 'North America')
('Eastern United States', 'North America')
('Central America', 'North America')
-- South America
('Venezuela', 'South America')
('Peru', 'South America')
('Brazil', 'South America')
('Argentina', 'South America')