"""Guard the YAML frontmatter block in the documentation templates.

Each page template opens with a frontmatter block that mkdocs reads for search
ranking:

    ---
    search:
      boost: 1.0
    ---

If the construct immediately after the closing ``---`` strips whitespace to its
left (a Jinja tag opening with ``{%-``), the closing fence collapses onto the
following line and mkdocs stops recognizing the block. It then renders as body
text, so every affected page opens with ``search: boost: 1.0 ---# Subset: ...``
and its search boost is silently inoperative.

That is what happened in
https://github.com/microbiomedata/nmdc-schema/issues/3344, across 153 enum and
subset pages plus 25 type pages. The class and slot templates were correct only
by accident: the construct after their fence happened to emit a newline.

These tests are string checks on the templates rather than a docs build, so they
run in milliseconds and need no generated artifact.
"""

import re
import unittest
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent.parent / "src" / "doc-templates"

# A closing fence followed by any amount of blank space and then a
# whitespace-stripping Jinja tag. The strip eats the newline after the fence.
COLLAPSING_FENCE = re.compile(r"^---\n\s*\{%-", re.MULTILINE)


def _templates_with_frontmatter():
    for path in sorted(TEMPLATE_DIR.glob("*.md.jinja2")):
        text = path.read_text()
        if text.startswith("---\n"):
            yield path, text


class TestDocTemplateFrontmatter(unittest.TestCase):
    def test_templates_with_frontmatter_are_found(self):
        """Fail loudly if the templates move, rather than passing vacuously."""
        self.assertTrue(
            list(_templates_with_frontmatter()),
            f"no templates with frontmatter found in {TEMPLATE_DIR}",
        )

    def test_closing_fence_is_not_followed_by_a_stripping_tag(self):
        for path, text in _templates_with_frontmatter():
            with self.subTest(template=path.name):
                self.assertIsNone(
                    COLLAPSING_FENCE.search(text),
                    f"{path.name}: the closing '---' is followed by a "
                    f"whitespace-stripping Jinja tag ('{{%-'), which collapses "
                    f"the fence onto the next line and breaks the frontmatter. "
                    f"Use '{{%' there instead.",
                )

    def test_frontmatter_block_closes_on_its_own_line(self):
        for path, text in _templates_with_frontmatter():
            with self.subTest(template=path.name):
                lines = text.split("\n")
                closing = next(
                    (i for i, line in enumerate(lines[1:], start=1) if line == "---"),
                    None,
                )
                self.assertIsNotNone(
                    closing, f"{path.name}: frontmatter block is never closed"
                )
                self.assertNotEqual(
                    lines[closing + 1].strip()[:1],
                    "#",
                    f"{path.name}: a heading sits directly after the closing "
                    f"fence with no blank line between them",
                )


if __name__ == "__main__":
    unittest.main()
