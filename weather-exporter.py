import prometheus_client
import time

UPDATE_PERIOD = 30

temp = prometheus_client.Gauge('weather_outside_temperature_C',
                              'Outside temperature')
hum = prometheus_client.Gauge('weather_relative_humidity_percent',
                              'Relative humidity')                              
dew = prometheus_client.Gauge('weather_dewpoint_C',
                              'Dewpoint') 
wspeed = prometheus_client.Gauge('weather_wind_speed_average_kmph',
                              'Wind speed average') 
wlatest = prometheus_client.Gauge('weather_latest_wind_speed_reading_kmph',
                              'Latest wind speed reading')
bearing = prometheus_client.Gauge('weather_wind_bearing_degrees',
                              'Wind bearing')
rrate = prometheus_client.Gauge('weather_current_rain_rate_mmph',
                              'Current rain rate per hour')
rfall = prometheus_client.Gauge('weather_rain_today_mm',
                              'Rain today')
press = prometheus_client.Gauge('weather_barometer_mb',
                              'Barometer sea level pressure')
beaufortnumber = prometheus_client.Gauge('weather_wind_speed_beaufort',
                              'Wind speed beaufort')
windrun = prometheus_client.Gauge('weather_wind_run_today_minutes',
                              'Wind run today')
rmonth = prometheus_client.Gauge('weather_monthly_rainfall_mm',
                              'Monthly rainfall')
ryear = prometheus_client.Gauge('weather_yearly_rainfall_mm',
                              'Yearly rainfall')
rfallY = prometheus_client.Gauge('weather_yesterdays_rainfall_mm',
                              'Yesterdays rainfall')
intemp = prometheus_client.Gauge('weather_inside_temperature_C',
                              'Inside temperature')
inhum = prometheus_client.Gauge('weather_inside_humidity_percent',
                              'Inside humidity')
wchill = prometheus_client.Gauge('weather_wind_chill_C',
                              'Wind chill')
temptrend = prometheus_client.Gauge('weather_temperature_trend_value',
                              'Temperature trend over the last 3 hours')
tempTH = prometheus_client.Gauge('weather_todays_high_temp_C',
                              'Todays high temperature')
tempTL = prometheus_client.Gauge('weather_todays_low_temp_C',
                              'Todays low temperature')
windTM = prometheus_client.Gauge('weather_todays_high_wind_speed_kmph',
                              'Todays high wind speed')
wgustTM = prometheus_client.Gauge('weather_todays_high_wind_gust_kmph',
                              'Todays high wind gust')
pressTH = prometheus_client.Gauge('weather_todays_high_pressure_mb',
                              'Todays high pressure')
pressTL = prometheus_client.Gauge('weather_todays_low_pressure_mb',
                              'Todays low pressure')
wgust = prometheus_client.Gauge('weather_10_minute_high_gust_kmph',
                              '10 minute high gust')
heatindex = prometheus_client.Gauge('weather_heat_index_value',
                              'Heat index')
humidex = prometheus_client.Gauge('weather_humidex_value',
                              'Humidex')
UV = prometheus_client.Gauge('weather_uv_index_value',
                              'UV index')
ET = prometheus_client.Gauge('weather_evapotranspiration_today_value',
                              'Evapotranspiration today')
SolarRad = prometheus_client.Gauge('weather_solar_radiation_Wperm2',
                              'Solar radiation')
avgbearing = prometheus_client.Gauge('weather_average_wind_bearing_degrees',
                              '10 minute average wind bearing')
rhour = prometheus_client.Gauge('weather_rainfall_last_hour_mm',
                              'Rainfall last hour')
forecastnumber = prometheus_client.Gauge('weather_zambretti_forecast_value',
                              'The number of the current Zambretti forecast')
isdaylight = prometheus_client.Gauge('weather_currently_in_daylight_boolean',
                              'Flag to indicate that the location of the station is currently in daylight')
SensorContactLost = prometheus_client.Gauge('weather_sensor_contact_boolean',
                              'Flag to indicate connectivity between station and remote sensors')
cloudbasevalue = prometheus_client.Gauge('weather_cloud_base_m',
                              'Cloud base')
apptemp = prometheus_client.Gauge('weather_apparent_temperature_C',
                              'Apparent temperature')
SunshineHours = prometheus_client.Gauge('weather_sunshine_hours_hours',
                              'Sunshine hours so far today')
CurrentSolarMax = prometheus_client.Gauge('weather_current_solar_max_hours',
                              'Current theoretical max solar radiation')
IsSunny = prometheus_client.Gauge('weather_is_it_sunny_boolean',
                              'Is it sunny')


if __name__ == '__main__':
  prometheus_client.start_http_server(9999)
  
while True:

#  with open('/home/pi/distance.txt', 'r') as f:
#      distance = f.readline()

    with open('/var/www/html/realtime.txt', 'r') as f:
        weather_string = f.read().split(' ')

    try: 
        float(weather_string[2])
        temp.set(float(weather_string[2]))
    except: pass
    try: 
        float(weather_string[3])
        hum.set(float(weather_string[3]))
    except: pass
    try: 
        float(weather_string[4])
        dew.set(float(weather_string[4]))
    except: pass
    try:
        float(weather_string[5])
        wspeed.set(float(weather_string[5]))
    except: pass
    try:
        float(weather_string[6])
        wlatest.set(float(weather_string[6]))
    except: pass
    try:
        float(weather_string[7])
        bearing.set(float(weather_string[7]))
    except: pass
    try:
        float(weather_string[8])
        rrate.set(float(weather_string[8]))
    except: pass
    try:
        float(weather_string[9])
        rfall.set(float(weather_string[9]))
    except: pass
    try:
        float(weather_string[10])
        press.set(float(weather_string[10]))
    except: pass
    try:
        float(weather_string[12])
        beaufortnumber.set(float(weather_string[12]))
    except: pass
    try:
        float(weather_string[17])
        windrun.set(float(weather_string[17]))
    except: pass
    try:
        float(weather_string[19])
        rmonth.set(float(weather_string[19]))
    except: pass
    try:
        float(weather_string[20])
        ryear.set(float(weather_string[20]))
    except: pass
    try:
        float(weather_string[21])
        rfallY.set(float(weather_string[21]))
    except: pass
    try:
        float(weather_string[22])
        intemp.set(float(weather_string[22]))
    except: pass
    try:
        float(weather_string[23])
        inhum.set(float(weather_string[23]))
    except: pass
    try:
        float(weather_string[24])
        wchill.set(float(weather_string[24]))
    except: pass
    try:
        float(weather_string[25])
        temptrend.set(float(weather_string[25]))
    except: pass
    try:
        float(weather_string[26])
        tempTH.set(float(weather_string[26]))
    except: pass
    try:
        float(weather_string[28])
        tempTL.set(float(weather_string[28]))
    except: pass
    try:
        float(weather_string[30])
        windTM.set(float(weather_string[30]))
    except: pass
    try:
        float(weather_string[32])
        wgustTM.set(float(weather_string[32]))
    except: pass
    try:
        float(weather_string[34])
        pressTH.set(float(weather_string[34]))
    except: pass
    try:
        float(weather_string[36])
        pressTH.set(float(weather_string[36]))
    except: pass
    try:
        float(weather_string[41])
        heatindex.set(float(weather_string[41]))
    except: pass
    try:
        float(weather_string[42])
        humidex.set(float(weather_string[42]))
    except: pass
    try:
        float(weather_string[43])
        UV.set(float(weather_string[43]))
    except: pass
    try:
        float(weather_string[44])
        ET.set(float(weather_string[44]))
    except: pass
    try:
        float(weather_string[45])
        SolarRad.set(float(weather_string[45]))
    except: pass
    try:
        float(weather_string[46])
        avgbearing.set(float(weather_string[46]))
    except: pass
    try:
        float(weather_string[47])
        rhour.set(float(weather_string[47]))
    except: pass
    try:
        float(weather_string[48])
        forecastnumber.set(float(weather_string[48]))
    except: pass
    try:
        float(weather_string[49])
        isdaylight.set(float(weather_string[49]))
    except: pass
    try:
        float(weather_string[50])
        SensorContactLost.set(float(weather_string[50]))
    except: pass
    try:
        float(weather_string[52])
        cloudbasevalue.set(float(weather_string[52]))
    except: pass
    try:
        float(weather_string[54])
        apptemp.set(float(weather_string[54]))
    except: pass
    try:
        float(weather_string[55])
        SunshineHours.set(float(weather_string[55]))
    except: pass
    try:
        float(weather_string[56])
        CurrentSolarMax.set(float(weather_string[56]))
    except: pass
    try:
        float(weather_string[57])
        IsSunny.set(float(weather_string[57]))
    except: pass

    time.sleep(UPDATE_PERIOD)
