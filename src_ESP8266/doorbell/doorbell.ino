/*
  Doorbell code
*/

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#ifndef STASSID
#define STASSID "GrawNet"
#define STAPSK  "#Euler410"
#endif

#define FLASH_ON 0

const char* ssid     = STASSID;
const char* password = STAPSK;
const int buttonFlash = 0;

int buttonVal = !FLASH_ON;
int buttonVal_old = !FLASH_ON;

unsigned long oldTime = 0;
unsigned long newTime = 0;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED off (LED is active LOW)

  // initialize FLASH button as input
  pinMode(buttonFlash, INPUT_PULLUP);
  
  Serial.begin(115200);

  // We start by connecting to a WiFi network

  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  /* Explicitly set the ESP8266 to be a WiFi-client, otherwise, it by default,
     would try to act as both a client and an access-point and could cause
     network-issues with your other WiFi-devices on your WiFi-network. */
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

// the loop function runs over and over again forever
void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    buttonVal = digitalRead(buttonFlash);
    
    if (buttonVal != buttonVal_old) {
      
      // The button has been pressed
      if (buttonVal == FLASH_ON) {
      // Make lights blink using python code
      /*
       * As far as I see, there are two ways that I could accomplish this:
       * 
       * 1. Somehow have the python code flashed to the ESP8266, and run
       *    the light blinking code directly from the board. This will
       *    probably be very hard due to incompatibility between pyFirmata
       *    and ESP8266.
       *    
       * 2. The ESP8266 sends a signal to the PieHole (192.168.1.137), which
       *    triggers the light blinking python code to run on the PieHole.
       *    This seems more feasible to me, but obviously there are some
       *    moving parts that have to be figured out.
       *    
       *    I WENT WITH #2
       */
        Serial.println("You pressed the FLASH button!");
        digitalWrite(LED_BUILTIN, LOW); // Turn the LED ON
        oldTime = millis();
        newTime = oldTime;
  
        // Set up HTTPClient
        HTTPClient http;
        http.begin("http://192.168.1.137:8090/ring");
  
        // Send the GET request
        int httpCode = http.GET();
        String payload = http.getString();
        Serial.println(httpCode);
        Serial.println(payload);
  
        // End the connection
        http.end();
      }
    }

    // If the LED is on, record time
    if (digitalRead(LED_BUILTIN) == LOW) {
      newTime = millis();
      // If LED has been on for 15 seconds, turn it off
      if (newTime - oldTime >= 15000) {
        digitalWrite(LED_BUILTIN, HIGH);
        oldTime = 0;
        newTime = 0;
      }
    }
    
    buttonVal_old = buttonVal;
  }
}
