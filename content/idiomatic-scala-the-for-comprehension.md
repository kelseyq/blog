Title: Idiomatic Scala: The For-Comprehension
Date: 2013-11-12 16:00
Slug: idiomatic-scala-the-for-comprehension

If you’re new to functional programming, it may be hard to see the
practical use of FP constructs in a real-world code base. This talk,
originally delivered at LambdaJam and PNW Scala, aims to show you how
you can get real, immediate benefits in safety & maintainability from
introducing functional structures without throwing out all your current
models & ways of thinking about them. I concentrate on the idiomatic
Scala “for-yield” or “for comprehension” and go over several types of
applications of for-yield statements.
<center>
<iframe width="560" height="315" src="//www.youtube.com/embed/MHw-dDxC8Z4" frameborder="0" allowfullscreen></iframe>
</center>

Code examples from the talk:

Using for-yield, we translated this nested list iteration:

	:::scala
	case class Postcard(msg: String)
	
	def sendPostcards: List[Postcard] = {
	    val states = List("Arizona", "New Mexico",
	                          "Texas", "Louisiana",
	                          "Mississippi", "Virginia",
	                          "New York", "Ohio",
	                          "Illinois")
	    val relatives = List("Grandma", "Grandpa", "Aunt Dottie", "Dad")
	    val travellers = List("Kelsey", "DJ")
	
	    var postcardList: List[Postcard] = List()
	
	    for (h <- 0 until travellers.length) {
	        val sender = travellers(h)
	
	        for (i <- 0 until relatives.length) {
	            val recipient = relatives(i)
	
	            for (j <- 0 until states.length) {
	                val theState = states(j)
	                postcardList ::=
	                    new Postcard("Dear " + recipient + ", " +
	                                  "Wish you were here in " +
	                                  theState + "! " +
	                                  "Love, " + sender)
	            }
	        }
	    }
	
	    postcardList
	}

into this:

	:::scala
	def sendPostcards3: List[Postcard] = {
	    val states = List("Arizona", "New Mexico",
	                          "Texas", "Louisiana",
	                          "Mississippi", "Virginia",
	                          "New York", "Ohio",
	                          "Illinois")
	    val relatives = List("Grandma", "Grandpa", "Aunt Dottie", "Dad")
	    val travellers = List("Kelsey", "DJ")
	
	    for {
	        traveller <- travellers
	        sender = traveller + " (your favorite)"
	        relative <- relatives
	        theState <- states
	        if (relative.startsWith("G"))
	    } yield {
	        new Postcard("Dear " + relative + ", " +
	                        "Wish you were here in " +
	                         theState + "! " +
	                         "Love, " + sender)
	    }
	}

We learned about Option and turned this:

<center>
![](http://nerd.kelseyinnis.com/images/fakeOption.png)
</center>

into:

<center>
![](http://nerd.kelseyinnis.com/images/optionforyield.png)
</center>

We handled exceptions by wrapping code in a Try, making:

<center>
![](http://nerd.kelseyinnis.com/images/exceptionhandling.png)
</center>

look like:

<center>
![](http://nerd.kelseyinnis.com/images/tryforyield.png)
</center>

Finally, we chained long-running asynchronous calls while avoiding
cumbersome callbacks with Future:

<center>
![](http://nerd.kelseyinnis.com/images/withfutures.png)

</center>

<center>
![](http://nerd.kelseyinnis.com/images/futureforyield.png)
</center>

If you’re ready to learn more about functional programming, check out my
list of [resources for getting started with FP and
Scala](/blog/2013/01/07/resources-for-getting-started-with-functional-programming-and-scala/).


