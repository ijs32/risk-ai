CREATE TABLE `edges` (
    `edge_id` int(11) NOT NULL AUTO_INCREMENT,
    `from_territory_id` int(11) NOT NULL,
    `to_territory_id` int(11) NOT NULL,
    PRIMARY KEY (`edge_id`),
    FOREIGN KEY (`from_territory_id`) REFERENCES `territories` (`territory_id`),
    FOREIGN KEY (`to_territory_id`) REFERENCES `territories` (`territory_id`)
)

INSERT INTO `edges` (`from_territory_id`, `to_territory_id`) VALUES
(1, 2), -- indonesia, new guinea
(1, 3), -- indonesia, western australia
(1, 7), -- indonesia, siam

(2, 1), -- new guinea, indonesia
(2, 3), -- new guinea, western australia
(2, 4), -- new guinea, eastern australia

(3, 1), -- western australia, indonesia
(3, 2), -- western australia, new guinea
(3, 4), -- western australia, eastern australia

(4, 2), -- eastern australia, new guinea
(4, 3), -- eastern australia, western australia

(7, 5), -- siam, china
(7, 6), -- siam, india
(7, 1), -- siam, indonesia

(6, 15), -- india, middle east
(6, 7), -- india, siam
(6, 5), -- india, china
(6, 13), -- india, afghanistan

(5, 7), -- china, siam
(5, 6), -- china, india
(5, 13), -- china, afghanistan
(5, 14), -- china, ural
(5, 12), -- china, siberia
(5, 8), -- china, mongolia

(8, 5), -- mongolia, china
(8, 9), -- mongolia, japan
(8, 10), -- mongolia, irkutsk
(8, 11), -- mongolia, kamchatka
(8, 12), -- mongolia, siberia

(9, 8), -- japan, mongolia
(9, 11), -- japan, kamchatka

(10, 8), -- irkutsk, mongolia
(10, 11), -- irkutsk, kamchatka
(10, 12), -- irkutsk, siberia
(10, 42), -- irkutsk, yakutsk

(11, 8), -- kamchatka, mongolia
(11, 9), -- kamchatka, japan
(11, 10), -- kamchatka, irkutsk
(11, 42), -- kamchatka, yakutsk
(11, 29), -- kamchatka, alaska

(12, 8), -- siberia, mongolia
(12, 10), -- siberia, irkutsk
(12, 42), -- siberia, yakutsk
(12, 14), -- siberia, ural
(12, 5), -- siberia, china

(13, 6), -- afghanistan, india
(13, 14), -- afghanistan, ural
(13, 15), -- afghanistan, middle east
(13, 24), -- afghanistan, ukraine
(13, 5), -- afghanistan, china

(14, 13), -- ural, afghanistan
(14, 12), -- ural, siberia
(14, 24), -- ural, ukraine
(14, 5), -- ural, china

(15, 6), -- middle east, india
(15, 13), -- middle east, afghanistan
(15, 24), -- middle east, ukraine
(15, 17), -- middle east, egypt
(15, 20), -- middle east, east africa
(15, 28), -- middle east, southern europe

(42, 10), -- yakutsk, irkutsk
(42, 11), -- yakutsk, kamchatka
(42, 12), -- yakutsk, siberia

(16, 28), -- north africa, southern europe
(16, 25), -- north africa, western europe
(16, 40), -- north africa, brazil
(16, 17), -- north africa, egypt
(16, 20), -- north africa, east africa
(16, 18), -- north africa, congo

(17, 15), -- egypt, middle east
(17, 20), -- egypt, east africa
(17, 16), -- egypt, north africa
(17, 28), -- egypt, southern europe

(18, 16), -- congo, north africa
(18, 20), -- congo, east africa
(18, 19), -- congo, south africa

(19, 18), -- south africa, congo
(19, 20), -- south africa, east africa
(19, 21), -- south africa, madagascar

(20, 16), -- east africa, north africa
(20, 17), -- east africa, egypt
(20, 18), -- east africa, congo
(20, 19), -- east africa, south africa
(20, 21), -- east africa, madagascar
(20, 15), -- east africa, middle east

(21, 19), -- madagascar, south africa
(21, 20), -- madagascar, east africa

(38, 39), -- venezuela, peru
(38, 40), -- venezuela, brazil
(38, 37), -- venezuela, central america

(39, 38), -- peru, venezuela
(39, 40), -- peru, brazil
(39, 41), -- peru, argentina

(40, 38), -- brazil, venezuela
(40, 39), -- brazil, peru
(40, 41), -- brazil, argentina
(40, 16), -- brazil, north africa

(41, 39), -- argentina, peru
(41, 40), -- argentina, brazil

(28, 15), -- southern europe, middle east
(28, 16), -- southern europe, north africa
(28, 17), -- southern europe, egypt
(28, 25), -- southern europe, western europe
(28, 27), -- southern europe, northern europe
(28, 24), -- southern europe, ukraine

(25, 16), -- western europe, north africa
(25, 28), -- western europe, southern europe
(25, 27), -- western europe, northern europe
(25, 26), -- western europe, great britain

(27, 28), -- northern europe, southern europe
(27, 25), -- northern europe, western europe
(27, 26), -- northern europe, great britain
(27, 24), -- northern europe, ukraine
(27, 23), -- northern europe, scandinavia

(24, 13), -- ukraine, afghanistan
(24, 14), -- ukraine, ural
(24, 15), -- ukraine, middle east
(24, 28), -- ukraine, southern europe
(24, 27), -- ukraine, northern europe
(24, 23), -- ukraine, scandinavia

(23, 27), -- scandinavia, northern europe
(23, 24), -- scandinavia, ukraine
(23, 26), -- scandinavia, great britain
(23, 22), -- scandinavia, iceland

(26, 25), -- great britain, western europe
(26, 27), -- great britain, northern europe
(26, 23), -- great britain, scandinavia
(26, 22), -- great britain, iceland

(22, 23), -- iceland, scandinavia
(22, 26), -- iceland, great britain
(22, 31), -- iceland, greenland

(29, 11), -- alaska, kamchatka
(29, 30), -- alaska, northwest territory
(29, 32), -- alaska, alberta

(31, 22), -- greenland, iceland
(31, 30), -- greenland, northwest territory
(31, 33), -- greenland, ontario
(31, 34), -- greenland, quebec

(37, 38), -- central america, venezuela
(37, 35), -- central america, western united states
(37, 36), -- central america, eastern united states

(35, 37), -- western united states, central america
(35, 36), -- western united states, eastern united states
(35, 33), -- western united states, ontario
(35, 32), -- western united states, alberta

(36, 37), -- eastern united states, central america
(36, 35), -- eastern united states, western united states
(36, 33), -- eastern united states, ontario
(36, 34), -- eastern united states, quebec

(33, 35), -- ontario, western united states
(33, 36), -- ontario, eastern united states
(33, 34), -- ontario, quebec
(33, 32), -- ontario, alberta
(33, 30), -- ontario, northwest territory
(33, 31), -- ontario, greenland

(34, 36), -- quebec, eastern united states
(34, 33), -- quebec, ontario
(34, 31), -- quebec, greenland

(32, 33), -- alberta, ontario
(32, 30), -- alberta, northwest territory
(32, 29), -- alberta, alaska
(32, 35), -- alberta, western united states

(30, 32), -- northwest territory, alberta
(30, 29), -- northwest territory, alaska
(30, 31), -- northwest territory, greenland
(30, 33)  -- northwest territory, ontario
