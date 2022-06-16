//Опсиание цифровых пинов
#define FIRST_SERVO 7
#define SEC_SERVO 8
#define TH_SERVO 9

void setup()
{
Serial.begin(9600);
Serial.println("Left driving - 1");
Serial.println("\t");
Serial.println("Right driving - 2");
Serial.println("\t");
Serial.println("STOP driving - 0");
Serial.println("\t");
Serial.println("Water/heat cleaning - 4");
Serial.println("\t");
Serial.println("Stop water/heat cleaning - 5");
}

void loop()
{
  if (Serial.available() > 0)
  {
      //Присваивание переменной с именем mode значение из последовательного порта
      char mode = Serial.read();
      //Если переменная с именем mode стала равна 1, то один цифровой пин FIRST_SERVO
      //приобретает высокий сигнал, а SEC_SERVO низкий
      if (mode == '1')
      {
        Serial.println("Left driving START!");
        digitalWrite(FIRST_SERVO, HIGH);
        digitalWrite(SEC_SERVO, LOW);
      }
      //Если переменная с именем mode стала равна 2, то один цифровой пин FIRST_SERVO
      //приобретает низкий сигнал, а SEC_SERVO высокий
      if (mode == '2')
      {
        Serial.println("Right driving START!");
        digitalWrite(FIRST_SERVO, LOW);
        digitalWrite(SEC_SERVO, HIGH);      
      }
      //Если переменная с именем mode стала равна 0, то оба цифровых пина FIRST_SERVO
      //и SEC_SERVO приобретают низкий сигнал
      if (mode == '0')
      {
        Serial.println("Driving STOP!");
        digitalWrite(FIRST_SERVO, LOW);
        digitalWrite(SEC_SERVO, LOW);      
      }
      //Если переменная с именем mode стала равна 4, то пин TH_SERVO приобретает высокий уровень
      if (mode == '4')
      {
        Serial.println("Water/Heat clean START!");
        digitalWrite(TH_SERVO, LOW);      
      }
      //Если переменная с именем mode стала равна 5, то пин TH_SERVO приобретает низкий уровень
      if (mode == '5')
      {
        Serial.println("Water/Heat clean STOP!");
        digitalWrite(TH_SERVO, LOW);      
      }
    
  }
}
