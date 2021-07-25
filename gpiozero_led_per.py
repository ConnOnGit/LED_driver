#!/usr/bin/python3

import signal
import sys
import subprocess
from time import sleep

from gpiozero import PWMLED


LED_1 = PWMLED(5)
LED_2 = PWMLED(6)
LED_3 = PWMLED(23)
LED_4 = PWMLED(22)
LED_5 = PWMLED(24)

#ALL_GPIO = [LED_2, LED_3, LED_4, LED_5, LED_1]

def sigterm_handler(*_):
    LED_1.off()
    LED_5.off()
    LED_1.close()
    LED_5.close()
    LED_2.off()
    LED_4.off()
    LED_2.close()
    LED_4.close()
    LED_3.off()
    LED_3.close()
#    for device in ALL_GPIO:
#        device.off()
#        device.close()
    sys.exit(0)


def getshell():
#    process = check_output("/bin/ps -ef | grep mopidy | grep -v grep | awk '{print $2}'", shell=True)
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
            LED_3.pulse(n=1, fade_in_time=0.2, fade_out_time=0.8)
            sleep(0.2)
        elif pos == 2:
            LED_2.pulse(n=1, fade_in_time=0.2, fade_out_time=0.8)
            LED_4.pulse(n=1, fade_in_time=0.2, fade_out_time=0.8)
            sleep(0.2)
        elif pos == 3:
            LED_5.pulse(n=1, fade_in_time=0.2, fade_out_time=0.8)
            LED_1.pulse(n=1, fade_in_time=0.2, fade_out_time=0.8)
            process = getshell()
            sleep(0.8)
            pos=0
        pos += 1
        sleep(0.04)

def leds_on():
    LED_1.on()
    LED_2.on()
    LED_3.on()
    LED_4.on()
    LED_5.on()

def main():
    dummy = ""
    while dummy == "":
        sleep(5)


if __name__ == "__main__":
    initiate_animation()
    leds_on()
    signal.signal(signal.SIGTERM, sigterm_handler)
    main()
