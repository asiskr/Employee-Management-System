import javax.swing.JOptionPane;

public class GUI {
    public static void main(String[] args) {

        String name = JOptionPane.showInputDialog("enter your name");
        JOptionPane.showMessageDialog(null, "hello " + name);

        int age = Integer.parseInt(JOptionPane.showInputDialog("what is your age"));
        JOptionPane.showMessageDialog(null, "age "+age);
    }
}