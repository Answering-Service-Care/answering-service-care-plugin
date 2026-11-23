#!/usr/bin/env python3
"""Offline checks. Not a substitute for schema, OAuth or live integration tests."""
import json
import pathlib
import re
import struct
import sys
import tempfile
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
PLUGIN = "plugins/answering-service-care"
PLUGIN_DIR = ROOT / PLUGIN
# The Claude directory accepts only these files in a plugin from an organization that
# isn't Verified, and refuses a version where any file names an image it could run.
DIRECTORY_SUFFIXES = {".md", ".json", ".png"}
DIRECTORY_NAMES = {"LICENSE"}
EXPECTED_ENDPOINT = "https://mcp.answeringservicecare.com/api/v2/mcp"
EXPECTED_NAME = "answering-service-care"
EXPECTED_SKILLS = {
    "setup",
    "answering-service-care",
    "message-triage",
    "follow-ups",
    "oncall-changes",
    "contact-delivery",
    "billing-handoff",
    "message-delivery",
    "coverage-check",
    "account-and-access",
}


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def check():
    claude = read_json(f"{PLUGIN}/.claude-plugin/plugin.json")
    marketplace = read_json(".claude-plugin/marketplace.json")
    portable = read_json(f"{PLUGIN}/plugin.json")
    cmcp = read_json(f"{PLUGIN}/.mcp.json")
    pmcp = read_json(f"{PLUGIN}/mcp.json")
    assert claude["name"] == portable["name"] == EXPECTED_NAME
    assert claude["version"] == portable["version"]
    listed = marketplace["plugins"]
    assert [p["name"] for p in listed] == [EXPECTED_NAME], listed
    assert listed[0]["source"] == f"./{PLUGIN}"
    assert listed[0]["version"] == claude["version"]
    assert portable["$schema"].endswith("plugin.schema.json")
    assert pmcp["$schema"].endswith("mcp.schema.json")
    assert portable["repository"].endswith("/answering-service-care-plugin")
    assert portable["extensions"]["com.openai"]["onboardingSkill"] == "./skills/setup/SKILL.md"
    assert portable["extensions"]["com.openai"]["interface"]["capabilities"] == ["Read", "Write"]

    for cfg in (cmcp, pmcp):
        servers = cfg["mcpServers"]
        assert set(servers) == {EXPECTED_NAME}, servers
        assert servers[EXPECTED_NAME]["url"] == EXPECTED_ENDPOINT
    assert cmcp["mcpServers"][EXPECTED_NAME]["type"] == "http"
    assert pmcp["mcpServers"][EXPECTED_NAME]["type"] == "streamable-http"
    assert pmcp["mcpServers"][EXPECTED_NAME]["extensions"]["com.openai"]["auth"]["type"] == "oauth"
    assert "headers" not in pmcp["mcpServers"][EXPECTED_NAME], "Public submission rejects server headers"

    # ChatGPT listing limits, and no billing in the ChatGPT listing.
    listing = portable["extensions"]["com.openai"]["interface"]
    assert len(listing["displayName"]) <= 30
    assert len(listing["shortDescription"]) <= 30
    assert len(listing["longDescription"]) <= 4000
    assert len(listing["defaultPrompt"]) <= 3
    assert all(len(p) <= 128 for p in listing["defaultPrompt"])
    assert claude["privacyPolicyUrl"] == listing["privacyPolicyURL"]
    assert "logo" not in listing and "composerIcon" not in listing, "the ZIP build adds the logo fields"
    assert claude["repository"] == portable["repository"]
    assert claude["supportUrl"].startswith("https://")
    for key in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        assert listing[key].startswith("https://"), key
    listing_text = json.dumps([portable["description"], listing]).lower()
    for word in ("billing", "balance", "pay"):
        assert not re.search(r"\b" + word, listing_text), word

    skills_dir = PLUGIN_DIR / "skills"
    actual = {p.name for p in skills_dir.iterdir() if p.is_dir()}
    assert actual == EXPECTED_SKILLS, (actual, EXPECTED_SKILLS)
    for name in EXPECTED_SKILLS:
        data = (skills_dir / name / "SKILL.md").read_text(encoding="utf-8")
        assert data.startswith("---\n"), name
        frontmatter = data.split("---", 2)[1]
        assert re.search(r"(?m)^name:\s*" + re.escape(name) + r"\s*$", frontmatter), name
        assert re.search(r"(?m)^description:\s*\S", frontmatter), name
        assert len(frontmatter) < 1200, name

    assert not (ROOT / "claude").exists(), "No duplicate platform-specific skills"
    assert not (ROOT / "chatgpt").exists(), "No duplicate platform-specific skills"
    assert not (ROOT / "server.json").exists(), "Public research server is separate"
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    assert "Kauneonga LLC" in license_text
    assert "Answering Service Care" in license_text

    for path in ROOT.rglob("*"):
        if not path.is_file() or path.resolve() == pathlib.Path(__file__).resolve():
            continue
        if path.suffix in {".json", ".md", ".yml", ".py"}:
            data = path.read_text(encoding="utf-8")
            assert "BEGIN PRIVATE KEY" not in data
            assert "sk-proj-" not in data
            if path.suffix == ".json" and path.name in {".mcp.json", "mcp.json"}:
                assert "mcp.kauneonga.com" not in data
                assert "answeringservicecare.com/mcp" not in data
    check_chatgpt_package()
    check_review_metadata()
    check_directory_folder()
    print("PASS: manifests, single skill source, endpoint, OAuth, safety checks, ChatGPT package")


def check_review_metadata():
    """OpenAI's first MCP review needs exactly 5 positive and 3 negative test cases."""
    review = read_json(f"{PLUGIN}/plugin.json")["extensions"]["com.openai"]["review"]
    cases = review["test_cases"]
    assert len(cases["positive"]) == 5 and len(cases["negative"]) == 3, cases
    served = set(re.findall(r"`([a-z]+_[a-z_]+)`", (ROOT / "docs" / "TOOLS.md").read_text(encoding="utf-8")))
    for case in cases["positive"]:
        assert case["prompt"] and case["expected_behavior"] and len(case["description"]) <= 4000, case
        for tool in (t.strip() for t in case["tools_triggered"].split(",")):
            assert tool in served, f"{tool} is not a client connector tool"
    for case in cases["negative"]:
        assert case["prompt"] and case["description"], case
    text = json.dumps(cases).lower()
    for word in ("billing", "balance", "pay"):
        assert not re.search(r"\b" + word, text), word
    assert "test_credentials" not in review and "reviewer_instructions" not in review, "reviewer access goes in the dashboard"


def check_directory_folder():
    """The folder submitted to the Claude directory holds only files it accepts."""
    for path in sorted(p for p in PLUGIN_DIR.rglob("*") if p.is_file()):
        rel = path.relative_to(PLUGIN_DIR).as_posix()
        assert path.suffix in DIRECTORY_SUFFIXES or path.name in DIRECTORY_NAMES, rel
        assert path.name.lower() not in {"agents.md", "claude.md", "claude.local.md"}, rel
        if path.suffix != ".png":
            text = path.read_text(encoding="utf-8")
            assert not text.startswith("#!"), rel
            for image in PLUGIN_DIR.rglob("*.png"):
                assert image.name not in text, f"{rel} names {image.name}"
    assert (PLUGIN_DIR / "LICENSE").read_text(encoding="utf-8") == (ROOT / "LICENSE").read_text(encoding="utf-8")
    assert not (ROOT / ".claude-plugin" / "plugin.json").exists(), "Claude manifest lives in the plugin folder"
    assert not (ROOT / ".mcp.json").exists(), "Claude connector config lives in the plugin folder"
    for name in ("plugin.json", "mcp.json", "skills"):
        assert not (ROOT / name).exists(), f"{name} lives in the plugin folder, beside the skills"


def check_chatgpt_package():
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_chatgpt_package

    with tempfile.TemporaryDirectory() as tmp:
        out = build_chatgpt_package.build(pathlib.Path(tmp) / "chatgpt.zip")
        with zipfile.ZipFile(out) as zf:
            names = set(zf.namelist())
            skills = {n.split("/")[1] for n in names if n.startswith("skills/")}
            assert skills == EXPECTED_SKILLS - {"billing-handoff"}, skills
            assert {"plugin.json", "mcp.json", "LICENSE", "assets/logo.png"} <= names, names
            listing = json.loads(zf.read("plugin.json"))["extensions"]["com.openai"]["interface"]
            for key in ("logo", "composerIcon"):
                logo = zf.read(listing[key].lstrip("./"))
                width, height = struct.unpack(">II", logo[16:24])
                assert logo[:8] == b"\x89PNG\r\n\x1a\n" and width == height >= 48, (key, width, height)
            assert not any(n.startswith(".claude-plugin/") or n == ".mcp.json" for n in names), names
            router = zf.read("skills/answering-service-care/SKILL.md").decode("utf-8")
            assert "billing-handoff" not in router
            assert "message-triage" in router


if __name__ == "__main__":
    check()
