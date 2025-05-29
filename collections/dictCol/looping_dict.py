countries : dict = {'ngr' : 'Nigeria',
                    'usa' : 'United States',
                    'uk' : 'United Kingdom',
                    'fr' : 'France',
                    'ger' : 'Germany'}
print(countries)

for key, country in countries.items():
   print(f'{key} ===== {country}')