# import sys
# import git
# from git_contributions_importer import *

# repos_path = [
#     'https://github.com/HexaHealth/opd',
# ]
# repos = []
# for repo_path in repos_path:
#     repos.append(git.Repo(repo_path))

# mock_repo_path = 'https://github.com/KaustubhBadve/ContributionsFromOtherPlatforms'
# mock_repo = git.Repo.init(mock_repo_path)

# importer = Importer(repos, mock_repo)
# importer.set_author(['vishalpatil12014017', 'kaustubhbadve@Kaustubhs-MacBook-Air.local'])
# importer.set_commit_max_amount_changes(15)
# importer.set_changes_commits_max_time_backward(60*60*24*30)
# importer.set_max_changes_per_file(60)
# importer.ignore_file_types(['.csv', '.txt', '.pdf', '.xsl', '.sql'])
# importer.set_collapse_multiple_changes_to_one(True)
# importer.import_repository()

# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo

# repo = git.Repo("/Users/kaustubhbadve/Desktop/OPD Service/opd")
# repo = git.Repo("/Users/kaustubhbadve/Desktop/ChatBot/chatbot")
# repo = git.Repo("/Users/kaustubhbadve/Desktop/hospital-bridge")
# repo = git.Repo("/Users/kaustubhbadve/Desktop/CRM-Bridge/crm-bridge")
# repo = git.Repo("/Users/kaustubhbadve/Desktop/Discovery/hexa-discovery")
# repo = git.Repo("/Users/kaustubhbadve/Desktop/EHR/ehr")
# repo = git.Repo("/Users/kaustubhbadve/Desktop/CMS/hexa-new-cms")
# repo = git.Repo("/Users/kaustubhbadve/Desktop/PatientService/patient")
# repo = git.Repo("/Users/kaustubhbadve/Desktop/Donna/donna")
repo = git.Repo("/Users/kaustubhbadve/Desktop/Lead/Lead")
# repo = git.Repo("/Users/kaustubhbadve/Desktop/apiGateway/api-gateway")
# repo = git.Repo("/Users/kaustubhbadve/Desktop/DMG/dmg")
# repo = git.Repo("/Users/kaustubhbadve/Desktop/call/call")
# repo = git.Repo("/Users/kaustubhbadve/Desktop/user/user")
# Your mock repo
mock_repo = git.Repo("/Users/kaustubhbadve/Desktop/untitled folder 3/ContributionsFromOtherPlatforms")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['kaustubhbadve7@gmail.com', 'kaustubhbadve@Kaustubhs-MacBook-Air'])
importer.import_repository()



