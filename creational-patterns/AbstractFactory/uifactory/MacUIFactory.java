package creationalPatterns.AbstractFactory.uifactory;

import creationalPatterns.AbstractFactory.Button;
import creationalPatterns.AbstractFactory.CheckBox;
import creationalPatterns.AbstractFactory.os.mac.MacButton;
import creationalPatterns.AbstractFactory.os.mac.MacCheckBox;

public class MacUIFactory implements UIFactory {

    @Override
    public Button createButton() {
        return new MacButton();
    }

    @Override
    public CheckBox createCheckBox() {
        // TODO Auto-generated method stub
       return new MacCheckBox();
    }
    
}
