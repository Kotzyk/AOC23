defmodule Day1 do
  @digit_regex ~r/\d/
  def find_numbers_in_string(str) do
    Regex.scan(@digit_regex, str)
    |> Enum.flat_map(&List.flatten/1)
  end

  def read_file_lines(filename) do
    lines = File.stream!(filename)
      |> Stream.map(&String.trim/1)
      |> Enum.to_list()
    lines
  end

  defmodule Part1 do
    def calculate_score_for_line(line) do
      digits = Day1.find_numbers_in_string(line)

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
      Enum.reduce(scores, 0, fn x, acc -> x + acc end)
    end
  end
end

input_file = "./input.txt"

IO.inspect(Day1.Part1.calculate_score_for_file(input_file))
