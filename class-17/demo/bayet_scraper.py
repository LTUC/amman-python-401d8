import requests

URL = "https://www.bayt.com/en/jordan/jobs/python-jobs/"
res = requests.get(URL)
print(res.content)

from bs4 import BeautifulSoup
soup = BeautifulSoup(res.content, 'html.parser')
# print(soup)

results_div = soup.find('div', id="results_inner_card")
# print(type(results_div))

results_ul = results_div.find('ul',class_="media-list")
# print(results_ul)

jobs_list = results_ul.find_all('li')
# print(len(jobs_list))

# for job in jobs_list:
#     print(job)
#     print("*"*50)
#     print("*"*50)

all_jobs_object = []
for job in jobs_list:
    job_dict = {'title':'', 'company_name':''}
    title_before_stripping = job.find('h2')
    company_before_strpping = job.find('b', class_='p10r')
    if title_before_stripping:
        title = title_before_stripping.get_text().strip()
        job_dict['title'] = title
        company_name = company_before_strpping.get_text().strip()
        job_dict['company_name'] = company_name
        all_jobs_object.append(job_dict)


print(all_jobs_object)
# Print title for 1 job
# print(jobs_list[1].find('h2').get_text())

import json

with open('all_jobs.json', 'w') as f:
    content = json.dumps(all_jobs_object)
    f.write(content)