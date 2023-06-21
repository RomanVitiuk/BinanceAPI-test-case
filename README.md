# BinanceAPI Test Case

***INSTALL***

> git clone git@github.com:RomanVitiuk/BinanceAPI-test-case.git

## Go to to the root of project. If You clone project in home directory (***for example: /home/cool_user***), you can go to the root of project with next command:

> cd /home/cool_user/binanceapi

or

> cd ~/binanceapi

Then make python environment

> python -m venv venv

Activate python environment

> source venv/bin/activate

Install requirements

> pip install -r requirements.txt

## Next step make two files executable:

> chmod +x app_launcher.sh

and

> chmod +x cron_job.sh

## Next step run application

Run command from project root directory.

> ./app_launcher.sh

This bash script will create database, csv file and insert first data into both of them. Script waiting 3 second and run web app with candlestick chart and pie chart.

By default script collect data every 4 hour for symbol BTCUSDT.

If you need change this default values, for example set symbol ETHUSDT you can do this in file app_launcher.sh, all you need is set line 6 as shown below

> python data_collector.py -s ETHUSDT

or if you need set interval with 1 day

> python data_collector.py -i 1d

you can combine this parameters

> python data_collector.py -i 1d -s ETHUSDT

File data_collector.py can take two arguments, -s or --symbol: symbol and -i or --interval: interval.

Interval need set with next definition (for hour and day):

- 5h
- 1d

**But remember if you change interval, you need make change also in crontab file as shown in step above**

## Next step check cron status

First of all make sure that your cron active:

> systemctl status cron

If it`s not, run (for arch based linux) command:

> systemctl enable --now cronie.service

For else linux distro it is may be (but I`m not sure):

> systemctl enable --now cron

or

> systemctl enable --now cron.service

## Next step make crontab file (cron job set up)

After executing next command, a new file will be opened automatically

> crontab -e

*in the open file insert next command*

*in project root directory copy path to cron_job.sh and **replace path (/home/cool_user/binanceapi/cron_job.sh), in command below, on your own path to file cron_job.sh***

> 0 */4 * * * /home/cool_user/binanceapi/cron_job.sh

Save file and exit from editor.

This command will run script for collecting data every 4 hour and insert into database and csv file.

*You can test crontab running to make sure the data is saving in database and csv file.*

To do that run command, with instruction as above:

> crontab -e

> * * * * * /home/cool_user/binanceapi/cron_job.sh

With this command data will be collecting every minute. If you just test cron work, you don`t need change app_launcher.sh
