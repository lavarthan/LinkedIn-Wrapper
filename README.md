# LinkedIn Wrapper
This is a scraping system extracting the company details from the [LinkedIn][1]
System is created with the help of [linkedin-api v2.0a][2] which is created by [Tomquirk][3]


## How to install?
> STEP 1: Clone the repository

> STEP 2: Go to the clone repository folder and open a command line

> STEP 3: Type `pip install -r requirements.txt` and hit Enter


## How to use?

> Go to the .env file and fill the LinkedIn credentials

> Run the mani.py 

> Enter the searching company name

> Enter the company website URL that you are looking for


>> **Note:** *Website URL ensure that system getting exact company. The URL should be same as the URL that present in the LinkedIn*



## Output
A company named json file containing the below data if available

> **1. Name**

> **2. Company website**

> **3. Company type**

> **4. No.of Employees in LinkedIn**

> **5. No.of Employees**

> **6. Country**

> **7. City**

> **8. Postal code**

> **9. Address**

> **10. Description**

> **11. No.of Followers**

> **12. Established year**

> **13. Logo**

> **14. Specialities**

> **15. One liner**

> **16. Founded Date**

> **17. Founders**

> **18. Operating Status**

> **19. Also Known As**

> **20. Legal Name**

> **21. Related Hubs**

>> **Note:** *Only first company system will check. If you want to change the number of companies system should look Go to `utils.py` change the `limit` in the `get_companies` function*


[1]: https://www.linkedin.com/
[2]: https://github.com/tomquirk/linkedin-api
[3]: https://github.com/tomquirk
