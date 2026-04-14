from album.runner.api import setup

# Please import additional modules at the beginning of your method declarations.
# More information: https://docs.album.solutions/en/latest/solution-development/

env_file = """channels:
  - conda-forge
dependencies:
  - python=3.12
  - scikit-image=0.25.2
  - pip:
    - napari[all]==0.5.6
"""


def run():
    import napari
    from skimage.io import imread
    from album.runner.api import get_args

    img = imread(get_args().input_image_path)
    viewer = napari.Viewer()
    viewer.add_image(img, rgb=False, name="Input image")
    napari.run()


setup(
    group="album",
    name="template-napari",
    version="0.1.1",
    title="Napari template",
    description="An Album solution template for running Napari.",
    solution_creators=["Album team"],
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
    album_api_version="0.7.1",
    doi="10.5281/zenodo.6409780",
    args=[{
        "name": "input_image_path",
        "type": "file",
        "description": "The image about to be displayed in Napari.",
        "required": True
    }],
    run=run,
    dependencies={'environment_file': env_file}
)
