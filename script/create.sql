CREATE TABLE `movie` (
  `Mname` char(50) COLLATE 'utf8_general_ci' NOT NULL,
  `MURL` char(50) COLLATE 'utf8_general_ci' NULL,
  `Mpic` char(50) COLLATE 'utf8_general_ci' NULL,
  `dtor` char(50) COLLATE 'utf8_general_ci' NULL,
  `ator` char(50) COLLATE 'utf8_general_ci' NULL,
  `info` char(150) COLLATE 'utf8_general_ci' NULL
) COMMENT='' COLLATE 'utf8_general_ci';

CREATE TABLE `user` (
  `Uname` char(20) COLLATE 'utf8_general_ci' NOT NULL,
  `Usex` char(20) COLLATE 'utf8_general_ci' NOT NULL,
  `Uage` int NOT NULL,
  `email` char(50) COLLATE 'utf8_general_ci' NULL
) COMMENT='' COLLATE 'utf8_general_ci';

ALTER TABLE `user`
ADD PRIMARY KEY `Uname` (`Uname`);


ALTER TABLE `favorite`
ADD FOREIGN KEY (`Uname`) REFERENCES `user` (`Uname`)


ALTER TABLE `movie`
ADD PRIMARY KEY `Mname` (`Mname`);


ALTER TABLE `favorite`
ADD FOREIGN KEY (`Mname`) REFERENCES `movie` (`Mname`)

