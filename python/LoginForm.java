import java.awt.*;
import java.applet.*;

public class LoginForm extends Applet {
    TextField user, pass;
    Button login;

    public void init() {
        Label userLabel = new Label("Username:");
        user = new TextField(20);

        Label passLabel = new Label("Password:");
        pass = new TextField(20);
        pass.setEchoChar('*');

        login = new Button("Login");

        add(userLabel);
        add(user);
        add(passLabel);
        add(pass);
        add(login);
    }
}
/* <applet code="LoginForm.class" width=300 height=200></applet> */
