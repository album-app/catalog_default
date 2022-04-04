from io import StringIO

from album.runner.api import setup

# Please import additional modules at the beginning of your method declarations.
# More information: https://docs.album.solutions/en/latest/solution-development/

env_file = StringIO("""channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - maven=3.8.1
  - openjdk=11.0.9.1
  - yattag=1.13.2
""")


def install():
    import subprocess
    import shutil
    from album.runner.api import get_app_path

    get_app_path().mkdir(exist_ok=True, parents=True)

    # write pom and main java file into app path
    _write_pom()
    _write_main()

    # compile app
    subprocess.run([shutil.which('mvn'), 'compile', '-B'], cwd=get_app_path())


def run():
    import shutil
    import subprocess
    from album.runner.api import get_app_path, get_args

    subprocess.run('%s exec:java -q -Dexec.mainClass="Main" -Dexec.args="\'%s\'"' % (shutil.which('mvn'), get_args().name),
                   shell=True, cwd=get_app_path())


def _write_pom():
    from album.runner.api import get_app_path, get_active_solution
    from yattag import Doc, indent

    doc, tag, text, line = Doc().ttl()
    solution = get_active_solution()

    with tag('project', **{'xmlns': 'http://maven.apache.org/POM/4.0.0',
                           'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                           'xsi:schemaLocation': 'http://maven.apache.org/POM/4.0.0\nhttp://maven.apache.org/xsd/maven-4.0.0.xsd'}):
        line('modelVersion', '4.0.0')
        line('groupId', solution.coordinates().group())
        line('artifactId', solution.coordinates().name())
        line('version', solution.coordinates().version())
        with tag('properties'):
            line('maven.compiler.source', '11')
            line('maven.compiler.target', '11')
            line('project.build.sourceEncoding', 'UTF-8')

    with open(get_app_path().joinpath('pom.xml'), 'w') as pom_file:
        pom_file.write(indent(doc.getvalue()))


def _write_main():
    from album.runner.api import get_app_path
    src_dir = get_app_path().joinpath('src', 'main', 'java')
    src_dir.mkdir(parents=True, exist_ok=True)
    with open(src_dir.joinpath('Main.java'), 'w') as main_file:
        main_file.write("""public class Main {
	public static void main(String...args) {
		System.out.println("Hello " + args[0]);
	}
}""")


setup(
    group="album",
    name="template-maven-singlefile",
    version="0.1.0",
    title="Maven template (single file version)",
    description="An Album solution template running Java code via Maven.",
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
    dependencies={'parent': {'resolve_solution': 'album:template-maven-java11:0.1.0'}}
)
