Greetings!

This is a simple rest interface with getters on top of the asus router integration (AsusRouterMonitor) built by lmeulen https://github.com/lmeulen/AsusRouterMonitor

There is no extra authentication layer in the rest interface, I strongly suggest you add validation in your apache or nginx server configuration in order to prevent all LAN users from reading your router informtion.

If you are using nginx you can either whitelist client IP-addresses allowed to access the app, or read a header value.

Setup and install:

    Dependencies:

    - flask (pip install flask)
    - dotenv (pip install dotenv)

    Installation:

    - Clone the repo
    - Create a file called .env in the root directory
    - Add the following values:

    ROUTER_IP="your-routers-internal-ip" (usually 192.168.1.1 or 10.0.0.1)
    ROUTER_USER="Your username used for logging in to the router admin GUI"
    ROUTER_PASS="Your password used for logging in to the router admin GUI"
