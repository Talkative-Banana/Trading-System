# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -std=c++11 -Wall -Wextra

# Targets and dependencies
TARGET = test_throughput.exe
OBJECTS = test_throughput.o Api.o Socket.o BSocket.o Socketpp.o

# Default target
all: $(TARGET)

# Link object files to create the executable
$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $(TARGET) -lssl -lcrypto -lboost_system

# Compile test_latency.cpp to test_latency.o
test_throughput.o: test_throughput.cpp
	$(CXX) $(CXXFLAGS) -c test_throughput.cpp -o test_throughput.o

# Compile Api.cpp to Api.o
Api.o: Api.cpp
	$(CXX) $(CXXFLAGS) -c Api.cpp -o Api.o

# Socket Dependencies
Socket.o: Socket.cpp
	$(CXX) $(CXXFLAGS) -c Socket.cpp -o Socket.o

# BSocket Dependencies
BSocket.o: BSocket.cpp
	$(CXX) $(CXXFLAGS) -c BSocket.cpp -o BSocket.o

# Socketpp Dependencies
Socketpp.o: Socketpp.cpp
	$(CXX) $(CXXFLAGS) -c Socketpp.cpp -o Socketpp.o

# Clean up generated files
clean:
	rm -f $(OBJECTS) $(TARGET)

# Phony targets
.PHONY: all clean
