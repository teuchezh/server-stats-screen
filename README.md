# Server stats screen
[![time tracker](https://wakatime.com/badge/github/teuchezh/server-stats-screen.svg)](https://wakatime.com/badge/github/teuchezh/server-stats-screen)  
[Перейти на русский README](/README_ru.md)  
##### (The images below were taken during development, the final result will look different)  
## What it is?  
![demo_gif](/images/demo.gif)  

It is a small Python script that collects information about a server on a PC hardware or RaspberryPi, compatible with both Linux and Windows. The script then transfers information in the form of a JSON object to the COM port on the Arduino or ESP, then the information is displayed on the LCD20x4 display.  

At the moment, the output is implemented:  
1. Hostname;  
2. Local IP address;  
3. Working time from the moment of launch in hours;  
4. Launch date;  
5. CPU usage as a percentage;  
6. The use of RAM in percent;  
7. Total amount of RAM in MB;  
8. Amount of used RAM in MB;  
9. The total number of system disk;  
10. Number of available system disk;  
11. Amount of outgoing traffic since launch;  
11. Number of incoming traffic since launch;  

## Usage:  
Before using, you need to set your data in the variables of the Python script:  
1. The path to the system disk;  
1.2. Ethernet interface name;  
1.3. COM port number;  
2. Flash the Arduino / ESP with a sketch from the "display" folder;  

### ToDo:  
1. Make a division into "screens";  
1.2. Make automatic scrolling + encoder;  
2. Add a few more items of system information;  
