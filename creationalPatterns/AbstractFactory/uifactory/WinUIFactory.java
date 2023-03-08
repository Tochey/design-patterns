package creationalPatterns.AbstractFactory.uifactory;

import creationalPatterns.AbstractFactory.Button;
import creationalPatterns.AbstractFactory.CheckBox;
import creationalPatterns.AbstractFactory.os.windows.WinButton;
import creationalPatterns.AbstractFactory.os.windows.WinCheckBox;

public class WinUIFactory implements UIFactory {

    @Override
    public Button createButton() {
        // TODO Auto-generated method stub
       return new WinButton();
    }

    @Override
    public CheckBox createCheckBox() {
        // TODO Auto-generated method stub
        return new WinCheckBox();
    }
    
}
