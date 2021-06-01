A significantly more optimized version of the DCU past exam papers website. The current site uses a google sheet as a database and makes requests to that each time someone searches for an exam paper. We scraped the contents of this doc and stored them in a csv file to improve search speeds. Additionally we made some tweaks to the UI to make the webpage more usable for everyone.

The page is not hosted anywhere and will not work locally unless you allow scripting in your browser. Otherwise for the JavaScript to run you must host the site locally or on a server.

I suggest using python3 -m http.server then opening the page in the browser but whatever works for you.


Sadly DCU refuses to take criticism or any new versions for their past papers site so it will inevitably break every semester before exams when the traffic gets too high.
