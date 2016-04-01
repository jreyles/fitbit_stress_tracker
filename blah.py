import fitbit
import ConfigParser
import json
  
#Load Settings
parser = ConfigParser.SafeConfigParser()
 
parser.read('config.ini')
 
CI_id              = parser.get('Login Parameters', 'CLIENT_ID')
CI_client_secret   = parser.get('Login Parameters', 'CLIENT_SECRET')
CI_access_token    = parser.get('Login Parameters', 'ACCESS_TOKEN')
CI_refresh_token   = parser.get('Login Parameters', 'REFRESH_TOKEN')
 
authd_client = fitbit.Fitbit(CI_id, CI_client_secret, oauth2=True, access_token=CI_access_token, refresh_token=CI_refresh_token)
 
intradayS = authd_client.intraday_time_series('activities/steps', base_date    = '2016-03-01', detail_level = '1min', start_time   = None, end_time     = None)
 
f = open('datadumpSteps.json', 'w')
json.dump(intradayS, f)
 
intradayH = authd_client.intraday_time_series('activities/heart', base_date    = '2016-03-30', detail_level = '1sec', start_time   = None, end_time     = None) 
f = open('datadumpHeart3-30.json', 'w')

intradayH = authd_client.intraday_time_series('activities/heart', base_date    = '2016-03-29', detail_level = '1sec', start_time   = None, end_time     = None) 
f = open('datadumpHeart3-29.json', 'w')

intradayH = authd_client.intraday_time_series('activities/heart', base_date    = '2016-03-28', detail_level = '1sec', start_time   = None, end_time     = None) 
f = open('datadumpHeart3-28.json', 'w')


json.dump(intradayH, f)