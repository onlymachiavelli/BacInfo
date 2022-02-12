

CREATE TABLE equipe (
    codeE INT (3) PRIMARY KEY , 
    nomE VARCHAR (20) NOT NULL 
)ENGINE = INNODB;

CREATE TABLE pays (
    codeP INT (3) PRIMARY KEY , 
    nomP VARCHAR (20) NOT NULL 
) ENGINE = INNODB ;

CREATE TABLE coureur (
    NumC INT (3) PRIMARY KEY ,
    NomC VARCHAR(20) NOT NULL , 
    codeE INT(3) NOT NULL , 
    codeP INT (3) NOT NULL , 
    FOREIGN KEY (codeE) REFERENCES equipe(codeE) , 
    FOREIGN KEY (codeP) REFERENCES pays(codeP) 

) ENGINE = INNODB; 
CREATE TABLE etape (
    NumET INT(3) PRIMARY KEY ,
    Date date NOT NULL  ,  
    villeDep VARCHAR (20) NOT NULL , 
    villeArr VARCHAR (20) NOT NULL ,
    Nbkm INT(3) NOT NULL DEFAULT 30 CHECK (Nbkm > 0)  
 ) ENGINE = INNODB ;  

 CREATE TABLE participer(
     NumC INT (3) ,
     NumET INT(3) ,
     tempsRealise VARCHAR(5) CHECK (tempsRealise  > 0 ) ,
     PRIMARY KEY (NumC, NumET , tempsRealise) ,
     FOREIGN KEY (NumC) REFERENCES coureur (NumC) ON UPDATE CASCADE ON DELETE CASCADE  , 
     FOREIGN KEY (NumET) REFERENCES etape (NumET) ON UPDATE CASCADE ON DELETE CASCADE 
      
 ) ENGINE = INNODB;


ALTER TABLE coureur ADD COLUMN sexe VARCHAR (1) ;
ALTER TABLE etape ADD CONSTRAINT checkDate CHECK (date between '2022-01-01' AND '2022-12-31') ;
ALTER TABLE pays ADD CONSTRAINT checkReg CHECK (nomP IN ('Tunisie', 'France')) ;
ALTER TABLE participer MODIFY tempsRealise TIME ; 

ALTER TABLE participer DROP PRIMARY KEY  , ADD CONSTRAINT primaries PRIMARY KEY (NumC ,NumET ) ;
ALTER TABLE participer DROP COLUMN tempsRealise ;
DROP TABLE participer ;
