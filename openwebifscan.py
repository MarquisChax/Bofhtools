import shodan
import requests


SHODAN_API = ''
api = shodan.Shodan(SHODAN_API)

list200 = []


try:
	results = api.search('openwebif')

	print 'Results found: %s' % results['total']


	for service in results['matches']:

	    try:
	        response = requests.get('http://{0}?'.format(service['ip_str']), auth=('root', ''),timeout=1)
	        if(response.status_code == 200):
	        	list200.append(service['ip_str'])
	    		print service['ip_str']
	    except:
	    	pass


except shodan.APIError, e:
	print 'Error: %s' % e


quit()
