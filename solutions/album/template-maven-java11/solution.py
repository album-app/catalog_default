from album.runner.api import setup

# Please import additional modules at the beginning of your method declarations.
# More information: https://docs.album.solutions/en/latest/solution-development/

env_file = """channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - maven=3.8.1
  - openjdk=11.0.9.1
  - yattag=1.13.2
"""


def install():
    import subprocess
    import shutil
    from album.runner.api import get_app_path, get_package_path

    get_app_path().mkdir(exist_ok=True, parents=True)

    shutil.copy(get_package_path().joinpath('pom.xml'), get_app_path())
    shutil.copytree(get_package_path().joinpath('src'), get_app_path().joinpath('src'))

    # compile app
    subprocess.run([shutil.which('mvn'), 'compile', '-B'], cwd=get_app_path())


def run():
    import shutil
    import subprocess
    from album.runner.api import get_app_path, get_args

    subprocess.run('%s exec:java -q -Dexec.mainClass="Main" -Dexec.args="\'%s\'"' % (shutil.which('mvn'), get_args().name),
                   shell=True, cwd=get_app_path())


setup(
    group="album",
    name="template-maven-java11",
    version="0.1.0",
    title="Maven template for Java 11",
    description="An Album solution template running Java code via Maven, providing the POM and source file separately.",
    authors=["Album team"],
    tags=["template", "java", "maven"],
    documentation=["documentation.md"],
    covers=[{
        "description": "Dummy cover image.",
        "source": "cover.png"
    }],
    license="unlicense",
    album_api_version="0.3.1",
    args=[{
        "name": "name",
        "type": "string",
        "default": "Bugs Bunny",
        "description": "How do you want to be addressed?"
    }],
    install=install,
    run=run,
    dependencies={'environment_file': env_file}
)
