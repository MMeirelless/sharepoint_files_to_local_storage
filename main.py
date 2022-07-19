import modules.collector as collector, modules.log_recorder as log_recorder

# Your credentials
client_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
client_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Remember to replace with your information
url = "https://{tenant}.sharepoint.com/sites/{your_site}/" # Your URL site
file_path = "/sites/{your_site}/Shared Documents/{folder_name}/" # Your files folder path

collector_response = collector.get(client_id, client_secret, url, file_path)
log_recorder.save_log(collector_response)


