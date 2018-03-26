// Arduino CODE TO CONTROL VARIOUS GAME SENSORS AND BUTTONS

// Sensors to use: Water Level Sensor,Joystick
// Sounds devices: Active Buzzer
// Animations: RGB LED - RED,YELLOW,GREEN 
 
//Water Level Sensor
const int water = A0; //Water Level Sensor AO pin to Arduino pin A0
int water_val;     		 //Variable to store the incomming data

//Buzzer Sound
const int buzzer = 9; //buzzer to arduino pin 9


// RGB LED
int redPin = 3;
int greenPin = 5;
int bluePin = 6;

int s_data = 0;
void setup()
{
	pinMode(buzzer, OUTPUT); // Set buzzer - pin 9 as an output
        pinMode(redPin,OUTPUT); 
        pinMode(greenPin,OUTPUT);
        pinMode(bluePin,OUTPUT);
  //Begin serial communication
	Serial.begin(9600);
}

void loop()
{
  while(Serial.available() ==0);
  char c = Serial.read();
  if (c =='p'){
        tone(buzzer, 1000); // Send 1KHz sound signal...
	water_val = analogRead(water); //Read data from analog pin and store it to value variable
	if (water_val<=50){ 
		Serial.println("PUT OUT THE FIRE"); 
                analogWrite(redPin,255);
                analogWrite(greenPin,0);
                analogWrite(bluePin,0);

	}
	else if (water_val>50){ 
		Serial.println("Fire Relinquished"); 
                analogWrite(redPin,0);
                analogWrite(greenPin,255);
                analogWrite(bluePin,0);
	}
  }
	
}
