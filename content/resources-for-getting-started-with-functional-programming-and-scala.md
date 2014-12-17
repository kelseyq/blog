Title: Resources for Getting Started with Functional Programming and Scala
Date: 2013-01-07 18:29
Slug: resources-for-getting-started-with-functional-programming-and-scala

This is the “secret slide” from my recent talk [Learning Functional
Programming without Growing a
Neckbeard](http://nerd.kelseyinnis.com/blog/2012/12/17/slides-from-learning-functional-programming-without-growing-a-neckbeard/),
with links to the sources I used to put the talk together and some
suggestions for ways to get started writing Scala code.

### Functional programming in general

- [What is Functional Programming?](http://devlicio.us/blogs/christopher_bennage/archive/2010/09/06/what-is-functional-programming.aspx) by [Christopher Bennage](http://dev.bennage.com/)<br/>A practical overview of some common functional concepts, with examples in [F\#](http://research.microsoft.com/en-us/um/cambridge/projects/fsharp/).
- [Functional Programming For the Rest of Us](http://www.defmacro.org/ramblings/fp.html) by [Slava Akhmechet](http://www.defmacro.org/)<br/>A bit of a ramble through the history and benefits of functional programming, with key concepts illustrated in Java.
- [Functional Programming](http://www.nicollet.net/2011/10/functional-programming/) by [Victor Nicollet](https://twitter.com/victorNicollet)<br/>Solid explanation of the meaning of a pure function and the implications of functions as first-class objects.
- [Functional programs rarely rot](http://michaelochurch.wordpress.com/2012/12/06/functional-programs-rarely-rot/) by [Michael O. Church](https://twitter.com/MichaelOChurch)<br/>Fantastic article about the maintainability of functional code.

### Immutable data

- [“Minimize Mutability”](http://books.google.com/books?id=ka2VUBqHiWkC&pg=PA73&lpg=PA73&dq=josh+bloch+minimize+mutability&source=bl&ots=yYHkLmq3PY&sig=d7x0vKiUo_ILrLgm69pNELnk4Ic&hl=en&sa=X&ei=T4PJULjQHYaKjAL624DADg&ved=0CDIQ6AEwAA#v=onepage&q=josh%20bloch%20minimize%20mutability&f=false) (excerpt) from [Effective Java](http://www.amazon.com/gp/product/B000WJOUPA/ref=as_li_qf_sp_asin_tl?ie=UTF8&tag=blogblogblo0c-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=B000WJOUPA) by [Josh Bloch](https://twitter.com/joshbloch)<br/>A chapter outlining the benefits of making your objects & data immutable in Java (and a reminder that the concept isn’t new or unique to functional programming)
- [Functional programming: immutability etc](http://stackoverflow.com/questions/361066/functional-programming-immutability-etc) on StackOverflow<br/>A discussion on StackOverflow about immutable data in practice
- [Scala Collections for the Easily Bored Part 1: A Tale of Two Flavors](http://www.codecommit.com/blog/scala/scala-collections-for-the-easily-bored-part-1) by [Daniel Spiewak](https://twitter.com/djspiewak)<br/>If you were wondering how immutable data can be used for anything without slowing the JVM down to a crawl, Daniel Spiewak explains how persistent data structures work.

### Map, flatmap, and for-yield:

- [Scala Collections for the Easily Bored Part 2: One at a Time](http://www.codecommit.com/blog/scala/scala-collections-for-the-easily-bored-part-2) and [Scala Collections for the Easily Bored Part 3: All at Once](http://www.codecommit.com/blog/scala/scala-collections-for-the-easily-bored-part-3) by [Daniel Spiewak](https://twitter.com/djspiewak)<br/>In the second and third parts of the series, Spiewak goes over the higher order functions defined on Scala collections.
-   [Map, map and flatMap in Scala](http://www.brunton-spall.co.uk/post/2011/12/02/map-map-and-flatmap-in-scala/) by [Michael Brunton-Spall](https://twitter.com/bruntonspall)<br/>Walk-through of map and flatmap as they apply to Option and Map types, with plenty of examples.
-   [Chapter 10: For-Comprehensions](http://www.scala-lang.org/docu/files/ScalaByExample.pdf#page=85) from Scala By Example by [Martin Odersky](https://twitter.com/odersky)<br/>A comprehensive explanation of the for-yield notation.

### Option and other monads

- [Best explanation for Languages without Null](http://stackoverflow.com/questions/3989264/best-explanation-for-languages-without-null) on StackOverflow<br/>Some great answers to why the Option monad is useful
- [Free Yourself from the Tyranny of Null Part 1](https://blog.stackmob.com/2013/01/free-yourself-from-the-tyranny-of-null-part-1/) and [Part 2](https://blog.stackmob.com/2013/01/free-yourself-from-the-tyranny-of-null-part-2-why-weve-banned-null-in-our-codebase/) by [Doug Rapp](https://twitter.com/platykurtic)<br/>An explanation of null-free programming from a Java perspective by my coworker Doug
- [scala.Option Cheat Sheet](http://blog.tmorris.net/scalaoption-cheat-sheet/) by [Tony Morris](https://twitter.com/dibblego)<br/>A cheat sheet for Option’s higher-order functions
- [Monads Are Not Metaphors](http://www.codecommit.com/blog/ruby/monads-are-not-metaphors) by [Daniel Spiewak](https://twitter.com/djspiewak)<br/>In my opinion, the clearest explanation out there of what a monad is and why it’s useful
-   [Functors, Monads, Applicatives – can be so simple](http://thedet.wordpress.com/2012/04/28/functors-monads-applicatives-can-be-so-simple/) by [Dirk Detering](https://twitter.com/developmind)<br/>A more technical (but still clear) description of monads and some related structures
-   [Rubyists Already Use Monadic Patterns](http://dave.fayr.am/posts/2011-10-4-rubyists-already-use-monadic-patterns.html) by [Dave Fayram](https://twitter.com/KirinDave)<br/>An illuminating post showing that monadic concepts are more commonly used than you might realize. See also the same author’s excellent [FizzBuzz, A Deep Navel to Gaze Into](http://dave.fayr.am/posts/2012-10-4-finding-fizzbuzz.html), about functional patterns as applied to everyone’s favorite weed-out interview question

### Other cool Scala stuff

- [Problems Scala Fixes](http://tersesystems.com/2012/12/16/problems-scala-fixes) by [Will Sargent](https://twitter.com/will_sargent/)<br/>A tour of some of Scala’s useful (mostly) non-functional features
- [What is ‘Pattern Matching’ in functional languages?](http://stackoverflow.com/questions/2502354/what-is-pattern-matching-in-functional-languages) on StackOverflow<br/>A non-Scala specific break down of what pattern matching does and what it’s good for
-   [The Neophyte’s Guide to Scala](http://danielwestheide.com/blog/2012/11/21/the-neophytes-guide-to-scala-part-1-extractors.html) by [Daniel Westheide](https://twitter.com/kaffeecoder)<br/>A 7-part tutorial that begins with pattern matching and case classes
- [Pimp my Library](http://www.artima.com/weblogs/viewpost.jsp?thread=179766) by [Martin Odersky](https://twitter.com/odersky)<br/>A short illustration of a common pattern in Scala that uses implicit conversions

### Getting started in Scala

- [Scala for Java Refugees](http://www.codecommit.com/blog/scala/scala-for-java-refugees-part-1) by [Daniel Spiewak](https://twitter.com/djspiewak)<br/>Great starting point for Java programmers looking to explore Scala
- [Scala School](http://twitter.github.com/scala_school/) and [Effective Scala](http://twitter.github.com/effectivescala/) from Twitter<br/>An introduction to Scala and a Scala style guide used by the engineering team at Twitter
-  [Functional Programming Principles in Scala](https://www.coursera.org/course/progfun) at [Coursera](https://www.coursera.org/)<br/>A free online course led by Martin Odersky, the creator of Scala
-   [Scalatra](http://www.scalatra.org/)<br/>A lightweight web framework that’s a great place to start building web apps & APIs in Scala
- [Lift](http://liftweb.net/) and [Play](http://www.playframework.org/)<br/>Two more heavy-duty Scala web frameworks that are widely used
-   [Akka](http://akka.io/)<br/>If you’re interested in using Scala for concurrent & distributed applications, the Akka toolkit is an Actor model framework with really accessible documentation & tutorials
-  [This Week in
    \#Scala](http://www.cakesolutions.net/teamblogs/category/chrisc/)<br/>Finally, keep up with what’s going on in the Scala world by following This Week in Scala, compiled each week by [Chris Cundill](https://twitter.com/ChrisCundill)
