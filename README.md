# Asset_Scrapper

## Project Description
Python application to get data from financial assets, using web scrapping.

## Project Details
This application was developed to get data from the website investing.com, using web scrapping techniques.. 
Please find below the fields that are being scrapped from the website:

- Close price of the day
- Highest price of the day
- Lowest price of the day
- Operation volume of the day

Other variables can also be scrapped from the web site, it is possible to use the same techniques in the script to separate the required strings.

### Notes

- If you are whilling to use the Python Script "as is", please follow the steps explained below:
  - Extract the files into a folder in your computer
  - Change the code in line 17 to the path of your folder (must be in Python language, otherwise it will not work ;))
  - Edit the file "assets_list.xlsx" and add the asset names of the assets your are whilling to get data from
  - Please be sure you have Python and the required packages installed in your computer (check them on the script)

- The former version of the script is using the current date as the date of the capture of the data

### Next Version Improvements

- Scrap the date of the capture from the website, instead of using today's date
- Create a secondary script to run daily automations, considering the holiday calendar of a certain country
