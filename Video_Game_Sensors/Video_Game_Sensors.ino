// Arduino CODE TO CONTROL VARIOUS GAME SENSORS AND BUTTONS

// Sensors to use: Water Level Sensor,Joystick
// Sounds devices: Active Buzzer
// Animations: RGB LED - RED,YELLOW,GREEN 
 
//Water Level Sensor
const int water = A0; //Water Level Sensor AO pin to Arduino pin A0
int water_val;     		 //Variable to store the incomming data

//Buzzer Sound
const int buzzer = 9; //buzzer to arduino pin 9

//Joystick
int xposition = 0;
int yPosition = 0;
int buttonState = 0;


// RGB Sensor
int redPin = 7;
int greenPin = 6;
int bluePin = 5;

void setup()
{
	//Begin serial communication
	Serial.begin(9600);

	pinMode(buzzer, OUTPUT); // Set buzzer - pin 9 as an output

        pinMode(redPin,OUTPUT); 
        pinMode(greenPin,OUTPUT);
        pinMode(blue,OUTPUT);
        
        pinMode(xPin,INPUT);
        pinMode(yPin,INPUT);
        pinMode(buttonPin,INPUT_PULLUP);
}

void loop()
{
        tone(buzzer, 1000); // Send 1KHz sound signal...
	Water_val = analogRead(water); //Read data from analog pin and store it to value variable
	
	if (Water_val<=480){ 
		Serial.println("PUT OUT THE FIRE"); 
                analogWrite(redPin,255);
                analogWrite(greenPin,0);
                analogWrite(bluePin,0);

	}
	else if (Water_val>480 && Water_val < 630){ 
		Serial.println("Fire Partly Relinquished Keep Going"); 
                analogWrite(redPin,255);
                analogWrite(greenPin,255);
                analogWrite(bluePin,0);
	}
        else if (Water_val>480 && Water_val < 630){ 
		Serial.println("Fire Relinquished"); 
                analogWrite(redPin,0);
                analogWrite(greenPin,255);
                analogWrite(bluePin,0);
	}
	

	delay(5000); // Check for new value every 5 sec
}
