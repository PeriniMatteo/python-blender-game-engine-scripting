
double s = 0.0;
double x = 0;
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

void loop() {
  
  double voltage = sin(x)*3.14-s;
  Serial.println(voltage);
  s=sin(x)*3.14;
  x= x+0.02;
  //s=voltage;
  //Serial.println("");
  //Serial.println(sin(x)*3.14);
  //Serial.println(s);
    delay(30);

}
