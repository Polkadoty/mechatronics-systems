---
title: ASE375 Lecture 2
date: 2024-01-22 13:58:52
lastmod: 2024-01-22 13:59:26
categories:
  - 
tags:
  - 
aliases: 
share: false
---

# ASE375 Lecture 2

## Measurement Uncertainty:

- A measurement can be made with different equipment, different procedures. and different days. Some inherent variability due to random processes → contributes to uncertainty

### Two types of uncertainty (error):

#### Systematic error (or bias) - occurs due to instruments. They have a definite magnitude and direction.

Let's say we have a ruler measuring a string. And the ruler has some slight offset in the regular intervals, so that there is an error of consistent direction (either along or against the ruler) and magnitude (some regular offset). This is also known as bias error, or least count error.
![[ASE375_Lecture2_Biaserror.png]]
In this case, the bias error used 1/2 of the least count for the precision.

#### Accidental or Precision error - random in occurrence, variable in magnitude and direction. They typically follow a [[Gaussian Distribution]] or random distribution $\varepsilon_p$.

- Total Uncertainty $\epsilon = \sqrt{\epsilon_b^2 + \epsilon_p^2}$
We can propagate these uncertainties to desired quantities.

Example:
![[ASE375_Lecture2_BallDropped.png]]

$$
h = \frac{1}{2}gt^2
$$
$$
\frac{\partial h}{\partial t}  gt
$$
$$
\Delta h = \frac{\partial h}{\partial t} \cdot \Delta t
$$
In this case, $\Delta h$ is the propagated uncertainty, and $\Delta t$ is the uncertainty in measured time.

If I user a stopwatch graduated in seconds (Least count $\equiv 1 sec$):
$$
\Delta t = 0.5 \ \text{seconds}
$$
Precision error: Human error of starting or stopping the stopwatch.

Let's ignore $\epsilon_p$ for now and consider a 100 m tall tower. Let's say you are timing how long it takes to get down the tower.
$$
\begin{align}
\Delta h = \frac{\partial h}{\partial t} * \Delta t \\
\frac{\partial h}{\partial t} = g\cdot t = 9.81 * 0.5 = 44.14 m \\
\Delta h = 44.14 * \frac{1}{2} = 22.07 m
\end{align}
$$
This means out of the relative error is $\frac{\Delta h}{h} = 22\%$. We need a stopwatch with a smaller least count.

What about precision error? In general, this follows a [[Gaussian Distribution]]. Let's take a probability that x is in the interval region we are looking for: $a \leq x \leq b$ is $\int_{a}^b f(x)dx$
where:
$$
f(x) = \frac{1}{\sigma{\sqrt{2\pi}}}e^{-\frac{1}{2}(\frac{x - \mu}{\sigma})^2}
$$
In this equation:
- $\sigma \equiv \text{Standard Deviation}$
- $\mu \equiv \text{Mean}$

We usually take multiple, let's say $N$ measurements. This is called a "sample." The true value is $x_0$ (this corresponds to the population mean) which we don't exactly know. We can define a sample mean as following:
$$
\bar{x} = \frac{1}{N}\sum_{i = 1}^{N} x_i
$$
But we do know that $x_i = x_o + e_i$, where $e_i$ is an error in the measurement.

We can never know the exact value of error because we can never measure an infinite number of samples, so instead we use an estimate for it, known as Uncertainty.
$$
\frac{1}{N}\sum_{i = 1}^{N} x_i < e_{max} \ \text{(maximum single error)}
$$
Because we don't know $x_o$, we use $\bar{x}$ as an estimate of $x_0$ and examine the values around $\bar{x}$.
$$
x_i = \bar{x} + d_i \quad \text{and} \quad \sum_{i = 1}^{N} d_i = 0
$$
Accuracy vs Precision:

- Accuracy: how close the measurement is to the true value, often specified as a % of a full-scale value.
	- If $e_i$ is small, → High Accuracy
- Precision: how close are the measurements to each other?
	- $d_i$ is small → High Precision

Accuracy can be improved by calibration but cannot exceed the precision.

We can bound uncertainty using statistical tools:
- Sample mean: $\bar{x} = \frac{1}{N}\sum_{i = 1}^{N} x_i$
- Sample Distribution: $\sigma^2 = \sum_{i = 1}^N \frac{(x_i - \bar{x})^2}{N}$
- Standard Error of the mean: $\sigma_x = \frac{\sigma^2}{N}$

![[ASE375_Lecture2_Example3.png]]

If the measured quantity is randomly distributed, then the sample means are also randomly distributed.













