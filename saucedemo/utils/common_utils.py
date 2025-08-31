from datetime import datetime
def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content + '\t' + get_current_timestamp() + '\n')