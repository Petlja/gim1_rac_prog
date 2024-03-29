Час 12 - Контрола тока - вежбање
################################

Након неколико часова на којима смо уводили нове концепте, време је да
поново направимо малу паузу и искористимо време да проверимо колико
смо до сада научили (твој наставник може да ти да контролни задатак
или петнаестоминутну проверу знања из области израчунавања и контроле
тока). Можеш урадити наредних неколико задатака да провериш своје
знање. Додатне задатке за вежбу можеш пронаћи `овде
<KontrolaTokaZadaci.html>`_.

Гранање - задаци
----------------

Повишена телесна темпратура
'''''''''''''''''''''''''''
.. level:: 1

.. questionnote::

   Повишена телесна температура је изнад 37 степени Целзијуса. Напиши
   програм у којем се уноси температура пацијента и који исписује
   поруку ако тај пацијент има повишену температуру.

.. activecode:: Повишена_телесна_температура

   temperatura = float(input("Unesi telesnu temperaturu:"))
   # dopuni ovaj program

   
Ко је урадио више задатака?
'''''''''''''''''''''''''''
.. level:: 1
   
.. questionnote::

   Пера вежба задатке са Јањом. Напиши програм који честита оном ко је
   урадио више задатака (ако су урадили исто, не честита се никоме).

.. activecode:: Пера_и_Јања_вежбају_програмирање

   pera = int(input("Koliko je zadataka uradio Pera?"))
   janja = int(input("Koliko je zadataka uradila Janja?"))
   # dopuni naredni kod
   print("Pera je uradio više")
   print("Janja je uradila više")

.. questionnote::

   Допуни претходни програм тако да исписује поруку ако су урадили
   исти број задатака.

.. activecode:: Пера_и_Јања_вежбају_програмирање2

   pera = int(input("Koliko je zadataka uradio Pera?"))
   janja = int(input("Koliko je zadataka uradila Janja?"))
   # dopuni naredni kod
   print("Pera je uradio više")
   print("Janja je uradila više")
   print("Uradili su isti broj zadatka")


Да ли је Милица у школи?
''''''''''''''''''''''''
.. level:: 1
   
.. questionnote::

   Милица иде у школу од 8 до 13 часова. Напиши програм који за унето
   време одређује да ли је она у школи (у 13 часова већ није).

.. activecode:: Милица_у_школи

   vreme = int(input())
   # završi program

Провери да ли програм за унети број 7 исписује ``ne``, за унети број 8
и број 11 исписује ``da``, а за унети број 13 и 20 исписује ``ne``.

Цена струје
'''''''''''
.. level:: 2
   
.. questionnote::

   У једној земљи се цена струје одређује на основу потрошње. Ко
   потроши мање од 350kWh плаћа цену од 5.1 динара по kWh, потрошња
   између 351 и 1600kWh плаћа се по цени од 7.7 динара по kWh, а
   потрошња преко 1600kWh плаћа се по цени од 15.3 динара по
   kWh. Напиши програм који за унету потрошњу израчунава цену.
   

.. activecode:: Потрошња_струје
   :runortest: potrosnja, cena

   # -*- acsection: general-init -*-
   # -*- acsection: var-init -*-
   potrosnja = int(input("Unesi broj utrošenih kWh"))
   # -*- acsection: main -*-
   if potrosnja <= 350:
       cena = 0  # ispravi ovaj red
   elif potrosnja <= 0:  # ispravi ovaj red
       cena = 350 * 5.1 + (potrosnja - 350) * 7.7
   else:
       cena = 0 # ispravi ovaj red
   # -*- acsection: after-main -*-
   print(cena)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
          for potrosnja, cena in [(220, 1122.0), (1035, 7059.5), (1824, 14837.2)]:
             self.assertEqual(acMainSection(potrosnja = potrosnja)["cena"],cena,"Ако је потрошња %s kWh, цена је %s динара." % (potrosnja, cena))
   myTests().main()


Температура у рерни
'''''''''''''''''''
.. level:: 2
   
.. questionnote::

   Да би се колач лепо испекао, температура у рерни мора бити између
   150 и 200 степени. Напиши програм у којем се уноси тренутна
   температура у рерни и одређује да ли рерну треба појачати, смањити
   или оставити каква јесте.

.. activecode:: рерна

   temperatura = int(input())
   # dopuni naredni kod
   print("Pojačaj")
   print("U redu je")
   print("Smanji")
   
   
Понављање - задаци
------------------

Понављање поруке n пута
'''''''''''''''''''''''
.. level:: 1

.. questionnote::

   Напиши програм који учитава број :math:`n`, а затим :math:`n` пута
   исписује текст ``Учим да програмирам!``.

.. activecode:: понављање_n_пута

   n = int(input())
   # dopuni ovaj program
   print("Учим да програмирам!")


Површине 10 квадрата
''''''''''''''''''''
.. level:: 1
   
.. questionnote::

   Напиши програм који израчунава и исписује површине 10 квадрата чије
   дужине странице корисник уноси.

.. activecode:: површине_10_квадрата

   # dopuni naredni program
   a = int(input())
   print(a*a)


Одбројавање по 5 унатраг
''''''''''''''''''''''''
.. level:: 1
       
.. questionnote::

   Напиши програм који одбројава од 100 до 0, тј. исписује бројеве
   100, 95, 90, ..., 5, 0.

.. activecode:: одбројавање_жмурке

   for i in range():  # dopuni ovaj red
       print()        # dopuni ovaj red

Квадрат од звездица
'''''''''''''''''''
.. level:: 2
       
.. questionnote::

   Напиши програм који исцртава квадрат помоћу карактера ``*``
   (исписује се n редова са по n звездица). На пример, за n=4, потребно
   је исписати:

::
   
   ****
   ****
   ****
   ****

.. activecode:: квадрат_од_звездица

   n = int(input())
   # dopuni ovde kod
	  
.. reveal:: квадрат_од_звездица_reveal
   :showtitle: Прикажи решење
   :hidetitle: Сакриј решење

   .. activecode:: квадрат_од_звездица_решење
		   
      n = int(input('Колико редова?'))
      for i in range(n):
          for j in range(n):
              print('*', sep='', end='')
          print()
		 
       
