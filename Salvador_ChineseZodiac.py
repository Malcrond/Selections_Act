Rat = [1948, 1960, 1972, 1984, 1996, 2008, 2020]
Ox = [1949, 1961, 1973, 1985, 1997, 2009, 2021]
Tiger = [1950, 1962, 1974, 1986, 1998, 2010, 2022]
Rabbit = [1951, 1963, 1975, 1987, 1999, 2011, 2023]
Dragon = [1952, 1964, 1976, 1988, 2000, 2012, 2024]
Snake = [1953, 1965, 1977, 1989, 2001, 2013, 2025]
Horse = [1954, 1966, 1978, 1990, 2002, 2014, 2026]
Goat = [1955, 1967, 1979, 1991, 2003, 2015, 2027]
Monkey = [1956, 1968, 1980, 1992, 2004, 2016, 2028]
Rooster = [1957, 1969, 1981, 1993, 2005, 2017, 2029]
Dog = [1958, 1970, 1982, 1994, 2006, 2018, 2030]
Pig = [1959, 1971, 1983, 1995, 2007, 2019, 2031]
while True:
    yearofbirth = input("What is your year of birth?: ")
    if yearofbirth.isdigit():
        yearofbirth = int(yearofbirth)
        if 1948 <= yearofbirth <= 2031:
            break
        elif yearofbirth == 2077:
            break
        else:
            print("The Chinese Zodiac starts at 1948 ---> 2031...")
    else:
        print("Please enter a valid year...")
enogeb = "zodiac"
if yearofbirth in Rat:
    enogeb = "Rat"
else:
    if yearofbirth in Ox:
        enogeb = "Ox"
    else:
        if yearofbirth in Tiger:
            enogeb = "Tiger"
        else:
            if yearofbirth in Rabbit:
                enogeb = "Rabbit"
            elif yearofbirth in Dragon:
                enogeb = "Dragon"
            elif yearofbirth in Snake:
                enogeb = "Snake"
            elif yearofbirth in Horse:
                enogeb = "Horse"
            elif yearofbirth in Goat:
                enogeb = "Goat"
            elif yearofbirth in Monkey:
                enogeb = "Monkey"
            elif yearofbirth in Rooster:
                enogeb = "Rooster"
            elif yearofbirth in Dog:
                enogeb = "Dog"
            elif yearofbirth in Pig:
                enogeb = "Pig"
            elif yearofbirth == 2077:
                enogeb = "Samurai"

print(f"{yearofbirth} is the year of the {enogeb}")
