library ieee;
use ieee.std_logic_1164.all;

-- Sorry, I don't know how to generate warning in xvhdl

--------------------------------------------------------------------------------
entity demo is
port (
  aclr  : in  std_logic;
  clk   : in  std_logic;
  d     : in  std_logic;
  q     : out std_logic
);
end entity;
--------------------------------------------------------------------------------
architecture beh of demo is
begin
  process (clk)
  begin
  if (aclr = '1') then
      q <= '0';
  elsif rising_edge(clk) then
      q <= dd;
  end if;
  end process;
end architecture;
