<?php
    echo "<head><style>*{font-family:'arial';}</style></head>"; //just for the font
    $user = array (
        "name"  => "ALAA",
        "lname" =>"BARKA",
        "ID" => 42069 ,
        "stack" => array("REACT", "EXPRESS", "DJANGO", "MONGODB", "SQL", "POSTGREE", "TAILWIND","VITE","NEXT","LARAVEL","JWT") 

    );
    echo $user["name"];


  


    $index = 0;
    while(isset($user["stack"][$index])){
        echo $user["stack"][$index] ." ";
        $index++;
    }
    echo "<br/>";

    $a = 4;
    $b = 6; 
    function Power($a,$b){
        if ($b > 0)return $a * Power($a,$b-1);
        return (1);
    }
    echo Power($a,$b);
     
?>