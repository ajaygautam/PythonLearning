import os

import yaml

path1 = "/Users/agautam/work/svn/HS_Config/Uat/parent_client_config"
path2 = "/Users/agautam/work/svn/HS_Config/Uat/client_config/UT68UAT"
yaml_file = "redis.yaml"

with open(os.path.join(path1, yaml_file), 'r') as config_file:
    yaml_data1 = yaml.load(config_file)

with open(os.path.join(path2, yaml_file), 'r') as config_file:
    yaml_data2 = yaml.load(config_file)

# yaml_data1.update(yaml_data2)

print("YAML DATA:")
print(yaml_data1)
