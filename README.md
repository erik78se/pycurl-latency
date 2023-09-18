# Mater latency with pycurl

This will return information pretty much like what with curl -w which will give very good precision of latency due to curl:s low level code for getting latency information.

# Install dependencies for pycurl

This might differ based on your distribution and python version. Make sure you build for your version

    sudo apt install python3.11-venv
    sudo apt-get install libssl-dev libcurl4-openssl-dev
    sudo apt-get install build-essential python3.11-dev

# Create a venv

    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip # might not need this
    pip install --upgrade setuptools # might not need this
    pip install pycurl

# Run

    python3 latmater.py

    erik@erik-thinkpad:~/pycurl-latency$ python latmeter.py 
    Total Time: 0.064819 seconds
    DNS Time: 0.010095 seconds
    Connect Time: 0.016823 seconds
    Pretransfer Time: 0.05676 seconds
    Starttransfer Time: 0.056763 seconds
    HTTP Response Code: 200
    Response Body:
    {"jsonrpc":"2.0","id":1,"result":"0x1151f51"}

