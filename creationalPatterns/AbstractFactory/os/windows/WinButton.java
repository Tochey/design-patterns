package creationalPatterns.AbstractFactory.os.windows;

import creationalPatterns.AbstractFactory.Button;

public class WinButton implements Button {

    @Override
    public void paint() {
        // TODO Auto-generated method stub
        System.out.println("This is a windows Button");
    }
    
}
