import datetime,os
from pathlib import Path
def upload(file, folder):
    date_time =  datetime.datetime.now()
    base_dir = Path(__file__).resolve().parent.parent
    location = 'wissen\\static\\assets\\img\\uploaded\\' + folder + date_time
    final_location = os.join(base_dir, location)
    with open(final_location, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

# folder = 'Events'
# base_dir = Path(__file__).resolve().parent.parent
# location = 'wissen\\static\\assets\\img\\uploaded\\' + folder
# final_location = os.path.join(base_dir, location)
# print(final_location)