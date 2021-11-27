# Microsoft Engage 2021

## Problem Statement  
Build a functional prototype of a platform that gives students an array of digital academic and social tools to stay engaged with their studies, peers and broader university community during pandemic.

#
## COMMON SPACE
#### <b> We Unite People </b>

 <img src="images/logo.png" /> 

 

It's a blogging + QnA website for enthusiast people from diverse background built solely by me using a completely different stack.

Built using flask 
* FrontEnd: HTML, CSS, Javascripts
* Database: MySQL
#
## Pre-requisites
* Python 3.9.9
* MySQL 8.0
#
## Installation Steps
1. Clone this repository to your desktop
``` python 
git clone https://github.com/kathuriasimran/common-space.git
```
2. Go to the ```Common_space``` directory and create a new virtual environment to create isolated Python environment.
**Note: I highly recommend using [Virtualenv](https://virtualenv.pypa.io/en/latest/).**
``` python 
py -m venv env
```

3. Activate the virtual environment
``` python 
env\Scripts\activate
```

4. Install the application requirements:
```python
pip install -r requirements\dev.txt
```
5. Configure the database and app  
for detail explaination go to <a href="#How it works">how it work</a> 

6. Run the application and go to [localhost:8000](http://127.0.0.1:8000/) to see the application running:
```python
python run.py
```
#
## How it works

As mention in point five of installation config look as below 

config.json 
```
{
    "startup_conf":
                        {
                            "app_name" : "Common Space",
                            "host":"0.0.0.0",
                            "port":8000,
                            "debug":true,
                            "use_reloader":true,
                            "secret_key":"S3$&F@$%DSRER"

                        },

    "database_conf":   
                        {
                            "type":"sql",
                            "url":"localhost",
                            "port":3306,
                            "database_name":"common_space",
                            "username":"root",
                            "password":"simran"

                        }
}
```
![Alt text](images/config.png?raw=true "Config Parameters")




 

#

## COMMON SPACE
<img src="images/New video.gif" />


# 

## Contributor 
Created by <b>Simran Kathuria</b>
