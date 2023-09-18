import pycurl
from io import BytesIO
import time

# URL to make the POST request to
url = "https://eth-mainnet-full-rpc-2.dwellir.com"

# Options to pycurl
curl_options = {
    "headers": ['Connection: keep-alive', 'Keep-Alive: timeout=5, max=20', "Content-Type: application/json"],
    "data": '{\"method\":\"eth_blockNumber\",\"params\":[],\"id\":1,\"jsonrpc\":\"2.0\"}'
}

# Initialize a Curl object
c = pycurl.Curl()

# Set the URL
c.setopt(pycurl.URL, url)

# Set the headers for the request
c.setopt(pycurl.HTTPHEADER, curl_options["headers"])

# Set the HTTP method to POST
c.setopt(pycurl.POST, 1)

# Set the POST data if applicable
if curl_options['data'] != "":
    c.setopt(pycurl.POSTFIELDS, curl_options['data'])

# Create a buffer to store the response
response_buffer = BytesIO()
c.setopt(pycurl.WRITEDATA, response_buffer)

# Start measuring time
#start_time = time.time()

# Set options to measure connection data
c.setopt(pycurl.TIMEOUT, 2)  # Set a timeout for the request
c.setopt(pycurl.NOSIGNAL, 1)  # Disable signals for multi-threaded applications

# Perform the POST request
c.perform()

# Calculate the latency
#end_time = time.time()
#latency = end_time - start_time

# Get connection data
total_time = c.getinfo(pycurl.TOTAL_TIME)
dns_time = c.getinfo(pycurl.NAMELOOKUP_TIME)
connect_time = c.getinfo(pycurl.CONNECT_TIME)
pretransfer_time = c.getinfo(pycurl.PRETRANSFER_TIME)
starttransfer_time = c.getinfo(pycurl.STARTTRANSFER_TIME)

# Get the HTTP response code
http_code = c.getinfo(pycurl.HTTP_CODE)

# Close the Curl object
c.close()

# Print the connection data
print(f"Total Time: {total_time} seconds")
print(f"DNS Time: {dns_time} seconds")
print(f"Connect Time: {connect_time} seconds")
print(f"Pretransfer Time: {pretransfer_time} seconds")
print(f"Starttransfer Time: {starttransfer_time} seconds")
print(f"HTTP Response Code: {http_code}")

# Print the response body (if needed)
response_body = response_buffer.getvalue().decode('utf-8')
print("Response Body:")
print(response_body)
