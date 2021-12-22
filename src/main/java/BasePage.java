import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

import java.util.concurrent.TimeUnit;

public class BasePage {

    public WebDriver driver;

    public WebDriver setUp(String browserName) {
        if (browserName.equalsIgnoreCase("chrome")) {
            System.setProperty("webdriver.chrome.driver", "C:\\Program Files (x86)\\chromedriver.exe");
            driver = new ChromeDriver();
        }else if(browserName.equalsIgnoreCase("firefox")){
            System.setProperty("webdriver.gecko.driver", "C:\\Program Files (x86)\\geckodriver.exe");
            driver = new FirefoxDriver();
        }
        driver.get("https://orteil.dashnet.org/cookieclicker/");
        driver.manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS);
        driver.manage().window().maximize();
        return driver;
    }
}
