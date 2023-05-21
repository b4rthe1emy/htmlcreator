from dataclasses import dataclass
import typing

CSS_GENERIC_FONTS = ["monospace", "serif", "sans-serif", "cursive", "fantasy"]

class Page:

    def add_css_element(self, selector: str, property_: str, value: str) -> None:
        if self.style.get(selector) == None:
            self.style[selector] = {}
        self.style[selector][property_] = value

    def __init__(self, title: str, body_content: list, style: dict[str, dict[str, str]]) -> None:
        self.title: str = title
        self.body_content: list = body_content
        self.style: dict[str, dict[str, str]] = style

        self.add_css_element("*", "margin", "0")
        self.add_css_element("*", "padding", "0")

    def set_main_font_family(self, font_family: str) -> None:

        if font_family.split(" ")[0] in CSS_GENERIC_FONTS:
            _font_family = font_family.split(" ")[0]
        else:
            _font_family = '"' + font_family.split(" ")[0] + '"'

        self.add_css_element("*", "font-family", _font_family)


@dataclass
class Tag:
    attributes: dict
    style: dict
    content: tuple
    id_: typing.Optional[str] = ""

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
