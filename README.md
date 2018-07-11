# africastalking-gateways

A collection of Africa's Talking Gateway classes to help with developing on our APIs.

**Please Note: These gateway classes are not under active development and will be deprecated soon. We advice you move to the [official SDKs](#official-sdks) for a richer set of features and improved development patterns. Read this [transition guide](https://blog.africastalking.com/) to help with moving from the gateway classes to the SDKs.**

## Official SDKs
1. [C#](https://github.com/AfricasTalkingLtd/africastalking.Net)
2. [Java](https://github.com/AfricasTalkingLtd/africastalking-java)
3. [Nodejs](https://github.com/AfricasTalkingLtd/africastalking-node.js)
4. [PHP](https://github.com/AfricasTalkingLtd/africastalking-php)
5. [Python](https://github.com/AfricasTalkingLtd/africastalking-python)
6. [Ruby](https://github.com/AfricasTalkingLtd/africastalking-ruby)

## Project Structure

Each gateway class folder has the gateway class file and code samples for various supported API methods. Some API methods are not available in the gateway classes and we advice you move to the SDKs for the full set of features.

```
gateway/
    |-- class_file
    |-- samples/
        |-- sms/
            - Sending a message
            - Sending a message using a sender id
            - Enqueuing messages
            - Fetching (inbox) messages
            - Creating a premium sms subscription
            - Fetching premium sms subscriptions
            - Sending a premium rated (subscription) message
            - Sending a premium rated (onDemand) message

        |-- voice/
            - Making an outgoing call
            - Handling an incoming call
            - Fetching number of queued calls
            - Uploading a media file

        |-- ussd/
            - Processing USSD sessions

        |-- airtime/
            - Sending Airtime

        |-- payments/
            - Initiating a mobile checkout
            - Making a mobile B2C payment
            - Making a mobile B2B payment
            - Initiating a Bank account checkout
            - Making a Bank checkout Validation
            - Making a Bank Transfer
            - Initiating a Card checkout
            - Making a card checkout validation

        |-- userData/
            - Fetching user balance
```

## Usage

To use the gateway classes download the respective class file and require it in your project. Refer to the code samples for usage examples.

