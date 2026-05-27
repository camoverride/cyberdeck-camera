## Set Up

## Client

- `git clone git@github.com:camoverride/cyberdeck-camera.git`
- `cd cyberdeck-camera`
- `sudo apt update`
- `sudo apt install -y python3-picamera2 python3-libcamera`
- `python3 -m venv .venv --system-site-packages`
- `source .venv/bin/activate`
- `pip install -r requirements-client.txt`

Inside `client.py` edit the line under `# Config` to set the correct IP address.

Start a service with systemd. This will start the program when the computer starts and revive it when it dies:

- `mkdir -p ~/.config/systemd/user`
- `cat client.service > ~/.config/systemd/user/client.service`

Start the service using the commands below:

- `systemctl --user daemon-reload`
- `systemctl --user enable client.service`
- `systemctl --user start client.service`

Start it on boot:

- `sudo loginctl enable-linger $(whoami)`

Get the logs:

- `journalctl --user -u client.service`


## Server

- `git clone git@github.com:camoverride/cyberdeck-camera.git`
- `cd cyberdeck-camera`
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements-server.txt`
- `sudo apt remove gnome-keyring` (prevent keyring pop-up when running chromium)
- `sudo reboot`

View on Pi: 
- `export DISPLAY=:0`
- `chromium-browser --kiosk --incognito --noerrdialogs --disable-infobars --disable-session-crashed-bubble http://127.0.0.1:5000`

Start a service with systemd. This will start the program when the computer starts and revive it when it dies:

- `mkdir -p ~/.config/systemd/user`
- `cat server.service > ~/.config/systemd/user/server.service`

Start the service using the commands below:

- `systemctl --user daemon-reload`
- `systemctl --user enable server.service`
- `systemctl --user start server.service`

Start it on boot:

- `sudo loginctl enable-linger $(whoami)`

Get the logs:

- `journalctl --user -u server.service`
