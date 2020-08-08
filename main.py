# import the libraries
import json
import re

# functions from utils
from utils import api
from utils import get_website
from utils import get_companies

while True:
    query = input("Enter the keyword")
    url = input("Enter the website URL")
    urn_ids = get_companies(query)
    print("First 5 company name scraped!")

    final = {}
    for i in urn_ids:
        # get the details of the company
        company = api.get_company(i)

        # get the website of the company
        website = get_website(company)
        print("checking company ", company['name'])

        # if company website URL and given URL same then get the all available data
        if website == url:
            print("Company found!")
            final['Name'] = company['name']
            try:
                final['Company website'] = company['companyPageUrl']
            except:
                pass
            try:
                final['Company type'] = company['companyIndustries'][0]['localizedName']
            except:
                pass
            try:
                final['One liner'] = company['tagline']
            except:
                pass
            try:
                final['No.of Employees in LinkedIn'] = company['staffCount']
            except:
                pass
            try:
                start = company['staffCountRange']['start']
                end = company['staffCountRange']['end']
                final['No.of Employees'] = str(start) + " - " + str(end)
            except:
                if company['staffCountRange']['start'] == 10001:
                    final['No.of Employees'] = '10001+'
                else:
                    final['No.of Employees'] = company['staffCountRange']['start']
            try:
                area = company['confirmedLocations'][0]['geographicArea']
                location = company['confirmedLocations'][0]['country']
                final['Country'] = area + " " + location
            except:
                pass
            try:
                final['City'] = company['confirmedLocations'][0]['city']
            except:
                pass
            try:
                final['Postal code'] = company['confirmedLocations'][0]['postalCode']
            except:
                pass
            try:
                line1 = company['confirmedLocations'][0]['line1']
                city = company['confirmedLocations'][0]['city']
                area = company['confirmedLocations'][0]['geographicArea']
                country = company['confirmedLocations'][0]['country']
                try:
                    line2 = company['confirmedLocations'][0]['line2']
                    final['Address'] = line1 + ", " + line2 + ", " + city + ", " + area + ", " + country

                except:
                    final['Address'] = line1 + ", " + city + ", " + area + ", " + country

            except:
                pass
            try:
                final['Description'] = re.sub(u"(\u2018|\u2019|\n|\u2014|\u2015|)", "'", company['description'])
            except:
                pass
            try:
                final['No.of Followers'] = company['followingInfo']['followerCount']
            except:
                pass
            try:
                final['Established year'] = company['foundedOn']['year']
            except:
                pass
            try:
                a = company['logo']['image']['com.linkedin.common.VectorImage']['artifacts'][0][
                    'fileIdentifyingUrlPathSegment']
                b = company['logo']['image']['com.linkedin.common.VectorImage']['rootUrl']
                final['Logo'] = b + a
            except:
                pass
            try:
                final['Specialities'] = ",".join(company['specialities'])
            except:
                pass

            # save the data into json file named in the company name
            file_name = final['Name']
            with open('company/' + file_name + '.json', 'w') as f:
                json.dump(final, f, indent=4, separators=(',', ': '))
            break

