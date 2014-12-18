Title: Talking to Yourself: A Twitter Bot in Clojure as a Total Newb
Date: 2014-05-06 20:04
Slug: talking-to-yourself-a-twitter-bot-in-clojure-as-a-total-newb

<style>
.codehilitetable {
	font-size:75%;
}
</style>

Although the [ermahgerd API](https://github.com/amoslanka/ermahgerd) we
called in our first [explorations in
Clojure](http://nerd.kelseyinnis.com/blog/2014/04/22/how-to-make-an-http-call-in-clojure-when-you-dont-know-anything/)
is pretty much endlessly useful, we want to push our Clojure
non-abilities farther with something a bit more complicated–and what
could be more complicated than Twitter?

We’ll start by making a restful call with the [twitter-api
library](https://github.com/adamwynne/twitter-api). After running
`lein new app twitterbot` to set up a project, we’ll need to declare a
dependency on twitter-api in our `project.clj` by adding
`[twitter-api "0.7.5"]` to the `:dependencies` vector. Next, our Twitter
bot won’t be much fun without some Twitter. Start a new account and set
yourself up with [a new application](https://apps.twitter.com/).
Authorize your bot-self for it with read permission; we’ll come back to
get write permission later. For a bot, a [dev.twitter.com
token](https://dev.twitter.com/docs/auth/tokens-devtwittercom) is
sufficient. Go ahead and tweet at the baby bot a few times, so we can
retrieve the mentions.

	:::clojure
	(ns tipbot.core
	  (:use
	   [twitter.oauth]
	   [twitter.callbacks]
	   [twitter.callbacks.handlers]
	   [twitter.api.restful])
	  (:import
	   (twitter.callbacks.protocols SyncSingleCallback)))
	
	(def my-creds (make-oauth-creds "my-special-personal-app-consumer-key"
	                                "none-of-your-business-app-consumer-secret"
	                                "mine-and-only-mine-user-access-token"
	                                "no-you-cant-have-my-user-access-token-secret"))
	
	(defn -main
	  []
	  (println
	      (statuses-mentions-timeline :oauth-creds my-creds
	                                :params {:screen-name "abotcalledquest"})))
                                
This prints out the entire, wordy HTTP response. The library provides
predefined callbacks. Let’s try one that only returns the body of the
response:

	:::clojure
	(defn -main
	  []
	  (println
	      (statuses-mentions-timeline :oauth-creds my-creds
	                                  :params {:screen-name "abotcalledquest"}
	                                  :callbacks (SyncSingleCallback. response-return-body
	                                                                  response-throw-error
	                                                                  exception-rethrow)))


That slims the response down some, but let’s try to get just the text of
the tweets. There’s a handy
[type](http://clojuredocs.org/clojure_core/clojure.core/type) method
that we can use to figure out that we’re dealing with a vector of maps.
We learned all kindsa ways to extract a value from a map last time, but
how to do that for each value in the vector of tweets? Well, as a proud
[Lambda Lady](http://www.lambdaladies.com) I know that [the superior way
to iterate is a higher-order map
function](http://nerd.kelseyinnis.com/blog/2012/12/17/slides-from-learning-functional-programming-without-growing-a-neckbeard/)–and
indeed, Clojure has a tidy [map
function](http://clojuredocs.org/clojure_core/1.3.0/clojure.core/map).
Yes, confusingly, this has nothing to do with the map datastructure. Nor
does it have anything to do with cartography, though that’s also
awesome. Onward!

***EDIT***
My instincts about `map` were sort of wrong as it turns out! See [this
excellent
comment](http://nerd.kelseyinnis.com/blog/2014/05/06/talking-to-yourself-a-twitter-bot-in-clojure-by-a-total-newb/#comment-1374191718)
from [Zane](https://twitter.com/zaneshelby) on why we should wrap
something that `map`s over a sequence in
[dorun](http://clojuredocs.org/clojure_core/clojure.core/dorun).

	:::clojure
	(defn -main
	  []
	  (dorun
	      (println 
	          (map :text
	              (statuses-mentions-timeline :oauth-creds my-creds
	                                      :params {:screen-name "abotcalledquest"}
	                                      :callbacks (SyncSingleCallback. response-return-body
	                                                                      response-throw-error
	                                                                      exception-rethrow))))))
	                                                                                                          
	                                                                                                          We want the user as well as the text, though, so we’re going to use [select-keys](http://blog.jayfields.com/2011/01/clojure-select-keys-select-values-and.html).
`select-keys` takes the response map as the *first* param though. How
can we pass this function to `map`? In Scala we’d use an underscore as a
placeholder.

To \#clojure IRC! [Alan Malloy](https://github.com/amalloy) showed me
that if I preface the function with \#, I can use `%` as a placeholder,
as in `#(select-keys % [:text :user])`, which can be passed to `map`.
This, as it turns out, is shorthand (via a special-case [reader
macro](http://en.wikibooks.org/wiki/Learning_Clojure/Reader_Macros)) for
[fn](http://clojuredocs.org/clojure_core/clojure.core/fn#example_408),
the way to declare an anonymous function in Clojure.
`#(select-keys % [:text :user])` is the same as writing
`(fn [x] (select-keys x [:text :user]))`. Handy!

	:::clojure
	(defn -main
	  []
	  (dorun 
	      (println 
	      (map #(select-keys % [:text :user])
	              (statuses-mentions-timeline :oauth-creds my-creds
	                                           :params {:screen-name "abotcalledquest"}
	                                           :callbacks (SyncSingleCallback. 
	                                                               response-return-body
	                                                               response-throw-error
	                                                               exception-rethrow))))))


Turns out the user has a *lot* of info. We want to get the user’s id
only. There’s a couple of ways of getting at [nested values in
maps](http://www.learningclojure.com/2009/09/nested-def-me-name-firstname-john.html)
in Clojure (don’t sleep on that arrow, we’ll come back to it!) Let’s use
`get-in` to pull the user id out here.

	:::clojure
	(defn -main
	  []
	  (dorun
	      (println 
	      (map #(get-in % [:user :id_str])
	              (statuses-mentions-timeline :oauth-creds my-creds
	                                           :params {:screen-name "abotcalledquest"}
	                                           :callbacks (SyncSingleCallback. 
	                                                               response-return-body
	                                                               response-throw-error
	                                                               exception-rethrow))))))



This works, but we need both the user id and the tweet’s text. Let’s go
ahead and pull the response formatting step out into its own function.

	:::clojure
	(defn extractTweetInfo
	  [tweetMap]
	  {:tweet (:text tweetMap), :user (get-in tweetMap [:user :id_str])})
	
	(defn -main
	  []
	  (dorun
	      (println 
	      (map extractTweetInfo
	              (statuses-mentions-timeline :oauth-creds my-creds
	                                           :params {:screen-name "abotcalledquest"}
	                                           :callbacks (SyncSingleCallback. 
	                                                               response-return-body
	                                                               response-throw-error
	                                                               exception-rethrow))))))


Ok, now we’ve got all the mentions, but we are building a bot of
discerning taste here. We want to
[filter](http://clojuredocs.org/clojure_core/clojure.core/filter) just
the tweets that include a certain line of text. Java, which Clojure
compiles to, has a fine method for detecting substrings already. Calling
Java from Clojure is a simple matter of [adding
dots](http://blog.jayfields.com/2011/12/clojure-java-interop.html).
We’ll bring back our anonymous function syntax to make this work:

	:::clojure
	(defn -main
	  []
	  (dorun
	      (println
	      (filter #(.contains (:tweet %) "can i kick it")
	              (map extractTweetInfo
	              (statuses-mentions-timeline :oauth-creds my-creds
	                                               :params {:screen-name "abotcalledquest"}
	                                               :callbacks (SyncSingleCallback. 
	                                                             response-return-body 
	                                                             response-throw-error 
	                                                             exception-rethrow))))
                                                                           
That anonymous function looks a bit backwards doesn’t it? It’s hard to
read it from the inside out. Enter the arrow! The function being passed
to `filter` can be rewritten as
`#(-> % :tweet (.contains "can i kick it"))` using the [threading
macro](http://clojuredocs.org/clojure_core/clojure.core/-%3E). Like
[Jessica](http://blog.jessitron.com/2014/04/left-to-right-top-to-bottom.html),
I find this very exciting! Turns out we can do
([almost](http://clojuredocs.org/clojure_core/clojure.core/-%3E%3E)) the
same thing to the entire method & it reads a lot like how you’d describe
what we doing in English:

	:::clojure
	(defn -main
	  []
	  (dorun
	    (->> (statuses-mentions-timeline :oauth-creds my-creds
	                                   :params {:screen-name "abotcalledquest"}
	                                   :callbacks (SyncSingleCallback. response-return-body  
	                                                                   response-throw-error  
	                                                                   exception-rethrow))
	         (map extractTweetInfo)
	         (filter #(-> % :tweet (.contains "can i kick it")))
	         (println))))
         
Of course, not to respond would be très rude. We’ll need to change our
app permission to allow writes, which may be more or less easy depending
on your current level of Twitter phone number authentication. I had to
set up a freakin Google Voice number, oy. Once that’s handled, add a
reply method and map over the result set with it:

	:::clojure
	(defn extractTweetInfo
	  [tweetMap]
	  {:tweet (clojure.string/lower-case (:text tweetMap)), :tweet_id (:id_str tweetMap),
                                          :user (get-in tweetMap [:user :id_str]),
                                          :screen-name (get-in tweetMap [:user :screen_name])})
	
	(defn replyToTweet
	  [tweetMap]
	  (statuses-update :oauth-creds my-creds
	                   :params {:status (str "@" (:screen-name tweetMap) " yes you can"),
	                            :in_reply_to_status_id (:tweet_id tweetMap)}
	                            :callbacks (SyncSingleCallback. response-return-body
	                                                            response-throw-error
	                                                            exception-rethrow)))
	
	(defn -main
	  []
	  (dorun
	    (->> (statuses-mentions-timeline :oauth-creds my-creds
	                                   :params {:screen-name "abotcalledquest"}
	                                   :callbacks (SyncSingleCallback. response-return-body
	                                                                   response-throw-error
	                                                                   exception-rethrow))
	         (map extractTweetInfo)
	         (filter #(-> % :tweet (.contains "can i kick it")))
	         (map replyToTweet)
	         (println))))
         
We can now ask our bot the fateful question, and upon running our
program …

![](http://nerd.kelseyinnis.com/images/ciki.png)

Hooray!

…kind of. We can’t run it again because it pulls & responds to all
mentions, whether already responded to or not, and Twitter rejects
duplicate tweets. Even if we fix that, we have to constantly poll for
new Tweets, and we’ll surely run afoul of Twitter’s rate limits very
quickly. Next blog-time, we’ll make the big switch to use the streaming
API. Spoiler alert: THAR BE DRAGONS. SCALY, MUTABLE STATE DRAGONS.

