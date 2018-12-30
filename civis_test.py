# test of the civis python module

import civis
import os


#'CIVIS_API_KEY' in os.environ
# Civis API key is exported as an environment variable in ~/.zshenv
client = civis.APIClient()

me = client.users.list_me()

print(me)

