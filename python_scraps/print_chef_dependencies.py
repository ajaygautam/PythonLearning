import os
import json
from pprint import pprint

berks_package_folder="/Users/agautam/work/git/chef/hs_hsconfig/tmp/cookbooks"

for cookbook in os.listdir(berks_package_folder):
    metadata_json_file = os.path.join(berks_package_folder, cookbook, "metadata.json")
    # print("Checking: " + metadata_json_file)
    if os.path.isfile(metadata_json_file):
        with open(metadata_json_file) as data_file:
            metadata = json.load(data_file)
        # pprint(metadata)
        if cookbook != metadata.get("name"):
            print("========= Name does not match for cookbook " + cookbook)
        print("{} {}".format(metadata.get("name"), metadata.get("version")))

# for dirName, subdirList, fileList in os.walk(berks_package_folder):
#     print('Found directory: %s' % dirName)
#     for fname in fileList:
#         print('\t%s' % fname)
#         if "metadata."