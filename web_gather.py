import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from requests.api import request

class SearchError(Exception):
    def __init__(self, message):
        self.message = message

class TweetSearch:
    def __init__(self, bearer_token: str, endpoint_url="https://api.twitter.com/2/tweets/search/", search_type='recent', max_results=10):
        self.bearer_token_ = bearer_token
        self.endpoint_url_ = endpoint_url
        self.search_type_ = search_type
        self.max_results_ = max_results
        self.headers_ = {'Authorization': f'Bearer {self.bearer_token_}'}
    def query(self, query: str):
        self.raw_query_ = query
        self.https_query_ = quote_plus(self.raw_query_)
        self.full_url_ = f'{self.endpoint_url_}{self.search_type_}?query={self.https_query_}&max_results={self.max_results_}'
        self.payload_ = {}
        self.response_ = requests.request('GET', self.full_url_, headers=self.headers_, data=self.payload_)
        if self.response_.status_code != 200:
            raise SearchError(f"Submission failed with code {self.response_.status_code}: {self.response_.reason}")
        elif self.response_.status_code == 200:
            self.result_text = self.response_.text
            self.json_ = self.response_.json()
            self.raw_string = ' '.join([x['text'] for x in self.json_['data']])
            return self.raw_string

class YelpSearch:
    def __init__(self, access_token: str):
        self.access_token_ = access_token
        self.url_ = "http://api.yelp.com/v3/businesses/search"
        self.headers_ = {'Authorization': f'Bearer {self.access_token_}'}
    def business_search(self, term: str, location: str, limit: int = 20):
        self.params_ = {
                        'term':term.replace(' ','+'),
                        'location':location.replace(' ','+'),
                        'limit': limit
        }
        self.response_ = requests.request('GET', self.url_, headers=self.headers_, params=self.params_)
        if self.response_.status_code != 200:
            raise SearchError(f"Submission failed with code {self.response_.status_code}: {self.response_.reason}")
        elif self.response_.status_code == 200:
            self.json_ = self.response_.json()
            self.businesses = [(x['name'],x['alias'], x['id']) for x in self.json_['businesses']]
            self.business_ids_ = [x['id'] for x in self.json_['businesses']]
            return self.businesses
    def get_all_businesses_reviews(self):
        self.all_businesses_text = []
        for i in self.business_ids_:
            id_url = f'http://api.yelp.com/v3/businesses/{i}/reviews'
            id_response = requests.request('GET', id_url, headers= self.headers_, params={})
            for resp in id_response.json()['reviews']:
                self.all_businesses_text.append(resp)
            self.reviews_list_ = [r['text'] for r in self.all_businesses_text]
            self.raw_string_all = ''.join(self.reviews_list_)
        return self.raw_string_all
    def get_business_reviews(self, id: str):
        self.business_text = []
        self.id_ = id
        id_url = f'http://api.yelp.com/v3/businesses/{self.id_}/reviews'
        id_response = requests.request('GET', id_url, headers= self.headers_, params={})
        for resp in id_response.json()['reviews']:
            self.business_text.append(resp)
        self.reviews_list_ = [r['text'] for r in self.business_text]
        self.raw_string = ' '.join(self.reviews_list_)
        return self.raw_string

class RSSFeed:
    def __init__(self, endpoint_url: str):
        self.endpoint_url_ = endpoint_url
        self.response_ = requests.get(self.endpoint_url_)
        if self.response_.status_code != 200: 
            raise SearchError(f'Submission failed with code: {self.response_.status_code}: {self.response_.reason}')
        else:
            self.xml_soup_ = BeautifulSoup(self.response_.text, 'lxml-xml')
            self.get_elements = list(set([x.name for x in self.xml_soup_.findAll()]))
    def join_elements(self, tag: str):
        self.text_list_ = [x.text for x in self.xml_soup_.findAll(tag)]
        self.raw_string = ' '.join(self.text_list_)
        return self.raw_string
