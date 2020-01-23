from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
#GPIO.setup(26, GPIO.OUT)

# Create your views here.
GPIO.output(25,GPIO.HIGH)#for enabling the motor
GPIO.output(4,GPIO.HIGH)#for enabling the motor

def stop(request):
#    GPIO.output(18, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    return render(request, 'home.html')
def command_up(request):
    #subprocess.call(['gpio','-g','mode','18','out'])
    #subprocess.call(['gpio','-g','write','18','1'])
    GPIO.output(24, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)

#    GPIO.output(18, GPIO.HIGH)
    #time.sleep(0.5)
    #GPIO.output(18, GPIO.LOW)
    #subprocess.call(['gpio','-g','write','18','0'])
    print('up18')
    return render(request, 'home.html')
def command_down(request):
    #subprocess.call(['gpio','-g','mode','21','out'])
    #subprocess.call(['gpio','-g','write','21','1'])
#    GPIO.output(18, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)

    #time.sleep(0.5)
    #subprocess.call(['gpio','-g','write','21','0'])
    print('down21')
    return render(request, 'home.html')
def command_left(request):
    #subprocess.call(['gpio','-g','mode','4','out'])
    #subprocess.call(['gpio','-g','write','4','1'])
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)    
    #subprocess.call(['gpio','-g','write','4','0'])
    print('left4')
    return render(request, 'home.html')
def command_right(request):
    #subprocess.call(['gpio','-g','mode','12','out'])
    #subprocess.call(['gpio','-g','write','12','1'])
    GPIO.output(24, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)    
    #subprocess.call(['gpio','-g','write','12','0'])
    print('rigth12')
    return render(request, 'home.html')

