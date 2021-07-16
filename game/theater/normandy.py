from game.theater.projections import TransverseMercator

PARAMETERS = TransverseMercator(
    central_meridian=-3,
    false_easting=-195526.00000000204,
    false_northing=-5484812.999999951,
    scale_factor=0.9996,
)

SEASONAL_CONDITIONS = SeasonalConditions(
    summer_avg_pressure=30.02,  # TODO: More science
    winter_avg_pressure=29.72,  # TODO: More science
    summer_avg_temperature=20.0,
    winter_avg_temperature=0.0,
    temperature_day_night_difference=5.0,
    
    weather_type_chances={
        # TODO: More science for all these values
        Season.Winter: WeatherTypeChances(
            thunderstorm=1,
            raining=20,
            cloudy=60,
            clear_skies=20,
        ),
        Season.Spring: WeatherTypeChances(
            thunderstorm=1,
            raining=20,
            cloudy=40,
            clear_skies=40,
        ),
        Season.Summer: WeatherTypeChances(
            thunderstorm=1,
            raining=10,
            cloudy=30,
            clear_skies=60,
        ),
        Season.Autumn: WeatherTypeChances(
            thunderstorm=1,
            raining=30,
            cloudy=50,
            clear_skies=20,
        ),
    },
)
