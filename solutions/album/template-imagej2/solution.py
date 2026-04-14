from album.runner.api import setup

# Please import additional modules at the beginning of your method declarations.
# More information: https://docs.album.solutions/en/latest/solution-development/

env_file = """channels:
  - conda-forge
dependencies:
  - python=3.12
  - pyimagej=1.8.0
  - openjdk=11.0.30
"""

def init_ij():
    import imagej
    import tempfile
    from scyjava import config

    # Silence log4j 1.x "no appenders" warnings from ImageJ2/SciJava
    log4j_props = tempfile.NamedTemporaryFile(
        mode="w", suffix=".properties", delete=False
    )
    log4j_props.write("log4j.rootLogger=ERROR, stderr\n")
    log4j_props.write("log4j.appender.stderr=org.apache.log4j.ConsoleAppender\n")
    log4j_props.write("log4j.appender.stderr.layout=org.apache.log4j.PatternLayout\n")
    log4j_props.close()
    config.add_option(f'-Dlog4j.configuration=file:{log4j_props.name}')

    # see this link for initialization options: https://github.com/imagej/pyimagej/blob/master/doc/Initialization.md
    return imagej.init('2.17.0')


def install():
    print("Downloading maven dependencies. This may take a while. "
          "By default, maven dependencies are shared between applications - "
          "installing another solution with similar dependencies should be fast.")
    init_ij()


def run():
    from album.runner.api import get_args
    from pathlib import Path
    from scyjava import jimport
    import os

    ij = init_ij()

    try:
        # create empty image
        img = ij.op().run("create.img", ij.py.to_java([100, 100, 100]))

        # write random values into image
        Random = jimport("java.util.Random")
        random = Random()
        for t in img:
            t.set(random.nextInt())

        # apply DoG filter
        img = ij.op().filter().dog(img, 5.0, 2.0)

        # delete output file if it exists already, create parent folder
        image_path = get_args().output_image_path
        if os.path.exists(image_path):
            os.remove(image_path)
        Path(os.path.abspath(image_path)).parent.mkdir(parents=True, exist_ok=True)

        # save image to output file
        ij.io().save(ij.dataset().create(img), str(image_path))

    finally:
        ij.dispose()


def prepare_test():
    from album.runner.api import get_cache_path
    return {
        "--output_image_path": str(get_cache_path().joinpath("output.tif"))
    }


def test():
    from album.runner.api import get_cache_path
    assert get_cache_path().joinpath("output.tif").exists()


setup(
    group="album",
    name="template-imagej2",
    version="0.1.1",
    title="ImageJ2 template",
    description="An Album solution template generating an ImgLib2 image with random values in ImageJ2.",
    solution_creators=["Album team"],
    cite=[{
        "text": "Rueden, C. T., Schindelin, J., Hiner, M. C., DeZonia, B. E., Walter, A. E., Arena, E. T., & Eliceiri, K. W. (2017). ImageJ2: ImageJ for the next generation of scientific image data. BMC Bioinformatics, 18(1).",
        "doi": "10.1186/s12859-017-1934-z",
        "url": "https://imagej.net"
    }],
    tags=["template", "java", "imagej2", "scijava", "scyjava"],
    license="unlicense",
    documentation=["documentation.md"],
    covers=[{
        "description": "Dummy cover image.",
        "source": "cover.png"
    }],
    album_api_version="0.7.1",
    doi="10.5281/zenodo.6411110",
    args=[{
        "name": "output_image_path",
        "type": "file",
        "description": "The output file name to where a random image is going to be saved.",
        "required": True
    }],
    install=install,
    run=run,
    pre_test=prepare_test,
    test=test,
    dependencies={'environment_file': env_file}
)
