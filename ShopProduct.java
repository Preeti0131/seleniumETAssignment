package stepDefinition;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;

public class ShopProduct {

    private WebDriver driver;

    @Given("Launch Weather Shopper website")
    public void navigateToWeatherShopperWebsite() {

        System.setProperty("webdriver.chrome.driver", "/usr/local/bin/chromedriver");
        driver = new ChromeDriver();
        driver.get("https://weathershopper.pythonanywhere.com/");
        driver.manage().window().maximize();
    }

    @When("Identify the temperature and read info")
    public void getTemperature() {
        WebElement temperatureElement = driver.findElement(By.id("temperature"));
        String temperature = temperatureElement.getText();
        System.out.println("Temperature: " + temperature);
        WebElement infoButton = driver.findElement(By.xpath("//span[@class='octicon octicon-info']"));
        infoButton.click();
    }

   // @And("Choose to buy either Moisturizer or Sun screen")
 //   public void chooseProduct() {
   //     WebElement infoButton = driver.findElement(By.xpath("//span[@class='octicon octicon-info']"));
     //   infoButton.click();
  //  }

    @Then("Choose the product")
    public void selectProduct() {
        WebElement temperatureElement = driver.findElement(By.id("temperature"));
        String temperature = temperatureElement.getText();
        System.out.println("Temperature: " + temperature);
        // Extract numbers from the string using regular expression
        String numberString = temperature.replaceAll("[^\\d.]", "");

        // Convert the extracted number to a double
        double number = Double.parseDouble(numberString);

        System.out.println("Extracted number: " + number);
        if(number <= 19.0){
            System.out.println("Moisturizer selected");
            WebElement moisturizer = driver.findElement(By.xpath("(//button[@class='btn btn-primary'])[1]"));
            moisturizer.click();
        }
        else{
            System.out.println("Sunscreen selected");
            WebElement sunscreen = driver.findElement(By.xpath("(//button[@class='btn btn-primary'])[2]"));
            sunscreen.click();
        }
    }

    @And("Read the instruction of product")
    public void readInstructions() {
        WebElement info = driver.findElement(By.xpath("//span[@class='octicon octicon-info']"));
        info.click();
        WebElement instructionElement = driver.findElement(By.xpath("//div[@class='popover-body']"));
        String instructions = instructionElement.getText();
        System.out.println("Instructions: " + instructions);
    }

    @And("Add the product to cart")
    public void addToCart() {
        WebElement addButton = driver.findElement(By.xpath("(//button[@class='btn btn-primary'])[1]"));
        addButton.click();

    }

    @And("Verify the cart value and initiate a payment")
    public void verifyCart() {
        WebElement cartButton = driver.findElement(By.id("cart"));
        cartButton.click();
            WebElement pay = driver.findElement(By.xpath("//button[@type='submit']"));
            pay.click();



    }

    @And("make payment")
    public void makePayment(){
        WebElement iframe = driver.findElement(By.xpath("/html/body/iframe"));
        //Switch to iframe
        driver.switchTo().frame(iframe);


        WebDriverWait wait = new WebDriverWait(driver, 10); // Wait up to 10 seconds

        // Wait until the element is present and visible
        //Enter email id
        WebElement emailInput = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//input[@id='email']")));
        emailInput.sendKeys("preeti@gmail.com");

        //enter card number
        WebElement cardNumber = driver.findElement(By.id("card_number"));
        String cardNumberValue = "4242 4242 4242 4242";
        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("arguments[0].value = arguments[1];", cardNumber, cardNumberValue);

        //enter card expiry date
        WebElement expiryDate = driver.findElement(By.id("cc-exp"));
        String expiryDateValue = "03/25";
        JavascriptExecutor js1 = (JavascriptExecutor) driver;
        js1.executeScript("arguments[0].setAttribute('value', arguments[1])", expiryDate, expiryDateValue);

        //Enter CVV number
        WebElement cvv = driver.findElement(By.id("cc-csc"));
        cvv.sendKeys("846");

        //Enter zip code
        WebElement zipCode = wait.until(ExpectedConditions.elementToBeClickable(By.id("billing-zip")));
        zipCode.sendKeys("560078");

        //Do the payment
        WebElement payment = driver.findElement(By.id("submitButton"));
        payment.click();

        //Verify the payment successful or not
        WebElement success = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//h2[.='PAYMENT SUCCESS']")));
        String ActualResult = success.getText();
        String expectedResult = "PAYMENT SUCCESS";

        Assert.assertEquals(ActualResult, expectedResult, "The actual result doesn't match the expected result.");
    }
        @And("Close the browser")
        public void closeBrowser(){
            driver.quit();
        }


}
