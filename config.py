# -*- coding: utf-8 -*-
"""
    File Name: config.py
    Author: Ari Madian
    Created: October 24, 2017 8:55 PM
    Python Version: 3.6
"""

## RSS URLs
# CNN
cnn_urls = {'cnn_test_url': 'https://www.cnn.com',
            'cnn_rss_politics': 'http://rss.cnn.com/rss/cnn_allpolitics.rss',
            'cnn_rss_science': 'http://rss.cnn.com/rss/cnn_tech.rss',
            'cnn_rss_US': 'http://rss.cnn.com/rss/cnn_us.rss',
            'cnn_rss_world': 'http://rss.cnn.com/rss/cnn_world.rss',
            'cnn_rss_topstories': 'http://rss.cnn.com/rss/cnn_topstories.rss'}


## Tweepy Auth
# Tweepy auth info is stored in a secret config file for what should be obvious reasons,
# but, if it was here, it would look like this.
tweepy_consumer_token = 'consumer token here'
tweepy_consumer_secret = 'consumer secret here'
tweepy_access_token = 'access token here'
tweepy_access_secret = 'access secret here'


## Substitutions
# Substitutions 1 - https://xkcd.com/1288/
# Substitutions 2 - https://xkcd.com/1625/
# Substitutions 3 - https://xkcd.com/1679/

substitutions = {'witnesses': 'these dudes I know',
                 'allegedly': 'kinda probably',
                 'new study': 'tumblr post',
                 'rebuild': 'avenge',
                 'space': 'spaaace',
                 'google glass': 'virtual boy',
                 'smartphone': 'pokedex',
                 'electric': 'atomic',
                 'senator': 'elf-lord',
                 'car': 'cat',
                 'election': 'eating contest',
                 'congressional leaders': 'river spirits',
                 'homeland security': 'homestar runner',
                 'could not be reached for comment': 'is guilty and everyone knows it',
                 'debate': 'dance off',
                 'self driving': 'uncontrollably swerving',
                 'poll': 'psychic reading',
                 'candidate': 'airbender',
                 'drone': 'dog',
                 'vows to': 'probably won\'t',
                 'at large': 'very large',
                 'successfully': 'suddenly',
                 'expands': 'physically expands',
                 'first degree': 'friggin\' awful',
                 'first-degree': 'friggin\' awful',
                 'second degree': 'friggin\' awful',
                 'second-degree': 'friggin\' awful',
                 'third degree': 'friggin\' awful',
                 'third-degree': 'friggin\' awful',
                 'an unknown number': 'like hundreds',
                 'front runner': 'blade runner',
                 'global': 'spherical',
                 'years': 'minutes',
                 'minutes': 'years',
                 'no indication': 'lots of signs',
                 'urged restraint by': 'drunkenly egged on',
                 'horsepower': 'tons of horsemeat',
                 'gaffe': 'magic spell',
                 'ancient': 'haunted',
                 'star-studded': 'blood-soaked',
                 'star studded': 'blood soaked',
                 'remains to be seen': 'will never be known',
                 'silver bullet': 'way to kill werewolves',
                 'subway system': 'tunnels I found',
                 'surprising': 'surprising (but not to me)',
                 'war of worlds': 'interplanetary war',
                 'tension': 'sexual tension',
                 'casually optimistic': 'delusional',
                 'doctor who': 'the big bang theory',
                 'win votes': 'find pokemon',
                 'behind the headlines': 'beyond the grave',
                 'email': 'poem',
                 'facebook post': 'poem',
                 'tweet': 'poem',
                 'facebook ceo': 'this guy',
                 'latest': 'final',
                 'disrupt': 'destroy',
                 'meeting': 'menage a trois',
                 'scientists': 'channing tatum and his friends',
                 'you won\'t believe': 'I\'m sad about'}
