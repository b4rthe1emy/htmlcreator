from htmlcreator.page_elements import *
import random


MAXIMUM_NUMBER_OF_ELEMENTS_IN_PAGE = 999_999


def _dict_to_html_tags(dict_):
    out = ''
    i = 0
    for key in dict_:
        value = dict_[key]
        out += key + '="' + value + '"'
        if i < len(dict_)-1:
            out += ' '
        i += 1

    return out


def _dict_to_css(dict_):
    out = ''
    for selector in dict_:
        out += "\n" + selector + " {\n"
        for property in dict_[selector]:
            value = dict_[selector][property]
            out += "    " + property + ": " + value + ";\n"
        out += "}\n"

    return out


generated_random_numbers: set = {0}
generated_random_numbers.remove(0)


def _loop_in_element(_container, page: Page, is_root=False, tabulation=0) -> str:
    out = ""
    if not is_root:
        container = _container.content
    else:
        container = _container

    i = 0
    for element in container:

        if isinstance(element, Tag):

            has_class = element.attributes.get("class", None) is not None

            if isinstance(element.id_, IDNotSpecified) and not has_class:
                rand = str(random.randint(MAXIMUM_NUMBER_OF_ELEMENTS_IN_PAGE/9, MAXIMUM_NUMBER_OF_ELEMENTS_IN_PAGE))
                while rand in generated_random_numbers:
                    rand = str(random.randint(MAXIMUM_NUMBER_OF_ELEMENTS_IN_PAGE/9, MAXIMUM_NUMBER_OF_ELEMENTS_IN_PAGE))
                id_ = "id" + rand
                generated_random_numbers.add(rand)

            else:
                id_ = element.id_


            element.check_valid()
            if BaseTag in type(element).__bases__:
                html_name = type(element).__name__.lower()
            else:
                html_name = element.html_name

            style = element.style
            if len(style) > 0:
                for property_ in style:
                    if has_class:
                        selector = "." + element.attributes["class"]
                    else:
                        selector = "#" + id_
                    page.add_css_element(selector, property_, style[property_])

            out += "    " * tabulation

            out += "<"
            out += html_name
            out += " "
            # out += (" " if element.attributes else "")
            attributes_ = element.attributes
            if not has_class:
                attributes_["id"] = id_
            out += _dict_to_html_tags(attributes_)
            out += ">"

            if len(element.content) > 0 and isinstance(element.content[0], Tag):
                out += "\n"

            if element.content:

                out += _loop_in_element(_container=element,
                                        tabulation=tabulation + 1,
                                        page=page)

                if isinstance(element.content[0], Tag):
                    out += "    " * tabulation

            out += f"</{html_name}>" + "\n"

        elif isinstance(element, str):
            out += element + (" " if not i == len(container) - 1 else "")

        i += 1

    return out


def generate_html(out_file: str, page) -> None:
    title = page.title
    _content = page.body_content

    content = _loop_in_element(_content, is_root=True, page=page)
    content = content.replace("\n", "\n    ")

    style = _dict_to_css(page.style)
    style = style.replace("\n", "\n        ")
    style = style.removesuffix("    ")

    out = f"""\
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    {"<style>" if style else ""}{style}{"</style>" if style else ""}
</head>

<body>

    {content}
</body>

</html>"""

    open(out_file, mode="w").write(out)
