#!/usr/bin/env python3
"""Build the ChatGPT plugin ZIP from the shared package.

ChatGPT discovers every folder under skills/ and its manifest cannot exclude
one, so the ChatGPT package is built without the billing-handoff skill:
OpenAI's commerce rules don't allow a link to pay a service bill. The router
skill's billing row is dropped for the same reason. Claude keeps both.

Skills and the logo live in the Claude plugin folder
(plugins/answering-service-care/) and keep their skills/ and assets/ paths in
the ZIP.

Usage: python3 scripts/build_chatgpt_package.py [output.zip]
"""
import pathlib
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "dist" / "answering-service-care-chatgpt.zip"
EXCLUDED_SKILLS = {"billing-handoff"}
ROUTER_SKILL = "skills/answering-service-care/SKILL.md"
# The portable manifest, its MCP config and the license; skills and any
# listing assets (assets/) are added below.
TOP_LEVEL = ["plugin.json", "mcp.json", "LICENSE"]
PLUGIN_DIR = ROOT / "plugins" / "answering-service-care"


def package_files():
    """(source path, name in the ZIP) pairs."""
    files = [(ROOT / name, name) for name in TOP_LEVEL]
    for path in sorted((PLUGIN_DIR / "skills").rglob("*")):
        if path.is_file() and path.relative_to(PLUGIN_DIR / "skills").parts[0] not in EXCLUDED_SKILLS:
            files.append((path, path.relative_to(PLUGIN_DIR).as_posix()))
    assets = PLUGIN_DIR / "assets"
    if assets.is_dir():
        files.extend((p, p.relative_to(PLUGIN_DIR).as_posix()) for p in sorted(assets.rglob("*")) if p.is_file())
    return files


def contents(path, name):
    data = path.read_bytes()
    if name == ROUTER_SKILL:
        lines = data.decode("utf-8").splitlines(keepends=True)
        data = "".join(l for l in lines if "billing-handoff" not in l).encode("utf-8")
    return data


def build(out=DEFAULT_OUT):
    out = pathlib.Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path, name in package_files():
            data = contents(path, name)
            if name.endswith((".md", ".json")):
                assert b"billing-handoff" not in data, f"{name} still refers to billing-handoff"
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, data)
    return out


if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUT))
