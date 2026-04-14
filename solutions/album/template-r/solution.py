from album.runner.api import setup

# Please import additional modules at the beginning of your method declarations.
# More information: https://docs.album.solutions/en/latest/solution-development/

env_file = """channels:
  - conda-forge
dependencies:
  - python=3.12
  - R
"""


script_file = """
args = commandArgs(trailingOnly=TRUE)
print(paste("Hi ", args[1], ", how are you?"))
print(sample(c(2,5,3), size=3, replace=FALSE))
"""


def run():
    import os
    import subprocess
    import tempfile
    from album.runner.api import get_args

    # write R script
    with tempfile.NamedTemporaryFile(suffix=".r", delete=False) as tmp:
        tmp.write(str.encode(script_file))

    # run R script
    subprocess.run(['Rscript', tmp.name, get_args().name])
    os.remove(tmp.name)


setup(
    group="album",
    name="template-r",
    version="0.1.1",
    title="R template",
    description="An Album solution template for running R code.",
    solution_creators=["Album team"],
    cite=[{
        "text": "R core team. R: A Language and Environment for Statistical Computing. R Foundation for Statistical Computing",
        "url": "https://www.R-project.org/"
    }],
    tags=["template", "R"],
    license="unlicense",
    documentation=["documentation.md"],
    covers=[{
        "description": "Dummy cover image.",
        "source": "cover.png"
    }],
    album_api_version="0.7.1",
    doi="10.5281/zenodo.6411064",
    args=[{
        "name": "name",
        "type": "string",
        "default": "Bugs Bunny",
        "description": "How to you want to be addressed?"
    }],
    run=run,
    dependencies={'environment_file': env_file}
)
