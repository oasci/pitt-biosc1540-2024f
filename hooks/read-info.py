import re

import textstat


def is_jupyter(markdown=None, html=None):
    if html:
        return '<div class="jupyter-wrapper">' in html
    if markdown:
        return False
    raise ValueError("Must provide either markdown or html")


def get_clean_text(markdown):
    clean_text = re.sub(r"(!\[.*?\]\(.*?\)|\[.*?\]\[.*?\])", "", markdown)
    clean_text = re.sub(re.compile(r"[\[\]]", re.MULTILINE), "", markdown)
    clean_text = re.sub(r"`.*?`", "", clean_text)
    clean_text = re.sub(r"#{1,6}\s*.*?(\n|$)", "", clean_text)
    clean_text = re.sub(r"\[.*?\]\(.*?\)", "", clean_text)
    clean_text = re.sub(re.compile(r"^\s*!!!.*$", re.MULTILINE), "", clean_text)
    clean_text = re.sub(re.compile(r"^\s*<.*$", re.MULTILINE), "", clean_text)
    clean_text = re.sub(re.compile(r"^\s*-\s*", re.MULTILINE), "", clean_text)
    clean_text = re.sub(re.compile(r"\*", re.MULTILINE), "", clean_text)
    clean_text = re.sub(re.compile(r"https://\S+", re.MULTILINE), "", clean_text)
    clean_text = re.sub(re.compile(r"http://\S+", re.MULTILINE), "", clean_text)
    return clean_text


def on_page_markdown(markdown, **kwargs):
    """Add a reading info to the page."""
    clean_text = get_clean_text(markdown)
    if not is_jupyter(markdown):
        if not markdown.strip()[0] == "#":
            return markdown

        flesch_kincaid_grade = textstat.flesch_kincaid_grade(clean_text)
        automated_readability_index = textstat.automated_readability_index(clean_text)
        reading_time = textstat.reading_time(clean_text, ms_per_char=1.0)

        lines = markdown.split("\n")
        blank_line_index = next(
            (index for index, line in enumerate(lines) if line.strip() == ""), 2
        )
        lines.insert(
            blank_line_index, f"**Reading time:** {reading_time:.0f} minute(s)"
        )
        markdown = "\n".join(lines)

        if automated_readability_index > 0:
            markdown += '\n\n??? quote print-site-plugin-ignore "Readability"\n\n'
            markdown += (
                "    **Not accurate at the moment due to markdown formatting.**\n\n"
            )
            markdown += f"    [Flesch-Kincaid Grade Level](/resources/readability/flesch-kincaid/): {flesch_kincaid_grade}\n\n"
            markdown += f"    [Automated Readability Index](/resources/readability/automated-readability-index/): {automated_readability_index}\n"
    return markdown
