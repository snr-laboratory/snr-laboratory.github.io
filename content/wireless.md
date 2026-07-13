---
title: Wireless and Battery-free
---

# Wireless and Battery-free

Cables are often treated as passive details, but each one introduces connectors, routing, mechanical support, grounding paths, thermal conduction, and potential failure points. In many instruments, removing a cable can simplify the surrounding system more than simplifying the sensor itself. Our goal is therefore broader than wireless data: we want sensors and actuators that can communicate and receive energy without permanent electrical connections.

:::commentary
**A cable is a subsystem**

The true cost of a cable includes its connector, strain relief, feedthrough, shield, ground path, installation labor, leak testing, and eventual service access. A fair comparison counts the complete wired channel, not only the wire.
:::

Vacuum vessels and high-pressure chambers make this trade especially visible. Every electrical penetration requires a qualified feedthrough and becomes part of the pressure boundary, background model, grounding scheme, and maintenance plan. Deploying pressure, temperature, current, voltage, position, and radiation sensors without dedicated penetrations could substantially reduce chamber complexity.

:::commentary
**Feedthrough cost is not connector price**

One additional channel can trigger machining, welding, cleaning, certification, leak checking, cabling, and documentation. In a radiopure or cryogenic apparatus, it can also add heat load and unwanted material near the active region.
:::

Imagine a double-beta decay detector whose chamber has no electrical feedthroughs at all, only the ports required for gas handling. That is an aspirational endpoint, but it is a useful design target because it forces communication, power, sensing, and control to be treated as one system.

## Wireless communication

There is no universally best wireless channel. Radio-frequency links can carry data through many nonmetallic boundaries but struggle inside conductive enclosures. Optical links offer high bandwidth and excellent electrical isolation but require a viable line of sight. Near-field magnetic coupling is attractive over short distances, while acoustic communication may be useful through fluids or solid walls. The environment should select the physical channel, not habit.

:::commentary
**Wireless does not mean radio**

"Wireless" describes the absence of a galvanic connection. The carrier may be electromagnetic, optical, magnetic, or acoustic. A hybrid instrument may use different carriers for data and power.
:::

The design begins with a link budget: distance, boundary materials, available spectrum, attenuation, antenna or transducer geometry, required data rate, and acceptable error probability. Timing matters as much as throughput. Distributed sensors may need a shared clock, bounded latency, event ordering, or deterministic wake-up even when their average data volume is small.

Local processing can reduce the communication burden. A sensor may transmit timestamps, fitted parameters, threshold crossings, compressed images, or anomaly scores instead of every raw sample. That can reduce both bandwidth and energy use, provided the instrument retains diagnostic and calibration modes that expose enough raw information to validate the processing.

:::commentary
**Send information, not necessarily waveforms**

Front-end reduction is powerful when the discarded data are genuinely redundant. It becomes dangerous when an irreversible trigger or learned model hides calibration errors. Raw-data access should remain available for commissioning and controlled validation.
:::

## Wireless power transfer

Wireless power must be designed from the load backward. Inductive and resonant coupling can deliver useful power over short, controlled geometries. Radio-frequency or optical delivery can reach farther but usually trades coupling efficiency for distance and alignment freedom. The correct choice depends on average power, peak power, receiver area, boundary materials, and allowable electromagnetic or optical exposure.

A low-duty-cycle device can accumulate energy in a capacitor, wake briefly to measure and communicate, then return to a near-zero-power state. This separates peak load from average delivered power and can make a weak but continuous power link practical. Sensors that must operate continuously require a much stricter accounting of conversion loss and heat deposition.

:::commentary
**Close the power budget first**

Start with the energy required for sensing, computation, communication, startup, and storage leakage. Divide by realistic end-to-end transfer efficiency, then include alignment and aging margin. If that budget does not close, changing the modulation scheme will not rescue the architecture.
:::

The power field must not compromise the measurement. Receiver coils, rectifiers, switching converters, and illumination can inject noise, create local heating, or perturb sensitive materials. Wireless power is successful only when the complete instrument performs better, not merely when the remote device turns on.

## Battery-free

Battery-free means that the deployed device carries no primary or rechargeable chemical cell. It may operate directly from delivered energy, harvest energy from its environment, or use a capacitor for temporary storage. Eliminating the battery avoids finite service life, cold-temperature degradation, outgassing, stored chemical energy, and replacement access in sealed or inaccessible systems.

:::commentary
**Battery-free is not energy-free**

Every measurement still consumes energy. The design question is where that energy originates, how it crosses the system boundary, how long it is stored, and what happens when delivery is interrupted.
:::

A practical battery-free device needs explicit startup, brownout, and recovery behavior. It should fail safely, preserve calibration state where necessary, and resume operation without manual intervention. Passive identifiers and backscatter sensors occupy one end of the design space; intermittently powered intelligent instruments occupy the other.

## Co-designing the complete channel

Communication, power, sensing, packaging, and data processing cannot be optimized independently. The research program should compare complete wireless prototypes against the wired channel they intend to replace. Relevant measurements include delivered power, data integrity, latency, thermal load, electromagnetic interference, mechanical complexity, and performance under the actual pressure, vacuum, radiation, or temperature conditions.

:::commentary
**The benchmark is the cable removed**

A wireless prototype should be judged against the full wired implementation: feedthroughs, harnesses, grounding, heat leaks, installation, and maintenance. Wireless is valuable when the system-level balance improves.
:::

The most compelling result is not a demonstration across a laboratory bench. It is a sealed instrument that operates reliably, measures accurately, and requires fewer penetrations and service operations because the link, power source, and sensor were designed together.
