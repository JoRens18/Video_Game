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
		Serial.println("Water level: 0mm - Empty!"); 
	}
	else if (Water_val>480 && Water_val<=530){ 
		Serial.println("Water level: 0mm to 5mm"); 
	}
	else if (Water_val>530 && Water_val<=615){ 
		Serial.println("Water level: 5mm to 10mm"); 
	}
	else if (Water_val>615 && Water_val<=660){ 
		Serial.println("Water level: 10mm to 15mm"); 
	}	
	else if (Water_val>660 && Water_val<=680){ 
		Serial.println("Water level: 15mm to 20mm"); 
	}
	else if (Water_val>680 && Water_val<=690){ 
		Serial.println("Water level: 20mm to 25mm"); 
	}
	else if (Water_val>690 && Water_val<=700){ 
		Serial.println("Water level: 25mm to 30mm"); 
	}
	else if (Water_val>700 && Water_val<=705){ 
		Serial.println("Water level: 30mm to 35mm"); 
	}
	else if (Water_val>705){ 
		Serial.println("Water level: 35mm to 40mm"); 
	}
	
	delay(5000); // Check for new value every 5 sec
}
