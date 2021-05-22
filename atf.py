__version__ = '0.0.1'


class Formatter:
    def __init__(
        self,
        title: str=None,
        description: str=None,
        bulletpoints: list=None,
    ):
        """
        [ATF Formatter]

        Args:
            title (str, optional): [Title]. Defaults to None.
            description (str, optional): [Description]. Defaults to None.
            bulletpoints (list, optional): [Bullet Points]. Defaults to None.
        """
        self.title = title
        self.description = description
        self.bulletpoints = bulletpoints
        self.form = '{}{}{}'
    
    def save(self, markdown:bool=True):
        if self.bulletpoints:
            self.bulletpoints.insert(0,'')
        if markdown:
            return (self.form.format(
                "**--" + self.title + "--**" if self.title else "",
                "\n" + "__" + self.description + "__"  if self.description else "",
                "\n" + "\n• ".join(self.bulletpoints) if self.bulletpoints else ""
            ))
        else:
            return self.form.format(
                "<b><u>" + self.title + "</u></b>" if self.title else "",
                "\n" + "<i>" + self.description + "</i>"  if self.description else "",
                "\n" + "\n• ".join(self.bulletpoints) if self.bulletpoints else ""
                )
