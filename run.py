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
#print(json.dumps(profile, indent=2))

#n_scores = profile["needs"]
scores_dict = dict()

def json_dict(profile_str):
    scores_dict[profile_str] = []
    for v in profile[profile_str]:
        temp_dict = dict()
        temp_dict["name"] = v["name"]
        temp_dict["raw_score"] = v["raw_score"]
        scores_dict[profile_str].append(temp_dict)

def get_scores(profile_str):
        scores_dict[profile_str] = dict()
        for v in profile[profile_str]:
            scores_dict[profile_str][v["name"]] = v["raw_score"]


get_scores("personality")
get_scores("needs")
get_scores("values")


print(scores_dict["values"]["Conservation"])
