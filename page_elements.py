from dataclasses import dataclass

CSS_GENERIC_FONTS = ["monospace", "serif", "sans-serif", "cursive", "fantasy"]

class IDNotSpecified:
    pass

class Page:

    def add_css_element(self, selector: str, property: str, value: str):
        if self.style.get(selector) == None:
            self.style[selector] = {}
        self.style[selector][property] = value

    def __init__(self, title: str, body_content: list, style: dict[str, dict[str, str]]):
        self.title: str = title
        self.body_content: list = body_content
        self.style: dict[str, dict[str, str]] = style

        self.add_css_element("*", "margin", "0")
        self.add_css_element("*", "padding", "0")

    def set_main_font_family(self, _font_family: str):

        if _font_family.split(" ")[0] in CSS_GENERIC_FONTS:
            font_family = _font_family.split(" ")[0]
        else:
            font_family = '"' + _font_family.split(" ")[0] + '"'

        self.add_css_element("*", "font-family", font_family)


@dataclass
class Tag:
    attributes: dict
    style: dict
    content: tuple
    id_: str = IDNotSpecified()

    def check_valid(self) -> None | TypeError:
        if not self.content:
            return

        main_type = type(self.content[0])

        for i in range(len(self.content)):

            type_i = type(self.content[i])
            if not i == 0:
                condition = (isinstance(self.content[i], str) and isinstance(self.content[0], Tag)) or (
                    isinstance(self.content[i], Tag) and isinstance(self.content[0], str))

                if condition:
                    raise \
                        TypeError("All elements of a Tag must be of the same type (not "
                                  + main_type.__name__ + " and " + type_i.__name__ + ")")

            if not type_i in [Tag, str]:

                for base in type_i.__bases__:

                    if not base in [BaseTag, Tag, str]:

                        raise \
                            TypeError("Elements of a Tag must be str or Tag, not "
                                      + type_i.__name__)
                    



class BaseTag:
    pass


@dataclass
class Div(Tag, BaseTag):
    pass


@dataclass
class P(Tag, BaseTag):
    pass


@dataclass
class Ul(Tag, BaseTag):
    pass


@dataclass
class Li(Tag, BaseTag):
    pass


@dataclass
class A(Tag, BaseTag):
    pass
