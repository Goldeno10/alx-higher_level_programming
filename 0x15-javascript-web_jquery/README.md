## JavaScript - Web jQuery
# Why JavaScript in the browser?
  Now that we can structure the document and its content with HTML, and that we 
can style it in many ways with CSS, we may want to go beyond those capabilities
(dynamically change the HTML document, perform some operations based on some current circumstances, …).
JavaScript was created with exactly that goal in mind, and is still being used as such; its recent
popular renewal as a language for scripts and web back-ends using Node.js is quite recent.
   All browsers expect HTML, CSS and JavaScript; Whatever you want to write for the web, even
the most complex applications (even GMail, Google Maps, …) will have no choice
but to be composed of those three technologies if they want to be understood by browsers.

# Introduction to AJAX 
   AJAX, short for Asynchronous JavaScript And XML, allows you to load data in the background
and display it on your webpage, without refreshing the page. This allows you to create websites
with much richer functionality. Popular web applications like Gmail, Outlook Web Access, and Google Maps
uses AJAX extensively, to provide you with a more responsive, desktop-like experience.
# Advantages
- Your page will be more pleasant to use, when you can update parts of it without a refresh, which causes the browser to flicker and the statusbar to run.
- Because you only load the data you need to update the page, instead of refreshing the entire page, you save bandwidth.
# Disadvantages
- Because the updates are done by JavaScript on the client, the state will not register in the browsers history, making it impossible to use the Back and Forward buttons to navigate between various states of the page.
- For the same reason, a specific state can't be bookmarked by the user.
- Data loaded through AJAX won't be indexed by any of the major search engines.
- People using browsers without JavaScript support, or with JavaScript disabled, will not be able to use the functionality that you provide through AJAX.
