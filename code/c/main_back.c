#include <avr/io.h>
#include <avr/interrupt.h>

#define F_CPU 16000000
#define BAUD 57600
#define BAUD_PRESCALER (((F_CPU / (BAUD * 16UL))) - 1)

volatile uint8_t adc_ready = 0;
volatile uint8_t adc_reading;

void USART_send(unsigned char data){
    while(!(UCSR0A & (1<<UDRE0)));
    UDR0 = data;
}

int main(){
    // set baud of USART
    UBRR0H = (BAUD_PRESCALER >> 8);
    UBRR0L = (BAUD_PRESCALER);
    // enable USART TX/RX
    UCSR0B = (1 << RXEN0) | (1 << TXEN0);
    UCSR0C = (1 << UCSZ00) | (1 << UCSZ01);

    // enable ADC, enable ADC interrupt, enable ADC auto trigger, 128 prescaler
    /* ADCSRA = (1 << ADEN) | (1 << ADATE) | (1 << ADIE) | (0 << ADPS0); */
    ADCSRA = (1 << ADEN) | (1 << ADATE) | (1 << ADIE) | (7 << ADPS0);
    // auto trigger ADC on Timer1 overflow
    ADCSRB = (1 << ADTS2) | (1 << ADTS1);
    // use internal reference for ADC, left-adjust ADC reading
    /* ADMUX = (1 << REFS1) | (1 << REFS0) | (1 << ADLAR); */
    // use VCC as reference for ADC, left-adjust ADC reading
    /* ADMUX = (1 << REFS0) | (1 << ADLAR); */
    ADMUX = (1 << REFS0);

    // Fast pwm mode, overflows @ OCR1A
    TCCR1A |= (1 << WGM10) | (1 << WGM11);
    // set prescaler to /1 and FAST PWM mode
    TCCR1B |= (1 << CS10) | (1 << WGM12) | (1 << WGM13);
    // about 7111.11 hz
    OCR1A = 2750;

    sei();

    while (1){
        if (adc_ready == 1){
            adc_ready = 0;
            USART_send(adc_reading);
        }
    }
}

ISR (ADC_vect){
    TIFR1 |= (1<<TOV1); // restart adc
    adc_ready = 1;
    adc_reading = ADCH;
}
