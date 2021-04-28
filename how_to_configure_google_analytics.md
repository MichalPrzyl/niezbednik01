Title: How to configure and use Google Analytics
Author: Michał Przyłucki
Date: 28.04.2021

---

# How to start #

Basically you want to go to google analytics and configure the account and assign your website to it.
Then it requires to put a JavaScript code in your site code. 

# How to do this with WordPress #

1. Use Total Commander or other application with FTP Client.
2. Connect to your serwer to see all your files.
3. Find the THEME catalog you're using in WordPress and find a file `functions.php`
4. You have to create a function in which you are enqueueing your script.
5. Below the function you want to call it with `add_action('wp_enqueue_scripts', 'help_me_god');`

```
function help_me_god(){
	wp_enqueue_script('skrypt', 'http://link_to_your_script_on_serwer_with_relative_path', false);
    wp_enqueue_script('skrypt2', 'https://link_to_script_that_google_analytics_gave_you_to_script_href', false);
}

add_action('wp_enqueue_scripts', 'help_me_god');
```

6. You upload and replace the `function.php` file and the script file to the server.

NOTE: If you wanna test it, just put some kind of alerts in the js script you wanna invoke from functions.php.
