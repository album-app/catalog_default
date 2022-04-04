import icy.main.Icy;
import icy.gui.viewer.Viewer;
import icy.file.Loader;
import icy.sequence.Sequence;

import javax.swing.SwingUtilities;
import java.lang.reflect.InvocationTargetException;

public class Main {
	public static void main(String...args) throws InterruptedException, InvocationTargetException {
		Icy.main(args);
		Sequence sequence = Loader.loadSequence(args[0], 0, true);
	}
}
