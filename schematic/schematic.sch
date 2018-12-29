EESchema Schematic File Version 4
LIBS:schematic-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L pspice:OPAMP U?
U 1 1 5C109C76
P 4850 3650
F 0 "U?" H 5191 3696 50  0000 L CNN
F 1 "LF442CN" H 5191 3605 50  0000 L CNN
F 2 "" H 4850 3650 50  0001 C CNN
F 3 "" H 4850 3650 50  0001 C CNN
	1    4850 3650
	1    0    0    -1  
$EndComp
$Comp
L MCU_Module:Arduino_Nano_v3.x A?
U 1 1 5C109D50
P 7250 3650
F 0 "A?" H 7250 2564 50  0000 C CNN
F 1 "Arduino_Nano_v3.x" H 7250 2473 50  0000 C CNN
F 2 "Module:Arduino_Nano" H 7400 2700 50  0001 L CNN
F 3 "http://www.mouser.com/pdfdocs/Gravitech_Arduino_Nano3_0.pdf" H 7250 2650 50  0001 C CNN
	1    7250 3650
	-1   0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5C109F35
P 6100 3800
F 0 "C?" H 6215 3846 50  0000 L CNN
F 1 ".2uF" H 6215 3755 50  0000 L CNN
F 2 "" H 6138 3650 50  0001 C CNN
F 3 "~" H 6100 3800 50  0001 C CNN
	1    6100 3800
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5C109FCB
P 5700 3650
F 0 "R?" V 5493 3650 50  0000 C CNN
F 1 "150" V 5584 3650 50  0000 C CNN
F 2 "" V 5630 3650 50  0001 C CNN
F 3 "~" H 5700 3650 50  0001 C CNN
	1    5700 3650
	0    1    1    0   
$EndComp
Wire Wire Line
	5150 3650 5550 3650
Wire Wire Line
	5850 3650 6100 3650
Connection ~ 6100 3650
Wire Wire Line
	6100 3650 6750 3650
$Comp
L power:GND #PWR?
U 1 1 5C10A079
P 6100 4900
F 0 "#PWR?" H 6100 4650 50  0001 C CNN
F 1 "GND" H 6105 4727 50  0000 C CNN
F 2 "" H 6100 4900 50  0001 C CNN
F 3 "" H 6100 4900 50  0001 C CNN
	1    6100 4900
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5C10A0E6
P 7150 4900
F 0 "#PWR?" H 7150 4650 50  0001 C CNN
F 1 "GND" H 7155 4727 50  0000 C CNN
F 2 "" H 7150 4900 50  0001 C CNN
F 3 "" H 7150 4900 50  0001 C CNN
	1    7150 4900
	1    0    0    -1  
$EndComp
Wire Wire Line
	7150 4900 7150 4650
Wire Wire Line
	6100 3950 6100 4900
$Comp
L power:+5V #PWR?
U 1 1 5C10A19D
P 4750 2850
F 0 "#PWR?" H 4750 2700 50  0001 C CNN
F 1 "+5V" H 4765 3023 50  0000 C CNN
F 2 "" H 4750 2850 50  0001 C CNN
F 3 "" H 4750 2850 50  0001 C CNN
	1    4750 2850
	1    0    0    -1  
$EndComp
Wire Wire Line
	4750 2850 4750 3350
$Comp
L power:GND #PWR?
U 1 1 5C10A228
P 4750 4900
F 0 "#PWR?" H 4750 4650 50  0001 C CNN
F 1 "GND" H 4755 4727 50  0000 C CNN
F 2 "" H 4750 4900 50  0001 C CNN
F 3 "" H 4750 4900 50  0001 C CNN
	1    4750 4900
	1    0    0    -1  
$EndComp
Wire Wire Line
	4750 4900 4750 3950
Wire Wire Line
	7050 2650 7050 2400
Text Label 7050 2400 0    50   ~ 0
USB
$Comp
L Device:R R?
U 1 1 5C10A427
P 4200 3150
F 0 "R?" H 4270 3196 50  0000 L CNN
F 1 "3.3K" H 4270 3105 50  0000 L CNN
F 2 "" V 4130 3150 50  0001 C CNN
F 3 "~" H 4200 3150 50  0001 C CNN
	1    4200 3150
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5C10A489
P 4200 4250
F 0 "R?" H 4270 4296 50  0000 L CNN
F 1 "3.3K" H 4270 4205 50  0000 L CNN
F 2 "" V 4130 4250 50  0001 C CNN
F 3 "~" H 4200 4250 50  0001 C CNN
	1    4200 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	4200 4100 4200 3550
Wire Wire Line
	4200 3550 4550 3550
Connection ~ 4200 3550
Wire Wire Line
	4200 3550 4200 3300
$Comp
L power:GND #PWR?
U 1 1 5C10A612
P 4200 4900
F 0 "#PWR?" H 4200 4650 50  0001 C CNN
F 1 "GND" H 4205 4727 50  0000 C CNN
F 2 "" H 4200 4900 50  0001 C CNN
F 3 "" H 4200 4900 50  0001 C CNN
	1    4200 4900
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 5C10A695
P 4200 2850
F 0 "#PWR?" H 4200 2700 50  0001 C CNN
F 1 "+5V" H 4215 3023 50  0000 C CNN
F 2 "" H 4200 2850 50  0001 C CNN
F 3 "" H 4200 2850 50  0001 C CNN
	1    4200 2850
	1    0    0    -1  
$EndComp
Wire Wire Line
	4200 2850 4200 3000
Wire Wire Line
	4200 4400 4200 4900
$Comp
L Device:R R?
U 1 1 5C10A8F2
P 4750 4200
F 0 "R?" V 4543 4200 50  0000 C CNN
F 1 "680K" V 4634 4200 50  0000 C CNN
F 2 "" V 4680 4200 50  0001 C CNN
F 3 "~" H 4750 4200 50  0001 C CNN
	1    4750 4200
	0    1    1    0   
$EndComp
Wire Wire Line
	4900 4200 5150 4200
Wire Wire Line
	5150 4200 5150 3650
Connection ~ 5150 3650
Wire Wire Line
	4600 4200 4450 4200
Wire Wire Line
	4450 4200 4450 3750
Wire Wire Line
	4450 3750 4550 3750
Wire Wire Line
	4450 3750 3700 3750
Connection ~ 4450 3750
$Comp
L Device:C C?
U 1 1 5C10AE2D
P 3550 3750
F 0 "C?" V 3298 3750 50  0000 C CNN
F 1 ".2uF" V 3389 3750 50  0000 C CNN
F 2 "" H 3588 3600 50  0001 C CNN
F 3 "~" H 3550 3750 50  0001 C CNN
	1    3550 3750
	0    1    1    0   
$EndComp
$Comp
L Device:Microphone MK?
U 1 1 5C10B20F
P 2400 4250
F 0 "MK?" H 2530 4296 50  0000 L CNN
F 1 "Microphone" H 2530 4205 50  0000 L CNN
F 2 "" V 2400 4350 50  0001 C CNN
F 3 "~" V 2400 4350 50  0001 C CNN
	1    2400 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	2400 4050 2400 3750
$Comp
L power:GND #PWR?
U 1 1 5C10B509
P 2400 4850
F 0 "#PWR?" H 2400 4600 50  0001 C CNN
F 1 "GND" H 2405 4677 50  0000 C CNN
F 2 "" H 2400 4850 50  0001 C CNN
F 3 "" H 2400 4850 50  0001 C CNN
	1    2400 4850
	1    0    0    -1  
$EndComp
Wire Wire Line
	2400 4850 2400 4450
Text Notes 6150 3550 0    50   ~ 0
~~5k samp/s
Wire Wire Line
	2400 3750 3400 3750
$EndSCHEMATC