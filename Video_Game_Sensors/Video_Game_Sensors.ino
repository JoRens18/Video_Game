// Sensors to use: Water Level Sensor,Joystick
// Sounds devices: Active Buzzer, Big Sound
// Animations: RGB LED - RED,YELLOW,GREEN 

const int water = A0; //Water Level Sensor AO pin to Arduino pin A0
int water_val;     		 //Variable to store the incomming data

const int buzzer = 9; //buzzer to arduino pin 9


void setup()
{
	//Begin serial communication
	Serial.begin(9600);
	pinMode(buzzer, OUTPUT); // Set buzzer - pin 9 as an output
}

void loop()
{
        tone(buzzer, 1000); // Send 1KHz sound signal...
	Water_val = analogRead(water); //Read data from analog pin and store it to value variable
	
	if (Water_val<=480){ 
		Serial.println("PUT OUT THE FIRE"); 
	}
	else if (Water_val>480 && Water_val < 630){ 
		Serial.println("Fire Partly Relinquished Keep Going"); 
	}
	

	delay(5000); // Check for new value every 5 sec
}
