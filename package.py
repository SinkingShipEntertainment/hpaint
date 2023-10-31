name = "hpaint"

version = "2.0.0.sse.1.0.0"

authors = [
    "Aaron Smith",
]

description = """Viewport drawing tool for Houdini."""

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
    "houdini",
]

private_build_requires = [
]

variants = [
]

build_command = "rez python {root}/rez_build.py"
uuid = "repository.hpaint"


def commands():
    env.REZ_HPAINT_ROOT = "{root}"
    env.PYTHONPATH.append("{root}/hda_py")

    # This will append the path to the otl/hdas in this package
    # to the variable that houdini will be looking for
    env.HOUDINI_OTLSCAN_PATH.append("{root}/otls;&")


def post_commands():
    pass
