import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

public class CookieClickerPage extends BasePage {
    WebElement bigCookie;

    //page actions
    public void coockieClickerTest(){
        bigCookie = driver.findElement(By.id("bigCookie"));
        for (int i=0; i<1000; i++){
            bigCookie.click();
        }
    }

    public static void main(String[] args) {
        CookieClickerPage page = new CookieClickerPage();
        page.setUp("chrome");
        page.coockieClickerTest();
    }
}
