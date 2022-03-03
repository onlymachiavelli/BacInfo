CREATE TABLE CITOYEN (
    Cin VARCHAR (20) PRIMARY KEY ,
    Nom VARCHAR (20) NOT NULL , 
    Prenom VARCHAR(20) NOT NULL , 
    theDate DATE NULL, 
    genre VARCHAR(30) , 
    ville VARCHAR(20 ) ,
    Tel VARCHAR(81)  
); 

CREATE TABLE vaccin (
    CodeV VARCHAR(20) PRIMARY KEY ,
    Nb_Dose INT(2) NOT NULL ,
    
)ENGINE = INNODB ;