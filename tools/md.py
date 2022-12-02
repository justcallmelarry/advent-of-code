from typing import Any

import httpx
import utils
from bs4 import BeautifulSoup


def get_url(year: int, day: int) -> str:
    return f"https://adventofcode.com/{year}/day/{day}"


def get_response(url: str) -> httpx.Response:
    response = httpx.get(url, cookies={"session": utils.get_token()})

    if response.status_code != 200:
        raise ValueError(
            f"Querying the url {url} resulted in status code {response.status_code} with the following "
            f"text: {response.text}"
        )

    return response


def get_html(year: int, day: int) -> str:
    return get_response(get_url(year, day)).text


def get_input(year: int, day: int) -> str:
    return get_response(get_url(year, day) + "/input").text


# Simplification of https://github.com/dlon/html2markdown/blob/master/html2markdown.py
def html_tags_to_markdown(tag: Any, is_first_article: bool) -> None:
    children = tag.find_all(recursive=False)
    if tag.name != "code":
        for child in children:
            html_tags_to_markdown(child, is_first_article)

    if tag.name == "h2":
        style = "##"
        tag.insert_before(f"{style} ")
        tag.insert_after("\n\n")
        tag.unwrap()

    elif tag.name == "p":
        tag.insert_after("\n")
        tag.unwrap()

    elif tag.name == "em":
        style = "**" if tag.has_attr("class") and tag["class"] == "star" else "*"
        tag.insert_before(style)
        tag.insert_after(style)
        tag.unwrap()

    elif tag.name == "a":
        tag.insert_before("[")
        tag.insert_after(f']({tag["href"]})')
        tag.unwrap()

    elif tag.name == "span":
        tag.insert_before("*")
        tag.insert_after("*")
        tag.unwrap()

    elif tag.name == "ul":
        tag.unwrap()

    elif tag.name == "li":
        tag.insert_before(" - ")
        tag.insert_after("\n")
        tag.unwrap()

    elif tag.name == "code":
        if "\n" in tag.text:
            tag.insert_before("```\n")
            tag.insert_after("```")
        else:
            tag.insert_before("`")
            tag.insert_after("`")
        tag.unwrap()

    elif tag.name == "pre":
        tag.insert_before("")
        tag.insert_after("\n")
        tag.unwrap()

    elif tag.name == "article":
        pass

    else:
        raise ValueError(f"Missing condition for tag: {tag.name}")


def get_markdown(year: int, day: int) -> str:
    soup = BeautifulSoup(get_html(year, day), features="html.parser")

    url = get_url(year, day)
    content = f"# {year}-{str(day).zfill(2)}\nLink: {url}\n\n"

    articles = soup.body.main.findAll("article", recursive=False)
    puzzle_answers = soup.body.main.findAll(lambda tag: tag.name == "p" and "Your puzzle answer was" in tag.text)

    for i, article in enumerate(articles):
        html_tags_to_markdown(article, i == 0)
        content += "".join([tag.string for tag in article.contents])
        if len(puzzle_answers) >= i + 1:
            answer = (
                str(puzzle_answers[i])
                .replace("<p>", "")
                .replace("</p>", "")
                .replace("<code>", "`")
                .replace("</code>", "`")
            )
            content += f"{answer}\n"
            if i == 0:
                content += "\n"

    return content
