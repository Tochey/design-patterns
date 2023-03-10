package creationalPatterns.AbstractFactory.uifactory;

import creationalPatterns.AbstractFactory.Button;
import creationalPatterns.AbstractFactory.CheckBox;

public interface UIFactory{
    Button createButton();
    CheckBox createCheckBox();
}