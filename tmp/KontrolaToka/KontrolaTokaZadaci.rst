Контрола тока - додатни задаци за вежбу
#######################################

Гранање - задаци
----------------

Број урађених задатака
''''''''''''''''''''''
.. level:: 1

   
.. questionnote::

   Пера је вежбао програмирање. Да би добио петицу, потребно је да
   уради бар 50 задатака. Напиши програм у којем се уноси број
   задатака које је Пера провежбао и одређује се да ли је то довољно
   да добије петицу. Ако јесте, програм исписује текст ``Bravo, dobio
   si pet!``.

.. activecode:: Пера_вежба_програмирање

   broj_zadataka = int(input("Koliko si zadataka uradio?"))
   # dopuni naredni kod
   print("Bravo, dobio si pet!")

.. questionnote::

   Допуни претходи програм тако да ако Пера није урадио довољан број
   задатака исписује поруку ``Dobro bi bilo da još malo vežbaš.``.

Двократно радно време
'''''''''''''''''''''
.. level:: 2

.. questionnote::

   Једна продавница ради двократно: од 8 до 12h и од 16 до 20h. Напиши
   програм који за унети број сати одређује да ли је продавница
   отворена или је затворена (у 8 и 16 је отворена, а у 12 и 20 је
   затворена).

.. activecode:: Двократно_радно_време

   sati = int(input("Koliko je sati?"))
   # dopuni naredni kod
   print("Prodavnica je otvorena")
   print("Prodavnica je zatvorena")

   
.. questionnote::
.. level:: 2

   Наставница програмирања је рекла да ће за оцену два на контролном
   бити потребно 50 поена, за оцену три 65 поена, за оцену четири 75
   поена, а за оцену пет 85 поена. Напиши програм који на основу броја
   поена одређује оцену.

.. activecode:: Оцена_на_основу_поена
   :runortest: broj_poena, ocena

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   broj_poena = int(input("Unesi broj poena: "))
   # -*- acsection: main -*-
   if True:
       ocena = 0
   elif True:
       ocena = 0
   # ispravi i dopuni prethodni kod
   # -*- acsection: after-main -*-
   print("Dobio si ocenu:", ocena)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for broj_poena, ocena in [(38, 1), (63, 2), (65, 3), (84, 4), (85, 5), (100, 5)]:
             self.assertEqual(acMainSection(broj_poena = broj_poena)["ocena"],ocena,"%s поена је оцена %s." % (broj_poena, ocena))
   myTests().main()

   
Понављање - задаци
------------------

Сви непарни бројеви прве стотине
''''''''''''''''''''''''''''''''
.. level:: 1
       
.. questionnote::

   Напиши програм који исписује све непарне бројеве прве стотине.

.. activecode:: непарни_бројеви_прве_стотине

   for i in ???  # dopuni ovaj red
       print(i)

Троугао од звездица
'''''''''''''''''''
.. level:: 2
       
.. questionnote::

   Напиши програм који исцртава троугао помоћу карактера `*`. У сваком
   од :math:`n` редова постоји једна звездица више него у претходном.
   На пример, за :math:`n=4` треба исписати:

::
   
   *
   **
   ***
   ****

.. activecode:: троугао_од_звездица

   n = int(input())
   # dopuni ovde kod
	  
.. reveal:: троугао_од_звездица_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   .. activecode:: троугао_од_звездица_решење
		   
      n = int(input('Колико редова?'))
      for i in range(n):
          for j in range(i):
              print('*', sep='', end='')
          print()
		 
