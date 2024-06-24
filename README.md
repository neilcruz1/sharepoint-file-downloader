# SharePoint File/Folder Downloader
A Python script that lets you download **all SharePoint files** including their respective folders/subfolders, or ONLY the files themselves WITHOUT any folders.

This script has been tested on Personal SharePoint sites and currently has the functionality to **only download every single file from a given SharePoint site.**

You **MUST HAVE SharePoint app permissions to authenticate** and log in with either:
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

# Instructions (for Windows)
1. Make sure you've installed the latest version of Python (3.10.0+) as well as Git (2.45.0+).
2. Clone this project by entering the following in a command-prompt: **git clone https://github.com/neilcruz1/sharepoint-file-downloader.git**
3. In the sharepoint-file-downloader folder, click and open the **"install.bat"** file to install Python libraries/requirements (You will only need to do this once)
5. Once all requirements have finished installing, click and open the **"main.bat"** file to run the script.
6. Authenticate your SharePoint credentials in the program and proceed with your file downloading needs. 

All downloaded files/folders will be saved into the **"sharepoint_downloads"** folder within your project. 

# Libraries Used
* Office365-REST-Python-Client 2.5.10
* Maskpass

