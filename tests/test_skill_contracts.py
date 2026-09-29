import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = {
    "magneticproxy",
    "magnetic-price-monitor",
    "magnetic-scraper-proxy-setup",
    "magnetic-geo-qa",
}
WORKFLOWS = EXPECTED - {"magneticproxy"}


class SkillContractTests(unittest.TestCase):
    def test_expected_skill_set(self):
        self.assertEqual({path.name for path in SKILLS.iterdir() if path.is_dir()}, EXPECTED)

    def test_frontmatter_name_matches_folder(self):
        for folder in SKILLS.iterdir():
            content = (folder / "SKILL.md").read_text(encoding="utf-8")
            match = re.search(r"(?m)^name:\s*([a-z0-9-]+)$", content)
            self.assertIsNotNone(match, folder.name)
            self.assertEqual(match.group(1), folder.name)

    def test_core_operates_browser_and_code_without_a_specialized_setup_skill(self):
        core = (SKILLS / "magneticproxy" / "SKILL.md").read_text(encoding="utf-8")
        for reference in ("browser-extension.md", "client-setup.md"):
            self.assertIn(reference, core)
            self.assertTrue((SKILLS / "magneticproxy" / "references" / reference).exists())
        self.assertNotIn("](../", core)

    def test_workflow_readmes_match_skill_titles(self):
        for name in WORKFLOWS:
            skill = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            readme = (SKILLS / name / "README.md").read_text(encoding="utf-8")
            skill_title = re.search(r"(?m)^# (.+)$", skill)
            readme_title = re.search(r"(?m)^# (.+)$", readme)
            self.assertIsNotNone(skill_title, name)
            self.assertIsNotNone(readme_title, name)
            self.assertEqual(skill_title.group(1), readme_title.group(1), name)

    def test_skill_instructions_are_model_neutral(self):
        for folder in SKILLS.iterdir():
            content = (folder / "SKILL.md").read_text(encoding="utf-8")
            self.assertNotIn("$magneticproxy", content.lower(), folder.name)
            self.assertNotRegex(content.lower(), r"\b(?:codex|openai|claude|glm|deepseek)\b")
        for name in WORKFLOWS:
            content = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("](https://github.com/MagneticProxy/magneticproxy-residential-proxy-agent-skills/tree/main/skills/magneticproxy)", content, name)

    def test_portability_contract_marks_adapter_optional(self):
        content = (ROOT / "COMPATIBILITY.md").read_text(encoding="utf-8").lower()
        self.assertIn("agents/openai.yaml", content)
        self.assertIn("optional", content)
        self.assertIn("ordinary python 3", content)

    def test_scraper_examples_cover_all_named_clients(self):
        references = SKILLS / "magnetic-scraper-proxy-setup" / "references"
        self.assertTrue((references / "python-requests.md").exists())
        self.assertTrue((references / "playwright.md").exists())
        self.assertTrue((references / "scrapy.md").exists())

    def test_relative_references_exist(self):
        for folder in SKILLS.iterdir():
            content = (folder / "SKILL.md").read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^)]+)\)", content):
                if "://" not in target:
                    self.assertTrue((folder / target).exists(), f"{folder.name}: {target}")

    def test_openai_metadata_invokes_matching_skill(self):
        for folder in SKILLS.iterdir():
            content = (folder / "agents" / "openai.yaml").read_text(encoding="utf-8")
            self.assertIn(f"${folder.name}", content)
            match = re.search(r'(?m)^  short_description: "([^"]+)"$', content)
            self.assertIsNotNone(match, folder.name)
            self.assertGreaterEqual(len(match.group(1)), 25)
            self.assertLessEqual(len(match.group(1)), 64)

    def test_no_unfinished_placeholders(self):
        unfinished = "|".join(("TO" + "DO", "T" + "BD", r"\[" + "TO" + "DO:"))
        for path in ROOT.rglob("*"):
            if "tests" in path.parts or not path.is_file():
                continue
            if path.suffix.lower() in {".md", ".yaml", ".py"}:
                self.assertNotRegex(path.read_text(encoding="utf-8"), unfinished)


if __name__ == "__main__":
    unittest.main()
