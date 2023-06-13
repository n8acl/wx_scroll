# Weather Scroller
Weather Data Scroller for the Raspberry Pi Sense-Hat

---
# Description

Here is a fun litle project I put together. I was sitting looking at the LED matrix on my Sense-hat and thought, "I should have weather data scroll across there". So that is what I did. 

This script will pull local weather data from the OpenWeatherMap API and from the sensors on the Sense-Hat and scrolls the temperatures across the screen.

You do need to have a Sense-Hat and a Raspberry Pi to run this script. Make sure you have the Sense-Hat API Library installed on the Pi.

## Text Colors

The text is colored based on the temperature reading.
| Color | Meaning |
|-------|---------|
|blue|Temp below 50 Degrees|
|green|Temp between 50 and 75 Degrees|
|red|Temp is greater then 75 Degrees|


## API's Used

This bot pulls data from the following locations:

| Service | Description | Website |
|---------|---------|---------|
|OpenWeatherMap|Used to pull weather data based on Zip Code|[https://openweathermap.org/](https://openweathermap.org/)|

---

# Installation/Setup

### Get OpenWeatherMap API Key
For this you only need to obtain one API Key, and that is from OpenWeatherMap. To get this key go to [https://openweathermap.org/api](https://openweathermap.org/api) and sign up for a free account.
  - NOTE: This is a free account, but you are limited to 60 calls per minute and 1000 calls per day. 

### Installing the Script

The next step is installing the needed packages, cloning the repo to get the script and then installing the needed libraries for the script to work properly.

This is probably the easiest step to accomplish.

Please run the following commands:

```bash
sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get -y dist-upgrade

sudo apt-get install python3 python3-pip git screen

git clone https://github.com/n8acl/wx_scroll.git

cd wx_scroll

pip3 install -r requirements.txt
```

Now you have everything installed and are ready to configure the script.

## Configure the Script
Once you have your API Key, have cloned the repo and installed everything, you can now start configuring the script. Open the config.py file in your editor of choice and fill in the following spots:

```python
# Configure variables
openweathermap_apikey = 'YOUR OPENWEATHERMAP API KEY HERE'
zipcode = 'YOUR ZIP CODE HERE'
scroll_delay_time = 15 # Scroll delay. Set in Seconds. This delays the amount of time between scrolls. 
use_timer = True # Use the sleep timer function. Yes use it = True, No Don't = False
start_time = '07:30AM' # This is the time for the display to turn on
end_time = '09:30PM' # This is the time for the display to turn off
```

* ```openweathermap_apikey``` This is, of course your OpenWeatherMap API Key.
* ```zipdcode``` This is your Zip Code. This allows the script to pull the weather data for the correct location.
* ```scroll_delay_time``` This sets the delay time between message scrolls on the screen. This is set in Seconds. It defaults to 15 Seconds
* ```use_timer``` enables or disables the sleep timer function. This allows the program to turn off the display outside the hours set below by the ```start_time``` and ```end_time``` variables.
* ```start_time``` This is the time you want the script to "Turn On", that is start scrolling the messages. Make sure to follow the example format.
* ```end_time``` This is the time you want the script to "Turn off", that is when to stop scrolling the message on the screen. Make sure to follow the example format.

## Running the Script

Once you have the config file edited, start the bot by typing the following:

```bash
screen -R wx_scroll
```

Then in the new window:
```bash
cd sx_scroll

python3 wx_scroll.py
```

If something ever happens, you can reconnect to the session by typing:

```bash
screen -R wx_scroll
```

And see why it errored or quit. This is useful if you need to contact me for support. That also allows you to restart the script.

---

## Contact
If you have questions, please feel free to reach out to me. You can reach me in one of the following ways:

- Discord: Ravendos
- Mastodon: @n8acl@mastodon.radio
- E-mail: n8acl@qsl.net

Or open an issue on Github. I will respond to it, and of course you, when I can. Remember, this is a hobby and there are other daily distractors that come first, like work, school and family.

If you reach out to me and have an error, please include what error you are getting and what you were doing. I may also ask you to send me certain files to look at. Otherwise just reach out to me :).

---

## Change Log
* 02/16/2022 - Initial Release 1.0