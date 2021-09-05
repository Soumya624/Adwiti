import cloudmersive_convert_api_client
from cloudmersive_convert_api_client.rest import ApiException
from pprint import pprint
# Configure API key authorization: Apikey
configuration = cloudmersive_convert_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'
# create an instance of the API class
api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/path/to/file' # file | Input file to perform the operation on.
try:
    # Convert PowerPoint PPTX to PNG image array
    api_response = api_instance.convert_document_pptx_to_png(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDocumentApi->convert_document_pptx_to_png: %s\n" % e)