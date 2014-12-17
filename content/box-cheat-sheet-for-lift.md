Box Cheat Sheet for Lift
########################
:date: 2012-05-16 18:40
:slug: box-cheat-sheet-for-lift

When you’re learning Scala, one of the first concepts that clicks is
pattern matching. Once you get the “hammer” of pattern matching in your
Scala toolbox, everything is a nail; you want to use it everywhere for
everything. Pattern matching **is** very powerful and easy to use, but
it turns out for many, many simple cases using a higher-order function
is more concise and performant. I have Tony Morris’s `Option Cheet
Sheet <http://blog.tmorris.net/scalaoption-cheat-sheet/>`__ bookmarked
and use it almost every day.

In Lift, though, we generally use
```Box`` <http://www.assembla.com/spaces/liftweb/wiki/Box>`__ instead of
``Option``. Box adds a third ``Failure`` state and a host of additional
methods. I got tired of translating the ``Option`` methods to ``Box``
ones in my head so I wrote up this translation of ``Box`` methods to
match statements. I used the `Lift API
Docs <http://scala-tools.org/mvnsites/liftweb-2.4/#net.liftweb.common.package>`__
and the `Lift source
code <https://github.com/lift/framework/blob/master/core/common/src/main/scala/net/liftweb/common/Box.scala>`__
to compile it.

.. raw:: html

   </p>

The next hammer-that-turns-everything-into-a-nail that I encountered in
learning Scala was for-comprehensions. I’m still kind of in love with
them! In the interest of length, I haven’t included any examples here,
but ``Box`` plays very nicely with for-comprehensions as well. I hope to
cover some ways we use ``Box`` in for-comprehensions in a future post.

.. raw:: html

   </p>

flatMap
^^^^^^^

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.flatMap(foo(\_))
 foo returns a Box of any type

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => Em |
|                                      | pty  case Failure(message, exception |
|                                      | , chain) => Failure(message, excepti |
|                                      | on, chain)  case Full(x) => foo(x)}  |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

map
^^^

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.map(foo(\_))
 foo returns any type

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => Em |
|                                      | pty  case Failure(message, exception |
|                                      | , chain) => Failure(message, excepti |
|                                      | on, chain)  case Full(x) => Full(foo |
|                                      | (x))}                                |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

dmap
^^^^

.. raw:: html

   </p>

Equivalent to ``.map(foo(_)).openOr(bar)``

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.dmap(bar)(foo(\_))
 foo returns a value of the same type as bar

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => ba |
|                                      | r  case Failure(message, exception,  |
|                                      | chain) => bar  case Full(x) => foo(x |
|                                      | )}                                   |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

choice
^^^^^^

.. raw:: html

   </p>

Equivalent to ``.flatMap(foo(_)).or(bar())``

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.choice(foo(\_))(bar())
 foo and bar are functions that return Boxes of the same type

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => ba |
|                                      | r()  case Failure(message, exception |
|                                      | , chain) => bar()  case Full(x) => f |
|                                      | oo(x)}                               |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

===
^^^

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox === bar
 bar is a value of any type

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => fa |
|                                      | lse  case Failure(message, exception |
|                                      | , chain) => false  case Full(x) => x |
|                                      | .equals(bar)}                        |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

equals
^^^^^^

.. raw:: html

   </p>

Determines equality based upon the the ``Box``\ ’s content. In the case
of two ``Failure``\ s being compared, the causes must match exactly.

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.equals(bar)
 bar is a value of any type

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     1234567                          |     (theBox, bar) match {  case (Emp |
|                                      | ty, Empty) => true  case (Failure(ms |
|                                      | g1, ex1, chain1), Failure(msg2, ex2, |
|                                      |  chain2)) => (msg1, ex1, chain1) ==  |
|                                      | (msg2, ex2, chain2)  case (Full(x),  |
|                                      | Full(y)) => x.equals(y)  case (Full( |
|                                      | x), y) => x.equals(y)  case _ => fal |
|                                      | se}                                  |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

isEmpty
^^^^^^^

.. raw:: html

   </p>

This one can be tricky!

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.isEmpty

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => tr |
|                                      | ue  case Failure(message, exception, |
|                                      |  chain) => true  case Full(x) => fal |
|                                      | se}                                  |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

isDefined
^^^^^^^^^

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.isDefined

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => fa |
|                                      | lse  case Failure(message, exception |
|                                      | , chain) => false  case Full(x) => t |
|                                      | rue}                                 |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

exists
^^^^^^

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.exists(foo(\_))
 foo returns Boolean

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => fa |
|                                      | lse  case Failure(message, exception |
|                                      | , chain) => false  case Full(x) => f |
|                                      | oo(x)}                               |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

forall
^^^^^^

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.forall(foo(\_))
 foo returns Boolean

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => tr |
|                                      | ue  case Failure(message, exception, |
|                                      |  chain) => true  case Full(x) => foo |
|                                      | (x)}                                 |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

foreach
^^^^^^^

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.foreach(foo(\_))
 foo returns Unit

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => {} |
|                                      |   case Failure(message, exception, c |
|                                      | hain) => {}  case Full(x) => foo(x)} |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

pass
^^^^

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.pass(foo(\_))
 foo takes a Box and returns Unit

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => Em |
|                                      | pty  case Failure(message, exception |
|                                      | , chain) => Failure(message, excepti |
|                                      | on, chain)  case Full(x) => foo(theB |
|                                      | ox); theBox}                         |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

filter
^^^^^^

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.filter(foo(\_))
 foo returns Boolean

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => Em |
|                                      | pty  case Failure(message, exception |
|                                      | , chain) => Failure(message, excepti |
|                                      | on, chain)  case Full(x) => if (foo( |
|                                      | x)) Full(x) else Empty}              |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

filterMsg
^^^^^^^^^

.. raw:: html

   </p>

Returns a ``Failure`` with the provided message if the predicate is not
met.

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.filterMsg(msg)(foo(\_))
 foo returns Boolean

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => Fa |
|                                      | ilure(msg, Empty, Empty)  case Failu |
|                                      | re(message, exception, chain) => Fai |
|                                      | lure(message, exception, chain)  cas |
|                                      | e Full(x) => if (foo(x)) Full(x) els |
|                                      | e Failure(msg, Empty, Empty)}        |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

filterNot
^^^^^^^^^

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.filterNot(foo(\_))
 foo returns Boolean

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => Em |
|                                      | pty  case Failure(message, exception |
|                                      | , chain) => Failure(message, excepti |
|                                      | on, chain)  case Full(x) => if (!foo |
|                                      | (x)) Full(x) else Empty}             |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

openOr
^^^^^^

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

box openOr(bar)
 bar is a value of the same type or a descendant of the Box’s type

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => ba |
|                                      | r  case Failure(message, exception,  |
|                                      | chain) => bar  case Full(x) => x}    |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

or
^^

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.or(bar)
 bar is a Box of the same type or a descendant of the Box’s type

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => ba |
|                                      | r  case Failure(message, exception,  |
|                                      | chain) => bar  case Full(x) => Full( |
|                                      | x)}                                  |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

toOption
^^^^^^^^

.. raw:: html

   </p>

``Box`` defines an implicit conversion from ``Box[T]`` to ``Option[T]``,
so you can call ``Option`` methods on ``Box``\ es if you want. This is
how that implicit conversion is defined (you also can call ``.toOption``
directly.)

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.toOption

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => No |
|                                      | ne  case Failure(message, exception, |
|                                      |  chain) => None  case Full(x) => Som |
|                                      | e(x)}                                |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

toList
^^^^^^

.. raw:: html

   </p>

``Box`` also defines an implicit conversion to ``Iterable``, so you can
call any methods from ``Iterable`` that you find useful. Note, though,
that if the ``Box`` is full ``.toList`` will always return a ``List``
with one element. If you want to call ``Iterable`` methods on the value
of a ``Box[List[Foo]]`` you probably want to use ``.elements``.

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.toList

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => Ni |
|                                      | l  case Failure(message, exception,  |
|                                      | chain) => Nil  case Full(x) => List( |
|                                      | x)}                                  |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

elements
^^^^^^^^

.. raw:: html

   </p>

``.elements`` returns an
```Iterator`` <http://www.tutorialspoint.com/scala/scala_iterators.htm>`__
over the value of the box. Good for manipulating the contents of a
``Box[List[Foo]]``.

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.elements

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => It |
|                                      | erator.empty  case Failure(message,  |
|                                      | exception, chain) => Iterator.empty  |
|                                      |  case Full(x) => Iterator(x)}        |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

isA
^^^

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.isA[Bar]
 Bar is a Class or primitive

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => Em |
|                                      | pty  case Failure(message, exception |
|                                      | , chain) => Empty  case Full(x) => i |
|                                      | f (Bar.isAssignableFrom(x.getClass)) |
|                                      |  Full(value.asInstanceOf[Bar]) else  |
|                                      | Empty}                               |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

asA
^^^

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

theBox.asA[Bar]
 Bar is a Class or primitive

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => Em |
|                                      | pty  case Failure(message, exception |
|                                      | , chain) => Empty  case Full(x) => i |
|                                      | f (Full(x).isA[Bar]) then Full(x).as |
|                                      | InstanceOf[Box[Bar]] else Empty}     |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

?~
^^

.. raw:: html

   </p>

Useful in for-comprehensions.

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

box ?~ emptyMsg
 emptyMsg is a string

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => Fa |
|                                      | ilure(emptyMsg, Empty, Empty)  case  |
|                                      | Failure(message, exception, chain) = |
|                                      | > Failure(message, exception, chain) |
|                                      |   case Full(x) => Full(x)}           |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

?~!
^^^

.. raw:: html

   </p>

Like ``?~``, but if the ``Box`` is already a ``Failure`` it replaces the
message and chains the existing ``Failure``.

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

box ?~! failMsg
 emptyMsg is a string

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => Fa |
|                                      | ilure(failMsg, Empty, Empty)  case F |
|                                      | ailure(message, exception, chain) => |
|                                      |  Failure(failMsg, Empty, Full(box))  |
|                                      |  case Full(x) => Full(x)}            |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

Constructors
~~~~~~~~~~~~

.. raw:: html

   </p>

from ``Option``
^^^^^^^^^^^^^^^

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

Box(foo: Option[T])

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     1234                             |     foo match {  case Some(x) => Ful |
|                                      | l(x)  case None => Empty}            |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

from ``List``
^^^^^^^^^^^^^

.. raw:: html

   </p>

This returns a ``Box`` with the head of the list, if the list isn’t
empty.

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

Box(foo: List[T])

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     1234                             |     foo match {  case x :: _ => Full |
|                                      | (x)  case Nil => Empty}              |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

null-safe
^^^^^^^^^

.. raw:: html

   </p>

This converts null values to ``Empty``, which is very useful when you’re
dealing with values from Java code.

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

Box !! bar

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     1234                             |     bar match {    case null => Empt |
|                                      | y    case _ => Full(bar)}            |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

EmptyBox
~~~~~~~~

.. raw:: html

   </p>

While ``Box``\ ’s advantage over ``Option`` is that it distinguishes
between the empty case and the failure case, if you don’t care whether a
``Box`` is a ``Failure`` or an ``Empty``, you can match on ``EmptyBox``.

The following code:

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     theBox match {  case Empty => fo |
|                                      | o  case Failure(message, exception,  |
|                                      | chain) => foo  case Full(x) => bar}  |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

is equivalent to:

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     1234                             |     theBox match {  case EmptyBox => |
|                                      |  foo  case Full(x) => bar}           |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

tryo
~~~~

.. raw:: html

   </p>

An insanely useful helper method that catches exceptions and converts
them to ``Failure``\ s. You can also pass a list of ``Exception``
classes that should be converted to ``Empty``\ s instead, and/or a
callback function that should be triggered if an exception is thrown.

.. raw:: html

   </p>
   <p>
   <figure class="code">
   <figcaption>

tryo(foo(bar))
 foo is a function that can throw an exception

.. raw:: html

   </figcaption>

.. raw:: html

   <div class="highlight">

+--------------------------------------+--------------------------------------+
| .. code:: line-numbers               | ::                                   |
|                                      |                                      |
|     12345                            |     try {  Full(foo(bar))} catch {   |
|                                      | case ex: Failure(ex.getMessage, Full |
|                                      | (ex), Empty)}                        |
                                                                             
+--------------------------------------+--------------------------------------+

.. raw:: html

   </div>

.. raw:: html

   </figure>
   </p>

