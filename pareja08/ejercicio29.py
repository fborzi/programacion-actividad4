'''Escribí la función sucesion_mira_y_deci(n) que calcule los primeros n números de una sucesión que comienza con 1 y cada uno de los demás números se construye a partir del anterior, contando cuántas veces consecutivas aparece cada uno de sus dígitos, formando así el próximo. Por ejemplo, el siguiente de 1 es 11, ya que 1 está formado por “un uno” => 11. El siguiente a 11 es 21 pues 11 está formado por “dos unos” => 21. El próximo a 21 es 1211 ya que 21 está formado por “un dos y un uno” => 12 11.
Ejemplo: sucesión_mirá_y_decí(9) retornará [1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, 31131211131221].'''

from funciones import sucesion_mira_y_deci

print(sucesion_mira_y_deci(9))
