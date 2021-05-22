from atf import Formatter

title = 'Hello world'
description = 'Sample Description'
points = 'one two three four five'

final = Formatter(title=title, description=description, bulletpoints=points.split(' ')).save(markdown=True)
print(final)