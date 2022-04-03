

CREATE TABLE condidat(
    id int(10) auto_increment  primary key, 
    nom varchar(20) NOT NULL ,
    prenom varchar(20) NOT NULL,
    genre enum('M', 'F') NOT NULL,
    email varchar(50) NOT NULL,
    bac varchar(10) NOT NULL

) ENGINE = innodb;

INSERT INTO `condidat` ( `nom`, `prenom`, `genre`, `email`, `bac`) VALUES 
( 'Benarab', 'Hedia', 'F', 'hediaben@gmail.com', '4si'),
( 'Ghannem', 'Tarek', 'M', 'T_GH@yahoo.fr', '4tech'),
( 'Salhi', 'Louay', 'M', 'LouayS@gmail.com', '4si');