---
title: ASE375 Lecture 5
date: 2024-02-11 21:24:57
lastmod: 2024-02-11 21:25:03
categories: 
tags: 
share: false
---

# ASE375 Lecture 5

Resistance of a wire changes with a change in temperature. Previously in [[ASE375 Lecture 4]], we ignored any change in resistivity $\rho$. Now if we consider a change in $\rho$, some metals have a large and stable temperature coefficient of resistance.

For example, a platinum wire has a $\frac{\Delta R/R}{\Delta T} \approx 3.9 * 10^{-3} /^\circ C$. These sensors are called RTDs (Resistance Temperature Detectors). Some other materials, like ceramics and semiconductors, have a large non-linear thermal coefficient of resistance. We call these [[Thermistors]]. We will look at four types of temperature sensors:
![[ASE375_Lecture5_TempSensors.png]]

### Thermocouple:

Consists of a junction of two dissimilar metals. Relies on the Seebeck effect.
- Seebeck Effect: when two dissimilar metals are in contact, electrons diffuse across the boundary until an electric field opposing the motion is set up and an equilibrium is reached. This creates a voltage across the junction, which is a function of temperature.
- ![[ASE375_Lecture5_Thermocouple_1.png]]
- The voltage across M-N is $V_0$, which is a function of $T_1 - T_2$. I can treat $T_1 - T_2$ as: $T_1 - T_2 = a_0 + a_1 v_0 + a_2 v_0^2 + \cdots + a_n v_0^n$
- The coefficients $a_0, a_1, \cdots a_n$ depend on the two metals, and $T_1 - T_2$ are either in $C, K$, or other temperature units. Usually one junction $J_2$ is kept at a known temperature so $T_1$ can be calculated from the measured $v_0$. This is called cold junction compensation.

There are a couple Thermocouple Laws:
1. The output $v_0$ does not depend on intermediate temperatures along the cable. $V_0 = T_1 - T_2$
	- ![[ASE375_Lecture5_ThermocoupleLaw1.png]]
2. An intermediate metal can be introduced in the circuit if the junctions are at the same temperature.
	- ![[ASE375_Lecture5_ThermocoupleLaw2.png]]

![[ASE375_Lecture5_ThermocoupleMaterials.png]]

![[ASE375_Lecture5_ThermocoupleMaterials2.png]]

Advantages of a Thermocouple:
- Requires no external power
- High measurement range
Disadvantages of a Thermocouple:
- Low sensitivity, meaning a low output voltage
- Requires cold junction compentation

### Thermistor:

Resistance is a strong non-linear function of temperature using the following relations:
$$
\ln\frac{R}{R_0} = \beta(\frac{1}{T} - \frac{1}{T_0})
$$
Or the Steinhart-Hart Relation:
$$
\frac{1}{T} = A + B\ln(R) + C[\ln(R)]^3
$$
The graph looks as follows:
![[ASE375_Lecture5_Thermistor.png]]
The coefficients $A, B$ and $C$ are constants, determined by calibration. Typically:
- $R = 3k\Omega$ @ $25^\circ C$
- $R = 1 k\Omega$ @ $100^\circ C$

We can measure this by using a potential divider:
![[ASE375_Lecture5_PotentialDivider.png]]
- $R_T$ - Thermistor (variable resistance)
- $R_1$ - known, fixed resistor
- $V_s$ - Constant (DC) voltage source
- $V_0$ - Voltage to be measured

$$
V_s - i(R_T + R_1) = 0 \quad \rightarrow \quad i = \frac{V_s}{R_1 + R_T} 
$$
$$
V_0 = i R_1 = \frac{R_1}{R_1 + R_T}*V_s
$$
Current flowing through a resistor causes heating, known as (Joule Heating). Heat generated equals power dissipated:
$$
P_T = i^2 R_T
$$
We want to keep this as small as possible.

