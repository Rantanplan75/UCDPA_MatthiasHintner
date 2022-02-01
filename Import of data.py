# Import package
from urllib.request import urlretrieve

# Assign url of file: url
url = 'https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results/download'

# Save file locally
urlretrieve(url, 'archive.zip')
