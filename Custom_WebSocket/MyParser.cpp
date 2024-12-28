#include <iostream>
#include <vector>
#include <string>
#include <cstdint>
#include <cstring>

int main() {
    WebSocketParser parser;

    // Simulate a WebSocket frame (text frame with "Hello" as payload)
    std::vector<uint8_t> rawFrame = {0x81, 0x85, 0x37, 0xFA, 0x21, 0x3D, 0x7F, 0x9F, 0x4D, 0x51, 0x58};
    parser.feedData(rawFrame);

    auto frames = parser.parseFrames();
    for (const auto& frame : frames) {
        std::cout << "Parsed Frame:" << std::endl;
        std::cout << "  FIN: " << frame.fin << std::endl;
        std::cout << "  Opcode: " << static_cast<int>(frame.opcode) << std::endl;
        std::cout << "  Masked: " << frame.masked << std::endl;
        std::cout << "  Payload: " << frame.payload << std::endl;
    }

    return 0;
}

