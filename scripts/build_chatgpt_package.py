#!/usr/bin/env python3
"""Build the ChatGPT plugin ZIP from the shared package.

ChatGPT discovers every folder under skills/ and its manifest cannot exclude
one, so the ChatGPT package is built without the billing-handoff skill:
OpenAI's commerce rules don't allow a link to pay a service bill. The router
skill's billing row is dropped for the same reason. Claude keeps both.

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


def package_files():
    files = [ROOT / name for name in TOP_LEVEL]
    for path in sorted((ROOT / "skills").rglob("*")):
        if path.is_file() and path.relative_to(ROOT / "skills").parts[0] not in EXCLUDED_SKILLS:
            files.append(path)
    assets = ROOT / "assets"
    if assets.is_dir():
        files.extend(sorted(p for p in assets.rglob("*") if p.is_file()))
    return files


def contents(path):
    data = path.read_bytes()
    if path.relative_to(ROOT).as_posix() == ROUTER_SKILL:
        lines = data.decode("utf-8").splitlines(keepends=True)
        data = "".join(l for l in lines if "billing-handoff" not in l).encode("utf-8")
    return data


def build(out=DEFAULT_OUT):
    out = pathlib.Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in package_files():
            data = contents(path)
            name = path.relative_to(ROOT).as_posix()
            if name.endswith((".md", ".json")):
                assert b"billing-handoff" not in data, f"{name} still refers to billing-handoff"
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, data)
    return out


if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUT))
