Title: How to Make an HTTP Call in Clojure When You Don't Know Anything
Date: 2014-04-22 07:01
Slug: how-to-make-an-http-call-in-clojure-when-you-dont-know-anything

**first**: Download [leiningen](http://leiningen.org/), or check to see
that it’s still there from the time you said you were going to try
Clojure 18 months ago (that’s `lein --version`, not `-V` or `-s` or
whatever other gajillion things you’ll try first)

**second**: Download [Light Table](http://www.lighttable.com/), which
barely existed 18 months ago!

**third**: Run `lein new i_am_a_golden_god` to create a new project.
Open Light Table & select View \> Workspace then right-click in the left
pane to add your newly created folder to the workspace. Skip the 4
minutes of bumbling around clicking aimlessly it took me to figure that
out.

**fourth**: Open `project.clj` and change the `:description` and `:url`
keys. The leading colons mean they are
[keywords](http://clojure.org/data_structures#toc8), which are basically
super-speedy strings often used as keys in maps. `defproject` more or
less takes a map for its arguments, but it’s using a feature called
[destructuring](http://blog.jayfields.com/2010/07/clojure-destructuring.html)
that is a way to achieve named arguments and also a pretty fantastically
silly place to start in a new language. Hey, I just put the links in the
blog post, I don’t force you to click on them.

**fifth**: Add [clj-http](https://github.com/dakrone/clj-http) to your dependencies:

    :::clojure
    (defproject i_am_a_golden_god "0.1.0-SNAPSHOT"
      :description "FIXME: I WAS NEVER BROKEN"
      :url "http://www.greatbigstuff.com/"
      :license {:name "Eclipse Public License"
                :url "http://www.eclipse.org/legal/epl-v10.html"}
      :dependencies [[org.clojure/clojure "1.5.1"]
                     [clj-http "0.6.0"]])


Stuff between square brackets is a
[vector](http://clojuredocs.org/clojure_core/clojure.core/vector), which
is a lot like an array. Each dependency in our project file is a vector
where the first member is the name the dependency is registered under
(in Leiningen’s adorably-named default repository
[Clojars](https://clojars.org/)) and the second member is the version
number we want to download. The `:dependencies` key corresponds to a
vector of these dependency vectors.

**fifth and a half**: Get distracted down a crappy rabbit-hole with a
whole bunch of outdated info about needing a special plugin to run lein
projects in Light Table. Light Table now downloads deps for you! Catch
up, Internet!

**sixth**: Find the stub file that lein made for you in
`i_am_a_golden_god/src/i_am_a_golden_god/core.clj`. Even though you see
a ”`println`” and you’ve learned from View \> Commands that
cmd-shift-enter evaluates the editor’s contents, despair over nothing
being printed. Use some hard-earned JVM debugging experience to realize
that you’re missing a main method. We want our main method to call
`foo`, how????

**seventh**: 
Time for a `foo` breakdown:

    :::clojure
	(defn foo
	  "I don't do a whole lot."
	  [x]
	  (println x "Hello, World!"))
	  	  
[defn](http://clojuredocs.org/clojure_core/clojure.core/defn) is how a
named function is defined in Clojure. It takes the name of the function,
an optional doc string, then a vector of parameters, then a body. First
taste of our infamous [Lisp nested parentheses](http://xkcd.com/297/)!
Turns out like how square brackets mean a vector, parentheses mean a
list. Your function body (which calls the library function
[println](http://clojuredocs.org/clojure_core/1.2.0/clojure.core/println))
is just a list, where the first value is the name of the function and
the next two values are its args. But wait the whole `defn foo` shebang
is wrapped in parens, so it’s just a list too. Guess what: EVERYTHING IN
CLOJURE IS A LIST. This is AMAZING and INSANE and turns out to be SUPER
POWERFUL. No time to dwell on it now, just let that fact float on top of
your brain and keep you up later tonight.

So: to define a main function, you’ll do:
    
    :::clojure
    (defn -main [] (foo "Kelsey"))

in the same file. Looks a lot like foo – `defn`, the function name,
you’ll skip the doc string cause you’re a jerk like me, an empty
argument vector, then a body (that’s ALSO A LIST AAAAH) where you call
`foo`. The `-` in front of `main` indicates the method is static, as
Java main methods are [required to
be](http://stackoverflow.com/a/151666/1308611). I found this out by
Googling, not because I’m some sort of JVM whisperer, in case you were
worried.

**eighth**: Ugh why doesn’t cmd-shift-enter do anything ugh I gave you a
stupid main method ugh what do you even want ugh! Oh, might help to
actually call main. Plop `(-main)` at the end of `core.clj`.

**ninth**: OH SWEET JAYSUS IT’S PRINTLN-ING! Do a little victory dance
(required step.)

**tenth**: Mess with foo a little.
    
    :::clojure
    (defn foo
      "Bow down before me, Clojure"
      [x]
      (println "I am become" x "the destroyer of worlds"))

**eleventh** Remember why we’re here. Import the `clj-http` client into
your app by changing `(ns i-am-a-golden-god.core)` to
    
    ::clojure
    (ns i-am-a-golden-god.core
        (:require [clj-http.client :as client]))
  
While you’re in the [clj-http
README](https://github.com/dakrone/clj-http), looks like a simple GET
call is `(client/get "http://site.com/resources/id")`. The forward slash
means you’re calling the `get` method in the `client`
[namespace](http://clojuredocs.org/clojure_core/clojure.core/require)
you defined in `:require`. Use your newfound method-defining expertise
to define an `httpCall` method that makes a GET call to a passed-in URL:

    :::clojure
    (defn httpCall
      [url]
      (println (client/get url)))
  
then call it from your main method:
    
    :::clojure
    (defn -main [] (httpCall "https://twitter.com/A_single_bear"))

**twelfth**: Feel somewhat unsatisfied with the bracket-y mess of HTML
returned. Think to yourself, “How hard could it be to parse JSON in a
language I’ve never used before?” Laugh so loud you wake up everyone in
the house. (Later, be pleasantly surprised!) Look for an unauthenticated
JSON API cause you’re too lazy to deal with OAuth. Find [something
perfect](https://github.com/amoslanka/ermahgerd). Pass query params as
[a map](http://clojuredocs.org/clojure_core/clojure.core/hash-map).
Figure out how to [access map values by
key](http://clojuredocs.org/clojure_core/1.3.0/clojure.core/get#example_934)
to get just the body from the response. Import [another
library](https://github.com/clojure/data.json). Access a map value in [a
different
way](http://clojuredocs.org/clojure_core/1.3.0/clojure.core/get#example_217),
just for fun. Break your code down into tidy lil functions. Finally,
declare…

    :::clojure
    (ns i-am-a-golden-god.core
      (:require [clj-http.client :as client]
                [clojure.data.json :as json]))
    
    (defn extractJson
      [responseBody]
      (get (json/read-str responseBody) "value1"))
    
    (defn makeCall
      [url input]
       (:body
        (client/get url
                    {:query-params {"value1" input}})))
    
    (defn getIt
      [url input]
       (println
        (extractJson
         (makeCall url input))))
    
    (defn -main [] (getIt "http://ermahgerd.herokuapp.com/ternslert" 
                          "I am become Kelsey, destroyer of worlds"))

    (-main)

I ERM BERCERME KERLSER, DERSTRER ERF WERLDS
-------------------------------------------

**thirteenth**: GO THE F\*\*\* TO SLEEP. <small><small><small>(but just
before you drift off, remember suddenly…it’s all made of
lists…)</small></small></small>

