from linkedin_api import Linkedin
import os
from dotenv import load_dotenv

# get the email and password
load_dotenv()
user_name = os.getenv("user_name")
password = os.getenv("password")

# create the connection
api = Linkedin(user_name, password)


def get_companies(query):
    """
    :param query: search keyword
    :return: first 5 company URN-ID

    """
    companies = api.search_companies(query, limit=5)
    return [i['urn_id'] for i in companies]


def get_website(data):
    """
    :param data: scraped data of a company
    :return: company website URL

    """
    return data['companyPageUrl']


