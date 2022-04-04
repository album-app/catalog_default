from album.runner.api import setup

# Please import additional modules at the beginning of your method declarations.
# More information: https://docs.album.solutions/en/latest/solution-development/

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
    from pathlib import Path
    from album.runner.api import get_app_path, get_args

    input_path = Path(get_args().input_image_path).absolute()
    subprocess.run('%s exec:java -q -Dexec.mainClass="Main" -Dexec.args="\'%s\'"' %
                   (shutil.which('mvn'), input_path), shell=True, cwd=get_app_path())


setup(
    group="album",
    name="template-icy",
    version="0.1.0",
    album_api_version="0.3.1",
    title="Icy template",
    description="An Album solution template for running Icy.",
    authors=["Album team"],
    cite=[{
        "text": "de Chaumont, F. et al. (2012). Icy: an open bioimage informatics platform for extended reproducible research, Nature Methods, 9, pp. 690-696",
        "doi": "10.1038/nmeth.2075",
        "url": "https://icy.bioimageanalysis.org"
    }],
    tags=["template", "icy"],
    license="unlicense",
    covers=[{
        "description": "Dummy cover image.",
        "source": "cover.png"
    }],
    documentation=["documentation.md"],
    args=[{
        "name": "input_image_path",
        "type": "file",
        "description": "The image about to be displayed in Icy.",
        "required": True
    }],
    install=install,
    run=run,
    dependencies={
        'parent': {
            'resolve_solution': 'album:template-maven-java11:0.1.0'
        }
    }
)
