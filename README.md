# Web_Gather
Repository for a small wrapper around Twitter API, Yelp API, and RSS Feed Collection

**Required Packages**

  requests
  
  bs4
  
  urllib
  
These are standard or were previously downloaded for past assignments



**Using the module**

You do not need to install anything via pip, simply download the web_gather.py file and save it in the same folder as your jupyter notebooks and scripts

You will need:

  For Twitter: Twitter API bearer token 

  For Yelp: Yelp API Key

  For RSS Feeds: The RSS Feed URL 

Using TweetSearch:

  The TweetSearch class is designed to take a minimum of just your Twitter API Bearer Token to connect to the API. Initialize the TweetSearch class with your bearer token passed via argument _bearer_token_, and optional arguments: _endpoint_url_, _search_type_, and _max_results_. The default endpoint_url is the twitter API tweetsearch endpoint, default for search_type is recent and the only other argument passed should be 'all' if you have academic API access, otherwise a SearchError will be thrown, and the max_results default is the minimum of 10 and the maximum is 100. 
  Use the method called query to search tweets based on the Twitter API query syntax detailed at https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query. The query method returns a single joined string of all the text from all the tweets that were retrieved.
  
Using YelpSearch:

  The YelpSearch class is designed to take your Yelp API Key (Access Token), and connect to the Yelp API. initializing the YelpSearch class returns a list of three-value tuples containing (Business Name, Business Alias, Business ID). 
  First, use the method called business_search to search for businesses matching one specified keyword (can be multiple words, but they are joined to be one keyword string) and location. The keyword is passed to business_search via argument _keyword_ and the location is passed via argument _location_, and the optional argument _limit_ setting the maximum result limit which has a default of 20 and a maximum of 200. Use the method get_all_business_reviews (no arguments) to get a single string of three reviews for each business retrieved via the business_search method. Use get_business_reviews to get a string of three reviews for one business. The get_business_reviews method takes one argument _id_ passed as the id of a specified business. 
  Documentation on the Yelp API is detailed at: https://www.yelp.com/developers/documentation/v3/get_started
  
Using RSSFeed:

  The RSSFeed class is designed to take an RSS Feed URL passed via argument _endpoing_url_ and scrape the data from that URL. Many websites have RSS feeds and they can be found via a quick google search. Access the attribute get_elements (no arguments, no parentheses) to see a list of the unique element tags from the specified RSS feed URL. Use the join_elements method to join the text from a specified element tag into one string of all the text, passing the tag via argument _tag_. 
  
  
__See example.ipynb to review simple examples of how to use each class and methods/attributes__
