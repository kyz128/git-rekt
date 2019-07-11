from ibm_watson import PersonalityInsightsV3
from os.path import join, dirname
import json

personality_insights = PersonalityInsightsV3(
    iam_apikey="vVm3UuuwXOq4A6QheE8pZ1cIiKaYVoGnPmWQRlE2vunM",
    version='2017-10-13',
    url="https://gateway.watsonplatform.net/personality-insights/api"
)

with open(join(dirname(__file__), './profile.json')) as profile_json:
    profile = personality_insights.profile(
        profile_json.read(),
        'application/json',
        content_type='application/json',
        consumption_preferences=True,
        raw_scores=True
    ).get_result()
print(json.dumps(profile, indent=2))