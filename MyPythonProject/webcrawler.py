"""
File: webcrawler.py
Name: Hsin-En, Tsai
Date: Dec 27, 2023
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        tags = soup.find_all('table', {'class': 't-stripe'})
        male_number = 0
        female_number = 0
        for table in tags:  # go into <tr>
            rows = table.find_all('tr')
            for row in rows:  # find out <td>
                cells = row.find_all('td')
                n = 2
                m = 4
                if len(cells) > n:  # for making sure that the number of <td> is larger than n.
                    data_male = cells[n].text
                    male_number += int(data_male.replace(',', ''))
                if len(cells) > m:
                    data_female = cells[m].text
                    female_number += int(data_female.replace(',', ''))
        print('Male Number: ' + str(male_number))
        print('Female Number: ' + str(female_number))


if __name__ == '__main__':
    main()
