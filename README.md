# SharePoint File/Folder Downloader
A Python script that lets you download SharePoint files with their respective folders/subfolders, or ONLY the files themselves WITHOUT including their folders/subfolders.
This script has been tested on Personal SharePoint sites and currently only has the functionality to **download EVERY SINGLE FILE FROM A GIVEN SHAREPOINT SITE. **

* You MUST HAVE SharePoint app permissions to authenticate and log in with either:
* USERNAME & PASSWORD
* CLIENT ID & CLIENT SECRET

# PLEASE READ BEFORE YOU RUN SCRIPT:
You may receive errors when logging in with your USERNAME AND PASSWORD to authenticate into your SharePoint site. 
**To solve this, disable Entra Admin Security Defaults** by following the directions with the link below:
* https://learn.microsoft.com/en-us/entra/fundamentals/security-defaults

If you would like to use Client ID/Client Secret credentials to authenticate with, 
please follow the instructions on how to **set up App-Only Tenant Permissions on your SharePoint site** with the link below: 
* https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azureacs

Once you have checked and performed the instructions above, follow the instructions on setting this up below.

# Instructions
1. Make sure you've installed the latest version of Python (3.10.0+).
2. Open command-prompt or terminal and install the Python library requirements by entering "install.bat"
3. Once all requirements have finished installing, run the script by entering "py main.py" on Windows, or "python3 main.py" on Mac OSX.
4. Select your method of authenticating (either username/password or client ID/Secret).
5. Select your file download choices (include ALL files/folders/subfolders & their structure, or no folders and ONLY files).
6. All downloaded files will be saved into the "sharepoint_downloads" folder within this project. 

# Libraries Used
* Office365-REST-Python-Client 2.5.10
* Maskpass

