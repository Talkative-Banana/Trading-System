<!-- ABOUT THE PROJECT -->
# Trading System
A high-performance order execution and management system to trade on [Deribit Test](https://test.deribit.com/).

This Project implement and justify optimization techniques for memory management, network communication, data structure selection, thread management and CPU optimization. It covers all supported symbols and instrument coverage include support for Spot, Future, and Options.

<!-- BUILT WITH -->
### Built With
* Cpp
* [Boost](https://www.boost.org/)
* [Websocketpp](https://www.zaphoyd.com/projects/websocketpp/)


<!-- TABLE OF CONTENTS -->
### Table of Contents
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#documentation">Documentation</a></li>
    <li><a href="#results">Results</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- DOCUMENTATION -->
## Documentation

### Main idea
The project aims to develop a high-performance order execution and management system for trading on the Deribit Test platform. It leverages C++ to achieve low-latency performance while ensuring robust functionality and scalability.

Key features of the system include:

- Order Management: Seamless order placement, cancellation, and modification for a variety of trading instruments, including Spot, Futures, and Options.
- Real-Time Market Data Streaming: Implements a WebSocket server to provide continuous and efficient updates of market data, supporting multiple client subscriptions.
- Market Coverage: Comprehensive support for all symbols available on the Deribit platform.
- Performance Optimization: Incorporates techniques for memory management, efficient data structure usage, and network communication to minimize latency.
- Error Handling and Logging: Ensures reliability and traceability through robust error management and detailed logging.

This system is designed to meet the demands of algorithmic trading by focusing on speed, accuracy, and scalability, making it a suitable solution for real-world financial markets.

### The method

Two Implementaion of the sockets are currently supported. Boost beast implementation and Websocket++ implementation. These implementations in turn can make both sync and async calls to remote api.

Trader supporting various functionalities.
![image](https://github.com/user-attachments/assets/18eca50e-753e-49dc-b584-435514815546)


<!-- RESULTS -->
## Results

### Average and Individual E2E latency while making sync request [WebSocket++].

![image](https://github.com/user-attachments/assets/96ef5a31-08ae-4aaf-ae07-102fb278054f)

### Average and Individual E2E latency while making sync request [Boost Beast].

![image](https://github.com/user-attachments/assets/62554b33-dee0-4739-863e-a434aacac0d9)


### Average and Individual E2E latency while making async requests [Boost Beast]

![image](https://github.com/user-attachments/assets/9eb14fce-4b0a-46bd-bfca-9fffe2e13eb1)


### Average and Individual E2E latency while making async requests [WebSocket++]

![image](https://github.com/user-attachments/assets/5dd4b775-f9e3-42d0-b0c2-de8c97e911e7)

### Averages and Standard Deviation

![image](https://github.com/user-attachments/assets/108c0488-8229-4843-b675-b98296d5b964)

<!-- GETTING-STARTED -->
## Getting Started
To get a local copy up and running follow these simple steps.

<!-- PREREQUISITES -->
### Prerequisites
* Basic understanding of CPP
* Boost and Websocket++ library
* GitHub Account ([Sign Up](https://github.com/))

<!-- INSTALLATION -->
### Installation
* Clone the repo
  ```bash
  git clone https://github.com/Talkative-Banana/Trading-System.git
  ```
  Make sure you have both Boost Beast and Websocket++ libraries then you can call make by going into directories having Makefile
  ```bash
  cd src/
  make
  ./algo.exe
  ```
  Make cahnges in the Api.cpp to switch implementations of socket and make changes in tes_latency.cpp to switch between sync or async
  ```bash
  cd test/test_latency/
  make
  ./test_latency.exe
  ```
  
  ```bash
  cd test/test_throughput/
  make
  ./test_throughput.exe
  ```
<!-- ROADMAP -->
## Roadmap
- Clone the repo and open it in suitable IDE for complete project source code. You can also fix the issues and hence contribute.

<!-- CONTRIBUTING -->
## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request
<!-- CONTACT -->
## Contact
Email ID - lakshay21059@iiitd.ac.in
<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
Lakshay Bansal lakshay21059@iiitd.ac.in
