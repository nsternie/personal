module mojo_top(
    input clk,
    input rst_n
    );

wire rst = ~rst_n; // make reset active high

endmodule // top

module ws2812(
    input clk,
    input rst,
    input [7:0] r,
    input [7:0] g,
    input [7:0] b,
    input load,
    input ws_reset,
    output reg dataline,
    output reg ready
    );

// States
parameter IDLE       = 3'b000;
parameter PULSE_DATA = 3'b010;
parameter WS_RST     = 3'b011;
reg [2:0] state;

// Clock delay targets, defines pulses
parameter RESET_TICKS = 3000;  // 20ns per tick
parameter ONE_HIGH_TICKS = 40;
parameter ONE_LOW_TICKS = 22;
parameter ZERO_HIGH_TICKS = 20;
parameter ZERO_LOW_TICKS = 42;

reg [23:0] data;  // Local color data

reg [31:0] counter;  // Counter for e'rythang

reg bit_state;
reg [31:0] data_index;
reg [31:0] counter_target;

always @ (posedge clk) begin
  if (rst) begin
    state <= IDLE;
    ready <= 0;
    dataline <= 0;
    counter <= 0;
    counter_target <= 0;
    data_index <= 0;
    bit_state <= 0;
    data <= 0;
  end else begin
        
    case (state)
    
      IDLE : begin
        if (ws_reset) begin
          state <= WS_RST;
          counter <= 0;
          counter_target <= RESET_TICKS;
          ready <= 0;
        end else if (load == 1) begin
          ready <= 0;
          data[15:8] <= r;
          data[23:16] <= g;
          data[7:0] <= b;
          state <= PULSE_DATA;
          data_index <= 24;
          
          if (g[7] == 1) counter_target <= ONE_HIGH_TICKS;
          else if (g[7] == 0) counter_target <= ZERO_HIGH_TICKS;
          
          counter <= 0;
          dataline <= 1;
        end else begin
          ready <= 1;
        end
      end
      
      PULSE_DATA : begin
        // All data has been sent, return to idle
        if (data_index == 0) begin
          state <= IDLE;
          dataline <= 0;
        end else begin // We have data to send
          // Currently on the high half of the pulse\
          ready <= 0;
          if (dataline == 1) begin
            if (counter == counter_target) begin
              dataline <= 0;
              counter <= 0;
              if (data[data_index-1] == 1) counter_target <= ONE_LOW_TICKS;
              else if (data[data_index-1] == 0) counter_target <= ZERO_LOW_TICKS;
            end else begin
              counter <= counter + 1;
            end
          end else begin
            if (counter == counter_target) begin
              dataline <= 1;
              counter <= 0;
              if (data[data_index-2] == 1) counter_target <= ONE_HIGH_TICKS;
              else if (data[data_index-2] == 0) counter_target <= ZERO_HIGH_TICKS;
              data_index <= data_index - 1;
            end else begin
              counter <= counter + 1;
            end
          end
        end
      end
      WS_RST : begin
        if (counter > counter_target) begin
          state <= IDLE;
        end else begin
          counter <= counter + 1;
          ready <= 0;
        end
      end
      
    endcase
    
  end
  
end // Alwyas @ clk



endmodule


// Clock divider module
module clock_divider(
    input clk_in,
    input rst,
    input [31:0] divisor,
    output reg clk_out
    );
  
reg [31:0] counter;
    
always @ (posedge clk_in) begin
  //if (rst) begin
    //clk_out <= 0;
    //counter <= 0;
  //end else 
  if (counter == divisor) begin
    clk_out <= ~clk_out;
    counter <= 0;
  end else begin
    counter <= counter + 1;
  end
end
  
endmodule