#!/usr/bin/env python3
"""Build the ChatGPT plugin ZIP from the shared package.

ChatGPT discovers every folder under skills/ and its manifest cannot exclude
one, so the ChatGPT package is built without the billing-handoff skill:
OpenAI's commerce rules don't allow a link to pay a service bill. The router
skill's billing row is dropped for the same reason. Claude keeps both.

plugins/answering-service-care/ is the package root for every app: the Claude
manifest and the portable Agent Plugins manifest (plugin.json, mcp.json) sit
beside one shared skills/ tree. The Claude directory refuses a plugin folder
where a file names an image, so the portable manifest in the repository has
no logo fields; they are added to the copy written into the ZIP.

To update the plugin already created in the OpenAI dashboard, pass its app id:
the dashboard requires plugin.json's name to be that id, and refuses an
mcp.json sign-in block because the app's connection is configured there.

Usage: python3 scripts/build_chatgpt_package.py [output.zip] [--openai-app-id app-...]
"""
import json
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
    files = [(PLUGIN_DIR / name, name) for name in TOP_LEVEL]
    for path in sorted((PLUGIN_DIR / "skills").rglob("*")):
        if path.is_file() and path.relative_to(PLUGIN_DIR / "skills").parts[0] not in EXCLUDED_SKILLS:
            files.append((path, path.relative_to(PLUGIN_DIR).as_posix()))
    assets = PLUGIN_DIR / "assets"
    if assets.is_dir():
        files.extend((p, p.relative_to(PLUGIN_DIR).as_posix()) for p in sorted(assets.rglob("*")) if p.is_file())
    return files


LOGO = "./assets/logo.png"


def contents(path, name, openai_app_id=None):
    data = path.read_bytes()
    if name == "mcp.json" and openai_app_id:
        config = json.loads(data.decode("utf-8"))
        for server in config["mcpServers"].values():
            openai = server.get("extensions", {}).get("com.openai", {})
            openai.pop("auth", None)
            if not openai:
                server.get("extensions", {}).pop("com.openai", None)
            if not server.get("extensions", True):
                server.pop("extensions")
        data = (json.dumps(config, indent=2) + "\n").encode("utf-8")
    if name == "plugin.json":
        manifest = json.loads(data.decode("utf-8"))
        interface = manifest["extensions"]["com.openai"]["interface"]
        interface["logo"] = LOGO
        interface["composerIcon"] = LOGO
        if openai_app_id:
            manifest["name"] = openai_app_id
        data = (json.dumps(manifest, indent=2) + "\n").encode("utf-8")
    if name == ROUTER_SKILL:
        lines = data.decode("utf-8").splitlines(keepends=True)
        data = "".join(l for l in lines if "billing-handoff" not in l).encode("utf-8")
    return data


def build(out=DEFAULT_OUT, openai_app_id=None):
    out = pathlib.Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path, name in package_files():
            data = contents(path, name, openai_app_id)
            if name.endswith((".md", ".json")):
                assert b"billing-handoff" not in data, f"{name} still refers to billing-handoff"
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, data)
    return out


if __name__ == "__main__":
    args = sys.argv[1:]
    app_id = None
    if "--openai-app-id" in args:
        i = args.index("--openai-app-id")
        app_id = args[i + 1]
        del args[i : i + 2]
    print(build(args[0] if args else DEFAULT_OUT, app_id))
