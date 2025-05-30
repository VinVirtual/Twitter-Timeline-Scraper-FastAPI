import os
import time
import re
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from groq import Groq
import logging

#logging.basicConfig(level=logging.DEBUG)
#logger = logging.getLogger(__name__)


load_dotenv()
def scrape_and_summarize():
    # Load API key
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return {"error": "GROQ_API_KEY is not set in the environment"}

    client = Groq(api_key=api_key)

   
    try:
        
         # Chrome options and setup
        chrome_options = Options()
        user_data_dir = "C:/Users/Ai Dev/AppData/Local/Google/Chrome/User Data"
        profile_name = "Default"
        chrome_options.add_argument(f"user-data-dir={user_data_dir}")
        chrome_options.add_argument(f"profile-directory={profile_name}")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        chromedriver_path ="C:/Users/AI Dev/Desktop/Twitter Timeline/Fast Api/chromedriver.exe"
        service = Service(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        # WebDriver setup and code here
    except Exception as e:
        #logger.error(f"An error occurred: {e}")
        raise
    try:
        driver.get("https://x.com/home")
        time.sleep(5)

        
        # Scroll and collect tweets
        def collect_tweets(driver, max_tweets=50):
            tweets = []
            unique_tweets = set()  # Make sure no duplicate tweets 

            while len(tweets) < max_tweets:
                tweet_elements = driver.find_elements(By.XPATH, '//article[@role="article"]')

                for tweet_element in tweet_elements:
                    # Extract tweet content
                    tweet_content = tweet_element.text
                    video_links = tweet_element.find_elements(By.XPATH, './/video')
                    media_links = []

                    for video in video_links:
                        video_url = video.get_attribute('src')
                        if video_url:
                            media_links.append(video_url)

                    if media_links:
                        tweet_content += "\nMedia Links: " + ', '.join(media_links)

                    # Add only unique tweets to the list 
                    if tweet_content not in unique_tweets:
                        unique_tweets.add(tweet_content)
                        tweets.append(tweet_content)

                    # Stop if
                    if len(tweets) >= max_tweets:
                        break

                # Scroll the page to load more tweets
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)  

            return tweets[:max_tweets]


        tweets = collect_tweets(driver, max_tweets=50)

        def clean_tweet_data(tweet, index):
            tweet = re.sub(r'http\S+', "", tweet)
            tweet = re.sub(r'@[\w]+', '', tweet)
            tweet = re.sub(r'#\w+', '', tweet)
            tweet = re.sub(r'[^\W\S]', '', tweet)
            tweet = re.sub(r'\n+', '\n', tweet)
            tweet = tweet.strip()
            tweet = tweet.replace('\n', ' ')
            return f"{index}. {tweet}"


        cleaned_tweets = [clean_tweet_data(tweet, idx + 1) for idx, tweet in enumerate(tweets)]


        print("\n--- Prepared Data for API ---")
        for tweet in cleaned_tweets:
            print(tweet)

        # Summarize the tweets using Groq API
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a smart assistant that reads twitter timeline. The twitter content is given to you in raw text that includes the author name, the timestamp and the engagement metrics value includes the comment, like, retweet, impression count. You should ignore the engagements metrics. Your goal is to read all the tweet content and then summarize what you have learnt, you should be specific and include some factual information in the summary. Be concise with sufficient context for others to know what you have learnt. You can make decision on what is important content and what is irrelevant content. You do not need to specify the tweet number in the summary. Summarize into 1000 words."},
                {"role": "user", "content": f"These are the tweets: \n" + "\n".join(cleaned_tweets)}
            ],
            model="llama-3.2-90b-vision-preview"
        )

        summary_response = chat_completion.choices[0].message.content
        print("")
        print("")
        print("Requested Homeline Tweets")
        print("")
        print(summary_response)
        print("")
        print("")
        return summary_response  # Return only the summary

    finally:
        driver.quit()
