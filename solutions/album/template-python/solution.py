from album.runner.api import setup

# Please import additional modules at the beginning of your method declarations.
# More information: https://docs.album.solutions/en/latest/solution-development/

env_file = """channels:
  - conda-forge
dependencies:
  - python=3.14
"""


def run():
    from album.runner.api import get_args
    args = get_args()
    print("Hi", str(args.name), "nice to meet you!")


setup(
    group="album",
    name="template-python",
    version="0.1.1",
    title="Python template",
    description="An Album solution template for running Python code.",
    solution_creators=["Album team"],
    cite=[],
    tags=["template", "python"],
    license="unlicense",
    documentation=["documentation.md"],
    covers=[{
        "description": "Dummy cover image.",
        "source": "cover.png"
    }],
    album_api_version="0.7.1",
    doi="10.5281/zenodo.6410028",
    args=[{
        "name": "name",
        "type": "string",
        "default": "Bugs Bunny",
        "description": "How to you want to be addressed?"
    }],
    run=run,
    dependencies={'environment_file': env_file}
)
