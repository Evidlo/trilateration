DEVICE     = atmega328p
CLOCK      = 16000000
PROGRAMMER = arduino
PORT	  	 = /dev/ttyUSB0
BAUD       = 57600
FILE    	 = main
COMPILE    = avr-gcc -Wall -Os -DF_CPU=$(CLOCK) -mmcu=$(DEVICE)

all: build upload

# 8mhz-internal:
# 	avrdude -v -p $(DEVICE) -c $(PROGRAMMER) -P $(PORT) -U lfuse:w:0xFF:m -U hfuse:w:0xDA:m -U efuse:w:0xff:m

build:
	$(COMPILE) -c $(FILE).c -o $(FILE).o
	$(COMPILE) -o $(FILE).elf $(FILE).o
	avr-objcopy -j .text -j .data -O ihex $(FILE).elf $(FILE).hex
	avr-size --format=avr --mcu=$(DEVICE) $(FILE).elf

upload:
	avrdude -v -p $(DEVICE) -c $(PROGRAMMER) -P $(PORT) -b $(BAUD) -U flash:w:$(FILE).hex:i

clean:
	rm main.o
	rm main.elf
	rm main.hex
