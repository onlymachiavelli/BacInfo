create table livre (
    codelivre primary key int(4) ,
    titre varchar (100), 
    auteur enum ('claude duigo', 'eric sarrion','christine berhardt' ), 
    annee varchar(4)  ,   
    nbrpage int(3)

) engine = innodb;

