"""
@Author : Avinash Jadhav
@Date : 2021-11-12
@Last Modify by : Avinash Jadhav
@Title : calculate wind chill rate
"""
import sys


def wind_chill_rate(temp, speed):
    """
        @Description : take temperature and wind speed and calculate wind chill rate
        @Parameter   : parameter is temp and speed
        @return      : wind chill rate
    """
    return 35.74 + (0.6415 * temp) + (0.4275 * temp - 35.75) * (speed ** 0.16)


temperature = float(sys.argv[1])
wind_speed = float(sys.argv[2])

wind_chill = wind_chill_rate(temperature, wind_speed)
print("wind_chill_rate=", wind_chill)

