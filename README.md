# africastalking-gateways

A collection of Africa's Talking Gateway classes to help with developing on our APIs.

**Please Note: These gateway classes are not under active development and will be deprecated soon. We advice you move to the [official SDKs](#official-sdks).
The SDKs offer a richer set of features and improved development patterns. We have put together [a transition guide](https://blog.africastalking.com/) to help with moving from the gateway classes to the SDKs and to better demonstrate the improved development patterns.**

## Official SDKs
1. [Java](https://github.com/AfricasTalkingLtd/africastalking-java)
2. [Nodejs](https://github.com/AfricasTalkingLtd/africastalking-node.js)
3. [PHP](https://github.com/AfricasTalkingLtd/africastalking-php)
4. [Python](https://github.com/AfricasTalkingLtd/africastalking-python)
5. [Ruby](https://github.com/AfricasTalkingLtd/africastalking-ruby)
6. [.Net](https://github.com/AfricasTalkingLtd/africastalking.Net)

## Project Structure

Each gateway class folder has the gateway class file and code samples for various supported API methods. Some API methods are not available on the gateway classes and we advice you move to the SDKs for the full set of features.

```
gateway/
    |-- class_file
    |-- samples/
        |-- SMS/
            - Sedning a message
            - Sending messages using a sender id or shortcode parameter
            - Enqueue messages
            - Sending premium rated (subscription) messages
            - Sending premium rated (onDemand) messages

        |-- Voice/
            - Making an outgoing call
            - Handling an incoming call
            - Fetching number of queued calls
            - Uploading a media file

        |-- USSD/
            - Processing USSD sessions

        |-- Airtime/
            - Sending Airtime

        |-- Payments/
            - Initiating a mobile checkout
            - Making a mobile B2C payment
            - Making a mobile B2B payment
            - Initiating a Bank account checkout
            - Making a Bank checkout Validation
            - Making a Bank Transfer
            - Initiating a Card checkout
            - Making a card checkout validation

        |-- User Data/
            - Fetching user balance
```

## Usage

To use the gateway classes download the respective class file and require it in your project. Refer to the code samples for usage examples.

