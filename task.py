import gpiozero 
from datetime import datetime
import psutil 

led_green=gpiozero.LED(17)
led_yellow=gpiozero.LED(22)
led_red=gpiozero.LED(27)

while True:
    date=datetime.now().strftime('%Y/%m/%d %Hh %Mm %Ss')  # formating the date
    cpu_cores_usage=psutil.cpu_percent(interval=5,percpu=True)
    cpu_mean_usage=sum(cpu_cores_usage)/len(cpu_cores_usage)  
    f=open("log.txt","w")
    f.write("Date is :"+ date +"\n")
    f.write("The avearage usage of cpu is :"+"{:.3f}%".format(cpu_mean_usage)) # {:.3f} =>old way in formating of numbers in python 

    if 0<cpu_mean_usage<50 :
        led_green.on()
        led_red.off()
        led_yellow.off()
    elif 50<cpu_mean_usage<80 :
        led_yellow.on()
        led_red.off()
        led_green.off()
    elif 80 < cpu_mean_usage < 100:
        led_red.on()
        led_yellow.off()
        led_green.off()
    else:
        pass
    f.close()
