import requests
import json
import datetime


def get_trending_repositories(top_size, days_ago):
    created_date = datetime.date.today() - datetime.timedelta(days_ago)
    request_link = (
        'https://api.github.com/search/repositories?q=created:>'
        '{}&sort=stars&order=desc'.
        format(created_date.strftime('%Y-%m-%d'))
    )
    return requests.get(request_link).json()['items'][:top_size]


def get_open_issues_amount(repository_owner, repository_name):
    request_link = (
        'https://api.github.com/repos/{}/{}/issues'.
        format(repository_owner, repository_name)
    )
    return requests.get(request_link).json()


def print_data_to_console(number, repository_name, repository_url, amount_issues):
    print('{}{}.{}Name: {}'.format('\n', number, '\t', repository_name))
    print('{}Url: {}'.format('\t', repository_url))
    print('{}Amount issues: {}{}'.format('\t', amount_issues, '\n'))


if __name__ == '__main__':
    top_size = 20
    days_ago = 7
    repositories = get_trending_repositories(top_size, days_ago)
    for number, repository in enumerate(repositories, start=1):
        issues = get_open_issues_amount(
            repository['owner']['login'],
            repository['name'])
        print_data_to_console(
            number,
            repository['name'],
            repository['html_url'],
            len(issues))
