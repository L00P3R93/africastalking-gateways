# Africa's Talking

> 


**Note on SSL Certificate Verification**

You may experienc certificate validation issues when connecting to our API. The error message you see may look something like this: `Unable to find valid certification path to requested target`

Please do not panic! Our certificate is [perfectly valid](http://www.sslshopper.com/ssl-checker.html#hostname=api.africastalking.com), and the error you are seeing is quite common amongst Java clients connecting to secure websites.

Here is how to fix the issue:

- Download and compile InstallCert.java (you can find the code under `utils/InstallCert.java`).

- On the CMD prompt(Windows) or Terminal(*nix), run: `java InstallCert api.africastalking.com`

This will download a copy of our Certificate and create a file named `jssecacerts` in the current directory.

- You can now add our Certificate to your trusted store by copying the created `jssecacerts` file to the Java security directory under `$JAVA_HOME/jre/lib/security`


#### Usage

```sh
# For example, to build the SMS sample, run the following commands:

# 1. Compile the sample code
$ javac -cp lib/json.jar AfricasTalkingGateway.java samples/SMS.java -d out

# 2. Go to output folder
$ cd out

# 3. Run the compiled code
$ java -cp ../lib/json.jar: SMS
```