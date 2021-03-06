# Application Manual - Data Scraper

**Team Name**: HZ-TASK Force 

**Team Members**: Allen Leigh, Hongyu Cheng, Kanishkah Anwari, SeGe Jung, Tommy Wang, Zahiduzzaman Biswas 

**Project Name**: Data Scraper 

**GitHub Link**: https://github.gatech.edu/gt-cs6440-hit-fall2020/Data-Scrapper 

# Table of Contents
1. Live Site
2. Functionalities
3. Local Development
4. Deploying to HDAP

## 1. Live Site
(Connect to GaTech VPN before connecting to the sites below)

* Live site: https://apps.hdap.gatech.edu/data-scrapper-app/
* CI: https://drone.hdap.gatech.edu/gt-cs6440-hit-fall2020/Data-Scrapper/ (Need to be on Ga Tech Network)
* Rancher: https://rancher.hdap.gatech.edu/ (Need to be on Ga Tech Network)

## 2. Functionalities
DataScrapper application takes in a HTML URL, JSON URL, FORM, and PDF data and creates a CSV file for users to then use for their projects. 

### 2.1 HTML Input
* [Click here for detailed instructions](https://github.gatech.edu/gt-cs6440-hit-fall2020/Data-Scrapper/blob/master/Final%20Delivery/How%20to%20Parse%20HTML%20Tables%20from%20a%20Website%20URL.pdf)
* On the home page click on HTML card
* Enter in a valid url i.e http://google.com, the URL should render an HTML page
* The application will scrape the HTML page for Tables and create a CSV for each table found
* After Click Convert CSV the application will prompt you that your job is done and a link to download your CSV

### 2.2 Form Input
* [Click here for detailed instructions](https://github.gatech.edu/gt-cs6440-hit-fall2020/Data-Scrapper/blob/master/Final%20Delivery/How%20to%20Parse%20HTML%20Tables%20from%20a%20Website%20URL.pdf)
* On the home page click on Form card
* Select Form template
* Upload PDF of Form
* After Click Convert CSV the application will prompt you that your job is done and a link to download your CSV

### 2.3 API Input
* On the home page click on API card
* Enter in a valid url i.e http://hapi.fhir.org/baseR4/Patient/1215584, the URL should render json
* The json options are `flat` or `structured`
* After Click Convert CSV the application will prompt you that your job is done and a link to download your CSV

### 2.4 PDF Input
* On the home page click on PDF card
* Upload valid PDF with tables
* The application will scrape the PDF page for Tables and create a CSV for each table found
* After Click Convert CSV the application will prompt you that your job is done and a link to download your CSV

### 2.5 History Page
* History button is located on the top right corner of the app
* Users can view job status and access download links to csv files

## 3. Local Development

**Pre-requisites**
* Python3, pip3
* Docker
* MySQL server

**NOTE: after pull from master branch, always install packages from `app/requirements.txt`**

We use Makefile to make development and testing more convenient.

**NOTE: `make` command should be executed inside `app/` ONLY :**

* `make setup`: create local database etc,.
* `make update`: update database schema and Python packages.
* `make server`: start app server on local.
* `make test`: run test suite.
* `make clear`: clear all data

### First time Setup

Run command `make setup && make update`.

This does:

* Create local database
* Install Python packages

If you need to change database configuration, please update the `app/makefile` locally.

### Run server without Docker

NOTE: after pulling the latest master branch, run `make update`.

Run command `make server`.

To switch environment, execute `ENV=<env name> python3 app/main.py`. Available environments are:

* `dev_local` (default)
* `dev_remote`
* `production`


### Run server With docker (TODO)

(As we are using a separate container for MySQL, this method for development is not support)

```shell
# Clone repository
git clone https://github.gatech.edu/gt-cs6440-hit-fall2020/Data-Scrapper

# Move to Data-Scrapper directory
cd Data-Scrapper

# Build docker image
docker build --tag datascrapper:1.0 .

# Run image as container
docker run --publish 5000:5000 --detach --name ds  datascrapper:1.0

# Visit homepage
curl localhost:5000

# Stop and remove Docker container
docker stop ds
docker rm ds
```

## 4. Deploying to HDAP

Merge master branch into the `deploy` branch, which will automatically trigger a deployment to HDAP.




