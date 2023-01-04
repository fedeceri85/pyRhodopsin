# pyRhodopsin

This repository contains software and instructions to run the optogenetic stimulation hardware. This setup can be used for long-term stimulation of ChR2-expressing primary cultures in the incubator. 

## Software requirements
- Arduino ide https://www.arduino.cc/download_handler.php?f=/arduino-1.8.2-windows.exe
- Miniconda Python2.7 https://conda.io/miniconda.html. 

## Python packages
- The GUI software allows to set different parameters for the stimulation protocol (light intensity, pulse duration and repetition rate, as well as whether to use a ramp or step prepulse). It requires a python environment (anaconda preferred) with pyqt4. More dependencies for the anaconda python environment are detailed in pyRhodopsin/environment.xml. 
- It is possible to run the arduino in headless mode (IncubatorFirmware_v1), which doesn't require a python environment or a connected computer (the stimulation parameters can be hard-coded in the firmware file).

## Hardware
- Arduino uno/mega http://uk.rs-online.com/web/p/processor-microcontroller-development-kits/7154081/   (2 for monitor+controller configuration)
- AD5171 digital potentiometer http://uk.rs-online.com/web/p/digital-potentiometers/8099301/
- Surface Mount (SMT) Board SOT Epoxy Glass Double-Sided 23.5 x 13.5 x 1.5mm FR4 
- RCD24 LED driver http://uk.rs-online.com/web/p/led-drivers/6689882/
- 2X 4.7 KOhm resistors
- More hardware requirements is detailed in the Manual.


## Software
- ArduinoSketches contains arduino code for different protocols, optimised for immature cochlea hair cells. All protocols interact with the python GUI, except IncubatorFirmware_v1, in which the parameters are hard-coded in the arduino firmware.
 