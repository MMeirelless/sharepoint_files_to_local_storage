from office365.runtime.auth.authentication_context import ClientCredential
from office365.sharepoint.client_context import ClientContext
import os

def get(client_id, client_secret, url, file_url):
    responses = {}
    credentials = ClientCredential(client_id, client_secret)
    ctx = ClientContext(url).with_credentials(credentials)

    # List of Files
    list_source = ctx.web.get_folder_by_server_relative_url(file_url)
    files = list_source.files
    ctx.load(files)
    ctx.execute_query()

    # Downloading Files
    for file_object in files:
        try:
            filename = file_object.name
            file_path = os.path.abspath(f"data/{filename}")
            with open(file_path, "wb") as local_file:
                file = ctx.web.get_file_by_server_relative_url(file_url+filename)
                file.download(local_file)
                ctx.execute_query()
            
            responses[filename] = {"status":"successful", "message":f"Your file is downloaded here: {file_path}"}

        except Exception as e:
            responses[filename] = {"status":"failed", "message":f"{e}"}
            continue

    return responses