# Task 1: Software configuration
## "Subtask 1: Why did I choose to participate in the Dare IT Challenge?"
*My name is Liliia.*
*In 2021 I decided to change my career from accountant to IT.* 
*I started my education as a QA Engineer at IT Step Academy in Ukraine .* 
*Now my studies in this course are almost complete.*
*I am looking for a place where I can put my knowledge into practice.*
*My expectations for the Dare IT project are to creat a portfolio, learn more about automation testing.*
*My goal in 2023 is to find an interesting job in IT.*

# Task 2: Selectors 👉
## "Subtask 1: Searching for selectors on the login pageList all the elements that are on the login page"
<ul>✔️The_login_field_xpath
<li>//*[@id="login"]</li>
<li>//input[@id="login"]</li>
<li>//*[@id="__next"]//child::div/input[@name="login"]</li>  
</ul>
<ul>✔️The_password_field_xpath
<li>//*[@id="password"]</li>
<li>//*[@name="password"]</li>
<li>//*[@id="__next"]//child::div/input[@name="password"]</li>  
</ul>
<ul>✔️The_sign_in_button_xpath
<li>//*[@class="MuiButton-label"]</li>
<li>//span[contains(text(),"Sign in")]</li>
<li>//button[contains(@class,"MuiButton")]//span[1]</li>  
</ul>
<ul>✔️The_language_drop_down_list_xpath
<li>//div[@class="MuiCardActions-root"]/div</li>
<li>//div[@class="MuiInputBase-root MuiInput-root MuiInput-underline jss31"]</li>
<li>//input[@class="MuiSelect-nativeInput"]/parent::div</li>  
</ul>
<ul>✔️The_language_EN_button_xpath
<li>//div[@role="button"][text()="English"]</li>
<li>//div[@class="MuiCardActions-root"]/div/div</li>
</ul>
<ul>✔️The_language_PL_button_xpath
<li>//div[@role="button"][text()="Polski"]</li>
<li>//div[@class="MuiCardActions-root"]/div/div</li>
</ul>
