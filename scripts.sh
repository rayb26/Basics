#!/bin/bash
# Rayhan Biju 


# First Query -> This obtains all the users who have made 1 commit in the last 
# 3 years to the linux repo. 
#=========================================
# GitHub token (I redacted it for privacy)
GITHUBTOKEN="#"

# GitHub API URL for the Linux repo 
REPO_URL="https://api.github.com/repos/torvalds/linux"

# Gets the date 3 years ago 
START_DATE=$(date -u -v -3y "+%Y-%m-%dT%H:%M:%SZ")

# Endpoint for all the commits from the start date 
COMMITS_URL="${REPO_URL}/commits?since=${START_DATE}"

# Get response using the tokens 
response=$(curl -s -H "Authorization: token ${GITHUBTOKEN}" "${COMMITS_URL}")

# Parse the json to only include contributors who have made 1 commit in the last 3 years 
contributors=$(echo "${response}" | jq -r '.[].commit.author.name' | sort | uniq -c | awk '$1 > 1 {print $2}')

# Convert contributors to JSON array
json_output="["
while read -r contributor; do
  json_output+="\"${contributor}\","
done <<< "${contributors}"
json_output="${json_output%,}" 
json_output+="]"

# Redirect json output in file 
echo "${json_output}" > contributors_last_3_years.json


# Second query to show everyone who has at least 1 open pull request in the Linux repo. 

#=========================================

PR_URL="${REPO_URL}/pulls?state=open"

# Query to fetch everyone who has an open pull request 
pr_response=$(curl -s -H "Authorization: token ${GITHUBTOKEN}" "${PR_URL}")

# Parsing returned json (from curl request) to obtain each PR's owner 
pr_contributors=$(echo "${pr_response}" | jq -r '.[].user.login' | sort | uniq -c | awk '{print "{\"name\":\"" $2 "\",\"open_prs\":" $1 "},"}')

# Convert contributors to JSON array
pr_json_output="["
while read -r pr_contributor; do
  pr_json_output+="${pr_contributor}"
done <<< "${pr_contributors}"
pr_json_output="${pr_json_output%,}" 
pr_json_output+="]"

# Output the JSON array for open pull requests to a file
echo "${pr_json_output}" > open_pr_contributors.json

