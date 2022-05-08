import exercise_country as country

class Continent:
    """대륙"""
    def __init__(self, name, countries):
        """ (Continent, str, list of Country) -> NoneType

        대륙명 name과 국가 리스트 countries로 초기화한다.
        """
        self.name = name
        self.countries = countries


    def total_population(self) -> int:
        """
        대륙의 인구수를 반환한다.
        """
        return sum(country.population for country in self.countries)

    def __str__(self) -> str:
        """
        대륙의 문자열 표현을 반환한다.
        """
        return '{}\n{}'.format(self.name, '\n'.join(str(country) for country in self.countries))
