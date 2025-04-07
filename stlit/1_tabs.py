import sys
import os

print(sys.path)
sys.path.append(os.path.abspath(os.path.join('..')))
print(sys.path)
