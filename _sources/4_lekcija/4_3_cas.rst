4.3. Петље
##########


У програмима које задајемо корњачи облици су често правилни и неке се
наредбе понављају. Стога, као и у програмима за робота Карела, и у
програмима за корњачу можемо користити петље.  Подсетимо се, две
основне петље у програмском језику Пајтон су условна петља `while` и
бројачка петља `for`.

Квадрат - петља
'''''''''''''''
	   
.. questionnote::

   Исправи наредни програм тако да корњача црта квадрат чија је
   страница дугачка 100 корака.

Програм који исцртава квадрат можемо да скратимо ако уведемо наредбу
којом постижемо да се неки задати низ наредби понови више пута. 
Већ знамо да је у језику Пајтон то најлакше урадити помоћу
наредбе ``for``.  Као што смо видели, наредбу *ponovi n puta*
можемо записати и као ``for i in range(n):``. Подсетимо се, не смемо да
заборавимо двотачку, а наредбе које се понављају наводимо увучене
неколико размака у односу на положај наредбе ``for``.
   
.. activecode:: корњача_квадрат_петља
   :nocodelens:

   import turtle
   for i in range(0):        # ponovi 4 puta:
       turtle.forward(0)     #   idi napred 100 koraka
       turtle.left(0)        #   okreni se nalevo za 90 stepeni

Погледај наредни видео:

.. ytpopup:: d1vAfYFq-l8
    :width: 735
    :height: 415
    :align: center

       
Правилни многоугао
''''''''''''''''''

.. questionnote:: 

   Уопшти претходни програм тако да уместо цртања квадрата корњача
   црта неки други правилан полигон (на пример, једнакостраничан
   троугао, правилан петоугао, правилан шестоугао и слично).


Ако је дат број *n* правилан *n*-тоугао (правилан полигон са *n*
страна) добијамо тако што нацртамо *n* његових страница. Зато је
цртање странице и окретање потребно поновити *n* пута. Након цртања
сваке странице корњача треба да се окрене тачно за величину спољашњег
угла полигона. Важи да је збир свих спољашњих углова у полигону једнак
360 степени, па пошто су сви они једнаки, сваки од њих је једнак
количнику бројева 360 и *n*. Други начин да одредимо угао за који се
корњача окреће у сваком кораку је да уочимо да она цртање почиње и
завршава окренута ка истоку и да се, у међувремену, током цртања,
окреће тачно за износ једног пуног круга, тј. за
:math:`360^\circ`. Пошто се у сваком кораку окреће подједнако, окрет
износи тачно :math:`\frac{360^\circ}{n}`. У програмском језику Пајтон,
количник бројева ``a`` и ``b`` можемо израчунати помоћу ``a / b``
(више речи о томе биће речено у поглављу о аритметичким операцијама и
дељењу), па број :math:`\frac{360}{n}` можемо израчунати 
помоћу ``360 / n``.

Као и у претходним случајевима, твој задатак је да исправиш грешке у
следећем програму.

.. activecode:: корњача_нтоугао_петља
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle
   n = 6
   for i in range(0):         # ponovi n puta:
       turtle.forward(0)        #   idi napred 100 koraka
       turtle.left(0)           #   okreni se za 360/n stepeni
   ====
   import turtle
   n = 6
   for i in range(n):         # ponovi n puta:
       turtle.forward(100)      #   idi napred 100 koraka
       turtle.left(360 / n)     #   okreni se za 360:n stepeni
     
.. learnmorenote:: Полигон - неправилан многоугао

   Збир унутрашњих углова сваког *n*-тоугла (у Еуклидској
   геометрији) једнак је вредности :math:`(n-2)\cdot
   180^\circ`. Заиста, ако из неког темена конвексног многоугла
   повучемо све његове дијагонале оне ће га поделити на укупно
   :math:`n-2` троугла (на наредној слици, петоугао је на тај начин
   подељен на три троугла).

   .. image:: ../../_images/uglovi_poligona.png
      :width: 300px   
      :align: center

   Збир углова у сваком троуглу (у Еуклидској геометрији) је
   :math:`180^\circ`.  Сваки унутрашњи угао полигона једнак је
   збиру неколико углова тих троуглова, док је сваки унутрашњи угао
   троугла део тачно једног од унутрашњих углова полигона, па је
   укупан збир унутрашњих углова полигона једнак укупном збиру
   углова тих троуглова, а то је тачно :math:`(n-2)\cdot
   180^\circ`.

   Сваки спољашњи угао полигона је допуна унутрашњег угла до
   :math:`180^\circ` степени (његов суплемент). Пошто је тих углова
   :math:`n`, важи да је збир спољашњих углова једнак разлици броја
   :math:`n \cdot 180^\circ` и збира унутрашњих углова полигона,
   који је, на основу претходног, једнак :math:`(n-2)\cdot
   180^\circ`. Зато је збир спољашњих углова полигона једнак
   :math:`n\cdot 180^\circ - (n-2)\cdot 180^\circ`, што је тачно
   :math:`360^\circ`.
       

	    
Провери своје разумевање петљи тако што ћеш поређати наредбе програма
у ком корњача исцртава једнакостранични троугао.

.. parsonsprob:: троугао_ређање

   Поређај делове кода тако да представљају исправно решење овог задатка.
   -----
   import turtle
   =====
   turtle.color("red")
   =====
   for i in range(3):
   =====
      turtle.forward(100)
   =====
      turtle.left(120)

       
Испрекидана линија
''''''''''''''''''

.. questionnote::

   У једном од претходних задатака нацртали смо испрекидану линију
   тако што смо више пута понављали исте наредбе. Скрати претходни
   програм коришћењем петље тако што ћеш нацртати испрекидану линију
   која се састоји од пет делова.

.. activecode:: испрекидана_линија
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle
   for i in range(5):
                                  # idi napred 20 koraka
                                  # podigni olovku
                                  # idi napred 20 koraka
                                  # spusti olovku
   ====
   import turtle
   for i in range(5):
       turtle.forward(20)           # idi napred 20 koraka
       turtle.penup()               # podigni olovku
       turtle.forward(20)           # idi napred 20 koraka
       turtle.pendown()             # spusti olovku


Погледај наредни видео:

.. ytpopup:: JeoAB84nG7w
    :width: 735
    :height: 415
    :align: center


Отисци корњаче
''''''''''''''

.. questionnote::
   
   Напиши програм који коришћењем понављања исцртава пет отисака корњаче
   размакнутих по 30 пиксела. Напиши програм без коришћења петље, а
   затим га скрати коришћењем петље.


.. activecode:: пет_отисака_корњаче
   :nocodelens:
   :enablecopy:
   :playtask:

   import turtle
   ====
   import turtle
   turtle.penup()
   turtle.shape("turtle")
   for i in range(5):
       turtle.stamp()
       turtle.forward(30)

