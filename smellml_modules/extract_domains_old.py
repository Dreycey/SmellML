#! /usr/bin/env python3
"""
Extracts topics (domains/tags) from given github repo
"""
import sys
import csv
import time
import github
from github import Github
import requests

"""
Extracts topics (domains/tags) from given github repo and returns

Input:
    github project (owner/project_title format)

Output:
    returns dictionary
"""
def get_topics(git_obj, git_project):
    topics = []
    try:
        time.sleep(1)
        # get Repository object from Github project
        repo = git_obj.get_repo(git_project)
        # retrieve topics form repo object and store in dictionary
        topics.append(repo.get_topics())
    except github.UnknownObjectException as e:
        print(e)

    return topics


def get_topics_from_csv(git_obj, csv_file):
    # "Project Name","URL","ML libraries","Number of Contributors","Number of Stars"
    topics_dict = {}
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            next(csv_reader)
            #print(get_topics(git_obj, row[0]))
            topics_dict[row[0]] = get_topics(git_obj, row[0])
            line_count += 1
        print(f'Processed {line_count} lines.')
    return topics_dict


def save_to_csv(dict):
    with open("project_topics.csv", mode='w') as csv_file:
        fieldnames = ['project_name', 'topics']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for key in dict:
            writer.writerow({'project_name': key, 'topics': data_dict[key]})


def main():
    """ controls the script """
    gitObj = Github()
    # # using an access token
    # gitObj = Github("access_token")
    #
    # # Github Enterprise with custom hostname
    # gitObj = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")
    topics = {}

    ### SCRIPT INPUT
    input = sys.argv[1]

    # TEST
    if '.csv' in input:
        topics = get_topics_from_csv(gitObj, input)
        save_to_csv(topics)
    else:
        print(f'Project: {input}, Topics: {get_topics(gitObj, input)}')


if __name__ == "__main__":
    main()
