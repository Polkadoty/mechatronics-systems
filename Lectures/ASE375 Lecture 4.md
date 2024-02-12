---
title: ASE375 Lecture 4
date: 2024-02-11 16:51:06
lastmod: 2024-02-11 16:51:10
categories: 
tags: 
share: false
---

# ASE375 Lecture 4

Following the explanation of the DAQ, transducer, and computer from last time.

The DAQ system digitizes the information into `bins`.
- Let's consider a DAQ with a `2-bit` resolution:
$$
\begin{pmatrix} 0 & 0 \\ 0 & 1 \\ 1 & 0 \\ 1 & 1\end{pmatrix} \} \text{The computer only knows 4 (values/levels)}
$$
Of those two bits, there is a least significant and most significant bit, labeled (LSB) and (MSB) respectively.
![[ASE375_Lecture4_Bits.png]]

All input analog voltages get put into these bins.
![[ASE375_Lecture4_InputGraphs.png]]

The graph on the left is a smoothly varying input, the graph on the right shows steps, or digitized information.

The `Bin Size` is:
$$
\frac{V_{Range}}{2^N - 1}
$$
That's equivalent to the least count of the DAQ. $N$ is the number of bits of the DAQ.

Example:
- $N = 12$
- $V_{Range} = 5V$
$$
\Rightarrow \Delta V = \frac{5}{2^{12} - 1} = \frac{5}{4095} = 1.22 mV
$$
This is the bias error, or least count.

From the graph from lecture 3:
![[ASE375_Lecture3_AnalogvsDigital.png]]

We can treat each one of the spaces between values as our $\Delta t$, which is $\Delta t - \frac{1}{F_s}$. We know that a computer also discretizes data in time. We can treat $F_s$ as our sampling frequency. In this class, we only consider $DAQs$ that measure voltage.

![[ASE375_Lecture4_Circuit_Example.png]]

We can use Ohm's Law to represent this circuit:
$$
V(t) = i(t) \cdot R
$$
- $i$ - Current
- $R$ - Resistance
- $V$ - Voltage
- $V(t)$ - Voltage Source

![[ASE375_Lecture4_ComplexCircuit.png]]

- $R$ - Resistance ($\Omega, Ohm$)
- $L$ - Inductance ($H, Henry$)
- $C$ - Capacitance ($F, Farad$)
- $q$ - Charge ($C, Coulomb$)

Kirchoff's Law: The total voltage around a loop is zero.
$$
V(t) - V_R - V_L - V_C = 0
$$
We can model the voltage drop across each item on the circuit as follows:
$$
\begin{align}
V_R = iR \\
V_L = L \cdot \frac{di}{dt} \\
V_c = \frac{q}{c}
\end{align}
$$
The expression for q for this example is:
$$
i = \frac{dq}{dt} = \dot{q}
$$
That means I can treat:
$$
V(t) - iR - L\frac{di}{dt} - q\frac{1}{c} = 0
$$
$$
V(t) = L\ddot{q} + R\dot{q} + q\frac{1}{c}
$$
This is analogous to a SDOF mass-spring-damper system.
- $q \equiv x$ - Displacement
- $V \equiv F$ - Force
- $L \equiv M$ - Inertia
- $R \equiv C$ - Damping Constant
- $C \equiv \frac{1}{K}$ - Compliance

If we know that $V(t)$ is harmonic, then:
$$
V(t) = V_0 e^{j\omega t}
$$
I can treat the impedance as:
$$
z_R = R, \quad z_L = j\omega L, \quad z_c = \frac{1}{j\omega c}
$$
That means the total impedance:
$$
z_{tot} = z_R + z_L + z_c
$$
$$
R + j\omega L + \frac{1}{j\omega c}
$$
I can treat:
$$
V = i\cdot Z_{tot}
$$
$$
i(\omega) = \frac{v_0 e^{j\omega t}}{z_{tot}}
$$
### Types of Transducers

There are multiple types of transducers in terms of response. Let's let the input quantity be $q_i = q_i u(t)$, so a step input:
![[ASE375_Lecture4_Transducer.png]]

Based on how the transducer responds, we can classify it as the following:

$Zero^{th}$ Order with output: $q_0 = R \cdot q_i$
 ![[ASE375_Lecture4_ZerothOrder.png]]
 
$First$ Order with output: $b_0 q_i = q_0 (a_1 \frac{d}{dt} + a_0)$
 ![[ASE375_Lecture4_FirstOrder.png]]
 There are a couple equations associated with a first order expression:
- $\tau \dot{q}_0 + q_0 = kq_i$     - $\tau$ is the time constant
- $q_0(t) = q_H(t) + q_{PI}(t) = Ae^{-t/\tau} + kq_i$
	- Note, usually $\tau > 0$.
	- If we apply the initial condition to the expression $q_0(0) = 0$, we get:
- $q_0(t) = R * q_i(1 - e^{-t/\tau})$

$Second$ Order: $Rq_i = a_0 q_0 + a_1 \dot{q}_0 + a_2 \ddot{q}_0$
![[ASE375_Lecture4_2ndOrder.png]]

For the first transducer, the 0th order output, how do we measure the temperature?

Temperature is related to the kinetic energy of molecules. We need a way to indirectly measure temperature using thermal expansion.
- For a mercury or alcohol thermometer, we can test an increase in volume.
- Or we can try a bimetallic strip:
![[ASE375_Lecture4_BimetallicStrip.png]]

$$
\begin{align}
\Delta\ell_1 = L(1 + \alpha_1 \Delta T) \\
\Delta\ell_2 = L(1 + \alpha_2 \Delta T)
\end{align}
$$
If $\alpha_1 > \alpha_2$, the strip bends down.
- $\alpha \approx 16*10^{-6} /^\circ C$ - Stainless Steel
- $\alpha \approx 0.02*10^{-6} /^\circ C$ - Invar

We can try to make use of a change in resistance in a wire:
![[ASE375_Lecture4_ResistanceChange.png]]
In this case, the wire has a circular cross-section.
$$
R = \rho \frac{L}{A}
$$
where:
- $\rho$ measures resistivity and we assume it to be constant (for now)

If the temperature increases by $\Delta T$:
$$
L_1 = L(1 + \alpha\Delta T)
$$
$$
A_1 = \frac{\pi}{4}d^2(1 + \alpha \Delta T)^2 = A(1 + 2\alpha \Delta T)
$$
We can assume that $\alpha$ is small. Thus we have a new resistance:
$$
R_1 = \rho\frac{L_1}{A_1} = \rho \frac{L(1 + \alpha \Delta T)}{A(1 + 2\alpha \Delta T)} \approx R(1-\alpha \Delta T)
$$
I also can assume that:
$$
R_1 = R + \Delta R
$$
where $\Delta R$ is the change in resistance due to temperature.
$$
\Rightarrow \frac{\Delta R}{R} = -\alpha \Delta T
$$
The sensitivity $\frac{\Delta R/R}{\Delta T} = -16 * 10^{-6} /^\circ C$ for stainless steel is very small.

In some materials, like semiconductor devices and metal alloys, $\rho$ is very sensitive to changes in temperature. A change in resistance is measured by supplying a constant current and measuring resulting change in voltage.

