from datetime import datetime

def save_log(response):
    files = response.keys()
    files_downloaded = 0
    event = ""

    with open("action.log", "a") as log_file:
        for file in files:
            status  = response[file]["status"]
            files_downloaded += 1 if status == "successful" else 0

        event = f"{datetime.now()} | successful | {files_downloaded}\n"
        log_file.write(event)

        for file in files:
            file_response = response[file]
            status  = file_response["status"]            
            message = file_response["message"]

            if status == "failed":
                event = f"{datetime.now()} | {status} | {file} | {message}\n"
                log_file.write(event)
