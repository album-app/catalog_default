from io import StringIO

from album.runner.api import setup

# Please import additional modules at the beginning of your method declarations.
# More information: https://docs.album.solutions/en/latest/solution-development/

env_file = StringIO("""channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.8
  - pip=22.0.3
  - scikit-image=0.19.1
  - pip:
    - napari[all]==0.4.14
""")


def run():
    import napari
    from skimage.io import imread
    from album.runner.api import get_args

    img = imread(get_args().input_image_path)
    napari.view_image(img, rgb=False, name="Input image")
    napari.run()


setup(
    group="album",
    name="template-napari",
    version="0.1.0",
    title="Napari template",
    description="An Album solution template for running Napari.",
    authors=["Album team"],
    cite=[{
        "text": "napari contributors (2019). napari: a multi-dimensional image viewer for python.",
        "doi": "10.5281/zenodo.3555620",
        "url": "https://github.com/napari/napari"
    }],
    tags=["template", "napari"],
    license="unlicense",
    documentation=["documentation.md"],
    covers=[{
        "description": "Dummy cover image.",
        "source": "cover.png"
    }],
    album_api_version="0.3.1",
    args=[{
        "name": "input_image_path",
        "type": "file",
        "description": "The image about to be displayed in Napari.",
        "required": True
    }],
    run=run,
    dependencies={'environment_file': env_file}
)
