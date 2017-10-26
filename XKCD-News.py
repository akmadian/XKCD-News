# -*- coding: utf-8 -*-
"""
    File Name: XKCD-News.py
    Author: Ari Madian
    Created: October 24, 2017 8:55 PM
    Python Version: 3.6
"""


import feedparser
import config
import private_config
import random
import tweepy
import arrow
import requests
from spacy.en import English
from string import Template
from textwrap import dedent

articles = []


class Article:
    def __init__(self, feed_data, title, summary, link):
        self.origin_data = feed_data
        self.title = title
        self.summary = summary
        self.link = link
        self.tweet_substituted = None


    def tweet_substituted(self):
        api = tweepy_auth()
        tweet = self.tweet_substituted


    def tweet_reply_meta_info(self):
        api = tweepy_auth()
        tweet = dedent('Feed name - $Feed_Title' + '\n' + 'Parse time - $Feed_Parsed')



    def substitute(self):
        NLP_Parser = English()
        summary = self.summary.split('<')[0]
        NLP_Tokens = NLP_Parser(summary)
        tokenized_summary = [token.orth_ for token in NLP_Tokens]
        substituted_summary = [word for word in tokenized_summary]
        for word in tokenized_summary:
            if word.lower() in config.substitutions:
                substituted_summary[substituted_summary.index(word)] = config.substitutions[word]

        self.tweet_substituted = ' '.join(substituted_summary)


def test_connection():
    status = requests.head('https://www.cnn.com')
    if str(status)[11:-2] == '200':
        return True
    else:
        return False



def get_articles(rss_url):
    feed = feedparser.parse(rss_url)
    article = random.choice(feed['entries'])
    source_dict = {'Feed_Title': feed['feed']['title'],
                   'Feed_Parsed': arrow.utcnow().to('US/Pacific').format('MMM D, YYYY - HH:mm') + ' PST'}

    new_article = Article(source_dict, article['title'],
                                       article['summary'],
                                       article['link'])
    articles.append(new_article)


def tweepy_auth():
    auth = tweepy.OAuthHandler(private_config.tweepy_consumer_token,
                               private_config.tweepy_consumer_secret)
    auth.set_access_token(private_config.tweepy_access_token,
                          private_config.tweepy_access_secret)
    api = tweepy.API(auth)
    return api


def main():
    if test_connection():
        for _, url in config.cnn_urls.items():
            if url != 'https://www.cnn.com':
                get_articles(url)

        for article in articles:
            article.substitute()
    else:
        raise RuntimeError('Connection Test Failed.')


if __name__ == '__main__':
    main()

