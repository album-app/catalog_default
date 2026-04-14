from album.runner.api import setup

# Please import additional modules at the beginning of your method declarations.
# More information: https://docs.album.solutions/en/latest/solution-development/

env_file = """channels:
  - conda-forge
dependencies:
  - python=3.12
  - gradle=8.11.1
  - openjdk=11.0.30
"""


def install():
    import subprocess
    import shutil
    from album.runner.api import get_app_path, get_package_path

    get_app_path().mkdir(exist_ok=True, parents=True)

    shutil.copy(get_package_path().joinpath('build.gradle'), get_app_path())
    shutil.copytree(get_package_path().joinpath('src'), get_app_path().joinpath('src'))

    # compile app
    subprocess.run([shutil.which('gradle'), 'build', '-Dorg.gradle.internal.http.socketTimeout=300000'], cwd=get_app_path())


def run():
    import shutil
    import subprocess
    from album.runner.api import get_app_path, get_args

    subprocess.run([shutil.which('gradle'), 'run', '-q', '--args="%s"' % get_args().name], cwd=get_app_path())


setup(
    group="album",
    name="template-gradle-java11",
    version="0.1.1",
    title="Gradle template for Java 11",
    description="An Album solution template running Java code via Gradle.",
    solution_creators=["Album team"],
    tags=["template", "java", "gradle"],
    documentation=["documentation.md"],
    covers=[{
        "description": "Dummy cover image.",
        "source": "cover.png"
    }],
    license="unlicense",
    album_api_version="0.7.1",
    doi="10.5281/zenodo.6580977",
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
