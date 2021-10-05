import requests

rating_pages = []

years = range(2010, 2013)
months = range(1, 13)
weeks = range(0, 5)

for year in years:
    for month in months:
        for week in weeks:
            url = "https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}".format(year, month, week)
            response = requests.get(url)
            rating_pages.append(response.text)


print(len(rating_pages)) 
print(rating_pages[0])
