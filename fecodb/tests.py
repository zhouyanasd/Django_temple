# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
#
# application = get_wsgi_application()
#
# from rest_framework.test import APIRequestFactory
# from rest_framework.test import force_authenticate
# from fecodb.views import location_views
#
# # Using the standard RequestFactory API to create a form POST request
# factory = APIRequestFactory()
# request = factory.get('/location/list/?format=json')
#
# # force authenticate
# # user = User.objects.get(username='olivia')
# # force_authenticate(request, user=user)
#
# # call the view request
# view = location_views.NmrLocationList.as_view()
# response = view(request)
#
# print(response.data)



import requests
import json

url = 'http://127.0.0.1:8000/api/nmr/detail/?nmr_id=1'  # django api路径

parms = {
    'location_id': 1,
}

headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}

# resp = requests.post(url, data=parms, headers=headers)
resp = requests.get(url)
# Decoded text returned by the request
text = resp.text
data = json.loads(text)['data']['value']
print(data)


