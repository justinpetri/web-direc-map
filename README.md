# web-direc-map
A simple script that uses the request package with a directory  text file to identify hidden web directories.

Users must create or download a .txt file with a list of potential directory names. After updating the path to that file, in the web_direct_map.py file, the script will store the contents into a data variable. It will then turn it into a list by separating every item by line. Each item in the list will be combined with the user-entered url to attempt to identify a directory. If an http-request code is returned and matches the list of specified codes, the program will return the result. Threading is employed to improve efficiency and send multiple requests.

NOTICE: This program is for educational use only.
