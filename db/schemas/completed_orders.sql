CREATE TABLE IF NOT EXISTS `completed_orders` 
(
    `Trip ID` INT,
    `Trip Origin` TEXT,
    `Trip Destination` TEXT,
    `Trip Start Time` TIMESTAMP,
    `Trip End Time` TIMESTAMP,
    PRIMARY KEY (`Trip ID`)
)