Title: Checking a service's status in the background in Lift using lazy-load
Date: 2012-05-01 18:00
Slug: checking-a-services-status-in-the-background-in-lift-using-lazy-load

At [work](http://www.stackmob.com) we recently built an HTML5 &
JavaScript hosting service that pulls files from
[GitHub](http://www.github.com). Of course, we managed to release this
feature smack in the middle of GitHub’s recent [DDOS
woes](http://github.com/blog/1036-about-this-week-s-availability).

Because GitHub’s outages were intermittent and other parts of our
functionality worked, we wanted some way of letting our users know if we
couldn’t reach GitHub. The outages sometimes manifested themselves as a
timeout rather than a returned error, so I didn’t want to block the
entire UI from loading while I waited to see if a request to GitHub
would terminate or not. I was starting to look at Lift’s powerful [Comet
support](http://www.assembla.com/spaces/liftweb/wiki/Comet_Support) when
the lovely and helpful [dpp](http://blog.goodstuff.im/) (who we are
lucky enough to share an office with!) suggested that I look at
[lazy\_load](http://demo.liftweb.net/lazy).

<!--more-->

The slightly tricky part was catching timeouts before `lazy_load`’s
default 2 minute timeout period ends. I was able to do that by
[tinkering with the Apache
HTTPClient](http://blog.jayway.com/2009/03/17/configuring-timeout-with-apache-httpclient-40/)
that is wrapped by the
[Dispatch](http://dispatch.databinder.net/Dispatch.html) library.

	:::scala
	import xml.NodeSeq
	import org.apache.http.params.HttpConnectionParams
	import org.apache.http.conn.ConnectTimeoutException
	import net.liftweb.common._
	import dispatch._
	
	def ping(xhtml : NodeSeq) : NodeSeq = {
	  val connectionTimeoutMillis = 10000;
	  val socketTimeoutMillis = 10000;
	  val http = new Http with thread.Safety
	  val httpParams = http.client.getParams
	  HttpConnectionParams.setConnectionTimeout(httpParams, 
	                                            connectionTimeoutMillis);
	  HttpConnectionParams.setSoTimeout(httpParams, socketTimeoutMillis);
	
	  val gitHubReq = url("https://api.github.com/user/repos") 
	                    <<? Map("access_token" -> gitHubAccessToken)
	
	  val pingResult = try {
	    http x(gitHubReq as_str) {
	      case (200, _, _, out) => Full(out())
	      case (error, _, _, out) => 
	          Failure("GitHub HTTP request failed with error code " + 
	                     error + ": " + out());
	    }
	  } catch {
	    case e: ConnectTimeoutException => 
	        Failure("GitHub HTTP request timed out")
	  } finally {
	    http.shutdown()
	  }
	
	  (pingResult failMsg "GitHub HTTP request returned empty") match {
	    case Failure(msg, _, _) => { 
	      log(msg)
	      <span class="error">We're currently having trouble connecting
	      to GitHub (<a href="https://status.github.com/">status</a>). 
	      Parts of this page might not work right now.<br /><br /></span> 
	    }
	    case _ => NodeSeq.Empty
	  }
	}


Surrounding a template call to this method with `lift:lazy-load` causes it
to load in the background after the rest of the page loads. One minor
wrinkle is that lazy-load displays a spinning indicator by default; you
can override this behavior with the `template` attribute. Since I didn’t
want anything to be displayed unless there was a problem, I created an
`empty.html` template that just contains a `<span/>`.
	
	:::scala
	<lift:lazy-load template="empty">
	  <lift:GitHub.ping />
	</lift:lazy-load>

Unexpected side effect of this code: now any time I go to pull a repo or
start a build and GitHub is down, I’m super excited to go to my page and
see the warning working.

