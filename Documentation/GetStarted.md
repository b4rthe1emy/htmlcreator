The Python `htmlcreator` Library
================================

[↩ Home](../README.md)

# 🎓 Get Started

## Basics

- Import the required modules.

    ```python
    import htmlcreator
    from htmlcreator.page_elements import *
    ```

- Create a page to group all the things you need in one class.

    ```python
    my_page = Page(
        title="Hello, World",   # The title of your page
        body_content=[],        # The elements of your page
        style={},               # The stylesheet of your page
    )
    ```

1. `title: str`: This is the title of your page. e.g: `<title>Hello, World!</title>`.

2. `body_content: list[Tag]`: It takes a `list` of `Tag` as its input.

    ```python
    body_content=[
        Div(...),   # -> represents <div>...</div>
        A(...),     # -> represents <a>...</a>
        ...
    ]
    ```
    Here, the classes `Div` and `A` are childrens of the class `Tag`.

3. `style: dict[str, dict[str, str]]`: Defines the overall style of your page. Use the following pattern:

    ```python
    style={
        "selector": {
            "property": "value",
            ...
        },
        ...
    }
    ```
- Use the `generate_html(page: Page)` function to get the result of your HTML page. 

1. `page: Page`: Use this parameter to pass the page to generate the content of.

## Create Elements

- `Tag` takes 4 parameters whitch one of them is optional.

    ```python
    Div(
        attributes: dict,
        style:      dict,
        content:    tuple,
        id_:        Optional[str]
    )
    ```

1. `attributes: dict`: It is placed in the tag like this: `<element attribute1="value" attribute2="value"...>`

2. `style: dict`: It differs from the style in the _page_, because here it only applies to that element. e.g: `style={selector: property}`

3. `content: list`: It represents the elements contained in this element. i.e: `<element> content... </element>`

4. `id_: str`: It is used to identify the element. e.g: `<element id="...">...</element>`

    If no value is given to `id_`, a random one is generated using the following method:

    - Start with the string `"id"`
    - Generate a random number between `100_000` and `999_999`
    - If the number has already been created, repeat the process until you find one that has not already been created
    - Add that number to the end of the string

    Here is the code for doing this:

    ```python
    import random

    random_number = str(random.randint(100_000, 999_999))

    while random_number in generated_random_numbers:
        random_number = str(random.randint(100_000, 999_999))

    id_ = "id" + random_number
    generated_random_numbers.add(random_number)
    ```

    Example result: `"id985624"`
