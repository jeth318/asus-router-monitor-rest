Greetings!

This is a simple rest interface with getters on top of the asus router integration (AsusRouterMonitor) built by lmeulen https://github.com/lmeulen/AsusRouterMonitor

There is no extra authentication layer in the rest interface, I strongly suggest you add validation in your apache or nginx server configuration in order to prevent all LAN users from reading your router informtion.

If you are using nginx you can either whitelist client IP-addresses allowed to access the app, or read a header value.
