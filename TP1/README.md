# TPC1
Neste TPC, foi-nos proposto criar uma expressão regular que representasse números binários que não contivessem a subcadeia "011" em nenhuma posição.

Após a realização de alguns [testes com regex](testes.png) e alguma pesquisa teórica, obtive a seguinte [expressão regular](expressao.txt):

```^1*0*(0|1)(0|01)*$```
