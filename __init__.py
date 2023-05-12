from htmlcreator.page_elements import *
import random


tabulation = " " * 4


def _dict_to_html_tags(dict_) -> str:
    out = ''
    i = 0
    for key in dict_:
        value = dict_[key]
        out += key + '="' + value + '"'
        if i < len(dict_)-1:
            out += ' '
        i += 1

    return out


def _dict_to_css(dict_) -> str:
    out = ''
    for selector in dict_:
        out += "\n" + selector + " {\n"
        for property_ in dict_[selector]:
            value = dict_[selector][property_]
            out += tabulation + property_ + ": " + value + ";\n"
        out += "}\n"

    return out


generated_random_numbers: set = {0}
generated_random_numbers.remove(0)


def _loop_in_element(_container, page: Page, is_root=False, tabulation_number=0) -> str:
    out = ""
    if not is_root:
        container = _container.content
    else:
        container = _container

    i = 0
    for element in container:

        if isinstance(element, Tag):

            # has_class = element.attributes.get("class", None) is not None

            if element.id_ == "":
                random_number = str(random.randint(100_000, 999_999))
                while random_number in generated_random_numbers:
                    random_number = str(random.randint(100_000, 999_999))
                id_ = "id" + random_number
                generated_random_numbers.add(random_number)

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
                    # if has_class:
                    #     selector = "." + element.attributes["class"]
                    # else:
                    #     selector = "#" + id_
                    selector = "#" + id_
                    page.add_css_element(selector, property_, style[property_])

            out += tabulation * tabulation_number

            out += "<"
            out += html_name

            out += " "
            attributes_ = element.attributes
            attributes_["id"] = id_
            out += _dict_to_html_tags(attributes_)

            out += ">"

            if element.content:
                if isinstance(element.content[0], Tag):
                    out += "\n"

                out += _loop_in_element(_container=element,
                                        tabulation_number=tabulation_number + 1,
                                        page=page)

                if isinstance(element.content[0], Tag):
                    out += tabulation * tabulation_number

            out += f"</{html_name}>" + "\n"

        elif isinstance(element, str):
            out += element + (" " if not i == len(container) - 1 else "")

        i += 1

    return out


def generate_html(page) -> str:
    title: str = page.title
    _content: list = page.body_content

    content: list = _loop_in_element(_content, is_root=True, page=page)
    content = content.replace("\n", "\n" + tabulation)

    style: str = _dict_to_css(page.style)
    style = style.replace("\n", "\n" + tabulation * 2)
    style = style.removesuffix(tabulation)

    out: str = f"""\
<!DOCTYPE html>
<html lang="en">

<head>
{tabulation}<meta charset="UTF-8">
{tabulation}<title>{title}</title>
{tabulation}{"<style>" + style + "</style>" if style else ""}
</head>

<body>

{tabulation}{content}
</body>

</html>"""

    return out
