from contextlib import contextmanager

from album.runner.api import setup


# Please import additional modules at the beginning of your method declarations.
# More information: https://docs.album.solutions/en/latest/solution-development/


def install():
    import subprocess
    import shutil
    from album.runner.api import get_app_path

    get_app_path().mkdir(exist_ok=True, parents=True)

    # write pom and main java file into app path
    with write_pom() as writer:
        with add_repositories(writer):
            add_repository(writer, 'scijava.public', 'https://maven.scijava.org/content/groups/public')
        with add_dependencies(writer):
            add_dependency(writer, 'sc.fiji:fiji:2.3.1', exclude=['net.imagej:imagej-updater'])

    write_main()

    # compile app
    subprocess.run([shutil.which('mvn'), 'compile', '-B'], cwd=get_app_path())


def run():
    import shutil
    import subprocess
    from album.runner.api import get_app_path, get_package_path, get_args
    from pathlib import Path

    output_path = Path(get_args().output_image_path).absolute()
    args = '%s %s %s' % (get_package_path().joinpath('macro.ijm'), 'output_file', output_path)

    subprocess.run('%s exec:java -q -Dexec.mainClass="Main" -Dexec.args="%s"' % (shutil.which('mvn'), args),
                   shell=True, cwd=get_app_path(), stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL)


@contextmanager
def write_pom():
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

        yield type('',(object,),{"tag": tag, "text": text, "line": line})()

    with open(get_app_path().joinpath('pom.xml'), 'w') as pom_file:
        pom_file.write(indent(doc.getvalue()))


@contextmanager
def add_dependencies(writer):
    with writer.tag('dependencies'):
        yield None


def add_dependency(writer, dependency, exclude):
    dep_parts = dependency.split(':')
    with writer.tag('dependency'):
        writer.line('groupId', dep_parts[0])
        writer.line('artifactId', dep_parts[1])
        if len(dep_parts) > 2:
            writer.line('version', dep_parts[2])
        with writer.tag('exclusions'):
            for exclusion in exclude:
                with writer.tag('exclusion'):
                    excl_parts = exclusion.split(':')
                    writer.line('groupId', excl_parts[0])
                    writer.line('artifactId', excl_parts[1])


@contextmanager
def add_repositories(writer):
    with writer.tag('repositories'):
        yield None


def add_repository(writer, id, url):
    with writer.tag('repository'):
        writer.line('id', id)
        writer.line('url', url)


def write_main():
    from album.runner.api import get_app_path
    src_dir = get_app_path().joinpath('src', 'main', 'java')
    src_dir.mkdir(parents=True, exist_ok=True)
    with open(src_dir.joinpath('Main.java'), 'w') as main_file:
        main_file.write("""import net.imagej.ImageJ;
import java.util.HashMap;
import java.io.File;
import javax.script.ScriptException;
import java.io.FileNotFoundException;
public class Main {
	public static void main(String...args) throws ScriptException, FileNotFoundException {
		ImageJ ij = new ImageJ();
		ij.launch();
		HashMap script_args = new HashMap();
		for(int i =1; i+1 < args.length; i++) {
			script_args.put(args[i], args[i+1]);
		}
		ij.script().run(new File(args[0]), true, script_args);
	}
}""")


setup(
    group="album",
    name="template-fiji-macro",
    version="0.1.0",
    title="Fiji Macro template",
    description="An Album solution template run a macro script in Fiji.",
    authors=["Album team"],
    cite=[{
        "text": "Schindelin, J., Arganda-Carreras, I., Frise, E., Kaynig, V., Longair, M., Pietzsch, T., … Cardona, A. (2012). Fiji: an open-source platform for biological-image analysis. Nature Methods, 9(7), 676–682. ",
        "doi": "10.1038/nmeth.2019",
        "url": "https://fiji.sc"
    }],
    tags=["template", "java", "fiji", "macro", "maven"],
    license="UNLICENSE",
    documentation=["documentation.md"],
    covers=[{
        "description": "Dummy cover image.",
        "source": "cover.png"
    }],
    album_api_version="0.3.1",
    args=[{
        "name": "output_image_path",
        "type": "file",
        "description": "The output file name to where the processed boat image is going to be saved.",
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
