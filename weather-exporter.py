import prometheus_client
import time

PORT = 9999
UPDATE_PERIOD = 30
REALTIME = '/glusterfs/ec0/weewx4/realtime.txt'
UNIT_SYSTEM = 'metricwx'		# Options are 'us', 'metric' or 'metricwx' (default unit for weewx database)

# Other unit setting could found it the 'crt' section of the weewx.conf file.  Those include:
#  wind_units, temperature_units, pressure_units and cloudbase_units

if UNIT_SYSTEM == 'metricwx':		# These should be set to match what is in weewx.conf
   group_altitude = 'foot'		# Options are 'foot' or 'meter'
   group_degree_day = 'degree_F_day'	# Options are 'degree_F_day' or 'degree_C_day'
   group_distance = 'mile'		# Options are 'mile' or 'km'
   group_pressure = 'inHg'		# Options are 'inHg', 'mmHg', 'mbar', 'hPa', or 'kPa'
   group_rain = 'inch'			# Options are 'inch', 'cm', or 'mm'
   group_rainrate = 'inch_per_hour'	# Options are 'inch_per_hour', 'cm_per_hour', or 'mm_per_hour'
   group_speed = 'mile_per_hour'	# Options are 'mile_per_hour', 'km_per_hour', 'knot', or 'meter_per_second'
   group_speed2 = 'mile_per_hour2'	# Options are 'mile_per_hour2', 'km_per_hour2', 'knot2', or 'meter_per_second2'
   group_temperature = 'degree_F'	# Options are 'degree_F' or 'degree_C'
elif UNIT_SYSTEM == 'us':
   group_altitude = 'foot'		# Option 'foot'
   group_degree_day = 'degree_F_day'	# Option 'degree_F_day'
   group_distance = 'mile'		# Option 'mile'
   group_pressure = 'inHg'		# Option 'inHg', 'mmHg', 'mbar', 'hPa', or 'kPa'
   group_rain = 'inch'			# Option 'inch'
   group_rainrate = 'inch_per_hour'	# Option 'inch_per_hour'
   group_speed = 'mile_per_hour'	# Options are 'mile_per_hour' or 'knot'
   group_speed2 = 'mile_per_hour2'	# Options are 'mile_per_hour2' or 'knot2'
   group_temperature = 'degree_F'	# Option 'degree_F'
else:
   group_altitude = 'meter'		# Option 'meter'
   group_degree_day = 'degree_C_day'	# Option 'degree_C_day'
   group_distance = 'km'		# Option 'km'
   group_pressure = 'mmHg'		# Options are 'mmHg', 'mbar', 'hPa', or 'kPa'
   group_rain = 'cm'			# Options are 'cm', or 'mm'
   group_rainrate = 'cm_per_hour'	# Options are 'cm_per_hour', or 'mm_per_hour'
   group_speed = 'km_per_hour'		# Options are 'km_per_hour', 'knot', or 'meter_per_second'
   group_speed2 = 'km_per_hour2'	# Options are 'km_per_hour2', 'knot2', or 'meter_per_second2'
   group_temperature = 'degree_C'	# Option 'degree_C'
            
if group_altitude == 'foot':		# Option 'foot'
   cloudbasevalue = prometheus_client.Gauge('weather_cloud_base_foot',
                              'Cloud base')
else:					# Option 'meter'
   cloudbasevalue = prometheus_client.Gauge('weather_cloud_base_meter',
                              'Cloud base')

#if group_degree_day == 'degree_f_day':	# Option 'degree_F_day'
#else:					# Option 'degree_C_day'

#if group_distance == 'mile':		# Option 'mile'
#else:					# Option 'km'

if group_pressure == 'inHg':		# Option 'inHg'
   press = prometheus_client.Gauge('weather_barometer_inHg',
                              'Barometer sea level pressure')
   pressTH = prometheus_client.Gauge('weather_todays_high_pressure_inHg',
                              'Todays high pressure')
   pressTL = prometheus_client.Gauge('weather_todays_low_pressure_inHg',
                              'Todays low pressure')
elif group_pressure == 'mmHg':		# Option 'mmHg'
   press = prometheus_client.Gauge('weather_barometer_mmHg',
                              'Barometer sea level pressure')
   pressTH = prometheus_client.Gauge('weather_todays_high_pressure_mmHg',
                              'Todays high pressure')
   pressTL = prometheus_client.Gauge('weather_todays_low_pressure_mmHg',
                              'Todays low pressure')
elif group_pressure == 'mbar':		# Option 'mbar'
   press = prometheus_client.Gauge('weather_barometer_mbar',
                              'Barometer sea level pressure')
   pressTH = prometheus_client.Gauge('weather_todays_high_pressure_mbar',
                              'Todays high pressure')
   pressTL = prometheus_client.Gauge('weather_todays_low_pressure_mbar',
                              'Todays low pressure')
elif group_pressure == 'hPa':		# Option 'hPa'
   press = prometheus_client.Gauge('weather_barometer_hPa',
                              'Barometer sea level pressure')
   pressTH = prometheus_client.Gauge('weather_todays_high_pressure_hPa',
                              'Todays high pressure')
   pressTL = prometheus_client.Gauge('weather_todays_low_pressure_hPa',
                              'Todays low pressure')
else:					# Option 'kPa'
   press = prometheus_client.Gauge('weather_barometer_kPa',
                              'Barometer sea level pressure')
   pressTH = prometheus_client.Gauge('weather_todays_high_pressure_kPa',
                              'Todays high pressure')
   pressTL = prometheus_client.Gauge('weather_todays_low_pressure_kPa',
                              'Todays low pressure')

if group_rain == 'inch':		# Option 'inch'
   rfall = prometheus_client.Gauge('weather_rain_today_inch',
                              'Rain today')
   rmonth = prometheus_client.Gauge('weather_monthly_rainfall_inch',
                              'Monthly rainfall')
   ryear = prometheus_client.Gauge('weather_yearly_rainfall_inch',
                              'Yearly rainfall')
   rfallY = prometheus_client.Gauge('weather_yesterdays_rainfall_inch',
                              'Yesterdays rainfall')
   rhour = prometheus_client.Gauge('weather_rainfall_last_hour_inch',
                              'Rainfall last hour')
elif group_rain == 'cm':		# Option 'cm'
   rfall = prometheus_client.Gauge('weather_rain_today_cm',
                              'Rain today')
   rmonth = prometheus_client.Gauge('weather_monthly_rainfall_cm',
                              'Monthly rainfall')
   ryear = prometheus_client.Gauge('weather_yearly_rainfall_cm',
                              'Yearly rainfall')
   rfallY = prometheus_client.Gauge('weather_yesterdays_rainfall_cm',
                              'Yesterdays rainfall')
   rhour = prometheus_client.Gauge('weather_rainfall_last_hour_cm',
                              'Rainfall last hour')
else:					# Option 'mm'
   rfall = prometheus_client.Gauge('weather_rain_today_mm',
                              'Rain today')
   rmonth = prometheus_client.Gauge('weather_monthly_rainfall_mm',
                              'Monthly rainfall')
   ryear = prometheus_client.Gauge('weather_yearly_rainfall_mm',
                              'Yearly rainfall')
   rfallY = prometheus_client.Gauge('weather_yesterdays_rainfall_mm',
                              'Yesterdays rainfall')
   rhour = prometheus_client.Gauge('weather_rainfall_last_hour_mm',
                              'Rainfall last hour')

if group_rainrate == 'inch_per_hour':	# Option 'inch_per_hour'
   rrate = prometheus_client.Gauge('weather_current_rain_rate_inch_per_hour',
                              'Current rain rate per hour')
elif group_rainrate == 'cm_per_hour':	# Option 'cm_per_hour'
   rrate = prometheus_client.Gauge('weather_current_rain_rate_cm_per_hour',
                              'Current rain rate per hour')
else:					# Option 'mm_per_hour'
   rrate = prometheus_client.Gauge('weather_current_rain_rate_mm_per_hour',
                              'Current rain rate per hour')

if group_speed == 'mile_per_hour':	# Option 'mile_per_hour'
   wspeed = prometheus_client.Gauge('weather_wind_speed_average_mile_per_hour',
                              'Wind speed average') 
   wlatest = prometheus_client.Gauge('weather_latest_wind_speed_reading_mile_per_hour',
                              'Latest wind speed reading')
   windTM = prometheus_client.Gauge('weather_todays_high_wind_speed_mile_per_hour',
                              'Todays high wind speed')
   wgustTM = prometheus_client.Gauge('weather_todays_high_wind_gust_mile_per_hour',
                              'Todays high wind gust')
   wgust = prometheus_client.Gauge('weather_10_minute_high_gust_mile_per_hour',
                              '10 minute high gust')
elif group_speed == 'km_per_hour':	# Option 'km_per_hour'
   wspeed = prometheus_client.Gauge('weather_wind_speed_average_km_per_hour',
                              'Wind speed average') 
   wlatest = prometheus_client.Gauge('weather_latest_wind_speed_reading_km_per_hour',
                              'Latest wind speed reading')
   windTM = prometheus_client.Gauge('weather_todays_high_wind_speed_km_per_hour',
                              'Todays high wind speed')
   wgustTM = prometheus_client.Gauge('weather_todays_high_wind_gust_km_per_hour',
                              'Todays high wind gust')
   wgust = prometheus_client.Gauge('weather_10_minute_high_gust_km_per_hour',
                              '10 minute high gust')
elif group_speed == 'knot':		# Option 'knot'
   wspeed = prometheus_client.Gauge('weather_wind_speed_average_knot',
                              'Wind speed average') 
   wlatest = prometheus_client.Gauge('weather_latest_wind_speed_reading_knot',
                              'Latest wind speed reading')
   windTM = prometheus_client.Gauge('weather_todays_high_wind_speed_knot',
                              'Todays high wind speed')
   wgustTM = prometheus_client.Gauge('weather_todays_high_wind_gust_knot',
                              'Todays high wind gust')
   wgust = prometheus_client.Gauge('weather_10_minute_high_gust_knot',
                              '10 minute high gust')
else:					# Option 'meter_per_second'
   wspeed = prometheus_client.Gauge('weather_wind_speed_average_meter_per_second',
                              'Wind speed average') 
   wlatest = prometheus_client.Gauge('weather_latest_wind_speed_reading_meter_per_second',
                              'Latest wind speed reading')
   windTM = prometheus_client.Gauge('weather_todays_high_wind_speed_meter_per_second',
                              'Todays high wind speed')
   wgustTM = prometheus_client.Gauge('weather_todays_high_wind_gust_meter_per_second',
                              'Todays high wind gust')
   wgust = prometheus_client.Gauge('weather_10_minute_high_gust_meter_per_second',
                              '10 minute high gust')

#if group_speed2 == 'mile_per_hour2':	# Option 'mile_per_hour2'
#elif group_speed2 == 'km_per_hour2':	# Option 'km_per_hour2'
#elif group_speed2 == 'knot2':		# Option 'knot2'
#else:					# Option 'meter_per_second2'

if group_temperature == 'degree_F':	# Option 'degree_F'
   temp = prometheus_client.Gauge('weather_outside_temperature_F',
                              'Outside temperature')
   dew = prometheus_client.Gauge('weather_dewpoint_F',
                              'Dewpoint') 
   intemp = prometheus_client.Gauge('weather_inside_temperature_F',
                              'Inside temperature')
   wchill = prometheus_client.Gauge('weather_wind_chill_F',
                              'Wind chill')
   tempTH = prometheus_client.Gauge('weather_todays_high_temp_F',
                              'Todays high temperature')
   tempTL = prometheus_client.Gauge('weather_todays_low_temp_F',
                              'Todays low temperature')
   apptemp = prometheus_client.Gauge('weather_apparent_temperature_F',
                              'Apparent temperature')
else:					# Option 'degree_C'
   temp = prometheus_client.Gauge('weather_outside_temperature_C',
                              'Outside temperature')
   dew = prometheus_client.Gauge('weather_dewpoint_C',
                              'Dewpoint') 
   intemp = prometheus_client.Gauge('weather_inside_temperature_C',
                              'Inside temperature')
   wchill = prometheus_client.Gauge('weather_wind_chill_C',
                              'Wind chill')
   tempTH = prometheus_client.Gauge('weather_todays_high_temp_C',
                              'Todays high temperature')
   tempTL = prometheus_client.Gauge('weather_todays_low_temp_C',
                              'Todays low temperature')
   apptemp = prometheus_client.Gauge('weather_apparent_temperature_C',
                              'Apparent temperature')

bearing = prometheus_client.Gauge('weather_wind_bearing_degrees',
                              'Wind bearing')
hum = prometheus_client.Gauge('weather_relative_humidity_percent',
                              'Relative humidity')                              
beaufortnumber = prometheus_client.Gauge('weather_wind_speed_beaufort',
                              'Wind speed beaufort')
windrun = prometheus_client.Gauge('weather_wind_run_today_minutes',
                              'Wind run today')
inhum = prometheus_client.Gauge('weather_inside_humidity_percent',
                              'Inside humidity')
temptrend = prometheus_client.Gauge('weather_temperature_trend_value',
                              'Temperature trend over the last 3 hours')
humidex = prometheus_client.Gauge('weather_humidex_value',
                              'Humidex')
UV = prometheus_client.Gauge('weather_uv_index_value',
                              'UV index')
heatindex = prometheus_client.Gauge('weather_heat_index_value',
                              'Heat index')
avgbearing = prometheus_client.Gauge('weather_average_wind_bearing_degrees',
                              '10 minute average wind bearing')
ET = prometheus_client.Gauge('weather_evapotranspiration_today_value',
                              'Evapotranspiration today')
forecastnumber = prometheus_client.Gauge('weather_zambretti_forecast_value',
                              'The number of the current Zambretti forecast')
isdaylight = prometheus_client.Gauge('weather_currently_in_daylight_boolean',
                              'Flag to indicate that the location of the station is currently in daylight')
SensorContactLost = prometheus_client.Gauge('weather_sensor_contact_boolean',
                              'Flag to indicate connectivity between station and remote sensors')
SunshineHours = prometheus_client.Gauge('weather_sunshine_hours_hours',
                              'Sunshine hours so far today')
CurrentSolarMax = prometheus_client.Gauge('weather_current_solar_max_hours',
                              'Current theoretical max solar radiation')
IsSunny = prometheus_client.Gauge('weather_is_it_sunny_boolean',
                              'Is it sunny')
SolarRad = prometheus_client.Gauge('weather_solar_radiation_Wperm2',
                              'Solar radiation')


if __name__ == '__main__':
  prometheus_client.start_http_server(PORT)
  
while True:

    with open(REALTIME, 'r') as f:
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
