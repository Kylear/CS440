DROP TABLE IF EXISTS `trials`;

CREATE TABLE `trials` (
  `id` int(8) NOT NULL,
  `url` varchar(43) NOT NULL,
  `title` varchar(100) NOT NULL,
  `lead_sponsor` varchar(100) NOT NULL,
  `source` varchar(100) NOT NULL,
  `status` varchar(20) NOT NULL,
  `start_date` date,
  `completion_date` date,
  `phase` varchar(8) NOT NULL,
  `study_type` varchar(20) NOT NULL,
  `primary_purpose` varchar(20) NOT NULL,
  `enrollment` int(7),
  `condition` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `minimum_age` int(3),
  `maximum_age` int(3),
  `country` varchar(50),
  `study_first_submitted` date,
  `study_first_posted` date,
  `last_update_submitted` date,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `keywords`;

CREATE TABLE `keywords` (
  `id` int NOT NULL AUTO_INCREMENT,
  `study_id` int(8) NOT NULL,
  `keyword` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;