]README.md
# 🛑 Практическая работа №5 🛑
  ➢ Условный оператор. Подпрограммы.  
__Контрольные вопросы:__  
✅Ответ на контрольные вопросы✅:  
==========================================================================================  
  
1 __Cинтаксис и семантика цикла for__  
-for "имя параметра цикла" in <выражение>  
  
--в выражении может быть: массив; выражение "range(j;n)" , где j -  начало , i - конец (не включительно)  
  
Параметр цикла будет принимать все промежуточные значения между начальным и конечным  
  
Число шагов цикла равно количеству значений, принимаемых его параметром, включая начальное и конечное значения  
  
Условием продолжения цикла является:  
  
<значение параметра цикла> <= <значение выражения2>, в случае использования служебного слова to  
  
(значения параметра цикла на каждом шаге увеличиваются)  
==========================================================================================  
  
2 __Синтаксис цикла while__  
  
while  < выражение  >   
  
Цикл будет выполняться пока значние выражения  == True.  
  
В противном случае выполнение оператора цикла завершается  

Условие цикла может иметь значение False уже на первом шаге – тогда цикл завершится, и тело цикла не будет выполнено ни разу
  
Тело оператора цикла с предусловием может быть выполнено ноль или более раз  
  
Число шагов для цикла с предусловием заранее не определено  
  
Для завершения цикла после конечного числа шагов необходимо, чтобы условие продолжения содержало хотя бы одну переменную, значение которой меняется в теле цикла.  
==========================================================================================  
3 __Каким образом модуль подключается к программе__  
  
Различные модули подключаются к файлу программы путем команды  
  
import <модуль> from <библиотека>  
==========================================================================================  

4 __Поясните значение строки программы: if __name__ == "__main__":__  
  
Функция проверят, что код запущен из файла под  именем "main.py"  
  
Это помогает избежать лишних выводов при импортировании файла "main.py" в другие файлы  
==========================================================================================  
  
5 __name__ - переменная которой передается название файла, из которого запущен код  
  __main__ - название основного файла  
==========================================================================================  
  
6 Чтобы открыть файл только для чтения необходимо указать  метод "r" - read =>  
=> f = open("example.txt", "r")  
==========================================================================================  
  
7 При попытке открыть не существующий фал выйдет ошибка =>  
=> FileNotFoundError: [Errno 2] No such file or directory: 'exmple.txt'  
==========================================================================================  
  
8   
 1. s = 0.2  
 2. s = 0  
 3. s = 1  
==========================================================================================