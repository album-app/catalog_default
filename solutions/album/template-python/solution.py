from album.runner.api import setup

# Please import additional modules at the beginning of your method declarations.
# More information: https://docs.album.solutions/en/latest/solution-development/

env_file = """channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
"""


def run():
    from album.runner.api import get_args
    args = get_args()
    print("Hi", str(args.name), "nice to meet you!")


setup(
    group="album",
    name="template-python",
    version="0.1.0",
    title="Python template",
    description="An Album solution template for running Python code.",
    authors=["Album team"],
    cite=[],
    tags=["template", "python"],
    license="unlicense",
    documentation=["documentation.md"],
    covers=[{
        "description": "Dummy cover image.",
        "source": "cover.png"
    }],
    album_api_version="0.3.1",
    args=[{
        "name": "name",
        "type": "string",
        "default": "Bugs Bunny",
        "description": "How to you want to be addressed?"
    }],
    run=run,
    dependencies={'environment_file': env_file}
)
