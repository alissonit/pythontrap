# import OS Module
import os

#set environment variable
os.environ['LESSON'] = "17"

# get environment variable
get_env = os.environ['LESSON']

#iterate and print variables
my_envs = os.environ.items()

for env in my_envs:
    print(env)