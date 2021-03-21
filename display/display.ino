#include <Wire.h>
#include <ArduinoJson.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

String inputString = "";
boolean stringComplete = false;
unsigned long previousUpdate = 0;
boolean screenOn = true;

byte fanChar1[8] = {
    0b00000,
    0b00000,
    0b01110,
    0b10101,
    0b11111,
    0b10101,
    0b01110,
    0b00000};

byte fanChar2[8] = {
    0b00000,
    0b00000,
    0b01110,
    0b11011,
    0b10101,
    0b11011,
    0b01110,
    0b00000};

byte celsius[8] = {
    0b01000,
    0b10100,
    0b01000,
    0b00011,
    0b00100,
    0b00100,
    0b00011,
    0b00000};

byte disk[8] = {
    0x1C,
    0x12,
    0x12,
    0x12,
    0x1C,
    0x00,
    0x1F,
    0x1F};

byte ram[] = {
    0x1C,
    0x14,
    0x18,
    0x14,
    0x14,
    0x00,
    0x1F,
    0x1F};

byte cpu[] = {
    0x1C,
    0x10,
    0x10,
    0x10,
    0x1C,
    0x00,
    0x1F,
    0x1F};

byte netup[] = {
    0x04,
    0x0E,
    0x1F,
    0x04,
    0x04,
    0x04,
    0x04,
    0x04};

byte netdown[] = {
    0x04,
    0x04,
    0x04,
    0x04,
    0x04,
    0x1F,
    0x0E,
    0x04};
void brknData()
{
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("No connection.");
  lcd.setCursor(0, 1);
  lcd.print("Check system.");
}

void setup()
{
  lcd.begin();
  lcd.backlight();

  Serial.begin(9600);
  while (!Serial)
    continue;

  lcd.createChar(0, fanChar1);
  lcd.createChar(1, fanChar2);
  lcd.createChar(2, celsius);
  lcd.createChar(3, disk);
  lcd.createChar(4, ram);
  lcd.createChar(5, cpu);
  lcd.createChar(6, netup);
  lcd.createChar(7, netdown);
}

void loop()
{
  while (!Serial.available())
    delay(50);

  StaticJsonDocument<400> doc;
  DeserializationError error = deserializeJson(doc, Serial);

  if (!error)
  {
    const char *sys_disk_free = doc["sys_disk_free"];
    const char *sys_disk_total = doc["sys_disk_total"];
    const char *ram_percent = doc["ram_percent"];
    const char *cpu_usage = doc["cpu_usage"];
    const char *temp = doc["temp"];
    const char *net_in = doc["net_in"];
    const char *net_out = doc["net_out"];
    const char *ip = doc["ip"];
    const char *uptime = doc["uptime"];


    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.write(3);
    lcd.setCursor(2, 0);
    lcd.print(sys_disk_total);
    lcd.setCursor(8, 0);
    lcd.write(3);
    lcd.print(sys_disk_free);
    lcd.setCursor(0, 1);
    lcd.write(4);
    lcd.setCursor(2, 1);
    lcd.print(ram_percent);
    lcd.setCursor(8, 1);
    lcd.write(5);
    lcd.setCursor(10, 1);
    lcd.print(cpu_usage);
    //lcd.setCursor(12,1);
    //lcd.print(temp);
    //lcd.setCursor(14,1);
    //lcd.write(2);

    lcd.setCursor(0, 2);
    lcd.write(6);
    lcd.setCursor(2, 2);
    lcd.print(net_in);
    lcd.setCursor(8, 2);
    lcd.write(7);
    lcd.setCursor(11, 2);
    lcd.print(net_out);
    lcd.setCursor(0, 3);
    lcd.print(ip);
    lcd.setCursor(12, 3);
    lcd.print(uptime);
  }
}
