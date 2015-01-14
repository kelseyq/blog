Title: 28 GIFs Only ScalaCheck Witches Will Understand
Date: 2015-01-13 09:00
Slug: 28-GIFs-only-scalacheck-witches-will-understand

<style>
article img {
	max-width: 500px;
	display: block;
	margin-bottom: 12px;
}
</style>

<b>Because your attention span.</b> [Stew O'Connor](http://stew.vireo.org/) and I recently gave a talk on [ScalaCheck](http://www.scalacheck.org/), the property-based testing library for Scala. You can watch the [video](http://www.infoq.com/presentations/scalacheck-magic), or absorb it here in the Internet's Truest Form. Here are 28 GIFs you have to be a total ScalaCheck witch to get:

#### 1. ScalaCheck is black magick...
![](/images/scalacheck/geniebottle.gif)

#### 2. ...that can make your tests VERY powerful.
![](/images/scalacheck/muscle.gif)
The standard imperative way of writing unit tests is limited. Property-based tests are a functional approach to testing: instead of asserting how our code should behave in a specific situation, we define truths about the code's output based on the input.

#### 3. You barely have to blink:
![](/images/scalacheck/jeannie.gif)
Scalacheck automatically generates many, many inputs and then automatically verifies properties you define about what your code should output for those inputs.

#### 4. It's got a serious background:
![](/images/scalacheck/background.gif)
The library takes inspiration and its name from Haskell's [QuickCheck](http://hackage.haskell.org/package/QuickCheck), and uses the types of your input data to infer how to generate examples.

#### 5. Good things come in threes:
![](/images/scalacheck/sabrina3.gif)
ScalaCheck **generates** input, takes these inputs and **verifies** properties on them, then if it finds failures **shrinks** the failure space to the smallest possible set of failing inputs.

#### 6. You get a lot of functionality right out of the bottle:
<img alt="" src="/images/scalacheck/xtina.gif" style="width:inherit"><br/>
There are provided input generators for primitive types, Throwable, Date, tuples, functions, and many types of containers including Option, List, and Map. 

#### 7. To say nothing of your little helpers:
![](/images/scalacheck/crow.gif)
You can also make use of provided helper functions like `posNum` and `alphaNumChar`.

#### 8. Dare to live on the edge:
![](/images/scalacheck/edge.gif)
It's important to cover edge cases in your automated tests. The provided generators have a bias towards generating edge case data specific to their type. For example, the Int generator will always generate `MAX_VALUE`, `MIN_VALUE`, 0 and 1 early on; the String generator tries Strings containing non-Roman characters first.

#### 9. Sometimes it's time to get fancy:
![](/images/scalacheck/glinda.gif)
`.oneOf`, `.someOf`, `.pick` and other [methods on Gen](http://www.scalacheck.org/files/scalacheck_2.11-1.12.1-api/index.html#org.scalacheck.Gen$) allow you to get specific with your input data.

#### 10. It slices! It dices!
![](/images/scalacheck/blender.gif)
You can also compose generators using `.map`, `.flatMap`, and `.filter` (also aliased as 	`.suchThat`.) These three methods mean you can build generators using a [for-yield](http://nerd.kelseyinnis.com/blog/2013/11/12/idiomatic-scala-the-for-comprehension/). For a powerful example, check out this [recursive JSON generator](http://etorreborre.blogspot.com/2011/02/scalacheck-generator-for-json.html).

#### 11. You've got to be careful with .suchThat...
![](/images/scalacheck/lighter.gif)
`.suchThat` (aka `.filter`) generates all input and then filters out any that don't match the supplied condition. If your condition is too restrictive, you may end up with so many tests discarded that your tests don't run. Try `.retryUntil` in that situation.

#### 12. ...for more than one reason.
<img alt="" src="/images/scalacheck/witchcomputer.gif" style="width:inherit">
More philosophically, you want to be sure you’re enforcing the condition you're filtering your input data on somewhere. You might assume all of your users' ages will be under 120, but witches can live to over 300 years old!

#### 13. Sometimes the standard distribution isn't quite what you're looking for:
![](/images/scalacheck/frequency.png)
Use `Prop.collect/classify` to verify the actual distribution of your generated data and `Gen.frequency` to tweak it to your heart's desire.

#### 14. P1 bug: Beyoncé not found!
![](/images/scalacheck/beyonce.gif)
True story: we had a production bug slip through our ScalaCheck test suite because we were using `alphaNumString` to generate test data and it never detected that our users couldn't find Beyoncé with the correct acute accent. Rather than fiddle with generators, the best solution for our dataset size was to have the generator select from our possible production queries, loaded in a text file. My coworker [Will Fitzgerald](http://willfitzgerald.org/) applied this approach to a dictionary combined with usage statistics and `Gen.frequency` to create a generator that spit out plausible English text, which turned out to be useful outside of tests. Thankfully, the `.sample` method on generators extracts a plain value that can be used in any context you want. 

#### 15. Generators can do double duty for performance testing:
![](/images/scalacheck/performance.gif)
[ScalaMeter](https://scalameter.github.io/), a microbenchmarking framework, uses a very similar DSL to generate values and you can easily convert generators to share between the two types of tests. Be careful of ScalaCheck's bias towards edge cases though!

#### 16. There's a lot of ways to run:
![](/images/scalacheck/running.gif)
You can use ScalaCheck's [built-in runner](http://scalacheck.org/#quickstart) to run assertion-based ScalaCheck tests from the command line.

#### 17. It's easy to integrate:
![](/images/scalacheck/wednesday.gif)
There are provided ScalaCheck integrations for [sbt](https://github.com/rickynils/scalacheck/tree/master/examples/simple-sbt), [ScalaTest](http://www.scalatest.org/user_guide/writing_scalacheck_style_properties), and [specs2](http://etorreborre.github.io/specs2/guide/org.specs2.guide.Matchers.html#ScalaCheck). You can drop ScalaCheck into your existing test architecture without any problems.

#### 18. Time isn't always on your side:
![](/images/scalacheck/hourglass.gif)
Cases where you can exhaust the entire test space are rare. Usually, you're limited by how long the tests will take to run. The concurrency level, number of successful tests required, and size of generated collections in ScalaCheck tests are all [configurable](http://www.scalacheck.org/files/scalacheck_2.11-1.12.1-api/index.html#org.scalacheck.Test$$Parameters).

#### 19. Spin it right round:
![](/images/scalacheck/roundtrip.gif)
If you're encoding & decoding, roundtrip properties are an elegant way to test both methods: take a generated input, encode it then decode the encoded value and verify that the result equals the original input.

#### 20. Invalid inputs are just as important to test as valid ones:
![](/images/scalacheck/cyanide.gif)
The Basho team has a good [writeup](http://basho.com/quickchecking-poolboy-for-fun-and-profit/) of their experience using property-based testing on negative inputs to discover and fix issues with the worker pool used for Riak.

#### 21. Don't limit your powers:
![](/images/scalacheck/pencil.gif)
Jessica Kerr has used Scalatest's Selenium integration with ScalaCheck to create [property-based tests of JavaScript](https://github.com/jessitron/js-with-scalacheck) without writing any extra JavaScript!

#### 22. You can command more than just methods:
![](/images/scalacheck/command.gif)
ScalaCheck's input-output model is meant for testing functions, but the framework also provides a model for testing stateful code. After you specify possible commands with pre and post conditions, the tests generate sequences of commands and verify that the conditions have held. See it in action testing Redis [here](http://scalacheck.org/files/scaladays2014/index.html#1).

#### 23. It only gets cooler from there:
![](/images/scalacheck/ooh.gif)
Rickard Nilsson, the creator of ScalaCheck, uses the command model with [Nix](https://nixos.org/nix/), the functional build tool, to test server networks. He generates VMs with randomly generated memory, OS versions, and IP addresses and uses commands to test what happens when they ping each other.

#### 24. Property-based testing scales up:
![](/images/scalacheck/network.gif)
Simulation testing applies the concept of property-based testing to entire systems. [Simulant](https://github.com/Datomic/simulant/wiki/Overview) is a simulation testing framework written in Clojure; it uses statistical modelling to generate test data and records outputs. Properties become queries that can be verified strictly or fuzzily.

#### 25. Even better, it scales down:
![](/images/scalacheck/shrink.gif)
One of the most useful features of ScalaCheck is shrinking. When a failure is found, ScalaCheck stops generating new cases. It tries to apply the failing property against successively "smaller" failure cases so it can present you with the most specific information it can discover about the failure. `Shrink` (and the concept of a "smaller" failure case) is defined per type--for example, `Int` literally [gets smaller](https://github.com/rickynils/scalacheck/blob/1.12.1/src/main/scala/org/scalacheck/Shrink.scala#L87). With a tuple it'll try to shrink [each member individually](https://github.com/rickynils/scalacheck/blob/1.12.1/src/main/scala/org/scalacheck/Shrink.scala#L110), and it'll methodically [remove chunks](https://github.com/rickynils/scalacheck/blob/1.12.1/src/main/scala/org/scalacheck/Shrink.scala#L62) from a list.

#### 26. In practice, you barely have to lift a finger:
![](/images/scalacheck/lightasfeather.gif)
Go watch Stew show ScalaCheck off in the [video](http://www.infoq.com/presentations/scalacheck-magic) already!

#### 27. Property-based testing: not only for Scala!
![](/images/scalacheck/morewitches.gif)
Besides the aforementioned [QuickCheck](https://hackage.haskell.org/package/QuickCheck) for Haskell, there are property-based testing frameworks for [many other languages](https://gist.github.com/npryce/4147916).

#### 28. Thank you so much, you've been wonderful.
![](/images/scalacheck/fairuza.gif)
