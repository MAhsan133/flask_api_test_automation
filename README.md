# Flask App

#### Prerequisite 

- Python must be installed 

#### Framework / Library

- Flask
- SQLLite
- Requests 
- PyTest

#### Installation

- Clone repository using **git clone git@github.com:MAhsan133/flask_api_test_automation.git**
- Move to "flask_api_test_automation" directory using **cd flask_api_test_automation**
- Run command **pip install -r requirements.txt** to install all libraries

#### Run Server 
- Move to "FLASK_REST_SERVICE" directory using **cd FLASK_REST_SERVICE**
- Start application by using command **python3 main.py** 
- Server must be listening on **Running on http://127.0.0.1:5000**


### Run Functional Test Cases
- Move to "tests" directory using **cd tests**
- Run test command **python3 -m pytest -qv test_main.py** 
- Testcases must be passed with message **20 passed**


### Non-Functional testcases - Load Testing (Apache Jmeter)

#### Prerequisite 

- Requires Java 8+ to be installed

#### Download & Installation

- Download latest binary ZIP file from **https://jmeter.apache.org/download_jmeter.cgi**
- Unzip **apache-jmeter-5.6** file

#### Run GUI mode

- Move to the directory using **cd apache-jmeter-5.6/bin**
- Run **sh jmeter.sh** from terminal
- Click the Run(Green color play) icon  
- View results under **View Results Tree** sampler

#### Run command line (Recommended)

- Move to the directory using **cd apache-jmeter-5.6/bin**
- Run command **./jmeter.sh -n -t "<path>/rest_api_load_test.jmx -f -l test-results-sample.csv** to generated results in CSV file
- Run command **./jmeter.sh -g test-results-sample.csv -f -o test_reports** to generate web based reoprt
- Moved to the directory using **cd test_reports**  
- Open **index.html** file to view report



# REST API Documentation

The REST API to the Banking app is described below.

## Get list of Users

### Request

`GET /api/users`

    curl -i -H 'Content-Type: application/json' http://localhost:5000/api/users

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.3.6 Python/3.8.10
    Date: Sun, 02 Jul 2023 07:13:33 GMT
    Content-Type: application/json
    Content-Length: 3
    Connection: close
    
    []

## Get user detail

### Request

`GET /api/users/<user_id>`

    curl -i -H 'Content-Type: application/json' http://localhost:5000//api/users/12345

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.3.6 Python/3.8.10
    Date: Sun, 02 Jul 2023 08:13:05 GMT
    Content-Type: application/json
    Content-Length: 3
    Connection: close
    
    {}

## Get account detail

### Request

`GET /api/account_detail/<account_number>`

    curl -i -H 'Content-Type: application/json' http://localhost:5000/api/account_detail/SCB12345

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.3.6 Python/3.8.10
    Date: Sun, 02 Jul 2023 07:16:50 GMT
    Content-Type: application/json
    Content-Length: 57
    Connection: close
    
    {"Message":"Account does not exists.", "Status":"Failed"}


## Create new User

### Request

`POST /api/users/add`

    curl -X POST http://localhost:5000/api/users/add -i -H 'Content-Type: application/json' -d '{"name": "Paul Serice", "email": "paul.serice@gamil.com", "phone": "067765434567", "address": "Paul Serice Street, Innsbruck", "country": "Austria"}' 

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.3.6 Python/3.8.10
    Date: Sun, 02 Jul 2023 07:27:30 GMT
    Content-Type: application/json
    Content-Length: 58
    Connection: close
    
    {"Message":"User created successfully","Status":"Passed"}

## Get list of Things again

### Request

`POST /api/accounts/add`

    curl -X POST http://localhost:5000/api/accounts/add -i -H 'Content-Type: application/json' -d '{"acc_no": "MEZN11223344556688", "acc_status": "Active", "total_balance": 500, "user_id": 1}'

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.3.6 Python/3.8.10
    Date: Sun, 02 Jul 2023 08:17:29 GMT
    Content-Type: application/json
    Content-Length: 61
    Connection: close
    
    {"Message":"Account created successfully","Status":"Passed"}

## Change a Thing's state

### Request

`POST /api/accounts/withdraws`

    curl -X POST http://localhost:5000/api/accounts/withdraws -i -H 'Content-Type: application/json' -d '{"acc_no": "MEZN11223344556688", "amt_withdrawn": 300}'

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.3.6 Python/3.8.10
    Date: Sun, 02 Jul 2023 08:19:27 GMT
    Content-Type: application/json
    Content-Length: 61
    Connection: close
    
    {"Message":"Amount withdraw successfully","Status":"Passed"}

## Get changed Thing

### Request

`POST /api/accounts/deposits`

    curl -X POST http://localhost:5000/api/accounts/deposits -i -H 'Content-Type: application/json' -d '{"acc_no": "MEZN11223344556688", "amt_deposit": 200}'

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.3.6 Python/3.8.10
    Date: Sun, 02 Jul 2023 08:20:54 GMT
    Content-Type: application/json
    Content-Length: 60
    Connection: close
    
    {"Message":"Amount deposit successfully","Status":"Passed"}

## Change a Thing

### Request

`POST /api/accounts/send`

    curl -X POST http://localhost:5000/api/accounts/send -i -H 'Content-Type: application/json' -d '{"from_acc_no": "MEZN11223344556688","to_acc_no": "SCB11223344556688", "amt_withdrawn": 400}'

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.3.6 Python/3.8.10
    Date: Sun, 02 Jul 2023 08:22:38 GMT
    Content-Type: application/json
    Content-Length: 59
    Connection: close
    
    {"Message":"Unable to transfer amount.","Status":"Failed"}
