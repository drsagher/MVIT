# Lesson 02 Noise, Media, Encoding in Transmission

## 1. Noise
Noise refers to unwanted disturbances that interfere with signal transmission, causing errors or degradation in communication systems. It affects both analog and digital transmissions but in different ways.

### Noise in Analog Transmission:
In analog systems, noise directly distorts the signal since the signal is continuous.
Common types of noise include thermal noise, intermodulation noise, and crosstalk.
Once noise enters an analog signal, it is difficult to remove completely, leading to poor signal quality in audio, video, or radio transmissions.

### Noise in Digital Transmission:
Digital signals use discrete values (0s and 1s), making them more resistant to noise than analog signals.
Noise in digital transmission can cause bit errors, leading to incorrect data reception.
Error detection and correction techniques (such as parity checks and forward error correction) help minimize noise effects.

### Effects of Noise on Data Transmission
1. Noise can reduce the data rate, making it slower to transmit data.
2. Noise can increase the error rate, requiring more retransmissions and reducing overall efficiency.
3. Noise can decrease signal quality, making it more difficult to accurately transmit data.
4. Noise can increase latency, making it take longer to transmit data.

### Noise Reduction Techniques
1. Using error-correcting codes, such as Reed-Solomon or Hamming codes, to detect and correct errors.
2. Amplifying the signal to increase its strength and reduce the impact of noise.
3. Using filters to remove noise from the signal.
4. Using modulation techniques, such as QAM or PSK, to reduce the impact of noise.
5. Using diversity techniques, such as spatial diversity or frequency diversity, to reduce the impact of noise.

### Noise Reduction Techniques in Analog and Digital Transmission
| Type | Description | Techniques | Use Cases |
| --- | --- | --- | --- |
| Analog Noise Reduction | Techniques to reduce noise in analog transmission | Filtering, Amplification, Modulation | Analog Telephone Systems, Radio Communication, Audio Systems |
| ‣ Filtering | Removes unwanted frequencies from the signal | Low-Pass Filters, High-Pass Filters, Band-Pass Filters | Audio Systems, Radio Communication |
| ‣ Amplification | Increases the strength of the signal to overcome noise | Amplifiers, Repeaters | Analog Telephone Systems, Cable TV |
| ‣ Modulation | Changes the characteristics of the signal to reduce noise | Amplitude Modulation (AM), Frequency Modulation (FM) | Radio Communication, Analog Telephone Systems |
| Digital Noise Reduction | Techniques to reduce noise in digital transmission | Error-Correcting Codes, Data Compression, Signal Processing | Computer Networks, Digital Telephone Systems, Data Storage |
| ‣ Error-Correcting Codes | Detects and corrects errors caused by noise | Cyclic Redundancy Check (CRC), Hamming Codes | Data Storage, Digital Communication Systems |
| ‣ Data Compression | Reduces the amount of data to be transmitted, reducing the impact of noise | Lossless Compression, Lossy Compression | Data Storage, Digital Communication Systems |
| ‣ Signal Processing | Techniques to improve the quality of the digital signal | Filtering, Equalization, Echo Cancellation | Digital Telephone Systems, Audio Systems |


## 2. Transmission Media
Transmission media refers to the physical pathways or channels through which data, voice, or video signals are transmitted from one device to another. Transmission media can be broadly classified into two categories: guided media and unguided media. Guided media, also known as wired media, use physical cables or wires to transmit data, examples include twisted pair cables, coaxial cables, and fiber optic cables. Unguided media, also known as wireless media, use electromagnetic waves to transmit data through the air, examples include radio waves, microwaves, infrared waves, and satellite communications. For instance, a computer connected to a router using a twisted pair cable is an example of guided media, while a smartphone connected to a Wi-Fi network is an example of unguided media.

Transmission media refers to the physical pathways or channels through which data, voice, or video signals are transmitted from one device to another.


Transmission Media
| Type | Description | Examples | Use Cases |
| --- | --- | --- | --- |
| Guided Media | Uses physical cables or wires to transmit data | Twisted Pair Cable, Coaxial Cable, Fiber Optic Cable | LANs, WANs, Internet connectivity |
| ‣ Twisted Pair Cable | Uses two insulated copper wires twisted together | Ethernet cables | Office networks, home networks |
| ‣ Coaxial Cable | Uses a central copper wire surrounded by insulation and a braided shield | Cable TV, broadband internet | Cable TV, internet service providers |
| ‣ Fiber Optic Cable | Uses thin glass or plastic fibers to transmit data as light signals | High-speed internet, data centers | High-speed internet, data centers, cloud computing |
| Unguided Media | Uses electromagnetic waves to transmit data through the air | Radio Waves, Microwaves, Infrared Waves, Satellite Communications | Wireless networks, mobile devices, satellite TV |
| ‣ Radio Waves | Uses low-frequency electromagnetic waves to transmit data | Wi-Fi, Bluetooth, cellular networks | Wireless networks, mobile devices |
| ‣ Microwaves | Uses high-frequency electromagnetic waves to transmit data | Satellite communications, microwave ovens | Satellite TV, microwave ovens |
| ‣ Infrared Waves | Uses high-frequency electromagnetic waves to transmit data | IR remotes, IR sensors | IR remotes, IR sensors |
| ‣ Satellite Communications | Uses satellites to transmit data over long distances | Satellite TV, satellite internet | Satellite TV, satellite internet, global communication networks |


### Types of Transmission Media

#### Wired Media: Uses physical cables to transmit data.
- Twisted Pair Cable
- Coaxial Cable
- Fiber Optic Cable

#### Wireless Media: Uses radio waves or infrared signals to transmit data.
- Radio Waves
- Microwaves
- Infrared Waves

### Characteristics of Transmission Media

1. Bandwidth: The range of frequencies that a transmission medium can support.
2. Data Rate: The amount of data that can be transmitted per unit time.
3. Distance: The maximum distance over which a signal can be transmitted without degradation.
4. Interference: The susceptibility of a transmission medium to electromagnetic interference.
5. Security: The level of protection provided by a transmission medium against unauthorized access.

### Advantages and Disadvantages of Transmission Media

#### Wired Media:

- Advantages: High bandwidth, low interference, high security.
- Disadvantages: Limited mobility, high installation cost.

#### Wireless Media:
- Advantages: High mobility, low installation cost, easy deployment.
- Disadvantages: Low bandwidth, high interference, low security.

### Applications of Transmission Media

1. Local Area Networks (LANs): Wired media (twisted pair, coaxial) and wireless media (Wi-Fi).
2. Wide Area Networks (WANs): Wired media (fiber optic, coaxial) and wireless media (microwaves, satellites).
3. Internet: Wired media (fiber optic, coaxial) and wireless media (Wi-Fi, cellular networks).

## 3. Encoding
Encoding is the process of converting data into a format that can be transmitted efficiently and accurately over a communication channel. It involves transforming the original data into a coded form using a specific algorithm or technique, such as line coding, block coding, or modulation. The primary purpose of encoding is to ensure reliable data transmission by detecting and correcting errors, reducing the impact of noise, and preventing data corruption. Additionally, encoding helps to optimize data transmission by reducing the amount of data that needs to be transmitted, thereby increasing the overall efficiency of the communication system. By converting data into a coded form, encoding enables secure and efficient data transmission over various communication channels, including wired and wireless networks.

### Types of Encoding Methods
#### Line Coding
- Unipolar Encoding: Uses a single voltage level to represent binary 1s and 0s.
- Polar Encoding: Uses two voltage levels to represent binary 1s and 0s.
- Bipolar Encoding: Uses two voltage levels to represent binary 1s and 0s, with a zero voltage level representing a binary 0.

#### Block Coding
- Block Coding: Divides data into fixed-length blocks and adds redundancy to each block for error detection and correction.
- Cyclic Redundancy Check (CRC): A type of block coding that uses a polynomial equation to generate a checksum for error detection.

#### Scrambling
- Scrambling: Randomizes the data sequence to avoid long sequences of 1s or 0s, reducing the risk of data corruption.

#### Modulation
- Amplitude Shift Keying (ASK): Modulates the amplitude of a carrier wave to represent binary 1s and 0s.
- Frequency Shift Keying (FSK): Modulates the frequency of a carrier wave to represent binary 1s and 0s.
- Phase Shift Keying (PSK): Modulates the phase of a carrier wave to represent binary 1s and 0s.

#### Spread Spectrum
- Frequency Hopping Spread Spectrum (FHSS): Rapidly switches the carrier frequency among many different frequency channels to minimize interference.
- Direct Sequence Spread Spectrum (DSSS): Multiplies the data signal with a pseudorandom noise (PN) code to spread the signal across a wide frequency band.

### Purpose of Encoding
1. Encoding methods like block coding and cyclic redundancy check (CRC) help detect and correct errors that occur during data transmission.
2. Encoding methods like modulation and spread spectrum help reduce the impact of noise on data transmission.
3. Encoding methods like scrambling and spread spectrum help secure data transmission by making it more difficult for unauthorized parties to intercept and decode the data.
4. Encoding methods like line coding and block coding help optimize data transmission by reducing the amount of data that needs to be transmitted.

### Encoding Schemes in Data Transmission
| Type | Description | Examples | Use Cases |
| --- | --- | --- | --- |
| Analog Encoding Schemes | Convert analog signals into a format suitable for transmission | Amplitude Shift Keying (ASK), Frequency Shift Keying (FSK), Phase Shift Keying (PSK) | Modems, Radio Communication, Analog Telephone Systems |
| ‣ Amplitude Shift Keying (ASK) | Modulates the amplitude of a carrier wave to represent binary 1s and 0s | Modems, Fax Machines | Dial-up Internet, Fax Transmission |
| ‣ Frequency Shift Keying (FSK) | Modulates the frequency of a carrier wave to represent binary 1s and 0s | Radio Communication, Telemetry Systems | Wireless Keyboards, Mouse, Radio Communication |
| ‣ Phase Shift Keying (PSK) | Modulates the phase of a carrier wave to represent binary 1s and 0s | High-Speed Modems, Satellite Communication | High-Speed Internet, Satellite TV |
| Digital Encoding Schemes | Convert digital data into a format suitable for transmission | Line Coding, Block Coding, Scrambling | Computer Networks, Digital Telephone Systems, Data Storage |
| ‣ Line Coding | Converts digital data into a format suitable for transmission over a communication channel | Unipolar, Polar, Bipolar | Computer Networks, Digital Telephone Systems |
| ‣ Block Coding | Adds redundancy to digital data to detect and correct errors | Cyclic Redundancy Check (CRC), Hamming Codes | Data Storage, Digital Communication Systems |
| ‣ Scrambling | Randomizes digital data to reduce the risk of data corruption | Pseudo-Random Noise (PN) Codes | Digital Communication Systems, Data Storage |
