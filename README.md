# Mass-Downloader-Tutorial
This is a mass downloader for files under the same domain name. If a file is available (returns a 200 status code), then it will be downloaded into the user's "Downloads" folder. If a file is unavailable (returns a 404 status code), then an error message will be printed to the terminal.  
  
Because the terminal has a limit of 1024 characters, input is pasted into the text file. The script.py file reads the text file and processes the links. The Requests (Python) library sends out an HTTP GET request for data. When a webpage is available, users receive a 200 status code. The Re library is used to establish domain name patterns. The OS module is used to save files to a user's "Downloads" folder.  
  
To use the program, follow the instructions below

1. Copy the links you'd like to evaluate
2. Paste the links into the "input.txt" file  
3. In "input.txt", use "CTRL" + "S" to save the changes  
4. Navigate to the "script.py" file  
5. To run the script file, either type "python script.py" in the terminal, or navigate to the top right corner and click the play button
