from album.runner.api import setup

# Please import additional modules at the beginning of your method declarations.
# More information: https://docs.album.solutions/en/latest/solution-development/

env_file = """channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.8
  - scyjava=1.4.1
  - openjdk=11.0.9.1
"""


def run():
    from album.runner.api import get_args
    from scyjava import config, jimport

    print("Hi " + str(get_args().name) + ", nice to meet you!")

    config.add_option('-Xmx6g')

    Runtime = jimport('java.lang.Runtime')
    print("Max. heap size: %sGB" % (Runtime.getRuntime().maxMemory() / 2 ** 30))

    System = jimport('java.lang.System')
    print("Java version: %s" % System.getProperty('java.version'))


setup(
    group="album",
    name="template-scyjava",
    version="0.1.0",
    title="ScyJava template",
    description="An Album solution template for running Java code via scyjava.",
    authors=["Album team"],
    tags=["template", "java", "scyjava"],
    license="unlicense",
    documentation=["documentation.md"],
    covers=[{
        "description": "Dummy cover image.",
        "source": "cover.png"
    }],
    cite=[{
        "text": "scyjava - supercharged Java access from Python",
        "url": "https://pypi.org/project/scyjava"
    }],
    album_api_version="0.3.1",
    args=[{
        "name": "name",
        "type": "string",
        "default": "Bugs Bunny",
        "description": "How do you want to be addressed?"
    }],
    run=run,
    dependencies={'environment_file': env_file}
)
