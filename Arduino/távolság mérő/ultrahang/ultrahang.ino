#define DIN 5
#define CS 6
#define CLK 7

void init()
{
  digitalWrite(CS, HIGH);
  pinMode(DIN, OUTPUT);
  pinMode(CS, OUTPUT);
  pinMode(CLK, OUTPUT);
}

void output(byte address, byte data)
{
  digitalWrite(CS, LOW);
  shiftOut(DIN, CLK, MSBFIRST, address);
  shiftOut(DIN, CLK, MSBFIRST, data);
  digitalWrite(CS, HIGH);
}

void setup()
{
  init();
  output(0x0f, 0x00);
  output(0x0c, 0x01);
  output(0x09, 0x00);
  output(0x0b, 0x07);
  output(0x01, 0x03);
  output(0x02, 0x03);
  output(0x03, 0x03);
  output(0x04, 0x03);
  output(0x05, 0x03);
  output(0x06, 0x03);
  output(0x07, 0x03);
  output(0x08, 0x03);
}

void loop(){
   
}
