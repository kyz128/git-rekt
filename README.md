# git-rekt

This is a personality trait text analyzer for hiring managers. It fetches a given user's Twitter tweets, processes them through IBM Watson Personality Insights, and filters the output through a KNN to match the user to the most appropriate hiring team. 

This project was built for IBM's 2019 3-day internal hackathon for interns. 

## How to get started

Use pip3 to install funcy, tweepy and ibm_watson . 

To run Tweepy to fetch new Twitter tweets, use
` python3 gettweets.py `

To run IBM Watson Personality Insights, use
` python3 run.py `
