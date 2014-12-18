Title: Box Cheat Sheet for Lift
Date: 2012-05-16 18:40
Slug: box-cheat-sheet-for-lift

<style>
.codehilitetable {
	font-size:75%;
}
</style>

When you’re learning Scala, one of the first concepts that clicks is
pattern matching. Once you get the “hammer” of pattern matching in your
Scala toolbox, everything is a nail; you want to use it everywhere for
everything. Pattern matching **is** very powerful and easy to use, but
it turns out for many, many simple cases using a higher-order function
is more concise and performant. I have Tony Morris’s Option Cheat
Sheet <http://blog.tmorris.net/scalaoption-cheat-sheet/> bookmarked
and use it almost every day.

In Lift, though, we generally use
[`Box`](http://www.assembla.com/spaces/liftweb/wiki/Box) instead of
`Option`. Box adds a third `Failure` state and a host of additional
methods. I got tired of translating the `Option` methods to `Box`
ones in my head so I wrote up this translation of `Box` methods to
match statements. I used the [Lift API
Docs](http://scala-tools.org/mvnsites/liftweb-2.4/#net.liftweb.common.package)
and the [Lift source
code](https://github.com/lift/framework/blob/master/core/common/src/main/scala/net/liftweb/common/Box.scala) to compile it.

The next hammer-that-turns-everything-into-a-nail that I encountered in
learning Scala was for-comprehensions. I’m still kind of in love with
them! In the interest of length, I haven’t included any examples here,
but `Box` plays very nicely with for-comprehensions as well. I hope to
cover some ways we use `Box` in for-comprehensions in a future post.

***flatMap***
<br/>
`theBox.flatMap(foo(_))` <br/>
foo returns a Box of any type

	:::scala
	theBox match {
	  case Empty => Empty
	  case Failure(message, exception, chain) => Failure(message, exception, chain)
	  case Full(x) => foo(x)
	}

***map***
<br/>
`theBox.map(foo(_))` <br/>
foo returns any type

	:::scala
	theBox match {
	  case Empty => Empty
	  case Failure(message, exception, chain) => Failure(message, exception, chain)
	  case Full(x) => Full(foo(x))
	}

***dmap***
<br/>
Equivalent to `.map(foo(_)).openOr(bar)` <br/>
`theBox.dmap(bar)(foo(_))` <br/>
foo returns a value of the same type as bar

	:::scala
	theBox match {
	  case Empty => bar
	  case Failure(message, exception, chain) => bar
	  case Full(x) => foo(x)
	}

***choice***
<br/>
Equivalent to `.flatMap(foo(_)).or(bar())` <br/>
`theBox.choice(foo(_))(bar())` <br/>
foo and bar are functions that return Boxes of the same type

	:::scala
	theBox match {
	  case Empty => bar()
	  case Failure(message, exception, chain) => bar()
	  case Full(x) => foo(x)
	}

***===***
<br/>
`theBox === bar` <br/>
bar is a value of any type

	:::scala
	theBox match {
	  case Empty => false
	  case Failure(message, exception, chain) => false
	  case Full(x) => x.equals(bar)
	}

***equals***
<br/>
Determines equality based upon the the `Box`’s content. In the case
of two `Failure`s being compared, the causes must match exactly. <br/>
`theBox.equals(bar)` <br/>
bar is a value of any type

	:::scala
	(theBox, bar) match {
	  case (Empty, Empty) => true
	  case (Failure(msg1, ex1, chain1), Failure(msg2, ex2, chain2)) => (msg1, ex1, chain1) == (msg2, ex2, chain2)
	  case (Full(x), Full(y)) => x.equals(y)
	  case (Full(x), y) => x.equals(y)
	  case _ => false
	}

***isEmpty***
<br/>
This one can be tricky!<br/>
`theBox.isEmpty`

	:::scala
	theBox match {
	  case Empty => true
	  case Failure(message, exception, chain) => true
	  case Full(x) => false
	}
	
***isDefined***
<br/>
`theBox.isDefined`

	:::scala
	theBox match {
	  case Empty => false
	  case Failure(message, exception, chain) => false
	  case Full(x) => true
	}

***exists***
<br/>
`theBox.exists(foo(_))`<br/>
foo returns Boolean

	:::scala
	theBox match {
	  case Empty => false
	  case Failure(message, exception, chain) => false
	  case Full(x) => foo(x)
	}

***forall***
<br/>
`theBox.forall(foo(_))`<br/>
foo returns Boolean

	:::scala
	theBox match {
	  case Empty => true
	  case Failure(message, exception, chain) => true
	  case Full(x) => foo(x)
	}

***foreach***
<br/>
`theBox.foreach(foo(_))`<br/>
foo returns Unit

	:::scala
	theBox match {
	  case Empty => {}
	  case Failure(message, exception, chain) => {}
	  case Full(x) => foo(x)
	}

***pass***
<br/>
`theBox.pass(foo(_))`<br/>
foo takes a Box and returns Unit

	:::scala
	theBox match {
	  case Empty => Empty
	  case Failure(message, exception, chain) => Failure(message, exception, chain)
	  case Full(x) => foo(theBox); theBox
	}

***filter***
<br/>
`theBox.filter(foo(_))`<br/>
foo returns Boolean

	:::scala
	theBox match {
	  case Empty => Empty
	  case Failure(message, exception, chain) => Failure(message, exception, chain)
	  case Full(x) => if (foo(x)) Full(x) else Empty
	}
	
***filterMsg***
<br/>
Returns a `Failure` with the provided message if the predicate is not
met.<br/>
`theBox.filterMsg(msg)(foo(_))`<br/>
foo returns Boolean

	:::scala
	theBox match {
	  case Empty => Failure(msg, Empty, Empty)
	  case Failure(message, exception, chain) => Failure(message, exception, chain)
	  case Full(x) => if (foo(x)) Full(x) else Failure(msg, Empty, Empty)
	}

***filterNot***
<br/>
`theBox.filterNot(foo(_))`<br/>
foo returns Boolean

	:::scala
	theBox match {
	  case Empty => Empty
	  case Failure(message, exception, chain) => Failure(message, exception, chain)
	  case Full(x) => if (!foo(x)) Full(x) else Empty
	}

***openOr***
<br/>
`box openOr(bar)`<br/>
bar is a value of the same type or a descendant of the Box’s type

	:::scala
	theBox match {
	  case Empty => bar
	  case Failure(message, exception, chain) => bar
	  case Full(x) => x
	}

***or***
<br/>
`theBox.or(bar)`<br/>
bar is a Box of the same type or a descendant of the Box’s type

	:::scala
	theBox match {
	  case Empty => bar
	  case Failure(message, exception, chain) => bar
	  case Full(x) => Full(x)
	}

***toOption***
<br/>
`Box` defines an implicit conversion from `Box[T]` to `Option[T]`,
so you can call `Option` methods on `Box`es if you want. This is
how that implicit conversion is defined (you also can call `.toOption`
directly.)<br/>
`theBox.toOption`

	:::scala
	theBox match {
	  case Empty => None
	  case Failure(message, exception, chain) => None
	  case Full(x) => Some(x)
	}

***toList***
<br/>
`Box` also defines an implicit conversion to `Iterable`, so you can
call any methods from `Iterable` that you find useful. Note, though,
that if the `Box` is full `.toList` will always return a `List`
with one element. If you want to call `Iterable` methods on the value
of a `Box[List[Foo]]` you probably want to use `.elements`.<br/>
`theBox.toList`

	:::scala
	theBox match {
	  case Empty => Nil
	  case Failure(message, exception, chain) => Nil
	  case Full(x) => List(x)
	}

***elements***
<br/>
`.elements` returns an
[`Iterator`](http://www.tutorialspoint.com/scala/scala_iterators.htm) over the value of the box. Good for manipulating the contents of a
`Box[List[Foo]]`.<br/>
`theBox.elements`

	:::scala
	theBox match {
	  case Empty => Iterator.empty
	  case Failure(message, exception, chain) => Iterator.empty
	  case Full(x) => Iterator(x)
	}

***isA***
<br/>
`theBox.isA[Bar]`<br/>
Bar is a Class or primitive

	:::scala
	theBox match {
	  case Empty => Empty
	  case Failure(message, exception, chain) => Empty
	  case Full(x) => if (Bar.isAssignableFrom(x.getClass)) Full(value.asInstanceOf[Bar]) else Empty
	}

***asA***
<br/>
`theBox.asA[Bar]`<br/>
Bar is a Class or primitive

	:::scala
	theBox match {
	  case Empty => Empty
	  case Failure(message, exception, chain) => Empty
	  case Full(x) => if (Full(x).isA[Bar]) then Full(x).asInstanceOf[Box[Bar]] else Empty
	}

***?~***
<br/>
Useful in for-comprehensions.<br/>
`box ?~ emptyMsg`<br/>
emptyMsg is a string

	:::scala
	theBox match {
	  case Empty => Failure(emptyMsg, Empty, Empty)
	  case Failure(message, exception, chain) => Failure(message, exception, chain)
	  case Full(x) => Full(x)
	}

***?~!***
<br/>
Like `?~`, but if the `Box` is already a `Failure` it replaces the
message and chains the existing `Failure`.<br/>
box ?~! failMsg<br/>
emptyMsg is a string

	:::scala
	theBox match {
	  case Empty => Failure(failMsg, Empty, Empty)
	  case Failure(message, exception, chain) => Failure(failMsg, Empty, Full(box))
	  case Full(x) => Full(x)
	}
	
<br/>

Constructors
=============

***from `Option`***
<br/>
`Box(foo: Option[T])`

	:::scala
	foo match {
	  case Some(x) => Full(x)
	  case None => Empty
	}

***from `List`***
<br/>
This returns a ``Box`` with the head of the list, if the list isn’t
empty.<br/>
`Box(foo: List[T])`

	:::scala
	foo match {
	  case x :: _ => Full(x)
	  case Nil => Empty
	}

***null-safe***
<br/>
This converts null values to `Empty`, which is very useful when you’re
dealing with values from Java code.<br/>
`Box !! bar`

	:::scala
	bar match {
	    case null => Empty
	    case _ => Full(bar)
	}

***EmptyBox***
<br/>
While `Box`’s advantage over `Option` is that it distinguishes
between the empty case and the failure case, if you don’t care whether a
`Box` is a `Failure` or an `Empty`, you can match on `EmptyBox`.

The following code:

	:::scala
	theBox match {
	  case Empty => foo
	  case Failure(message, exception, chain) => foo
	  case Full(x) => bar
	}

is equivalent to:

	:::scala
	theBox match {
	  case EmptyBox => foo
	  case Full(x) => bar
	}

***tryo***
<br/>
An insanely useful helper method that catches exceptions and converts
them to `Failure`s. You can also pass a list of `Exception`
classes that should be converted to `Empty`s instead, and/or a
callback function that should be triggered if an exception is thrown.<br/>
`tryo(foo(bar))`<br/>
foo is a function that can throw an exception

	:::scala
	try {
	  Full(foo(bar))
	} catch {
	  case ex: Failure(ex.getMessage, Full(ex), Empty)
	}