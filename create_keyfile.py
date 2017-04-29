import os
import sys

keyfile_data = os.environ.get('GOOG_KEYFILE', None)
if keyfile_data is None:
    print('GOOG_KEYFILE is not defined')
    sys.exit(1)

with open('keyfile', 'w') as f:
    f.write(keyfile_data)
    f.close()

print('Keyfile data written')
