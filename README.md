## Akagi Text Formatter

just a simple text formating utility for my projects :^)

### Example Usage:
```
from atf import Formatter

title = 'Hello world'
description = 'Sample Description'
points = 'one two three four five'

final = Formatter(title=title, description=description, bulletpoints=points.split(' ')).save(markdown=True)


# OUTPUT:
**--Hello world--**   
__Sample Description__

• one
• two
• three
• four
• five
```
_Note_: All parameters are Optional