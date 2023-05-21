The Python `htmlcreator` Library
================================

[↩ Home](../README.md)

# 💻 API

##### Check the code for more information.

## `class Page`

```python
def __init__(self, title: str, body_content: list, style: dict[str, dict[str, str]]) -> None:
```

Defines a page to group all the things needed to build your website. When created, it automaticly adds `margin: 0;` and `padding: 0;` in the style.

Parameters:
- `title: str` The title of the page. e.g: `<title> title... </title>`.

- `body_content: list` The page content in `<body></body>`.

- `style: dict[str, dict[str, str]]` The style of the page

```python
def add_css_element(self, selector: str, property_: str, value: str) -> None:
```

Adds a value to the style of the page. Same as `Page.style[selector][property_] = value` (this only works if the selector has already been created, so the function will create it if it has not).

Parameters:
- `selector: str` The selector. e.g: `*`, `div`, `.main_title`...

- `property_: str` The property. e.g: `font-family`, `margin`, `font-size`...

- `value: str` The value. e.g: `"Tahoma"`, `none`, `50`...

```python
def set_main_font_family(self, font_family: str) -> None:
```

Set the main font of the page. Same as `add_css_element(selector="*", property_="font-family", value=font_family)`.

Parameters:
- `font_family: str` The font to set as the main font.

## `class Tag`

```python
def __init__(self, attributes: dict, style: dict, content: tuple, id_: typing.Optional[str] = "")
```

