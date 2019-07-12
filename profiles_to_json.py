from ibm_watson import PersonalityInsightsV3
from os.path import join, dirname
import json
import pandas as pd
import numpy
from itertools import chain
from collections import defaultdict
from funcy import merge_with
import os


def json_to_dict(filename):
    personality_insights = PersonalityInsightsV3(
        iam_apikey="vVm3UuuwXOq4A6QheE8pZ1cIiKaYVoGnPmWQRlE2vunM",
        version='2017-10-13',
        url="https://gateway.watsonplatform.net/personality-insights/api"
    )

    with open(join(dirname(__file__), filename)) as profile_json:
        profile = personality_insights.profile(
            profile_json.read(),
            'application/json',
            content_type='application/json',
            consumption_preferences=True,
            raw_scores=True
        ).get_result()

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

    personality = scores_dict["personality"]

    needs = scores_dict["needs"]

    dictionary = {**personality, **needs}

    return dictionary


def personality_df(path=os.getcwd()):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if 'profile.json' in file:
                files.append(os.path.join(r, file))

    for num, f in enumerate(files):
        files[num] = json_to_dict(f)

    header = list(files[0].keys())

    multi_dict = merge_with(list, files)

    # print(type(test))
    # print(test)

    df = pd.DataFramedf = pd.DataFrame(multi_dict, columns=header)
    # print(dictionary)
    return df
    # print(type(df))


def main():

    df = personality_df()

    df.to_json(r'{}/testdata.json'.format(os.getcwd()))


if __name__ == "__main__":
    main()
