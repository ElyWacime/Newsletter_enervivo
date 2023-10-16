import webbrowser
from utils import *

newsletter_number = input("what is the number of the newsletter that you wanna create?: ")

title0 = create_title(0)
description0 = create_description(0)
image = create_image(0)

message = f'''
<html>
<head></head>
<body>
<img src="{image}" />
<h1> {title0} </h1>
<p>{description0}</p>
</body>
</html>
'''

with open(f"newsletter{newsletter_number}.html", "w") as f:
    f.write(message)