module demo (
    out     ,  // Output of the counterq
    enable  ,  // enable for counter
    clk     ,  // clock Input
    reset      // reset Input
);

// Ports
output [7:0] out;
input enable, clk, reset;

// Parameter
parameter TEST = 4294967295;

// Internal Variables
reg [7:0] out;
wire      valid = rd_en;

always @(posedge clk)
if (rest) begin
    out <= 8'b0;
end else if (enable) begin
    out <= out + 1;
end else begin
    out <= out;
end

// Another Internal Variable
signal rd_en;

endmodule
