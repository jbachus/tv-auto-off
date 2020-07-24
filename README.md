# TV Auto Off
Certain members of my household like to fall asleep with the TV on, but leaving it on all night can impact how well you sleep and uses unnecessary power.  So I created this script to automatically turn off the TV after it has been on for a certain amount of time.

Our bedroom TV has a [Roku stick](https://amzn.to/39msFJ6), so I use that IP to check the current power state of the TV.  If it stays on for a certain amount of time (MAX_MINUTES=60 by default) then it uses a [Broadlink RM4 IR blaster](https://amzn.to/2BrfGcu) to turn off the TV.

## Configuration
The following variables are required:  
ROKU_IP  
BROADLINK_IP  
POWER_IR_SIGNAL (in Hex string format)

Optionally you can also provide:  
ROKU_PORT (defaults to 8060)  
MAX_MINUTES (defaults to 60)  
TZ (Timezone, defaults to UTC e.g. "America/Denver")

## Usage
1. Create a .env file with the required environment variables.  For example:
    ```
    ROKU_IP=192.168.1.1
    BROADLINK_IP=192.168.1.2
    POWER_IR_SIGNAL=123123123123
    ```
2. Run `docker-compose build`
3. Run `docker-compose up -d`
