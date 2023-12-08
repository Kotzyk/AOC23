defmodule Day1 do
  def find_regex_in_string(str, regex) do
    Regex.scan(regex, str)
    |> Enum.flat_map(&List.flatten/1)
  end

  def read_file_lines(filename) do
    lines = File.stream!(filename)
      |> Stream.map(&String.trim/1)
      |> Enum.to_list()
    lines
  end

  defmodule Part1 do
    @digit_regex ~r/\d/
    def calculate_score_for_line(line) do
      digits = Day1.find_regex_in_string(line, @digit_regex)

      score = if length(digits) > 0 do
        List.first(digits) <> List.last(digits)
      else
        0
      end
      String.to_integer(score)
    end

    def calculate_score_for_file(filename) do
      lines = Day1.read_file_lines(filename)
      scores = lines
                |> Enum.map(fn line -> calculate_score_for_line(line) end)
                |> Enum.sum()
      scores
    end
  end


  defmodule Part2 do
    @digits %{
      "one" => 1,
      "two" => 2,
      "three" => 3,
      "four" => 4,
      "five" => 5,
      "six" => 6,
      "seven" => 7,
      "eight" => 8,
      "nine" => 9
    }

    def solve(input_file) do
      File.stream!(input_file)
      |> Stream.map(&String.trim/1)
      |> Enum.map(&convert_line/1)
      |> Enum.sum()
    end

    def convert_line(line) do
      10 * first_digit(line) + last_digit(String.reverse(line))
    end

    for digit <- 1..9 do
      string = Integer.to_string(digit)
      defp first_digit(<<unquote(string), _::binary>>), do: unquote(digit)
      defp last_digit(<<unquote(string), _::binary>>), do: unquote(digit)
    end

    for {string, digit} <- @digits do
      reverse_string = String.reverse(string)
      defp first_digit(<<unquote(string), _::binary>>), do: unquote(digit)
      defp last_digit(<<unquote(reverse_string), _::binary>>), do: unquote(digit)
    end

    defp first_digit(<<_::utf8, rest::binary>>), do: first_digit(rest)
    defp last_digit(<<_::utf8, rest::binary>>), do: last_digit(rest)
  end
end
IO.puts(Day1.Part1.calculate_score_for_file("input.txt"))
IO.inspect(Day1.Part2.solve("input.txt"))
