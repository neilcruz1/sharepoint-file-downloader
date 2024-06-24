# SharePoiont File/Folder Downloader
A Python script that lets you download SharePoint files with their respective folders/subfolders, or ONLY the files themselves WITHOUT including their folders/subfolders.
This script has been tested on Personal SharePoint sites. 

* You MUST HAVE SharePoint app permissions to authenticate and log in with either:
* USERNAME & PASSWORD
* CLIENT ID & CLIENT SECRET

# PLEASE READ BEFORE YOU RUN SCRIPT:
* If you are receiving login errors using your USERNAME AND PASSWORD to authenticate into your SharePoint site, you may need to disable Entra Admin Security Defaults by following the directions here --> https://learn.microsoft.com/en-us/entra/fundamentals/security-defaults
* If you would like to use Client ID/Client Secret credentials, please follow the instructions on how to set up App-Only Tenant Permissions on your SharePoint site here --> https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azureacs

Once you have checked and performed the instructions above, go ahead and run main.py

# Libraries Used
* Office365-REST-Python-Client 2.5.10
* Maskpass

