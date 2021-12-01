Program Projet;
Uses Wincrt;
Var
  alpha,mot, aff, rep : String;
  long, i,j, cap : Integer;
  gagne : Boolean;
Begin
  Randomize;
  alpha := 'abcdefghijklmnopqrstuvwxyz';
  long := 5+ Random(10-5)+1;
  mot := '';
  Writeln(mot);
  aff := '';
  gagne := False;
  For i := 1 To long Do
    Begin
      cap := Random(2);
      If (cap = 1) Then
        Begin
          mot := mot + Upcase(alpha[Random(Length(alpha)+1)])
        End
      Else
        Begin
          mot := mot + alpha[Random(Length(alpha)+1)]
        End;
      aff := aff + '-' ;
    End ;
  i := 0;
  Writeln('Longeur de MID : ' , long);
  Repeat
    Begin
      Writeln(mot);
      i := i+1;
      Writeln('Masquee : ' , aff);
      Writeln('Essais N ', i);
      Readln(rep) ;
      For j:= 1 To Length(rep) Do
        Begin
          If ( Upcase(rep[j] )=Upcase(mot[j] ) ) Then
            Begin
              aff[j] := mot[j]
            End ;
        End ;
    End;
    If (Pos('-' , aff) = 0) Then
      Begin
        gagne := True ;
      End ;
  Until ( gagne )Or( i = long) ;
  Writeln('le mot a devenir est ', mot);
  If (gagne) Then
    Writeln('Bravo !')
  Else
    Writeln('desole ! vous avez perdu :( ' );
  Readln ;
End.
