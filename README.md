# 17_sites_monitoring

This script takes file with urls and prints status every of them.<br />
Response for successful HTTP requests - 200, all other negative.<br />
Expiration date successful if date more or equals to 1 month.<br />

# How to run:<br />
1. Install libraries:<br />
pip install -r requirements.txt<br />
2. You can run the program by two ways:<br />
py -3 check_sites_health.py \<path_to_file\><br />
or program will ask the path to file with urls:<br />
py -3 check_sites_health.py<br />
3. Check output. <br />
3.1. If status code and expiration date are right you will get next output:<br />
https://docs.python.org/3 - PASSED.<br />
3.2. If status code or expiration date not right you will get next output:<br />
http://www.yaoq.net/dasfasdfsdafasdthread-1359fsdafdasfd006-1-1.html - status code FAILED.<br />
