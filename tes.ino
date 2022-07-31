#define led_1 10
#define led_2 11
#define led_3 12
#define led_4 13
int datapython;
String mydata;
int S1 =  2;
int S2 =  3;
int S3 =  4;
int S4 =  5;
bool data1 = 0;
bool data2 = 0;
bool data3 = 0;
bool data4 = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led_1, OUTPUT);
  pinMode(led_2, OUTPUT);
  pinMode(led_3, OUTPUT);
  pinMode(led_4, OUTPUT);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  
}

void loop() {
  data1 = digitalRead(S1);
  data2 = digitalRead(S2);
  data3 = digitalRead(S3);
  data4 = digitalRead(S4);
  // put your main code here, to run repeatedly:
  //mydata = Serial.readStringUntil('\n');
  if (Serial.available()){
    datapython = Serial.read();
    switch (datapython){
  case 'A' :
    digitalWrite(led_1, HIGH);
    digitalWrite(led_3, HIGH);
    digitalWrite(led_2, LOW);
    digitalWrite(led_4, LOW);
    break;
  // process in data A
  // on

  case 'B' :
    digitalWrite(led_2, HIGH);    
    digitalWrite(led_4, HIGH);
    digitalWrite(led_1, LOW);
    digitalWrite(led_3, LOW);
    break;

  // process in data B
  // on
  
  case 'C' :
    digitalWrite(led_1,LOW);
    digitalWrite(led_2, LOW);
    digitalWrite(led_3, HIGH);
    digitalWrite(led_4,LOW);
    break;
  // process in data C
  // on
    
  case  'D' : 
    digitalWrite(led_2, LOW);    
    digitalWrite(led_4, HIGH);
    digitalWrite(led_1, LOW);
    digitalWrite(led_3, LOW);
      break;
    }
  }

else{
    if (data1==LOW){
      if(data2==LOW){
        if(data3==LOW){
          if(data4==LOW){
            Serial.println('A');
            delay(4000);
          }
        }
      }
    }
    if (data1==HIGH){
      if(data2==LOW){
        if(data3==LOW){
          if(data4==LOW){
            Serial.println('B');
            delay(4000);
          }
        }
      }
    }
    if (data1==LOW){
      if(data2==HIGH){
        if(data3==LOW){
          if(data4==LOW){
            Serial.println('C');
            delay(4000);
          }
        }
      }
    }
    if (data1==HIGH){
      if(data2==HIGH){
        if(data3==LOW){
          if(data4==LOW){
            Serial.println('D');
            delay(4000);
          }
        }
      }
    }
    if (data1==LOW){
      if(data2==LOW){
        if(data3==HIGH){
          if(data4==LOW){
            Serial.println('E');
            delay(4000);
          }
        }
      }
    }
    if (data1==LOW){
      if(data2==LOW){
        if(data3==LOW){
          if(data4==HIGH){
            Serial.println('F');
            delay(4000);
          }
        }
      }
    }
  }
}
