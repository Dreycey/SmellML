#! /usr/bin/env python3
"""
Extracts topics (domains/tags) from given github repo

USAGE:
    python extract_domains.py <CSV_file>
    python extract_domains.py <"owner/project">
"""
import sys
import csv
import time
import github
from progressbar import progressbar
from tqdm import tqdm
from github import Github

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
        print(f'Project name: {git_project}, Error: {e}')

    return topics


def get_topics_from_csv(git_obj, csv_file):
    # "Project Name","URL","ML libraries","Number of Contributors","Number of Stars"
    topics_dict = {}
    url_dict = {}
    MAX_READS = 100

    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # skip header
        next(csv_reader, None)
        line_count = 0
        for row in tqdm(csv_reader, total=MAX_READS):
            # limit reads to 100 due to github api query restrictions
            if line_count > MAX_READS:
                return topics_dict, url_dict
            else:
                topics_dict[row[0]] = get_topics(git_obj, row[0])
                url_dict[row[0]] = row[1]
                line_count += 1
        #print(f'Processed {line_count} lines.')

    return topics_dict, url_dict


def save_to_csv(dict1, dict2):
    with open("project_topics.csv", mode='w') as csv_file:
        fieldnames = ['project_name', 'url', 'topics']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for key in dict1:
            writer.writerow({'project_name': key, 'url': dict2[key], 'topics': dict1[key]})
    csv_file.close()

def main():
    # using an access token allows for more queries
    # gitObj = Github("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")
    # create github object without an access token (limits queries per hour)
    gitObj = Github()

    topics = {}
    urls = {}

    ### SCRIPT INPUT
    input = sys.argv[1]

    # TEST
    if '.csv' in input:
        (topics,urls) = get_topics_from_csv(gitObj, input)
        save_to_csv(topics, urls)
    else:
        print(f'Project: {input}, Topics: {get_topics(gitObj, input)}')


if __name__ == "__main__":
    main()
