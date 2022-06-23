# Producent_Consumer_UT
Aplication Producent-Consumer
The Producer is a thread which is using source frame data and put it to first queue every 50ms.
The Consumer is a thread which is receiving from first queue and make two data conversion:
        Resize frame size by twice
        Median filter 5x5
Then Consumer put new frame to second queue
Main function is receiving frames from second queue and save it in directory : processed
After 100 frames terminates program

## Install 
### Ubuntu (Wsl 2.0)
        sudo apt update && sudo apt upgrade -y
        sudo apt install python3-pip

        pip3 install numpy

## Usage
