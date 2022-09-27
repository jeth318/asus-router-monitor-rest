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
    PORT="Your port of preference" (will default to 3555 if not set here)

Usage:
If you want to fork the app in the background instead, I suggest using PM2:
`pm2 start app.py --interpreter python3 --name asus-router-monitor-rest --watch`
If you just want to spin it up as is, then run `python app.py` in your terminal while in the app root directory.

The server will now be live at http://localhost:3555.
Access the API through the following endpoints:

- /settings
- /clients-info
- /client-info/[id] (mac-address in the format XX-XX-XX-XX-XX)
- /online-clients
- /dhcp-list
- /cpu-usage
- /memory-usage

For detailed documentation of the return values for each endpoint, please visit https://github.com/lmeulen/AsusRouterMonitor and checkout the corresponding values. While you're there, give the guy a star!
