package cucumber;

import io.cucumber.testng.AbstractTestNGCucumberTests;
import io.cucumber.testng.CucumberOptions;

// Add feature file path
@CucumberOptions(features = "src/test/java/cucumber", glue = "stepDefinition", monochrome = true, plugin = {
        "html:target/cucumber.html" })

public class TestRunnerFile extends AbstractTestNGCucumberTests {

}