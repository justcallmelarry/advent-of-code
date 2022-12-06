"""
Things to help gather information (sample, description) from the AoC website.
"""
import os
from pathlib import Path
from typing import Any, Literal

import httpx
from bs4 import BeautifulSoup


def _get_token() -> str:
    token_path = Path(__file__).parent.parent / "token.txt"
    with open(token_path) as f:
        return f.read().strip()


def get_actual(day: int, year: int) -> str:
    """
    Loads the input for year/day and returns the value as a string.
    If the input is not saved, attempt to get it from AoC.
    """
    input_destination_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        str(year),
        f"{day}".zfill(2),
        "input.user",
    )
    try:
        with open(input_destination_path) as actual_input:
            return actual_input.read()
    except FileNotFoundError:
        pass

    # is it time?
    from datetime import datetime, timedelta, timezone

    est = timezone(timedelta(hours=-5))
    unlock_time = datetime(year, 12, day, tzinfo=est)
    cur_time = datetime.now(tz=est)
    delta = unlock_time - cur_time
    if delta.days >= 0:
        print(f"Remaining time until unlock: {delta}")
        return ""

    import httpx

    url = get_url(year, day) + "/input"
    response = httpx.get(url, cookies={"session": _get_token()})
    response.raise_for_status()
    with open(input_destination_path, "w") as input_file:
        input_file.write(response.text)

    print("Input saved!")
    return response.text


def get_url(year: int, day: int) -> str:
    return f"https://adventofcode.com/{year}/day/{day}"


def _get_response(url: str) -> httpx.Response:
    response = httpx.get(url, cookies={"session": _get_token()})

    if response.status_code != 200:
        raise ValueError(
            f"Querying the url {url} resulted in status code {response.status_code} with the following "
            f"text: {response.text}"
        )

    return response


def _get_html(year: int, day: int) -> str:
    return _get_response(get_url(year, day)).text


def _html_tags_to_markdown(tag: Any, is_first_article: bool) -> None:
    """
    Mostly stolen from https://github.com/antonio-ramadas/aoc-to-markdown
    """
    children = tag.find_all(recursive=False)
    if tag.name != "code":
        for child in children:
            _html_tags_to_markdown(child, is_first_article)

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
    soup = BeautifulSoup(_get_html(year, day), features="html.parser")

    url = get_url(year, day)
    content = f"# {year}-{str(day).zfill(2)}\nLink: {url}\n\n"

    articles = soup.body.main.findAll("article", recursive=False)
    puzzle_answers = soup.body.main.findAll(lambda tag: tag.name == "p" and "Your puzzle answer was" in tag.text)

    for i, article in enumerate(articles):
        _html_tags_to_markdown(article, i == 0)
        content += "".join([tag.string for tag in article.contents if tag.string])
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


def submit(year: int, day: int, part: Literal[1, 2], answer: str) -> bool:
    """
    Cache all answers for each puzzle, in order not to spam AoC with requests.
    """
    cache_path = Path(__file__).parent.parent / ".cache" / f"{year}-{str(day).zfill(2)}--{part}"
    if os.path.isfile(cache_path):
        with open(cache_path) as cache_file:
            cache = set(cache_file.read().splitlines())
    else:
        cache = set()

    if answer in cache:
        print("This answer was already tried. Aborting!")
        return False

    url = get_url(year, day)
    response = httpx.post(
        url=url + "/answer",
        cookies={"session": _get_token()},
        data={"level": part, "answer": answer},
    )
    if not 200 <= response.status_code <= 299:
        print("Got error response while trying to submit:")
        print(response.text)
        return False

    soup = BeautifulSoup(response.text, "html.parser")
    message = soup.article.text
    message = message.lower()

    with open(cache_path, "a") as cache_file:
        cache_file.write(f"{answer}\n")

    if "that's the right answer" in message:
        print("Correct! 🌟")
        return True

    elif "that's not the right answer" in message:
        if "too high" in message:
            print("Your answer is too high. ⬆️")

        elif "too low" in message:
            print("Your answer is too low. ⬇️")

        else:
            print("That's not the right answer. ❌")

    elif "did you already complete it" in message:
        print("It seems this puzzle has already been completed. 💡")

    elif "you gave an answer too recently" in message:
        print("You gave an incorrect answer too recently, please wait a bit before trying to submit again. ⏱️")

    return False
