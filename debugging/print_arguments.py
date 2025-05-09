#!/usr/bin/python3
import sys

# Print only arguments (skip script name at index 0)
for arg in sys.argv[1:]:
    print(arg)

# Alternative version with error handling:
# if len(sys.argv) > 1:
#     for arg in sys.argv[1:]:
#         print(arg)
# else:
#     print("No arguments provided")
