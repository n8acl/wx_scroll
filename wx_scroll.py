#################################################################################

# WX Scroll
# Developed by: Jeff Lehman
# Current Version: 1.0
# https://github.com/n8acl/wx_scroll

# Questions? Comments? Suggestions? Contact me one of the following ways:
# E-mail: n8acl@qsl.net
# Twitter: @n8acl
# Discord: Ravendos#7364
# Mastodon: @n8acl@mastodon.radio
# Website: https://www.qsl.net/n8acl

###################   DO NOT CHANGE BELOW   #########################

###################################################
# Import Libraries

import config as cfg
import sys
import os
import time
import json
import requests
from time import sleep
from datetime import datetime, time, timedelta
from sense_hat import SenseHat

###################################################
# Define Variables/objects

sense = SenseHat()

degree_sign= u'\N{DEGREE SIGN}'
linefeed = "\n"
timestart = datetime.strptime(cfg.start_time, "%I:%M%p")
timeend = datetime.strptime(cfg.end_time, "%I:%M%p")
wx_url = "http://api.openweathermap.org/data/2.5/weather?zip="+ cfg.zipcode + ",us&units=imperial&APPID=" + cfg.openweathermap_apikey
first_run = True

blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)

###################################################
# Define Functions

def get_api_data(url):
    # get JSON data from api's with just a URL
    return requests.get(url=url).json()

def get_curr_wx():
    # Return Conditions and Temp for the packet location.

    data = get_api_data(wx_url)
    return data['weather'][0]['main'], data['main']['temp'] # Conditions, temp

def is_now_in_timeperiod(starttime, endtime, nowtime):
    if starttime < endtime:
        return nowtime >= starttime and nowtime <= endtime
    else: #Over midnight
        return nowtime >= starttime or nowtime <= endtime

def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    t = float(res.replace("temp=","").replace("'C\n",""))
    return(t)

def get_sensor_temp():
    t_h = sense.get_temperature_from_humidity()
    t_cpu = get_cpu_temp()

    # calculates the real temperature compesating CPU heating
    t_corr = t_h - ((t_cpu-t_h)/1.5)
    t = (t_corr * 1.8) + 32 # convert from Celcius to Fahrenheit

    return round(t,2)

def get_temp_color(temp):
    if temp <= 50:
        return blue
    elif temp > 50 and temp <= 75:
        return green
    else:
        return red

def scroll(msg, temp):
    sense.set_rotation(180)
    sense.low_light = True 
    sense.show_message(msg, text_colour= get_temp_color(temp), scroll_speed=0.08)
    sense.clear()

###################################################
# Main Program

try:
    while True:
        now = datetime.now()
        timenow = datetime.strptime(time.strftime(datetime.time(datetime.now()),"%I:%M%p"), "%I:%M%p")

        if cfg.use_timer and is_now_in_timeperiod(timestart, timeend, timenow):
            if first_run:
                nextwxcheck = (datetime.now() + timedelta(minutes=10))
                first_run = False
                conditions, temp = get_curr_wx()
            
            if now >= nextwxcheck:
                nextwxcheck = (datetime.now() + timedelta(minutes=10))
                conditions, temp = get_curr_wx()
            
            sensor_temp = get_sensor_temp()
            
            scroll("Outside " + str(temp) + " " + conditions, temp)
            scroll("Inside " + str(sensor_temp), sensor_temp)

        else:

            if first_run:
                nextwxcheck = (datetime.now() + timedelta(minutes=10))
                first_run = False
                conditions, temp = get_curr_wx()
            
            if now >= nextwxcheck:
                nextwxcheck = (datetime.now() + timedelta(minutes=10))
                conditions, temp = get_curr_wx()
            
            sensor_temp = get_sensor_temp()
            
            scroll("Outside " + str(temp) + " " + conditions, temp)
            scroll("Inside " + str(sensor_temp), sensor_temp)

        sleep(cfg.scroll_delay_time)

except KeyboardInterrupt:
    sense.clear()

except Exception as e:
    sense.clear()
    print(e)