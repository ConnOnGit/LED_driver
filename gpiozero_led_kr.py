#!/usr/bin/python3

import signal
import sys
import subprocess
from time import sleep

from gpiozero import PWMLED

LED_1 = PWMLED(5)
LED_2 = PWMLED(6)
LED_3 = PWMLED(22)
LED_4 = PWMLED(24)
LED_5 = PWMLED(23)

#ALL_GPIO = [LED_1, LED_2, LED_3, LED_4, LED_5]

def sigterm_handler(*_):
    LED_1.off()
    LED_1.close()
    sleep(0.1)
    LED_2.off()
    LED_2.close()
    sleep(0.1)
    LED_3.off()
    LED_3.close()
    sleep(0.1)
    LED_4.off()
    LED_4.close()
    sleep(0.1)
    LED_5.off()
    LED_5.close()
#    for device in ALL_GPIO:
#        device.off()
#        device.close()
    sys.exit(0)


def getshell():
#    process = check_output("/bin/ps -ef | grep mpd | grep -v grep | awk '{print $2}'", shell=True)
#    process = process.decode()
#    return process
    process = subprocess.Popen("echo -e status\\nclose | nc -w 1 localhost 6600 | grep 'OK MPD'", shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    return process


#def ledon(ledname):
#    for x in range(100):
#        ledname.value = x * 0.001
#        sleep(0.02)


#def ledoff(ledname):
#    for x in range(100, -1, -1):
#        ledname.value = x * 0.001
#        sleep(0.02)

def initiate_animation():
    process = ""
    pos = 1
    direction = 0
    while process == "":
        print(process)
        if pos == 1:
            LED_1.pulse(n=1, fade_in_time=0.2, fade_out_time=0.5)
            sleep(0.1)
            direction = 0
        elif pos == 2:
            LED_2.pulse(n=1, fade_in_time=0.2, fade_out_time=0.4)
            sleep(0.05)
        elif pos == 3:
            LED_3.pulse(n=1, fade_in_time=0.2, fade_out_time=0.3)
        elif pos == 4:
            LED_5.pulse(n=1, fade_in_time=0.2, fade_out_time=0.4)
            sleep(0.05)
        elif pos == 5:
            LED_4.pulse(n=1, fade_in_time=0.2, fade_out_time=0.5)
            process = getshell()
            direction = 1
            sleep(0.1)
        if direction == 0:
            pos += 1
        else:
            pos -= 1
        sleep(0.07)

def leds_on():
    LED_1.on()
    sleep(0.1)
    LED_2.on()
    sleep(0.1)
    LED_3.on()
    sleep(0.1)
    LED_5.on()
    sleep(0.1)
    LED_4.on()

def main():
    dummy = ""
    while dummy == "":
        sleep(5)


if __name__ == "__main__":
    initiate_animation()
    leds_on()
    signal.signal(signal.SIGTERM, sigterm_handler)
    main()
