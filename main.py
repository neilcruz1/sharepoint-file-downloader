import os
import maskpass
from office365.sharepoint.client_context import ClientContext

ITEMS_TO_IGNORE = [
    'AllItems.aspx',
    'Combine.aspx',
    'DispForm.aspx',
    'EditForm.aspx',
    'repair.aspx',
    'template.dotx',
    'Thumbnails.aspx',
    'Upload.aspx'
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Start Client Context login
def get_client_context(client_id, client_secret, site_url):
    ctx = ClientContext(site_url).with_client_credentials(client_id, client_secret)
    return ctx

def get_user_context(username, password, site_url):
    ctx = ClientContext(site_url).with_user_credentials(username, password)
    return ctx

# Get ALL FILES in a specified folder path
def get_all_files(path):
    sp_files = path.files
    ctx.load(sp_files)
    ctx.execute_query()
    files = []
    for file in sp_files:
        #print(f'File name: {file}')
        files.append(file)
    return files

# Download a file in SharePoint site
def download_file(ctx, file_url, download_path):
    with open(download_path, 'wb') as local_file:
            file = (
                ctx.web.get_file_by_server_relative_url(file_url)
                .download(local_file)
                .execute_query()
            )
            print(f'[OK] file downloaded to: {download_path}')

# Recursively download every file in a SharePoint without subfolders 
def download_all_files_without_folders(ctx, folder_url, local_path, choice):
    
    # Root folder should "Shared Documents" or the "Documents" folder in any SharePoint site
    folder = ctx.web.get_folder_by_server_relative_url(folder_url)
    ctx.load(folder)
    ctx.execute_query()
    
    # This is where all of our files will be downloaded and saved to
    if not os.path.exists(local_path):
        os.makedirs(local_path)

    # Get subfolders and start traversing
    subfolders = folder.folders
    ctx.load(subfolders)
    ctx.execute_query()

    # Download ALL FOLDERS with their respective files and location
    if choice.casefold() == 'y':
         for subfolder in subfolders:
            if subfolder.name == 'Forms':
                continue 
            subfolder_url = subfolder.properties["ServerRelativeUrl"]
            print(f'Now Accessing: {subfolder_url}')
            local_path = 'sharepoint_downloads' + subfolder_url
            download_all_files_without_folders(ctx, subfolder_url, local_path, choice)

    # Download ONLY FILES, NO FOLDERS !!!
    if choice.casefold() == 'n':
        for subfolder in subfolders:
            subfolder_url = subfolder.properties["ServerRelativeUrl"]
            print(f'Now Accessing: {subfolder_url}')
            download_all_files_without_folders(ctx, subfolder_url, local_path, choice)
    
    sp_files = get_all_files(folder)
 
    # Iterate through each file and download
    for file in sp_files:
        file_url = file.properties["ServerRelativeUrl"]
        if file.name in ITEMS_TO_IGNORE:
            break
        if choice.casefold() == 'n':
            download_path = os.path.join('sharepoint_downloads', os.path.basename(file_url))
            download_file(ctx, file_url, download_path)    
        else:
            download_path = 'sharepoint_downloads' + file_url
            download_file(ctx, file_url, download_path)

def enter_credentials():
    while True:
        clear_screen()
        print('*** SharePoint File/Folder Downloader ***\n')
        print('Please login with either your SharePoint "Username/Password" or "Client ID/Secret"')
        print('Press CTRL + C to terminate the program at any time\n')
        choice = str(input('Select [U/u] Username | [C/c] Client ID/Secret: '))
        if choice.casefold() == 'u':
            clear_screen()
            username = str(input('Enter username: '))
            password = maskpass.askpass('Enter password: ')
            print('\nEnter your SharePoint URL with the following format --> https://{tenant}.sharepoint.com/sites/{site}')
            site_url = str(input('URL: '))
            ctx = get_user_context(username, password, site_url)
            return ctx
            
        if choice.casefold() == 'c':
            clear_screen()
            client_id = str(input('Enter or paste your Client ID: '))
            client_secret = maskpass.askpass('Enter or paste your Client Secret: ')
            print('\nEnter your SharePoint URL with the following format --> https://{tenant}.sharepoint.com/sites/{site}')
            site_url = str(input('URL: '))
            ctx = get_client_context(client_id, client_secret, site_url)
            return ctx

if __name__ == "__main__":
    clear_screen()
    ctx = enter_credentials()
    folder_url = 'Shared Documents'
    local_path = 'sharepoint_downloads'
    clear_screen()
    
    while True:
        print('Would you like to include ALL ASSOCIATED FOLDERS with your SharePoint files while downloading?')
        print('Files will be downloaded to sharepoint_downloads\n')
        choice =  str(input('[Y/y] Yes | [N/n] No | [Q/q] Quit : '))

        if choice.casefold() == 'y' or choice.casefold() == 'n':
            download_all_files_without_folders(ctx, folder_url, local_path, choice)
            print('DONE\n')

        if choice.casefold() == 'q':
            exit()