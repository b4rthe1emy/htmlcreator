# `htmlcreator`: a quick way to create HTML using Python
# How to use it

_First, you must have a working knowledge of Python and HTML._

---

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

1. `title: `_`str`_: This is the title of your page. e.g: `<title>`_`Hello, World!`_`</title>`.

2. `body_content: `_`list[Tag]`_: It takes a `list` of `Tag` as its input.

    ```python
    body_content=[
        Div(...),   # -> represents <div>...</div>
        A(...),     # -> represents <a>...</a>
        ...
    ]
    ```
    Here, the classes `Div` and `A` are childrens of the class `Tag`.

3. `style: `_`dict[str, dict[str, str]]`_: Defines the overall style of your page. Use the following pattern:

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

1. `page: `_`Page`_: Use this parameter to pass the page to generate the content of.

---

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

1. `attributes: `_`dict`_: It is placed in the tag like this: `<element `_`attribute1="value" attribute2="value"...`_`>`

2. `style: `_`dict`_: It differs from the style in the _page_, because here it only applies to that element.

3. `content: `_`list`_: It represents the elements contained in this element. i.e: `<element> `_`content...`_` </element>`

4. `id_: `_`str`_: It is used to identify the element. e.g: `<element `_`id="..."`_`>...</element>`

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


